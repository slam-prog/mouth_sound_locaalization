# 🤝 المساهمة في المشروع

نرحب بمساهماتكم في مشروع **Mouth Sound Localization System**!

## 📋 كيفية المساهمة

### 1. التفرع (Fork)
اضغط على زر **Fork** في أعلى الصفحة لإنشاء نسخة من المشروع.

### 2. الاستنساخ (Clone)
```bash
git clone https://github.com/YOUR_USERNAME/mouth-sound-localization.git
cd mouth-sound-localization
```

### 3. إنشاء فرع جديد
```bash
git checkout -b feature/your-feature-name
```

### 4. إجراء التغييرات
- اتبع معايير الكود (انظر أدناه)
- أضف اختبارات للتغييرات الجديدة
- حدّث التوثيق إذا لزم الأمر

### 5. الالتزام (Commit)
```bash
git add .
git commit -m "feat: إضافة ميزة جديدة

وصف تفصيلي للتغييرات"
```

### 6. الرفع (Push)
```bash
git push origin feature/your-feature-name
```

### 7. طلب السحب (Pull Request)
افتح Pull Request من فرعك إلى `main`.

## 📏 معايير الكود

### التنسيق
- استخدم 4 مسافات للـ indentation
- اتبع [PEP 8](https://pep8.org/)
- استخدم `black` للتنسيق التلقائي:
  ```bash
  black src/ tests/ examples/
  ```

### التسمية
- **الدوال**: `snake_case` (مثال: `calculate_tdoa`)
- **الفئات**: `PascalCase` (مثال: `AudioCapture`)
- **الثوابت**: `UPPER_CASE` (مثال: `SAMPLE_RATE`)

### الاختبارات
- أضف اختبارات لكل ميزة جديدة
- تأكد من نجاح جميع الاختبارات:
  ```bash
  pytest tests/ -v
  ```

### التوثيق
- استخدم docstrings لجميع الدوال والفئات
- حدّث `README.md` إذا أضفت ميزات جديدة

## 🐛 الإبلاغ عن الأخطاء

### إنشاء Issue
1. اذهب إلى تبويب **Issues**
2. اضغط **New Issue**
3. اختر القالب المناسب:
   - 🐛 Bug Report
   - ✨ Feature Request
   - 📚 Documentation

### وصف المشكلة
- وصف واضح ومفصل
- خطوات لإعادة الإنتاج
- النتيجة المتوقعة vs الفعلية
- بيئة التشغيل (OS, Python version)

## 💡 اقتراح ميزة جديدة

### قبل الاقتراح
- تحقق من وجود الميزة بالفعل
- ابحث في Issues السابقة

### في الاقتراح
- وصف الميزة
- الفائدة المرجوة
- أمثلة استخدام مقترحة

## 📊 أنواع المساهمات

| النوع | الوصف |
|-------|-------|
| 🐛 Bug Fix | إصلاح خطأ |
| ✨ Feature | ميزة جديدة |
| 📚 Docs | تحسين التوثيق |
| 🧪 Tests | إضافة اختبارات |
| 🎨 Style | تحسين التنسيق |
| ♻️ Refactor | إعادة هيكلة الكود |
| ⚡ Performance | تحسين الأداء |
| 🌐 i18n | ترجمة/لغات |

## 🙏 الشكر

جميع المساهمين سيُذكرون في قسم [المساهمون](README.md#-الشكر-والتقدير).

**شكرًا لمساهمتكم! 🎉**