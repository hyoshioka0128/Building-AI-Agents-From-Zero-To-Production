<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:30:10+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "my"
}
-->
# Lesson 2 Agent Development

"Building AI Agent from Zero to Production Course" ၏ ဒုတိယသင်ခန်းစာသို့ စိတ်ကျေနပ်စွာ ကြိုဆိုပါတယ်။

ဒီသင်ခန်းစာမှာ ကျွန်တော်တို့ ကောက်နုတ်သွားမှာကတော့ -

- ကျွန်တော်တို့၏ AI Agent များကိုဖန်တီးရန် အသုံးပြုမည့် ကိရိယာများ

- ဖွံ့ဖြိုးတိုးတက်ရေးရင်းမြစ်များအတွက် ဆက်တင်ပြုလုပ်ခြင်းအညွှန့်အတမ်းများ

- AI Agent ဖွံ့ဖြိုးတိုးတက်ရေး ကျင့်စဉ်များ

- ကျွန်တော်တို့၏ AI Agent များကို ဖန်တီးခြင်းအတွက် ကုဒ် ခေါက်သရော

ကျွန်တော်တို့ရဲ့ AI Agent များဖန်တီးရာမှာ အသုံးပြုမယ့် ကိရိယာတွေကို ကြည့်ရှုခြင်းမှ စရအောင်။

## Tools and Setup Instructions

### Microsoft Foundry

ကြီးမားသောဘာသာစကားမော်ဒယ်များ (LLMs) သို့ 접근ရန် [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) ကို အသုံးပြုမည် ဖြစ်ပါသည်။ Foundry ကို အသုံးပြုရာတွင်ค่าใช้จ่าย ရှိနိုင်သောကြောင့် သင့်တွင် အကောင့်မရှိသေးလျှင် အကောင့်ဆက်တင် ပြုလုပ်ရန် လမ်းညွှန်ချက်များအတိုင်း လိုက်နာပေးပါ။

### OpenAI Models

ဒီသင်ခန်းစာရှိ agent ကုဒ်နမူနာများကို [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) မှ OpenAI မော်ဒယ်များ အသုံးပြုရန် ပြုစုပ်ထားပါသည်။

Foundry ကို အသုံးပြုပြီး မော်ဒယ်တစ်ခု ထည့်သွင်းရန် ဤလမ်းညွှန်ကို အသုံးပြုပါ - [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

ဤသင်ခန်းစာအတွက် GPT-4.1 သို့မဟုတ် နောက်ဆုံး မော်ဒယ်တစ်ခု ရွေးချယ်ပါ။

### Microsoft Agent Framework

မကြာသေးမီတွင် ရေးသားခဲ့သလို ကျွန်တော်တို့၏ AI Agent များ ဖန်တီးခြင်းနှင့် စီမံခန့်ခွဲခြင်းတွင် [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) ကို အသုံးပြုမှာ ဖြစ်ပါတယ်။

Microsoft Agent Framework နှင့် အခြားလိုအပ်သော package များကို သွင်းရန် ဒီ project ရဲ့ root directory မှာ အောက်ပါ command ကို run ပါ-

```bash
pip install -r requirements.txt
```

### Setup .env Variables

ဒီသင်ခန်းစာရှိကုဒ်နမူနာများကို run ဖို့၊ ဒီ project ရဲ့ root directory မှာ `.env` ဖိုင်တစ်ခု ဖန်တီးရမည် ဖြစ်ပါတယ်။

ပိုမိုအဆင်ပြေစေရန် ပေးထားသော `.env.example` ဖိုင်ကို ကူးယူနိုင်ပါသည် -

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အမိန့်ချမှု**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုပေးသည့် [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ တိကျမှန်ကန်မှုကို ကြိုးစားအားထုတ်ပေမယ့် အလိုအလျောက်ဘာသာပြန်ခြင်း ရလဒ်အနေဖြင့် အမှားများ သို့မဟုတ် မှန်ကန်မှုနည်းပါးမှုများရှိနိုင်သည်ကို သတိပြုပါရန် လိုအပ်ပါသည်။ မူရင်းစာရွက်စာတမ်းကို မိမိဘာသာစကားဖြင့် တရားဝင်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပြည့်စုံကျွမ်းကျင်သော လူမှန်ဘာသာပြန်အား အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းဖတ်သိခြင်းများအတွက် ကျနော်တို့ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->