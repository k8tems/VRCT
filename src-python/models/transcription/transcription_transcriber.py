"""Runtime transcriber that wraps Google SpeechRecognition, faster-whisper, and Qwen ASR.

This class focuses on converting incoming raw audio buffers into text using
the Google web recognizer (online), a local Whisper model (offline), or a
Qwen ASR server that exposes an OpenAI-compatible API.
"""

import os
import tempfile
import time
from io import BytesIO
from threading import Event
import wave
from typing import Any, Dict, List, Optional, Union
from speech_recognition import Recognizer, AudioData, AudioFile
from speech_recognition.exceptions import UnknownValueError
from datetime import timedelta
from pyaudiowpatch import get_sample_size, paInt16
from .transcription_languages import transcription_lang
from .transcription_whisper import getWhisperModel, checkWhisperWeight

from openai import OpenAI
import torch
import numpy as np
from pydub import AudioSegment
from utils import errorLogging

import warnings
warnings.simplefilter('ignore', RuntimeWarning)

PHRASE_TIMEOUT = 3
MAX_PHRASES = 10
QWEN_HOST = "192.168.1.3"
QWEN_BASE_URL = f"http://{QWEN_HOST}:8765/v1"
QWEN_MODEL = "Qwen/Qwen3-ASR-0.6B"


