# أفاق مستقبلية
# Tanweer Core & 3D Acoustic Positioning System 🚀

An autonomous, ultra-lightweight, and human-led open-source project for 3D acoustic localization and voice tracking. It features the breakthrough "Tanweer" algorithm, operating completely in the time domain without relying on Fourier Transforms (FFT), making it tailored for low-power embedded processors like the RP2040.

---


## 💡 الرؤية الهندسية وفلسفة الابتكار (Core Concept)

تعتمد المنظومات التقليدية لتحديد اتجاه الصوت (DoA) على إشارات منتظمة، وتفشل غالباً أمام عشوائية الترددات الصوتية البشرية وتعدد اللغات. يكمن ابتكار هذا المشروع في كسر هذا القيد عبر منظومة عتادية ورياضية متكاملة تعتمد على **"التموضع الحركي النسبي"** وبساطة التصميم المسانِد للتكنولوجيا الحالية.

### 📐 التصميم الهندسي للمصفوفة (Hardware Topology)
يتكون النظام من **مصفوفة خماسية الميكروفونات (5-Mic Array)** موزعة هندسياً في الفضاء ثلاثي الأبعاد كالتالي:
* **نقطة الأصل (0,0,0):** ميكروفون مركزي [Mic 1] لضبط محاور الإحداثيات الديكارتية.
* **محاور الفضاء (X, Y, Z):** ثلاثة ميكروفونات محيطية [Mic 2, Mic 3, Mic 4] تغطي أبعاد الفراغ بالكامل.
* **الميكروفون الخامس (المرجع الداني - Close Reference):** يوضع في أقرب نقطة ممكنة من فم المتكلم ليلتقط الإشارة الصوتية الخام لحظة تولدها (\(T_0\)).

```text
                     +Z (محور الارتفاع)
                      |
                      |   [Mic 4] (0, 0, d)
                      |
                      |
                      |
                      |
                      |_______________________ +Y (محور السمت)
                     / 0,0,0
                    /  [Mic 1] (مركزي) \
                   /                    \  [Mic 3] (0, d, 0)
                  /                      \
                 /                        \
               +X                          \
         (محور العرض)                       \
         [Mic 2] (d, 0, 0)                   \
                                              ▼
                                      [Mic 5] (المرجع الداني)
                                    (Close-talk Reference)
                                     [T0 - البصمة الزمنية الثابتة]
```

### 🧠 آلية العمل والرياضيات الحركية (How it Works)
إذا قمنا بتبسيط المفهوم؛ فإن مستشعر المسافة فوق الصوتي التقليدي (Ultrasonic) يقيس الزمن الذي تستغرقه موجة "معلومة ومنتظمة" للذهب والإياب. 

تخيل الآن **6 سماعات** موزعة بشكل عشوائي، تعمل سماعة واحدة منها فقط في كل مرة لتبث كلاماً بشرياً عشوائياً مستحيل التنبؤ بتردداته، مع جهل تام بزمن الانتقال بينها. كيف نحدد السماعة المتكلمة بدقة وفيزيائية تامة؟

هنا يتدخل العقل البشري عبر **خوارزمية تنوير في النطاق الزمني النسبي**:
1. **تحييد شدة الصوت (Gain-Invariance):** يتم أخذ العينة الصوتية الحية لكل ميكروفون وتحويل قيمها إلى **نسب داخلية هندسية**. بفضل هذه الخطوة، لا يهم إذا كان صوت المتحدث عالياً أم منخفضاً؛ فالمقارنة تتم بالتساوي التام لأن البصمة النسبية للموجة ثابتة.
2. **التقاط المرجع ($T_0$):** يلتقط الميكروفون الخامس القريب الصوت فوراً، ليعمل كبصمة زمنية مرجعية ثابتة (Zero-Time Baseline) تخترق عشوائية الكلام البشري.
3. **التدوير والطرح المباشر (Circular Shift & Subtraction):** بدلاً من إرهاق المعالج بحسابات تحويل فورير (FFT) المعقدة، تقوم الخوارزمية بعملية **طرح حسابي مباشر وبسيط** بين مصفوفة الميكروفون المحيطي ومصفوفة المرجع بعد تدويرها دائرياً (Circular Roll) خطوة تلو الأخرى.
4. **اقتناص الفارق الزمني:** خطوة التدوير التي تعطي **أقل ناتج لعملية الطرح (Minimum Absolute Error)** هي مباشرة الفارق الزمني الدقيق (TDOA) المستغرق لوصول الصوت من فم المتكلم إلى ذلك الميكروفون.
5. **التثليث الفضائي (Spatial Trilateration):** يتم تحويل هذه الفروق الزمنية المحسوبة بلا جهد معالجة إلى مسافات فيزيائية دقيقة، لمعادلة نقطة نشوء الصوت $P(r, \theta, \phi)$ ضمن نظام الإحداثيات الكروية.


