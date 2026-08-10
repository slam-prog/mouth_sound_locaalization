"""
اختبارات وحدة حساب TDOA
"""

import numpy as np
import pytest
from src.tdoa_calculation import gcc_phat, calculate_tdoa

class TestGCCPHAT:
    """اختبارات دالة GCC-PHAT"""
    
    def test_zero_delay(self):
        """اختبار إشارة بدون تأخير"""
        sample_rate = 192000
        t = np.linspace(0, 0.01, int(sample_rate * 0.01))
        signal = np.sin(2 * np.pi * 1000 * t)
        
        tdoa = gcc_phat(signal, signal, sample_rate)
        assert abs(tdoa) < 1e-6, "يجب أن يكون التأخير صفرًا"
    
    def test_known_delay(self):
        """اختبار تأخير معروف"""
        sample_rate = 192000
        delay_seconds = 0.0001  # 100 ميكروثانية
        delay_samples = int(delay_seconds * sample_rate)
        
        t = np.linspace(0, 0.01, int(sample_rate * 0.01))
        signal1 = np.sin(2 * np.pi * 1000 * t)
        signal2 = np.zeros_like(signal1)
        signal2[delay_samples:] = signal1[:-delay_samples]
        
        tdoa = gcc_phat(signal1, signal2, sample_rate)
        assert abs(tdoa - delay_seconds) < 1e-5, f"التأخير المقاس {tdoa} يجب أن يكون قريبًا من {delay_seconds}"

class TestCalculateTDOA:
    """اختبارات دالة حساب TDOA"""
    
    def test_multi_channel(self):
        """اختبار إشارة متعددة القنوات"""
        sample_rate = 192000
        num_samples = int(sample_rate * 0.01)
        num_channels = 4
        
        audio_data = np.random.randn(num_samples, num_channels)
        tdoas = calculate_tdoa(audio_data, sample_rate)
        
        assert len(tdoas) == num_channels - 1, "يجب أن يكون عدد TDOAs = num_channels - 1"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])