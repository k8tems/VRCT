"""Function-based Qwen ASR REST client.

This module targets OpenAI-compatible /audio/transcriptions endpoints.
Only the subset used by the local Qwen test server is implemented:
- model
- file
- language (optional)
- response_format

The caller owns audio capture and phrase segmentation. This helper only sends
one WAV payload and returns recognized text.
"""

from __future__ import annotations

from os import environ
from typing import Optional

from requests import post


DEFAULT_QWEN_ASR_BASE_URL = "http://127.0.0.1:8000/v1"
DEFAULT_QWEN_ASR_MODEL = "qwen-asr"
DEFAULT_QWEN_ASR_RESPONSE_FORMAT = "text"
DEFAULT_QWEN_ASR_TIMEOUT = 30.0


def _get_qwen_asr_url(base_url: Optional[str] = None) -> str:
    base = (base_url or environ.get("VRCT_QWEN_ASR_BASE_URL") or DEFAULT_QWEN_ASR_BASE_URL).rstrip("/")
    return f"{base}/audio/transcriptions"


def transcribeQwenAudio(
    wav_bytes: bytes,
    language: Optional[str] = None,
    response_format: Optional[str] = None,
    model: Optional[str] = None,
    base_url: Optional[str] = None,
    timeout: Optional[float] = None,
) -> str:
    """Transcribe one WAV payload through a Qwen/OpenAI-compatible REST API.

    Args:
        wav_bytes: Complete WAV bytes.
        language: Optional ISO language code, e.g. "ja", "en", "zh".
        response_format: OpenAI-style response format. Defaults to "text".
        model: Model name sent to the endpoint.
        base_url: Base URL ending before /audio/transcriptions.
        timeout: HTTP timeout in seconds.

    Returns:
        Transcribed text. Empty string is returned for empty/non-text responses.
    """
    selected_response_format = (
        response_format
        or environ.get("VRCT_QWEN_ASR_RESPONSE_FORMAT")
        or DEFAULT_QWEN_ASR_RESPONSE_FORMAT
    )
    selected_model = model or environ.get("VRCT_QWEN_ASR_MODEL") or DEFAULT_QWEN_ASR_MODEL
    selected_timeout = timeout or float(environ.get("VRCT_QWEN_ASR_TIMEOUT", DEFAULT_QWEN_ASR_TIMEOUT))

    data = {
        "model": selected_model,
        "response_format": selected_response_format,
    }
    if language:
        data["language"] = language

    headers = {}
    api_key = environ.get("VRCT_QWEN_ASR_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    response = post(
        _get_qwen_asr_url(base_url),
        data=data,
        files={"file": ("audio.wav", wav_bytes, "audio/wav")},
        headers=headers,
        timeout=selected_timeout,
    )
    response.raise_for_status()

    if selected_response_format in {"json", "verbose_json"}:
        payload = response.json()
        return str(payload.get("text", "") or "")

    return response.text or ""
