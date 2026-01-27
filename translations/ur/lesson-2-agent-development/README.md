<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:06:09+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "ur"
}
-->
# اسباق 2 ایجنٹ کی ترقی

"زیرو سے پروڈکشن تک AI ایجنٹ بنانے کا کورس" کے دوسرے سبق میں خوش آمدید!

اس سبق میں ہم درج ذیل موضوعات پر گفتگو کریں گے:

- ہمارے AI ایجنٹس بنانے کے لیے آلات
  
- ہمارے ترقیاتی وسائل کے لیے سیٹ اپ کی ہدایات

- AI ایجنٹ کی ترقی کی بہترین عملی تدابیر
  
- ہمارے AI ایجنٹس بنانے کے لیے کوڈ کا جائزہ
  
آئیں سب سے پہلے ان آلات کو دیکھیں جنہیں ہم اپنے AI ایجنٹس بنانے کے لیے استعمال کریں گے۔

## آلات اور سیٹ اپ کی ہدایات

### Microsoft Foundry

بڑے لینگویج ماڈلز (LLMs) تک رسائی کے لیے ہم [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) استعمال کریں گے۔ Foundry کے استعمال کے ساتھ کچھ لاگت منسلک ہوتی ہے، لہٰذا براہ کرم اکاؤنٹ سیٹ اپ کی ہدایات کو ضرور فالو کریں اگر آپ کے پاس پہلے سے رسائی نہیں ہے۔

### OpenAI ماڈلز

اس کورس میں ایجنٹ کوڈ کے نمونے OpenAI ماڈلز کو [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) کے ذریعے استعمال کرنے کے لیے ترتیب دیے گئے ہیں۔

Foundry استعمال کرتے ہوئے ماڈل تعینات کرنے کے طریقے سیکھنے کے لیے اس گائیڈ کا استعمال کریں: [Foundry پورٹل میں Microsoft Foundry ماڈلز تعینات کریں](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

اس کورس کے لیے GPT-4.1 یا اس کے بعد کا کوئی ماڈل منتخب کریں۔

### Microsoft Agent Framework

جیسا کہ پہلے ذکر کیا گیا، ہم اپنے AI ایجنٹس کو بنانے اور ان کی ترتیب دینے کے لیے [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) استعمال کریں گے۔

Microsoft Agent Framework اور دیگر مطلوبہ پیکجز کو انسٹال کرنے کے لیے، اس پروجیکٹ کی روٹ ڈائریکٹری میں درج ذیل کمانڈ چلائیں:

```bash
pip install -r requirements.txt
```

### .env ویریبلز سیٹ اپ کریں

اس کورس کے کوڈ نمونوں کو چلانے کے لیے، آپ کو اس پروجیکٹ کی روٹ ڈائریکٹری میں `.env` فائل بنانی ہوگی۔

آسانی کے لیے، آپ فراہم کردہ `.env.example` فائل کو کاپی کر سکتے ہیں:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ ذمہ داری**:  
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم اس بات کا خیال رکھیں کہ خودکار ترجموں میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز کو اس کی مادری زبان میں ہی مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے ہونے والے کسی بھی قسم کے غلط فہمی یا غلط تشریحات کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->