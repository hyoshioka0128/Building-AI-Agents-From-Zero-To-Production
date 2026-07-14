# שיעור 2 פיתוח סוכן

ברוכים הבאים לשיעור השני בקורס "בניית סוכן בינה מלאכותית מאפס עד הפקה"!

בשיעור זה נסקור:

- הכלים ליצירת סוכני הבינה המלאכותית שלנו
  
- הוראות התקנה למשאבי הפיתוח שלנו

- שיטות עבודה מומלצות לפיתוח סוכן בינה מלאכותית
  
- הסבר קוד ליצירת סוכני הבינה המלאכותית שלנו
  
נתחיל בהתבוננות בכלים שבהם נשתמש ליצירת סוכני הבינה המלאכותית שלנו.

## כלים והוראות התקנה

### Microsoft Foundry

לגישה למודלים שפתיים גדולים (LLMs) נשתמש ב-[Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). יש עלויות הכרוכות בשימוש ב-Foundry, אז ודאו לעקוב אחר הוראות ההתקנה אם אין לכם גישה כבר.

### מודלי OpenAI

דוגמאות הקוד לסוכן בקורס זה מוגדרות להשתמש במודלים של OpenAI דרך [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

השתמשו במדריך זה כדי ללמוד כיצד לפרוס מודל באמצעות Foundry: [פרוס מודלי Microsoft Foundry בפורטל Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

בחרו מודל אחד מסדרת GPT-5 (למשל `gpt-5.1`) עבור הקורס הזה. הימנעו ממודלים שיצאו משימוש כגון GPT-4o ו-GPT-4.1, אשר מגיעים לסוף החיים ב-2026.

### Microsoft Agent Framework

כפי שהוזכר קודם, נשתמש ב-[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) כדי ליצור וגם לארגן את סוכני הבינה המלאכותית שלנו.

תזדקקו ל-**Python 3.12 או חדש יותר**. להתקין את Microsoft Agent Framework וחבילות נוספות הנחוצות, הריצו את הפקודה הבאה בזמן שאתם בתיקיית השורש של הפרויקט:

```bash
pip install -r requirements.txt
```

### אימות עם Azure

הסוכנים מאמתים את עצמם מול Microsoft Foundry באמצעות אישורי Azure CLI שלכם
(`AzureCliCredential`), לכן יש להיכנס לפני הרצת כל דוגמה:

```bash
az login
# אם יש לך יותר מהמנוי אחד, בחר את זה עם פרויקט Foundry שלך:
az account set --subscription "<your-subscription-id>"
```

ודאו שהחשבון שלכם כולל את התפקיד **Azure AI User** (או שווה ערך) בפרויקט Foundry
כדי שיוכל לקרוא ל-API של המודל והסוכן.

### הגדרת משתני .env

כדי להריץ את דוגמאות הקוד בקורס זה, תצטרכו ליצור קובץ `.env` בתיקיית השורש של הפרויקט.

כדי להקל, תוכלו להעתיק את קובץ הדוגמה `.env.example` שסופק:

```bash
cp .env.example .env
``` 

לאחר מכן מלאו את שני המשתנים שהסוכנים קוראים (ה-`FoundryChatClient` מאתר אותם
אוטומטית):

| משתנה | מה זה | איפה למצוא אותו |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | נקודת הקצה של **פרויקט** Foundry שלכם, שמסתיימת ב- `/api/projects/<project>` | פורטל Foundry → הפרויקט שלכם → **סקירה כללית** → *נקודות קצה* |
| `FOUNDRY_MODEL` | שם פריסת המודל שבו הסוכנים שלכם רצים (למשל `gpt-5.1`) | פורטל Foundry → **מודלים + נקודות קצה** |

### יצירת מאגר וקטורי של עובדים

דוגמה אחת — **סוכן חיפוש עובדים** — מחפש בתיקיית עובדים השמורה ב-
Microsoft Foundry **מאגר וקטורי**. צרו אותו פעם אחת והעתיקו את ה-ID המודפס לתוך `.env`
תחת `VECTOR_STORE_ID` (הריצו מתיקיית השורש של מאגר הקוד כדי שיקרא את `.env` שלכם):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### הרצת דוגמה

כל סוכן מריץ ממשק DevUI מקומי משלו. לדוגמה:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

לאחר מכן פתחו את כתובת ה-URL המודפסת `http://localhost:<port>` בדפדפן שלכם כדי לשוחח עם הסוכן.

## הסוכנים בשיעור זה

כל דוגמה היא סוכן עצמאי שנבנה עם Microsoft Agent Framework. ביחד הם
מממשים את התרחישים שתכננתם ב-[שיעור 1](../lesson-1-agent-design/README.md):

| דוגמה | תרחיש שיעור 1 | הכלי שבו השתמשו | פורט |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | תרחיש 1 — חיפוש עובדים | חיפוש בקבצים שמוקרן ע"י Foundry על מאגר וקטורי | 8090 |
| `task-recommendation-agent.py` | תרחיש 2 — המלצת משימות | שרת **GitHub MCP** (כלי MCP מתארח) | 8095 |
| `azure-learning-agent.py` | תרחיש 3 — עוזר קוד (מחקר) | שרת **Microsoft Learn MCP** (כלי MCP מתארח) | 8092 |
| `coding-agent.py` | תרחיש 3 — עוזר קוד (קוד) | **מתרגם קוד** | 8093 |
| `learning-recommendation-agent.py` | סוכן תומך | Learn MCP + הסקה | 8091 |
| `agent-orchestration.py` | מקשר בין התרחישים | תזמור **העברת משימות** מרובי סוכנים | 8094 |

> **הערה על סוכן המלצת המשימות.** `task-recommendation-agent.py` זקוק ל-
> `GITHUB_PERSONAL_ACCESS_TOKEN` בקובץ `.env` שלכם (צרו אחד בכתובת
> <https://github.com/settings/personal-access-tokens/new>). הסוכן קורא פעילות אחרונה
> ב-GitHub של המפתח וממליץ על 1–3 סוגיות פתוחות שתואמות — בדיוק לפי עיצוב תרחיש 2.
> זוהי הדוגמה היחידה שקוראת ל-GitHub; האחרות זקוקות רק לפרויקט ה-Foundry שלכם.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->