# Tanweer Core Algorithm (خوارزمية تنوير البرمجية المستقلة) 🚀

An autonomous, ultra-fast, and pure software framework designed for high-performance data fingerprinting and universal Speech-to-Text conversion. It operates entirely in the time domain on standard computers, **requiring zero specialized hardware, zero microphone arrays, and zero Fourier Transforms (FFT)**.

---

## 💡 The Core Concept & Language Breakthrough (الفكرة الرائدة واختراق حواجز اللغة)

Traditional Speech-to-Text engines (like Whisper or Google Speech) fail to break language barriers because they rely on massive acoustic dictionaries and language-specific training models. **Tanweer** bypasses this computational bottleneck by analyzing the **internal geometric ratios and relative time-domain dynamics** of digital audio signals.

### 🧠 How it Breaks Language Barriers Dynamically (بدون قواميس أو لغات مسبقة)
Human speech, regardless of the language spoken (Arabic, English, Japanese), is physically produced by the same phonetic articulation paths (Lips, Teeth, Palate, Throat). These physical movements leave a permanent, quantifiable **"Relative Time-Domain Signature"** inside the digital audio file.

Tanweer decodes this signature using a highly optimized, hardware-free software pipeline:

1. **Volume & Pitch Invariance (تحويل الإشارة إلى نسب):** The algorithm converts raw digital audio samples into internal proportional ratios. This normalizes the file, making the analysis completely immune to whether the voice is loud, quiet, high-pitched, or low-pitched.
2. **Time-Domain Comparison via Circular Roll (التدوير والطرح المباشر):** Instead of exhausting the CPU with heavy Fourier Transforms (FFT), Tanweer performs a sequence of circular shifts (`numpy.roll` logic) on the audio matrix, calculating the mathematical absolute difference at each step.
3. **Painless Delay Catching:** The specific rotation index that yields the **Absolute Minimum Subtraction Error** instantly reveals the internal time-delay signature of the speech mechanics.
4. **Instant Text Generation:** The system translates these mechanical signatures directly into universal text characters based on the physical articulation source, bypassing standard dictionaries and achieving instant, cross-lingual translation and transcription with total privacy.

---
## 🕊️ Ethical & Humanitarian Mandate (اللتزام الأخلاقي)
This pure software technology is bound by a strict humanitarian decree by its author, Engineer Naguib: It is exclusively permitted for healthcare, medical translation, assistive typing, and educational tools, and is strictly prohibited from any surveillance or military operations.

---

## 🚀 الآفاق التطبيقية والأثر الإنساني (Disruptive Applications)

النجاح في صياغة هذا المنطق الرياضي والعتادي البسيط يفتح الباب لطفرة تكنولوجية هائلة:

* **الترجمة الفورية والدبلوماسية الرقمية (Real-Time Translation):** يتيح بناء تطبيقات ذكية للهواتف (سواء وجهاً لوجه أو من هاتف إلى هاتف) قادرة على تحديد لغة المتحدث فورياً بناءً على فسيولوجيا نطق الحروف، وترجمتها فوراً للمستمع بلغته الأم، مما يلغي حواجز اللغة تماماً ويحقق تقارباً إنسانياً وتلاقحاً معرفياً كبيراً.
* **حصن الخصوصية ومكافحة التزييف الصوتي (Anti-Deepfake):** أنظمة الذكاء الاصطناعي التوليدي اليوم تستطيع تقليد نبرة الصوت، ولكنها **مستحيلة القدرة على تزييف البصمة الفيزيائية والزاوية الحركية لنشوء الصوت** من الجهاز التنفسي البشري حقيقي. يمثل هذا النظام بمثابة جدار حماية حيوي يمنع اختراق وانتحال الشخصيات رقمياً.
* **التشخيص الطبي الرقمي (Vocal Diagnostics):** رصد وتتبع اعتلالات الحنجرة، أمراض الحبسة الكلامية، والتغيرات العصبية العضلية بدقة متناهية [٠.١.١١].

## 🕊️ الالتزام الأخلاقي والإنساني (Ethical Mandate)
بناءً على شرط مبتكر الخوارزمية، المهندس نجيب، فإن هذه التكنولوجيا مفتوحة المصدر محمية بشرط إنساني صارم: يُسمح باستخدامها **حصرياً** في الأغراض الطبية، التأهيلية، حماية الخصوصية، والخدمات المدنية لتقريب البشر، ويُحظر حظراً تاماً استخدامها في أي تطبيقات عسكرية أو تجسسية أو ضارة.
