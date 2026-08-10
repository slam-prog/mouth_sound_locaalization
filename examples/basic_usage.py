"""
مثال أساسي لاستخدام النظام
"""

import numpy as np
from src import AudioCapture, calculate_tdoa, match_pattern

def main():
    print("=" * 60)
    print("مثال أساسي: تحديد موقع الصوت من الفم")
    print("=" * 60)
    
    # 1. إعداد جهاز التسجيل
    print("\n1. إعداد جهاز التسجيل...")
    capture = AudioCapture(channels=4, sample_rate=192000)
    capture.list_devices()
    
    # 2. تسجيل الصوت
    print("\n2. تسجيل الصوت (تكلم الآن)...")
    audio_data = capture.record(duration=2.0)
    
    # 3. حساب TDOA
    print("\n3. حساب فروق زمن الوصول (TDOA)...")
    tdoas = calculate_tdoa(audio_data, sample_rate=192000)
    print(f"   TDOAs: {tdoas}")
    
    # 4. تحديد الموقع
    print("\n4. تحديد موقع الصوت...")
    position = match_pattern(tdoas)
    if position is not None:
        print(f"   الموقع المقدّر: {position}")
    else:
        print("   لم يتم تحديد الموقع")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()