class AudioTranscriber:
    """Convert queued audio buffers into transcripts.

    Public attributes set by the constructor:
    - speaker: bool
    - phrase_timeout: int
    - max_phrases: int

    Methods are intentionally permissive about input types to match the
    existing codebase; this wrapper adds typing for clarity.
    """

    def __init__(
        self,
        speaker: bool,
        source: Any,
        phrase_timeout: int,
        max_phrases: int,
        transcription_engine: str,
        root: Optional[str] = None,
        whisper_weight_type: Optional[str] = None,
        device: str = "cpu",
        device_index: int = 0,
        compute_type: str = "auto",
    ) -> None:
        self.speaker = speaker
        self.phrase_timeout = phrase_timeout
        self.max_phrases = max_phrases
        self.transcript_data: List[Dict[str, Any]] = []
        self.transcript_changed_event = Event()
        self.audio_recognizer = Recognizer()
        self.transcription_engine = "Google"
        self.whisper_model = None
        self.audio_sources: Dict[str, Any] = {
            "sample_rate": source.SAMPLE_RATE,
            "sample_width": source.SAMPLE_WIDTH,
            "channels": source.channels,
            "last_sample": bytes(),
            "last_spoken": None,
            "new_phrase": True,
            "process_data_func": self.processSpeakerData if speaker else self.processSpeakerData,
        }

        if transcription_engine == "Whisper" and checkWhisperWeight(root, whisper_weight_type) is True:
            self.whisper_model = getWhisperModel(
                root, whisper_weight_type, device=device, device_index=device_index, compute_type=compute_type
            )
            self.transcription_engine = "Whisper"
        elif transcription_engine == "Qwen":
            self.transcription_engine = "Qwen"

    def transcribeAudioQueue(
        self,
        audio_queue: Any,
        languages: List[str],
        countries: List[str],
        avg_logprob: float = -0.8,
        no_speech_prob: float = 0.6,
        no_repeat_ngram_size: int = 0,
        vad_filter: bool = False,
        vad_parameters: Optional[Union[dict, Any]] = None,
    ) -> bool:
        if audio_queue.empty():
            time.sleep(0.01)
            return False
        audio, time_spoken = audio_queue.get()
        self.updateLastSampleAndPhraseStatus(audio, time_spoken)

        confidences: List[Dict[str, Any]] = [{"confidence": 0, "text": "", "language": None}]
        try:
            audio_data = self.audio_sources["process_data_func"]()
            match self.transcription_engine:
                case "Google":
                    for language, country in zip(languages, countries):
                        try:
                            text, confidence = self.audio_recognizer.recognize_google(
                                audio_data,
                                language=transcription_lang[language][country][self.transcription_engine],
                                with_confidence=True
                                )
                            confidences.append({"confidence": confidence, "text": text, "language": language})
                        except Exception:
                            pass
                case "Whisper":
                    audio_data = np.frombuffer(
                        audio_data.get_raw_data(convert_rate=16000, convert_width=2), np.int16
                    ).flatten().astype(np.float32) / 32768.0
                    if isinstance(audio_data, torch.Tensor):
                        audio_data = audio_data.detach().numpy()

                    for language, country in zip(languages, countries):
                        text = ""
                        source_language = (
                            transcription_lang[language][country][self.transcription_engine]
                            if len(languages) == 1
                            else None
                        )
                        segments, info = self.whisper_model.transcribe(
                            audio_data,
                            beam_size=5,
                            temperature=0.0,
                            log_prob_threshold=-0.8,
                            no_speech_threshold=0.6,
                            language=source_language,
                            word_timestamps=False,
                            without_timestamps=True,
                            task="transcribe",
                            no_repeat_ngram_size=no_repeat_ngram_size,
                            vad_filter=vad_filter,
                            vad_parameters=vad_parameters,
                        )
                        for s in segments:
                            if s.avg_logprob < avg_logprob or s.no_speech_prob > no_speech_prob:
                                continue
                            text += s.text
                        confidences.append({"confidence": info.language_probability, "text": text, "language": language})
                        if (len(languages) == 1) or (
                            transcription_lang[language][country][self.transcription_engine] == info.language
                        ):
                            break
                case "Qwen":
                    language = None
                    result_language = None
                    if len(languages) == 1:
                        language = transcription_lang[languages[0]][countries[0]][self.transcription_engine]
                        result_language = languages[0]

                    text = self.transcribeQwen(audio_data, language=language)
                    confidences.append({"confidence": 1, "text": text, "language": result_language})

        except UnknownValueError:
            pass
        except Exception:
            errorLogging()
        finally:
            pass

        result = max(confidences, key=lambda x: x["confidence"])
        if result["text"] != "":
            self.updateTranscript(result)
        return True

    def updateLastSampleAndPhraseStatus(self, data: bytes, time_spoken) -> None:
        source_info = self.audio_sources
        if source_info["last_spoken"] and time_spoken - source_info["last_spoken"] > timedelta(seconds=self.phrase_timeout):
            source_info["last_sample"] = bytes()
            source_info["new_phrase"] = True
        else:
            source_info["new_phrase"] = False

        source_info["last_sample"] += data
        source_info["last_spoken"] = time_spoken

    def processMicData(self) -> AudioData:
        audio_data = AudioData(
            self.audio_sources["last_sample"], self.audio_sources["sample_rate"], self.audio_sources["sample_width"]
        )
        return audio_data

    def processSpeakerData(self) -> AudioData:
        temp_file = BytesIO()
        with wave.open(temp_file, 'wb') as wf:
            wf.setnchannels(self.audio_sources["channels"])
            wf.setsampwidth(get_sample_size(paInt16))
            wf.setframerate(self.audio_sources["sample_rate"])
            wf.writeframes(self.audio_sources["last_sample"])
        temp_file.seek(0)

        if self.audio_sources["channels"] > 2:
            audio = AudioSegment.from_file(temp_file, format="wav")
            mono_audio = audio.set_channels(1)
            temp_file = BytesIO()
            mono_audio.export(temp_file, format="wav")
            temp_file.seek(0)

        with AudioFile(temp_file) as source:
            audio = self.audio_recognizer.record(source)
        return audio

    @staticmethod
    def transcribeQwen(audio_data: AudioData, language: Optional[str] = None) -> str:
        client = OpenAI(
            api_key="test",
            base_url=QWEN_BASE_URL,
        )

        temp_file_path = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
                temp_file.write(audio_data.get_wav_data(convert_rate=16000, convert_width=2))
                temp_file_path = temp_file.name

            with open(temp_file_path, "rb") as audio_file:
                response = client.audio.transcriptions.create(
                    model=QWEN_MODEL,
                    file=audio_file,
                    language=language,
                    response_format="verbose_json",
                )

            return response.text
        finally:
            if temp_file_path is not None:
                try:
                    os.remove(temp_file_path)
                except OSError:
                    pass

    def updateTranscript(self, result: dict) -> None:
        source_info = self.audio_sources
        transcript = self.transcript_data

        if source_info["new_phrase"] or len(transcript) == 0:
            if len(transcript) > self.max_phrases:
                transcript.pop(-1)
            transcript.insert(0, result)
        else:
            transcript[0] = result

    def getTranscript(self) -> dict:
        if len(self.transcript_data) > 0:
            result = self.transcript_data.pop(-1)
        else:
            result = {"confidence": 0, "text": "", "language": None}
        return result

    def clearTranscriptData(self) -> None:
        self.transcript_data.clear()
        self.audio_sources["last_sample"] = bytes()
        self.audio_sources["new_phrase"] = True