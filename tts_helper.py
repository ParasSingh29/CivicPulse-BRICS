import io
try:
    from gtts import gTTS
except ImportError:
    gTTS = None
import base64

# Language mappings for Google Text-to-Speech
LANG_MAP = {
    "en": "en",
    "hi": "hi",
    "ta": "ta",
    "te": "te",
    "ru": "ru",
    "zh": "zh-CN",
    "pt": "pt"
}

def generate_speech_audio(text: str, lang_code: str = "en") -> bytes:
    """Generates MP3 audio bytes using Google Text-to-Speech (gTTS)."""
    target_lang = LANG_MAP.get(lang_code, "en")
    try:
        tts = gTTS(text=text, lang=target_lang, slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.read()
    except Exception:
        try:
            tts = gTTS(text=text, lang="en", slow=False)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            return fp.read()
        except Exception:
            return b""
