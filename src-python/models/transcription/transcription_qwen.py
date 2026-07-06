"""OpenAI-compatible Qwen ASR transcription helper.

This module intentionally exposes a small function instead of a class so it can
be tested independently from VRCT's AudioTranscriber wrapper.
"""

from os import environ
from typing import Optional

from requests import post


DEFAULT_QWEN_ASR_BASE_URL = "http://127.0.0.1:8000/v1"
DEFAULT_QWEN_ASR_MODEL = "qwen3-asr"


def _get_transcription_url() -> str:
    explicit_url = environ.get("QWEN_ASR_URL")
    if explicit_url:
        return explicit_url

    base_url = environ.get("QWEN_ASR_BASE_URL", DEFAULT_QWEN_ASR_BASE_URL).rstrip("/")
    return f"{base_url}/audio/transcriptions"


def transcribeQwen(
    audio_wav: bytes,
    language: Optional[str] = None,
    response_format: str = "text",
    timeout: float = 30.0,
) -> str:
    """Transcribe WAV bytes with an OpenAI-compatible Qwen ASR endpoint.

    Supported OpenAI-style parameters are deliberately limited to the subset
    implemented by the Qwen wrapper:
    - model
    - file
    - language
    - response_format

    Runtime configuration is environment-based to keep VRCT config/UI changes
    minimal while the integration is being tested:
    - QWEN_ASR_URL: full endpoint URL, e.g. http://127.0.0.1:8000/v1/audio/transcriptions
    - QWEN_ASR_BASE_URL: base URL, e.g. http://127.0.0.1:8000/v1
    - QWEN_ASR_MODEL: model name sent to the endpoint
    - QWEN_ASR_API_KEY: optional bearer token
    """
    files = {
        "file": ("audio.wav", audio_wav, "audio/wav"),
    }
    data = {
        "model": environ.get("QWEN_ASR_MODEL", DEFAULT_QWEN_ASR_MODEL),
        "response_format": response_format,
    }
    if language:
        data["language"] = language

    headers = {}
    api_key = environ.get("QWEN_ASR_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    response = post(
        _get_transcription_url(),
        files=files,
        data=data,
        headers=headers,
        timeout=timeout,
    )
    response.raise_for_status()

    if response_format == "text":
        return response.text.strip()

    payload = response.json()
    if isinstance(payload, dict):
        return str(payload.get("text", "")).strip()
    return ""
