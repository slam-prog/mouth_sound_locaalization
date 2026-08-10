"""
وحدة مطابقة الأنماط النسبية لتحديد الموقع
"""

import numpy as np
from typing import Tuple, Optional, List

class RelativePatternMatcher:
    """
    فئة لمطابقة الأنماط النسبية لتحديد موقع الصوت
    """
    
    def __init__(self, mic_positions: np.ndarray, search_range: float = 0.5, grid_resolution: int = 21):
        """
        Args:
            mic_positions: مواقع الميكروفونات (num_mics, 3)
            search_range: مدى البحث (وحدات نسببة)
            grid_resolution: دقة الشبكة
        """
        self.mic_positions = mic_positions
        self.search_range = search_range
        self.grid_resolution = grid_resolution
        
        # بناء شبكة البحث
        self._build_search_grid()
    
    def _build_search_grid(self):
        """بناء شبكة من المواقع المحتملة"""
        x_range = np.linspace(-self.search_range, self.search_range, self.grid_resolution)
        y_range = np.linspace(-self.search_range, self.search_range, self.grid_resolution)
        z_range = np.linspace(-self.search_range, self.search_range, self.grid_resolution // 2)
        
        self.search_grid = []
        for x in x_range:
            for y in y_range:
                for z in z_range:
                    self.search_grid.append(np.array([x, y, z]))
        
        self.search_grid = np.array(self.search_grid)
    
    def _calculate_relative_delays(self, source_pos: np.ndarray) -> np.ndarray:
        """حساب التأخيرات النسبية لموقع معين"""
        distances = np.linalg.norm(self.mic_positions - source_pos, axis=1)
        reference = distances[0]
        return distances - reference
    
    def _calculate_ratios(self, delays: np.ndarray) -> np.ndarray:
        """حساب النسب من التأخيرات"""
        reference = delays[0]
        if abs(reference) < 1e-10:
            reference = 1e-10
        return delays[1:] / reference
    
    def match(self, measured_tdoas: List[float]) -> Tuple[Optional[np.ndarray], float]:
        """
        مطابقة TDOAs مقاسة مع المواقع المحتملة
        
        Args:
            measured_tdoas: قائمة فروق الزمن المقاسة
            
        Returns:
            (الموقع المقدّر, خطأ المطابقة)
        """
        measured_tdoas = np.array(measured_tdoas)
        measured_ratios = measured_tdoas / (measured_tdoas[0] + 1e-10)
        
        best_match = None
        min_error = float('inf')
        
        for candidate_pos in self.search_grid:
            expected_delays = self._calculate_relative_delays(candidate_pos)
            expected_ratios = self._calculate_ratios(expected_delays)
            
            error = np.linalg.norm(measured_ratios - expected_ratios)
            
            if error < min_error:
                min_error = error
                best_match = candidate_pos.copy()
        
        return best_match, min_error

def match_pattern(tdoas: List[float], mic_positions: Optional[np.ndarray] = None) -> Optional[np.ndarray]:
    """
    دالة مساعدة لمطابقة نمط TDOA
    
    Args:
        tdoas: قائمة فروق الزمن
        mic_positions: مواقع الميكروفونات (اختياري)
        
    Returns:
        الموقع المقدّر
    """
    if mic_positions is None:
        # مواقع افتراضية (ميكروفونات على هيدفون)
        mic_positions = np.array([
            [1.0, 0.0, 0.0],
            [-1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, -1.0, 0.0]
        ])
    
    matcher = RelativePatternMatcher(mic_positions)
    position, error = matcher.match(tdoas)
    
    return position