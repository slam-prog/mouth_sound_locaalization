"""
عرض توضيحي في الوقت الفعلي
"""

import numpy as np
import sounddevice as sd
from src import calculate_tdoa, match_pattern
import time

class RealTimeDemo:
    """فئة للعرض التوضيحي في الوقت الفعلي"""
    
    def __init__(self, channels=4, sample_rate=192000, buffer_size=4096):
        self.channels = channels
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        
    def audio_callback(self, indata, frames, time_info, status):
        """دالة معالجة الصوت في الوقت الفعلي"""
        if status:
            print(f"Status: {status}")
        
        # حساب TDOA
        tdoas = calculate_tdoa(indata, self.sample_rate)
        
        # تحديد الموقع
        position = match_pattern(tdoas)
        
        # عرض النتائج
        if position is not None:
            print(f"\rموقع الصوت: {position}", end="", flush=True)
    
    def run(self, duration=10.0):
        """تشغيل العرض التوضيحي"""
        print("=" * 60)
        print("عرض توضيحي في الوقت الفعلي")
        print("=" * 60)
        print(f"المدة: {duration} ثانية")
        print("تكلم الآن...\n")
        
        with sd.InputStream(
            channels=self.channels,
            samplerate=self.sample_rate,
            callback=self.audio_callback,
            blocksize=self.buffer_size
        ):
            time.sleep(duration)
        
        print("\n\n" + "=" * 60)
        print("انتهى العرض التوضيحي")
        print("=" * 60)

if __name__ == "__main__":
    demo = RealTimeDemo()
    demo.run(duration=10.0)