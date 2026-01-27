<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:21:01+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "he"
}
-->
# שיעור 2 פיתוח סוכנים

ברוכים הבאים לשיעור השני של הקורס "בניית סוכן בינה מלאכותית מאפס עד לפרודקשן"!

בשיעור זה נסקור:

- הכלים ליצירת סוכני הבינה המלאכותית שלנו
  
- הוראות הגדרה למשאבי הפיתוח שלנו

- שיטות עבודה מומלצות לפיתוח סוכני בינה מלאכותית
  
- סקירת קוד ליצירת סוכני הבינה המלאכותית שלנו
  
נתחיל במבט על הכלים בהם נשתמש ליצירת סוכני הבינה המלאכותית שלנו.

## כלים והוראות הגדרה

### Microsoft Foundry

לגישה למודלים שפתיים גדולים (LLMs) נשתמש ב-[Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). יש עלויות הכרוכות בשימוש ב-Foundry, לכן בבקשה וודאו לעקוב אחרי ההוראות להקמת חשבון אם עדיין אין לכם גישה.

### מודלי OpenAI

דוגמאות הקוד לסוכנים בקורס זה מוגדרות להשתמש במודלים של OpenAI דרך [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

השתמשו במדריך זה כדי ללמוד כיצד לפרוס מודל באמצעות Foundry: [פרוס מודלים של Microsoft Foundry בפורטל Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

בחרו מודל GPT-4.1 או מתקדמים יותר לקורס זה.

### מסגרת סוכנים של Microsoft

כאמור קודם, נשתמש ב-[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) הן ליצירה והן לתזמור של סוכני הבינה המלאכותית שלנו.

להתקנת Microsoft Agent Framework וחבילות נוספות הנדרשות, הריצו את הפקודה הבאה בזמן שאתם בתיקיית השורש של הפרויקט הזה:

```bash
pip install -r requirements.txt
```

### הגדרת משתני .env

להרצת דוגמאות הקוד בקורס זה, תצטרכו ליצור קובץ `.env` בתיקיית השורש של הפרויקט הזה. 

כדי להקל, תוכלו להעתיק את קובץ `.env.example` המסופק:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לזכור כי תרגומים ממוחשבים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. למידע קריטי מומלץ לפנות לתרגום מקצועי על ידי מתרגם אנושי. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעת מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->