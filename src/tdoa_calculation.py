"""
وحدة حساب فروق زمن الوصول (TDOA) باستخدام GCC-PHAT
"""

import numpy as np
from numpy.fft import fft, ifft
from typing import List, Tuple

def gcc_phat(sig1: np.ndarray, sig2: np.ndarray, sample_rate: int) -> float:
    """
    حساب فرق زمن الوصول (TDOA) بين إشارتين باستخدام GCC-PHAT
    
    Args:
        sig1: الإشارة الأولى
        sig2: الإشارة الثانية
        sample_rate: معدل العيّنات
        
    Returns:
        فرق الزمن بالثواني
    """
    # حساب FFT
    SIG1 = fft(sig1)
    SIG2 = fft(sig2)
    
    # الارتباط المتقاطع المعمم
    R = SIG1 * np.conj(SIG2)
    R = R / np.abs(R + 1e-10)  # تطبيع PHAT
    
    # IFFT
    corr = ifft(R).real
    
    # إيجاد أقصى قيمة
    lag = np.argmax(corr) - len(sig1) // 2
    tdoa = lag / sample_rate
    
    return tdoa

def calculate_tdoa(audio_data: np.ndarray, sample_rate: int) -> List[float]:
    """
    حساب TDOAs بين القناة الأولى وجميع القنوات الأخرى
    
    Args:
        audio_data: بيانات صوتية (num_samples, num_channels)
        sample_rate: معدل العيّنات
        
    Returns:
        قائمة فروق الزمن (بالثواني)
    """
    num_channels = audio_data.shape[1]
    tdoas = []
    
    for ch in range(1, num_channels):
        tdoa = gcc_phat(audio_data[:, 0], audio_data[:, ch], sample_rate)
        tdoas.append(tdoa)
    
    return tdoas