<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:10:17+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "hi"
}
-->
# पाठ 2 एजेंट विकास

"शून्य से उत्पादन तक एआई एजेंट निर्माण कोर्स" के दूसरे पाठ में आपका स्वागत है!

इस पाठ में हम निम्नलिखित विषयों को कवर करेंगे:

- हमारे एआई एजेंट बनाने के लिए उपकरण
  
- हमारे विकास संसाधनों के लिए सेटअप निर्देश

- एआई एजेंट विकास के सर्वोत्तम अभ्यास
  
- हमारे एआई एजेंट बनाने के लिए कोड वॉकथ्रू
  
आइए शुरू करें उन उपकरणों को देखकर जिनका उपयोग हम अपने एआई एजेंट बनाने के लिए करेंगे।

## उपकरण और सेटअप निर्देश

### Microsoft Foundry

लार्ज लैंग्वेज मॉडल्स (LLMs) तक पहुँच प्राप्त करने के लिए हम [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) का उपयोग करेंगे। Foundry के उपयोग के साथ कुछ लागत जुड़ी है इसलिए यदि आपके पास पहले से पहुँच नहीं है तो कृपया खाता सेटअप के निर्देशों का पालन करें।

### OpenAI मॉडल्स

इस कोर्स में एजेंट कोड सैंपल OpenAI मॉडल्स का उपयोग करने के लिए [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) के माध्यम से सेटअप किए गए हैं।

Foundry का उपयोग करके एक मॉडल तैनात करने के लिए इस गाइड का उपयोग करें: [Foundry पोर्टल में Microsoft Foundry मॉडल तैनात करें](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

इस कोर्स के लिए किसी एक GPT-4.1 या बाद के मॉडल को चुनें।

### Microsoft Agent Framework

जैसा कि पहले बताया गया था, हम अपने AI एजेंट बनाने और उनका समन्वय करने के लिए [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) का उपयोग करेंगे।

Microsoft Agent Framework और अन्य आवश्यक पैकेज स्थापित करने के लिए, इस प्रोजेक्ट की रूट डायरेक्टरी में निम्न कमांड चलाएं:

```bash
pip install -r requirements.txt
```

### .env वैरिएबल्स सेटअप करें

इस कोर्स के कोड सैंपल चलाने के लिए, आपको इस प्रोजेक्ट की रूट डायरेक्टरी में `.env` फाइल बनानी होगी।

इसे आसान बनाने के लिए, आप उपलब्ध `.env.example` फाइल की कॉपी कर सकते हैं:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। हम सटीकता के लिए प्रयासरत हैं, लेकिन कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रधान स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->