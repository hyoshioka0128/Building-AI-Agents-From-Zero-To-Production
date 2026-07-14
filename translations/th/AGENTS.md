# AGENTS.md

คำแนะนำสำหรับตัวแทน AI โค้ดดิ้ง (และผู้ร่วมงานมนุษย์) ที่ทำงานในที่เก็บนี้ หากคุณเป็น
ตัวแทนอัตโนมัติที่ทำการเปลี่ยนแปลงที่นี่ โปรดอ่านไฟล์นี้ก่อนและปฏิบัติตาม

## ที่เก็บนี้คืออะไร

**การสร้างเอเย่นต์ AI จากศูนย์สู่การผลิต** เป็นหลักสูตรการเรียนรู้ของ Microsoft ซึ่งสอนนักพัฒนา
ในการออกแบบ สร้าง ประเมินค่า นำไปใช้งาน และดำเนินงานเอเย่นต์ AI บน **Microsoft Foundry** โดยใช้
**Microsoft Agent Framework (MAF)** เนื้อหาจัดเป็นลำดับของบทเรียน แต่ละบทมี
`README.md` และตัวอย่าง Python ที่สามารถรันได้

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

เอกสารหลัก: `README.md` (เริ่มที่นี่), `MIGRATION-GUIDE.md` (รายละเอียดการย้าย SDK), `CHANGELOG.md`

## กฎทองคำ

1. **อย่าคอมมิตความลับใดๆ** เฉพาะไฟล์ `*.env.example` เท่านั้นที่ถูกติดตาม; ไฟล์ `.env` จริงจะถูก
   กำหนดให้ git เพิกเฉย อย่ารหัสปลายทาง กุญแจ โทเค็น หรือสตริงการเชื่อมต่อในตัวอย่างหรือเอกสาร
2. **อย่าแตะต้อง `translations/` หรือ `translated_images/`** โฟลเดอร์เหล่านี้ถูกสร้างอัตโนมัติโดย
   GitHub Action การแปล อย่ามือแก้ไข ให้ทำการเปลี่ยนแปลงต้นฉบับเฉพาะในไฟล์บทเรียนระดับบนสุดเท่านั้น

3. **ไม่ใช้โมเดลที่เลิกใช้แล้ว** ใช้ **`gpt-5.1`** สำหรับแชท/ประเมินค่า และ **`gpt-5-codex`** สำหรับการเขียนโค้ด
   อย่าใช้ `gpt-4o`, `gpt-4.1` หรือโมเดลใดที่ถูกเลิกใช้ และอย่าใช้ *GitHub Models*
   (จะเลิกใช้ในวันที่ 30 กรกฎาคม 2026) — โมเดลทั้งหมดให้บริการผ่าน Microsoft Foundry
4. **ใช้ SDK เวอร์ชันปัจจุบัน** ตัวอย่างมุ่งเป้าไปที่ `agent-framework` (ปักหมุดใน `requirements.txt`)
   กับ `FoundryChatClient` และ **Responses API** อย่านำรูปแบบเก่าอย่าง
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient` กลับมาใช้
5. **รักษาคำศัพท์ให้ทันสมัย**: *Microsoft Foundry* (ไม่ใช่ "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*

## การตั้งค่า

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # ตัวอย่างตรวจสอบตัวตนด้วยตัวตนผู้พัฒนาของคุณ
cp .env.example .env         # จากนั้นกรอก endpoint โครงการ Foundry และรุ่นของคุณ
```

ความต้องการ: **Python 3.12+**, **Azure CLI**, และสิทธิ์เข้าใช้งานโปรเจกต์ **Microsoft Foundry**
ที่มีโมเดลชุด GPT-5 ติดตั้งไว้ แต่ละบทเรียน README จะแสดงรายการสิ่งที่ต้องมีและตัวแปร env
ที่ต้องใช้ (ดู `.env.example` ของแต่ละบทเรียนที่มี)

## การรันตัวอย่าง

ตัวอย่างส่วนใหญ่ของบทเรียน 2 จะเปิด **DevUI** ท้องถิ่นบนพอร์ตเฉพาะ (เช่น 8090–8096); เซิร์ฟเวอร์ A2A
ในบทเรียน 7 จะฟังบนพอร์ต 9000 ตรวจสอบ docstring/README ของแต่ละตัวอย่างสำหรับคำสั่งและพอร์ตที่แน่นอน
เนื่องจากตัวอย่างเรียกใช้จุดสิ้นสุด Foundry จริงจึงต้องมี `.env` ที่ถูกต้องและ `az login`

## การตรวจสอบการเปลี่ยนแปลง

ไม่มีชุดทดสอบหน่วย; การตรวจสอบเป็นแบบสแตติก + แบบสด:

- **เกตสแตติก (ต้องผ่านก่อนคอมมิต):** คอมไพล์ byte ทุกตัวอย่าง
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  บน Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **ลิงก์มาร์กดาวน์:** งาน CI `static` รัน `markdown-link-check`
  (คอนฟิก: `.github/workflows/markdown-link-check-config.json`) ตรวจสอบว่าลิงก์ภายนอกใหม่ๆ
  ถูกแก้ไขได้ (HTTP 200)
- **ทดสอบควัน (Smoke test):** `.github/workflows/smoke-test-hosted-agent.yml` รัน AI Smoke Test action
  กับโฮสต์เอเย่นต์ที่ติดตั้ง (`workflow_dispatch`, OIDC) การรันเอเย่นต์จริงต้องมีสิทธิ์ Azure

CI (งาน `static`) ตรวจจับไฟล์ `.py` อัตโนมัติ ดังนั้นตัวอย่างใหม่จะถูกครอบคลุมโดยไม่ต้องแก้ไข
workflow อย่าคอมมิตโค้ดที่ล้มเหลว `py_compile`

## ข้อตกลงการคอมมิต

- เขียนคอมมิตที่มุ่งเน้นด้วยข้อความที่ชัดเจนและเป็นคำสั่ง
- รวมท้ายผู้ร่วมเขียนในการคอมมิตที่ช่วยโดยเอเย่นต์:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- อย่าคอมมิตแคชที่เกิดขึ้น, สภาพแวดล้อมเสมือน หรือไฟล์ `.env` (ทั้งหมดถูก git-ignore)

## ที่ที่จะทำการเปลี่ยนแปลงเฉพาะ

| การเปลี่ยนแปลง | ตำแหน่ง |
|--------|----------|
| เรื่องเล่า / ข้อความบทเรียน | `lesson-*/README.md` (ต้นฉบับเท่านั้น — หลีกเลี่ยง `translations/`) |
| โค้ดที่รันได้ | `lesson-*/**.py`, `setup_vector_store.py` |
| ขึ้นอยู่กับ | `requirements.txt` (ล็อกเวอร์ชันไว้) |
| เอกสารตัวแปร Env | `.env.example`, `.env.example` ของบทเรียน |
| CI / เกตสแตติก | `.github/workflows/` |
| ทักษะของหลักสูตรสำหรับผู้ช่วย AI | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->