"""
مثال على الدمج مع أنظمة ASR
"""

import numpy as np
from src import AudioCapture, calculate_tdoa, match_pattern

# مثال: دمج مع Whisper
def transcribe_with_mouth_localization(audio_data, sample_rate, whisper_model):
    """
    تحويل الصوت إلى نص مع تحديد موقع الفم
    
    Args:
        audio_data: بيانات صوتية
        sample_rate: معدل العيّنات
        whisper_model: نموذج Whisper
    
    Returns:
        (النص, موقع الصوت)
    """
    # 1. حساب TDOA
    tdoas = calculate_tdoa(audio_data, sample_rate)
    
    # 2. تحديد الموقع
    position = match_pattern(tdoas)
    
    # 3. تحويل الصوت إلى نص
    # دمج القنوات إلى أحادي
    mono_audio = np.mean(audio_data, axis=1).flatten()
    result = whisper_model.transcribe(mono_audio)
    text = result["text"]
    
    return text, position

def main():
    print("=" * 60)
    print("دمج مع نظام ASR (Whisper)")
    print("=" * 60)
    
    try:
        import whisper
        model = whisper.load_model("base")
    except ImportError:
        print("خطأ: يرجى تثبيت whisper-openai")
        print("  pip install whisper-openai")
        return
    
    # تسجيل الصوت
    capture = AudioCapture(channels=4, sample_rate=192000)
    audio_data = capture.record(duration=3.0)
    
    # تحويل إلى نص مع تحديد الموقع
    text, position = transcribe_with_mouth_localization(
        audio_data, 
        192000, 
        model
    )
    
    print(f"\nالنص: {text}")
    print(f"موقع الصوت: {position}")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()