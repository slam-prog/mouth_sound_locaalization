"""
دوال مساعدة عامة
"""

import numpy as np
from typing import Tuple

def calculate_distance(pos1: np.ndarray, pos2: np.ndarray) -> float:
    """حساب المسافة بين نقطتين"""
    return np.linalg.norm(pos1 - pos2)

def normalize_vector(vector: np.ndarray) -> np.ndarray:
    """تطبيع متجه"""
    norm = np.linalg.norm(vector)
    if norm > 0:
        return vector / norm
    return vector

def add_noise(signal: np.ndarray, snr_db: float = 20) -> np.ndarray:
    """
    إضافة ضوضاء لإشارة
    
    Args:
        signal: الإشارة الأصلية
        snr_db: نسبة الإشارة إلى الضوضاء (dB)
    
    Returns:
        إشارة مع ضوضاء
    """
    signal_power = np.mean(signal ** 2)
    noise_power = signal_power / (10 ** (snr_db / 10))
    noise = np.random.randn(*signal.shape) * np.sqrt(noise_power)
    return signal + noise

def save_audio(audio_data: np.ndarray, filename: str, sample_rate: int):
    """حفظ الصوت في ملف WAV"""
    import soundfile as sf
    # تطبيع إلى [-1, 1]
    audio_normalized = audio_data / np.max(np.abs(audio_data))
    sf.write(filename, audio_normalized, sample_rate)

def load_audio(filename: str) -> Tuple[np.ndarray, int]:
    """تحميل الصوت من ملف WAV"""
    import soundfile as sf
    data, sample_rate = sf.read(filename)
    return data, sample_rate