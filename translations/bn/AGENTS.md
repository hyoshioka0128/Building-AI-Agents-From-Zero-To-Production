# AGENTS.md

এই রিপজিটরিতে কাজ করা AI কোডিং এজেন্ট এবং মানব সহযোগীদের জন্য নির্দেশনা। আপনি যদি একজন
স্বয়ংক্রিয় এজেন্ট হন যিনি এখানে পরিবর্তন করছেন, তাহলে প্রথমে এই ফাইলটি পড়ুন এবং তা অনুসরণ করুন।

## এই রিপজিটরিটি কী

**শূন্য থেকে উৎপাদনে AI এজেন্ট তৈরি করা** একটি মাইক্রোসফট শেখার কোর্স। এটি বিকাশকারীদের শেখায়
কিভাবে ডিজাইন, নির্মাণ, মূল্যায়ন, মোতায়েন এবং পরিচালনা করতে হয় AI এজেন্টগুলি **Microsoft Foundry** ব্যবহার করে
**Microsoft Agent Framework (MAF)** এর সাহায্যে। বিষয়বস্তু একটি পাঠ্যক্রম হিসেবে সংগঠিত,
প্রতিটির সাথে একটি `README.md` এবং চালানোর উপযোগী পাইথন নমুনা রয়েছে।

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

মূল ডকুমেন্ট: `README.md` (এখান থেকেই শুরু করুন), `MIGRATION-GUIDE.md` (SDK মাইগ্রেশন বিস্তারিত), `CHANGELOG.md`।

## স্বর্ণকিয়া নিয়মাবলি

1. **কখনই সিক্রেট কমিট করবেন না।** শুধুমাত্র `*.env.example` ফাইল ট্র্যাক করা হয়; আসল `.env` ফাইলগুলি
   গিট-অগ্রাহ্য করা হয়। স্যাম্পল বা ডকুমেন্টে কখনও এন্ডপয়েন্ট, কী, টোকেন বা সংযোগ স্ট্রিং হার্ডকোড করবেন না।
2. **`translations/` বা `translated_images/` স্পর্শ করবেন না।** এগুলো স্বয়ংক্রিয়ভাবে একটি
   অনুবাদ GitHub অ্যাকশনের মাধ্যমে তৈরি হয়। কখনও এগুলো হাতে সম্পাদনা করবেন না; মূল পরিবর্তন শুধুমাত্র শীর্ষ-স্তরের পাঠ্য
   ফাইলেই করুন।
3. **অপ্রচলিত মডেল ব্যবহার করবেন না।** চ্যাট/মুল্যায়নের জন্য **`gpt-5.1`** এবং কোডিংয়ের জন্য **`gpt-5-codex`** ব্যবহার করুন।
   `gpt-4o`, `gpt-4.1` বা অন্য কোন অবসরপ্রাপ্ত মডেল ব্যবহার করবেন না, এবং *GitHub Models* 
   (৩০ জুলাই, ২০২৬ থেকে অবসর গ্রহণকারী) ব্যবহার করবেন না — সব মডেল Microsoft Foundry এর মাধ্যমে পরিবেশন করা হয়।
