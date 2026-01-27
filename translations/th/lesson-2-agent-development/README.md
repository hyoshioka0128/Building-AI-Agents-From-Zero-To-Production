<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:17:31+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "th"
}
-->
# Lesson 2 Agent Development

ยินดีต้อนรับสู่บทเรียนที่สองของหลักสูตร "การสร้าง AI Agent ตั้งแต่เริ่มต้นจนถึงการนำไปใช้งานจริง"!

ในบทเรียนนี้เราจะครอบคลุม:

- เครื่องมือสำหรับการสร้าง AI Agents ของเรา
  
- คำแนะนำการตั้งค่าสำหรับทรัพยากรการพัฒนาของเรา

- แนวปฏิบัติที่ดีที่สุดสำหรับการพัฒนา AI Agent
  
- การอธิบายโค้ดสำหรับการสร้าง AI Agents ของเรา
  
เรามาเริ่มต้นด้วยการดูเครื่องมือที่เราจะใช้ในการสร้าง AI Agents ของเรากัน

## Tools and Setup Instructions

### Microsoft Foundry

สำหรับการเข้าถึง Large Langauge Models (LLMs) เราจะใช้ [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) มีค่าใช้จ่ายที่เกี่ยวข้องกับการใช้ Foundry ดังนั้นโปรดตรวจสอบให้แน่ใจว่าได้ปฏิบัติตามคำแนะนำสำหรับการตั้งค่าบัญชี หากคุณยังไม่มีสิทธิ์เข้าถึง

### OpenAI Models

ตัวอย่างโค้ด agent ในหลักสูตรนี้ถูกตั้งค่าให้ใช้โมเดล OpenAI ผ่านทาง [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)

ใช้คำแนะนำนี้เพื่อเรียนรู้วิธีการปรับใช้โมเดลโดยใช้ Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

เลือกโมเดล GPT-4.1 หรือรุ่นที่ใหม่กว่าสำหรับหลักสูตรนี้

### Microsoft Agent Framework

อย่างที่กล่าวไว้ก่อนหน้านี้ เราจะใช้ [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) เพื่อสร้างและประสานการทำงานของ AI Agents ของเรา

ในการติดตั้ง Microsoft Agent Framework และแพ็กเกจที่จำเป็นอื่น ๆ ให้รันคำสั่งต่อไปนี้ขณะที่อยู่ในไดเรกทอรีหลักของโปรเจกต์นี้:

```bash
pip install -r requirements.txt
```

### Setup .env Variables

เพื่อรันตัวอย่างโค้ดในหลักสูตรนี้ คุณจะต้องสร้างไฟล์ `.env` ในไดเรกทอรีหลักของโปรเจกต์นี้

เพื่อให้ง่ายขึ้น คุณสามารถคัดลอกไฟล์ `.env.example` ที่ให้มา:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาแบบอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญที่เป็นมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->