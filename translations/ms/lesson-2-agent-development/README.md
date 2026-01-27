<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:22:48+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "ms"
}
-->
# Lesson 2 Pembangunan Ejen

Selamat datang ke pelajaran kedua kursus "Membina Ejen AI dari Asas ke Pengeluaran"!

Dalam pelajaran ini kita akan membincangkan:

- Alat untuk Mencipta Ejen AI kita
  
- Arahan Persediaan untuk Sumber Pembangunan kita

- Amalan Terbaik Pembangunan Ejen AI
  
- Laluan Kod untuk Mencipta Ejen AI kita
  
Mari mula dengan melihat alat yang akan kita gunakan untuk mencipta Ejen AI kita.

## Alat dan Arahan Persediaan

### Microsoft Foundry

Untuk akses kepada Model Bahasa Besar (LLM) kita akan menggunakan [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Terdapat kos yang berkaitan dengan penggunaan Foundry jadi sila pastikan untuk mengikuti arahan untuk penyediaan akaun jika anda belum mempunyai akses.

### Model OpenAI

Contoh kod agen dalam kursus ini disediakan untuk menggunakan model OpenAI melalui [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Gunakan panduan ini untuk belajar cara melancarkan model menggunakan Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Pilih satu model GPT-4.1 atau lebih baru untuk kursus ini.

### Microsoft Agent Framework

Seperti yang disebutkan sebelum ini, kita akan menggunakan [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) untuk mencipta dan menyelaraskan Ejen AI kita.

Untuk memasang Microsoft Agent Framework dan pakej lain yang diperlukan, jalankan arahan berikut semasa berada dalam direktori root projek ini:

```bash
pip install -r requirements.txt
```

### Persediaan Pembolehubah .env

Untuk menjalankan contoh kod dalam kursus ini, anda perlu membuat fail `.env` dalam direktori root projek ini.

Untuk memudahkan, anda boleh salin fail `.env.example` yang disediakan:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha mencapai ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->