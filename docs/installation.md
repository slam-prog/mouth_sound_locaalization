# 📥 التثبيت

## المتطلبات

- Python 3.8 أو أحدث
- نظام تشغيل: Windows, macOS, Linux
- جهاز صوتي بـ 4 قنوات على الأقل (مستحسن)

## التثبيت الأساسي

### 1. استنساخ المستودع

```bash
git clone https://github.com/YOUR_USERNAME/mouth-sound-localization.git
cd mouth-sound-localization
```

### 2. إنشاء بيئة افتراضية (مستحسن)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. تثبيت المتطلبات

```bash
pip install -r requirements.txt
```

### 4. تثبيت الحزمة (اختياري)

```bash
pip install -e .
```

## التثبيت المتقدم

### مع مكتبات التطوير

```bash
pip install -e ".[dev]"
```

### مع جميع المكتبات

```bash
pip install -e ".[dev,examples]"
```

## اختبار التثبيت

```bash
# تشغيل الاختبارات
pytest tests/

# تشغيل المحاكاة
python src/simulation.py

# تشغيل مثال أساسي
python examples/basic_usage.py
```

## استكشاف الأخطاء

### مشكلة: لا توجد أجهزة صوتية

```bash
# عرض الأجهزة المتاحة
python -c "import sounddevice as sd; sd.query_devices()"
```

### مشكلة: أخطاء في التبعيات

```bash
# تحديث pip
pip install --upgrade pip

# إعادة تثبيت المتطلبات
pip install -r requirements.txt --force-reinstall
```

## الخطوات التالية

- راجع [دليل API](api_reference.md)
- شغّل [الأمثلة](../examples/)
- اقرأ [نموذج العمل](business_model.md)