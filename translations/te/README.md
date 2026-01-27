<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T10:09:05+00:00",
  "source_file": "README.md",
  "language_code": "te"
}
-->
# నולט నుంచి ప్రొడక్షన్ వరకు AI ఏజెంట్స్ నిర్మించడం

![నోల్ట్ నుంచి ప్రొడక్షన్ వరకు AI ఏజెంట్స్ నిర్మించడం](../../../../translated_images/te/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 బహుభాషా మద్దతు

#### GitHub చర్య ద్వారా మద్దతు (ఆటోమేటెడ్ & ఎప్పుడూ తాజాదైనది)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](./README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **స్థానికంగా క్లోన్ చేయాలని ఇష్టపడతారా?**

> ఈ రిపోజిటరీ 50+ భాషా అనువాదాలను కలిగి ఉండి, ఇది డౌన్‌లోడ్ పరిమాణాన్ని గణనీయంగా పెంచుతుంది. అనువదింపులు లేకుండా క్లోన్ చేయడానికి, స్పార్స్ చౌట్ ఉపయోగించండి:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ఇది కోర్సును పూర్తి చేసేందుకు అవసరమైన എല്ലാ అంశాలను చాలా వేగంగా డౌన్‌లోడ్ చేస్తుంది.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## AI ఏజెంట్ డెవలప్‌మెంట్ లైఫ్‌సైకిల్ మూలభూతాలు నేర్పించే కోర్సు

[![GitHub లైసెన్స్](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub సహకారులు](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub సమస్యలు](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub పుల్ రిక్వెస్టులు](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs స్వాగతం](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 ప్రారంభం

ఈ కోర్సు AI ఏజెంట్స్ నిర్మాణం మరియు అమలుపై మూలభూతాలు చూసే పాఠాలు కలిగి ఉంది.

ప్రతి పాఠం మునుపటి పాఠంపై ఆధారపడి ఉంటుంది, అందువల్ల మొదలు నుంచి ప్రారంభించి చివరికి వరకూ తరవాతగా సాగాలని మేము సిఫార్సు చేస్తాం.

మీకు AI ఏజెంట్ విషయాలపై మరింత అన్వేషించాలనిపిస్తే, మీరు [AI ఏజెంట్స్ ఫర్ బిగినర్స్ కోర్సు](https://aka.ms/ai-agents-beginners) చూడవచ్చు.

### ఇతర నేర్పరితో సమావేశమయ్యి, మీ ప్రశ్నలకు సమాధానాలు పొందండి

మీకు ఏ సమస్యలు వస్తే లేదా AI ఏజెంట్స్ గురించి ఏదైనా సందేహాలుంటే, మా ప్రత్యేక Discord చానల్‌లో చేరండి: [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### మీరు అవసరం పెట్టుకోవాలి

ప్రతి పాఠం దానికి సంబంధించిన కోడ్ నమూనా కలిగిఉంది, దీన్ని మీరు స్థానికంగా రన్ చేయవచ్చు. మీరు [ఈ రిపోను ఫోర్క్](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) చేసి మీ స్వంత కాపీ తయారు చేసుకోండి.

ఈ కోర్సులో ప్రస్తుతానికి ఈ క్రింది సదుపాయాలు వాడుతున్నాం:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

ప్రారంభించే ముందు ఈ సేవలకు మీకు యాక్సెస్ ఉండాలని దయచేసి నిర్ధారించుకోండి.

మోడల్ హోస్టింగ్ మరియు సేవలపై మరిన్ని ఎంపికలు త్వరలో అందుబాటులో ఉంటాయి.

## 🗃️ పాఠాలు

| **పాఠం**         | **వివరణ**                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| [ఏజెంట్ డిజైన్](./lesson-1-agent-design/README.md)       | మా "డెవలపర్ ఆన్‌బోర్డింగ్" ఏజెంట్ వినియోగ కేసుకు పరిచయం మరియు సమర్థవంతమైన ఏజెంట్లు ఎలా డిజైన్ చేయాలో  |
| [ఏజెంట్ డెవలప్‌మెంట్](./lesson-2-agent-development/README.md)  | Microsoft Agent Framework (MAF) ఉపయోగించి, కొత్త డెవలపర్లకు సహాయం చేసే 3 ఏజెంట్లు సృష్టించండి.       |
| [ఏజెంట్ ఎవాల్యూషన్స్](./lesson-3-agent-evals/README.md)  | Microsoft Foundry ఉపయోగించి, మా AI ఏజెంట్లు ఎలాంటి పనితీరు చూపిస్తున్నాయో తెలుసుకోండి మరియు మెరుగుపరచడం ఎలా అనేది నేర్చుకోండి. |
| [ఏజెంట్ డిప్లాయ్‌మెంట్](./lesson-4-agent-deployment/README.md)   | హోస్టెడ్ ఏజెంట్లు మరియు OpenAI చాట్‌కిట్ ఉపయోగించి, AI ఏజెంట్‌ను ప్రొడక్షన్‌లో ఎలా విడుదల చేయాలో చూడండి.       |


## 🎒 ఇతర కోర్సులు

మా టీమ్ ఇతర కోర్సులను తయారు చేస్తోంది! వీటిని చూసి తెలుసుకోండి:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### కోర్ లెర్నింగ్
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![డేటా సైన్స్ ఫర్ బిగినర్స్](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ఫర్ బిగినర్స్](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### కోపైలట్ సిరీస్
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## సహకారం

ఈ ప్రాజెక్ట్ సహకారాలు మరియు సూచనలను స్వాగతిస్తుంది. చాలా సహకారాలు మీరు ఒక
సహకారదారుల లైసెన్స్ ఒప్పందం (CLA)కు సంతకం చేయాల్సి ఉంటుంది అని ప్రకటించాలి, మీరు 
మీ సహకారాన్ని ఉపయోగించడానికి హక్కులు కలిగి ఉన్నారు మరియు నిజంగా హక్కులు ఇచ్చారనీ నిరూపించాలి. వివరాలకు, సందర్శించండి <https://cla.opensource.microsoft.com>.

మీరు ఒక పుల్ రిక్వెస్ట్ పంపినప్పుడు, CLA బెట్ ఆటోమేటిగ్గా మీరు CLA అందించాల్సిన అవసరం ఉందా మరియు PRను సరిపోయే విధంగా అలంకరించండి (ఉదా: స్థితి తనిఖీ, వ్యాఖ్య) అని నిర్ణయిస్తుంది. బట్ అందించే సూచనలు అనుసరించండి. మా CLA ఉపయోగించే అన్ని రెపోస్‌లో మీరు ఇది ఒక్కసారి మాత్రమే చేయాలి.

ఈ ప్రాజెక్ట్ [Microsoft ఓపెన్ సోర్స్ కోడ్ ఆఫ్ కాన్డక్ట్](https://opensource.microsoft.com/codeofconduct/)ను అనుసరించింది.
మరింత సమాచారం కోసం [కోడ్ ఆఫ్ కాన్డక్ట్ FAQ](https://opensource.microsoft.com/codeofconduct/faq/) చూడండి లేదా
ఏవైనా అదనపు ప్రశ్నలు లేదా వ్యాఖ్యల కోసం [opencode@microsoft.com](mailto:opencode@microsoft.com) తో సంప్రదించండి.

## ట్రేడ్మార్క్లు

ఈ ప్రాజెక్ట్ ప్రాజెక్టులు, ఉత్పత్తులు, లేదా సేవల ట్రేడ్మార్క్లు లేదా లోగోలను కలిగి ఉండవచ్చు. Microsoft
ట్రేడ్మార్క్ల లేదా లోగోల అధికారిక ఉపయోగం కింద ఉండాలి మరియు
[Microsoft యొక్క ట్రేడ్మార్క్ & బ్రాండ్ మార్గదర్శకాలు](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ని అనుసరించాలి.
ఇప్పటి ప్రాజెక్ట్ లో మోడిఫై చేసిన వెర్షన్లలో Microsoft ట్రేడ్మార్క్ లేదా లోగోల ఉపయోగం Microsoft స్పాన్సర్షిప్ను కలిగించనట్లు లేదా సందేహాన్ని కలిగించనట్లు ఉండకూడదు.
మూడవ పక్ష ట్రేడ్మార్క్లు లేదా లోగోలు ఉపయోగం ఆ తృతీయుల విధానాలకు అనుగుణంగా ఉంటుంది.

## సహాయం పొందడం

మీకు అడ్డంకి ఎదురైనట్లయితే లేదా AI అనువర్తనాలు రూపొందించినప్పుడు ఏవైనా ప్రశ్నలు ఉన్నట్లయితే, చేరండి:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

మీకు ఉత్పత్తి అభిప్రాయం లేదా లోపాలుంటే, నిర్మిస్తుండగా సందర్శించండి:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. నేను ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటిక్ అనువాదాలలో పొరపాట్లు లేదా లోపాలు ఉండవచ్చు. మూల డాక్యుమెంట్ దాని స్థానిక భాషలోనే అధికారిక మూలంగా పరిగణించాలి. కీలక సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫార్సు చేస్తాము. ఈ అనువాదం ఉపయోగించడంతో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదూడల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->