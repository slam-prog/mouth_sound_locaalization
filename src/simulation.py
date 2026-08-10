"""
وحدة المحاكاة الكاملة للنظام
"""

import numpy as np
from .audio_capture import AudioCapture
from .tdoa_calculation import calculate_tdoa
from .relative_pattern_matching import match_pattern

def generate_test_signal(duration: float = 0.01, sample_rate: int = 192000, frequency: int = 1000) -> np.ndarray:
    """توليد إشارة اختبار"""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    window = np.hanning(len(signal))
    return signal * window

def run_simulation(num_sources: int = 5, sample_rate: int = 192000, verbose: bool = True):
    """
    تشغيل محاكاة كاملة
    
    Args:
        num_sources: عدد مصادر الصوت
        sample_rate: معدل العيّنات
        verbose: عرض تفاصيل
    """
    print("=" * 60)
    print("محاكاة نظام تحديد موقع الصوت من الفم")
    print("=" * 60)
    
    # مواقع الميكروفونات
    mic_positions = np.array([
        [1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, -1.0, 0.0]
    ])
    
    # مصادر صوت عشوائية
    np.random.seed(42)
    source_positions = np.random.uniform(-0.3, 0.3, (num_sources, 3))
    
    results = []
    
    for i, source_pos in enumerate(source_positions):
        if verbose:
            print(f"\n--- مصدر صوت {i+1} ---")
            print(f"الموقع الحقيقي: {source_pos}")
        
        # محاكاة التسجيل (مبسّط)
        # ... (كود المحاكاة الكامل)
        
        results.append({
            'source': source_pos,
            'estimated': None,  # سيتم حسابه
            'error': None
        })
    
    # عرض النتائج
    print("\n" + "=" * 60)
    print("ملخص النتائج")
    print("=" * 60)
    
    return results

if __name__ == "__main__":
    run_simulation()