"""
وحدة التقاط الصوت من الميكروفونات
"""

import numpy as np
import sounddevice as sd
from typing import Optional

class AudioCapture:
    """
    فئة لالتقاط الصوت من多个 قنوات
    
    Args:
        channels: عدد القنوات (الميكروفونات)
        sample_rate: معدل العيّنات (Hz)
        device: جهاز التسجيل (اختياري)
    """
    
    def __init__(self, channels: int = 4, sample_rate: int = 192000, device: Optional[int] = None):
        self.channels = channels
        self.sample_rate = sample_rate
        self.device = device
        
    def record(self, duration: float = 1.0) -> np.ndarray:
        """
        تسجيل الصوت لمدة محددة
        
        Args:
            duration: مدة التسجيل بالثواني
            
        Returns:
            مصفوفة من البيانات الصوتية (num_samples, channels)
        """
        num_samples = int(self.sample_rate * duration)
        
        print(f"جاري التسجيل لمدة {duration} ثانية...")
        audio_data = sd.rec(
            num_samples,
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype='float32',
            device=self.device
        )
        sd.wait()
        print("تم التسجيل.")
        
        return audio_data
    
    def list_devices(self):
        """عرض أجهزة التسجيل المتاحة"""
        devices = sd.query_devices()
        print("أجهزة التسجيل المتاحة:")
        for i, dev in enumerate(devices):
            if dev['max_input_channels'] > 0:
                print(f"  {i}: {dev['name']} ({dev['max_input_channels']} قنوات)")