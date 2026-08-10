# 📚 مرجع API

## الفئات الرئيسية

### AudioCapture

```python
from src import AudioCapture

capture = AudioCapture(channels=4, sample_rate=192000)
audio_data = capture.record(duration=1.0)
```

**الوسائط:**
- `channels` (int): عدد القنوات
- `sample_rate` (int): معدل العيّنات
- `device` (int, optional): جهاز التسجيل

**الطرق:**
- `record(duration)`: تسجيل الصوت
- `list_devices()`: عرض الأجهزة المتاحة

### calculate_tdoa

```python
from src import calculate_tdoa

tdoas = calculate_tdoa(audio_data, sample_rate=192000)
```

**المدخلات:**
- `audio_data` (np.ndarray): بيانات صوتية (num_samples, num_channels)
- `sample_rate` (int): معدل العيّنات

**المخرجات:**
- `List[float]`: قائمة فروق الزمن (ثواني)

### match_pattern

```python
from src import match_pattern

position = match_pattern(tdoas)
```

**المدخلات:**
- `tdoas` (List[float]): قائمة فروق الزمن

**المخرجات:**
- `np.ndarray`: الموقع المقدّر (x, y, z)

## دوال مساعدة

### gcc_phat

```python
from src.tdoa_calculation import gcc_phat

tdoa = gcc_phat(signal1, signal2, sample_rate)
```

## أمثلة متقدمة

### معالجة في الوقت الفعلي

```python
import sounddevice as sd
from src import calculate_tdoa, match_pattern

def callback(indata, frames, time, status):
    tdoas = calculate_tdoa(indata, sample_rate)
    position = match_pattern(tdoas)
    print(f"الموقع: {position}")

with sd.InputStream(callback=callback, channels=4, samplerate=192000):
    while True:
        sd.sleep(1000)
```

### دمج مع Whisper

```python
import whisper
from src import AudioCapture, calculate_tdoa, match_pattern

model = whisper.load_model("base")
capture = AudioCapture(channels=4)
audio = capture.record(duration=3.0)

tdoas = calculate_tdoa(audio, 192000)
position = match_pattern(tdoas)

mono = audio.mean(axis=1)
result = model.transcribe(mono)
print(f"النص: {result['text']}")
print(f"الموقع: {position}")
```