# Lesson 2 Agent Development

Welcome to the second lesson of the  "Building AI Agent from Zero to Production Course"!

In this lesson we will cover:

- Инструментите за създаване на нашите AI агенти
  
- Инструкции за настройка на нашите ресурси за разработка

- Най-добри практики за разработка на AI агенти
  
- Преглед на кода за създаване на нашите AI агенти
  
Let's start by looking at the tools we will use to create our AI Agents.

## Tools and Setup Instructions

### Microsoft Foundry

За достъп до големи езикови модели (LLMs) ще използваме [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Използването на Foundry има свързани разходи, затова моля следвайте инструкциите за настройка на акаунт, ако все още нямате достъп.

### OpenAI Models

Примерите с код за агентите в този курс са настроени да използват OpenAI модели чрез [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Използвайте това ръководство, за да научите как да внедрите модел с помощта на Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Изберете един модел GPT-4.1 или по-нова версия за този курс.

### Microsoft Agent Framework

Както беше споменато по-рано, ние ще използваме [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), за да създаваме и оркестрираме нашите AI агенти.

За да инсталирате Microsoft Agent Framework и другите необходими пакети, изпълнете следната команда докато сте в коренната директория на този проект:

```bash
pip install -r requirements.txt
```

### Setup .env Variables

За да стартирате примерите с код в този курс, ще трябва да създадете `.env` файл в коренната директория на този проект.

За по-лесно, можете да копирате предоставения файл `.env.example`:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за всякакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->