4. **বর্তমান SDK সারফেস ব্যবহার করুন।** নমুনাগুলো `agent-framework` (ঋদ্ধ `requirements.txt` এ)
   সহ `FoundryChatClient` এবং **Responses API** লক্ষ্য করে। পুরোনো
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` প্যাটার্ন পুনরায় পরিচয় করাবেন না।
5. **শব্দ ব্যবহারে সতর্ক থাকুন:** *Microsoft Foundry* (না "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*।

## সেটআপ

```bash
python -m venv .venv
# উইন্ডোজ:  .venv\Scripts\Activate.ps1
# ম্যাকওএস/লিনাক্স:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # নমুনাগুলি আপনার ডেভেলপার পরিচয় দিয়ে প্রমাণীকরণ করে
cp .env.example .env         # তারপর আপনার Foundry প্রকল্পের এন্ডপয়েন্ট + মডেল পূরণ করুন
```

প্রয়োজনীয়তা: **Python 3.12+**, **Azure CLI**, এবং একটি **Microsoft Foundry** প্রকল্প
যেখানে GPT-5-সিরিজ মডেল মোতায়েন আছে। প্রতিটি পাঠের README তার নিজস্ব প্রয়োজনীয়তা এবং প্রয়োজনীয় এনভি ভেরিয়েবল তালিকাভুক্ত করে
(যেখানে থাকে, সেই পাঠ স্তরের `.env.example` দেখুন)।

## নমুনা চালানো

বেশিরভাগ লেসন-২ নমুনা একটি স্থানীয় **DevUI** চালু করে একটি নির্দিষ্ট পোর্টে (যেমন ৮০৯০–৮০৯৬); লেসন ৭ এর A2A
সার্ভার পোর্ট ৯০০০ এ শুনে। সঠিক কমান্ড এবং পোর্টের জন্য প্রতিটি নমুনার ডক্সস্ট্রিং/README দেখুন।
যেহেতু নমুনাগুলি লাইভ Foundry এন্ডপয়েন্ট কল করে, তাই একটি বৈধ `.env` এবং `az login` প্রয়োজন।

## পরিবর্তন যাচাই

ইউনিট টেস্ট স্যুট নেই; যাচাই স্থ্যাটিক + লাইভ:

- **স্থ্যাটিক গেট (কমিটের আগে অবশ্যই পাস করতে হবে):** প্রতিটি নমুনাকে বাইট-কম্পাইল করুন।
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  উইন্ডোজ পাওয়ারশেলে:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **মার্কডাউন লিঙ্ক:** CI `static` কাজটি `markdown-link-check` চালায়
  (কনফিগ: `.github/workflows/markdown-link-check-config.json`). নতুন যে কোন বাহ্যিক লিঙ্ক
  সংমিলিত (HTTP ২০০) কিনা যাচাই করুন।
- **স্মোক টেস্ট:** `.github/workflows/smoke-test-hosted-agent.yml` AI স্মোক টেস্ট অ্যাকশন চালায়
  মোতায়েন করা হোস্টেড এজেন্টের বিরুদ্ধে (`workflow_dispatch`, OIDC)। লাইভ এজেন্ট রান করার জন্য Azure অ্যাক্সেস প্রয়োজন।

CI (`static` কাজ) স্বয়ংক্রিয়ভাবে `.py` ফাইলগুলি আবিষ্কার করে, তাই নতুন নমুনাগুলি কাজের ফাইল সম্পাদনা ছাড়াই ধরা পড়ে। `py_compile` এ ব্যর্থ কোড কমিট করবেন না।


## কমিট রীতি

- স্পষ্ট, আদেশমূলক বার্তা সহ ফোকাসড কমিট লিখুন।
- এজেন্ট সাহায্যপ্রাপ্ত কমিটে কো-অথর ট্রেইলার অন্তর্ভুক্ত করুন:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- জেনারেটেড ক্যাশ, ভার্চুয়াল এনভায়রনমেন্ট, বা `.env` ফাইল (সব গিট-অগ্রাহ্য) কমিট করবেন না।

## নির্দিষ্ট পরিবর্তন কোথায় করবেন

| পরিবর্তন | অবস্থান |
|--------|----------|
| কোর্স বর্ণনা / পাঠ্য | `lesson-*/README.md` (শুধুমাত্র সোর্স — কখনই `translations/` নয়) |
| চালানোর উপযোগী কোড | `lesson-*/**.py`, `setup_vector_store.py` |
| নির্ভরশীলতা | `requirements.txt` (সংস্করণ জমা রাখুন) |
| এনভি ভেরিয়েবল ডকুমেন্টেশন | `.env.example`, পাঠ স্তরের `.env.example` |
| CI / স্থ্যাটিক গেট | `.github/workflows/` |
| AI সহায়কের জন্য কোর্স দক্ষতা | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->