# AGENTS.md

या रेपॉझिटरीमध्ये कार्यरत AI कोडिंग एजंट्स (आणि मानवी सहयोगी) साठी मार्गदर्शन. आपण जर
येथे बदल करणारे स्वयंचलित एजंट असाल, तर प्रथम हा फाइल वाचा आणि त्याचा पाठपुरावा करा.

## ही रेपॉझिटरी काय आहे

**Building AI Agents from Zero to Production** ही मायक्रोसॉफ्टची शिकण्याची कोर्स आहे. हे विकसकांना
**Microsoft Foundry** वापरून AI एजंट्स डिझाइन, बांधकाम, मूल्यांकन, तैनात आणि ऑपरेट करायला शिकवते,
जे Microsoft Agent Framework (MAF) वापरते. सामग्री धड्यांच्या मालिकेत आयोजित केलेली आहे, प्रत्येकासोबत
`README.md` आणि चालवता येणारे Python नमुने असतात.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

मूळ दस्तऐवज: `README.md` (इथे सुरू करा), `MIGRATION-GUIDE.md` (SDK स्थलांतरण तपशील), `CHANGELOG.md`.

## सुवर्ण नियम

1. **कधीही गुपिते कमिट करू नका.** फक्त `*.env.example` फाइल्स ट्रॅक केल्या जातात; वास्तविक `.env` फाइल्स
   git-ignored आहेत. नमुन्यांमध्ये किंवा दस्तऐवजांमध्ये एंडपॉइंट्स, कीज, टोकन्स किंवा कनेक्शन स्ट्रिंग्ज हार्डकोड करू नका.
2. **`translations/` किंवा `translated_images/` स्पर्श करू नका.** हे स्वयंचलितपणे
   एका ट्रान्सलेशन GitHub Action द्वारा तयार केले जातात. कधीही त्यांना हँड-एडिट करू नका; स्रोत बदल शीर्षस्तरीय धडा
   फाइल्समध्येच करा.
3. **कधीही जुनी मॉडेल वापरू नका.** चॅट/मूल्यमापनासाठी **`gpt-5.1`** आणि कोडिंगसाठी **`gpt-5-codex`** वापरा.
   `gpt-4o`, `gpt-4.1`, किंवा कोणतेही निवृत्त मॉडेल आणू नका आणि *GitHub मॉडेल्स*
   (30 जुलै 2026 पासून निवृत्त होणार) वापरु नका — सर्व मॉडेल्स Microsoft Foundry द्वारे सेवा पुरवली जातात.
4. **सध्याचा SDK इंटरफेस वापरा.** नमुने `agent-framework` (pinned `requirements.txt` मध्ये)
   वापरतात ज्यात `FoundryChatClient` आणि **Responses API** असते. जुने
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` नमुने पुन्हा वापरू नका.
5. **टर्मिनॉलॉजी अद्ययावत ठेवा:** *Microsoft Foundry* (नाही "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## सेटअप

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # नमुने आपल्या विकसक ओळखीने प्रामाणिक करतात
cp .env.example .env         # नंतर आपला Foundry प्रकल्पाचा एन्डपॉईंट + मॉडेल भरा
```

आवश्यकताः **Python 3.12+**, **Azure CLI**, आणि **Microsoft Foundry** प्रोजेक्टमध्ये GPT-5-सीरीज मॉडेल
तैनात असलेली आवश्यक आहे. प्रत्येक धड्याच्या README मध्ये त्याचे स्वतःचे पूर्वअट आणि आवश्यक env व्हरिएबल्स दिलेले आहेत
(धडा-स्तराचे `.env.example` वापरून पाहा जेथे उपलब्ध आहे).

## नमुने चालविणे

बहुतेक धडा-2 च्या नमुन्यांसाठी स्थानिक **DevUI** समर्पित पोर्टवर (उदाहरणार्थ 8090–8096) लाँच होतो; धडा 7 मध्ये A2A
सर्व्हर पोर्ट 9000 वर ऐकतो. प्रत्येक नमुन्याच्या docstring/README मध्ये अचूक कमांड आणि पोर्ट तपासा.
कारण नमुने थेट Foundry एंडपॉइंट कॉल करतात, त्यांना वैध `.env` आणि `az login` आवश्यक असतो.

## बदलांची पुष्टी करणे

कोणतीही युनिट-टेस्ट सुइट नाही; पुष्टीकरण statik + live आहे:

- **Static gate (कमिटपूर्वी पास होणे आवश्यक):** प्रत्येक नमुन्याला बाइट-कंपाईल करा.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Windows PowerShell वर:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Markdown links:** CI `static` जॉब `markdown-link-check`
  चालवते (कॉन्फिग: `.github/workflows/markdown-link-check-config.json`). कोणतेही नवीन बाह्य दुवे
  HTTP 200 रीझॉल्व होतात का ते तपासा.
- **Smoke test:** `.github/workflows/smoke-test-hosted-agent.yml` AI स्मोक टेस्ट अॅक्शन चालवते
  एक तैनात होस्टेड एजंटवर (`workflow_dispatch`, OIDC). लाइव्ह एजंट रनसाठी Azure प्रवेश आवश्यक आहे.

CI (`static` जॉब) .py फाइल्स आपोआप शोधतो, त्यामुळे नवीन नमुने workflow संपादित न करता कव्हर होतात.
`py_compile` ला अपयशी करणारे कोड कमिट करू नका.

## कमिट कन्व्हेन्शन्स

- स्पष्ट, आवश्यक सूचनांसह लक्ष केंद्रित कमिट लिहा.
- एजंट-सहाय्यक कमिट्सवर सह-लेखक ट्रेलर समाविष्ट करा:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- जनरेट केलेली कॅशे, वर्चुअल एन्व्हायर्नमेंट्स, किंवा `.env` फाइल्स (सर्व git-ignored) कमिट करू नका.

## कुठे विशिष्ट बदल करायचे

| बदल | स्थान |
|--------|----------|
| कोर्स वर्णन / धडा मजकूर | `lesson-*/README.md` (फक्त स्रोत — कधीच `translations/` मध्ये नाही) |
| चालवता येणारा कोड | `lesson-*/**.py`, `setup_vector_store.py` |
| अवलंबित्वे | `requirements.txt` (आवृत्त्या पिन ठेवा) |
| Env व्हरिएबल दस्तऐवज | `.env.example`, धडा-स्तर `.env.example` |
| CI / स्थिर गेट | `.github/workflows/` |
| AI सहाय्यकांसाठी कोर्स कौशल्ये | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->