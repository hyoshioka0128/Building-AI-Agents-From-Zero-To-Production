# Pelajaran 2 Pengembangan Agen

Selamat datang di pelajaran kedua dari  "Kursus Membangun Agen AI dari Nol hingga Produksi"!

Dalam pelajaran ini kita akan membahas:

- Alat untuk Membuat Agen AI kita
  
- Instruksi Pengaturan untuk Sumber Daya Pengembangan kita

- Praktik Terbaik Pengembangan Agen AI
  
- Penelusuran Kode untuk Membuat Agen AI kita
  
Mari mulai dengan melihat alat yang akan kita gunakan untuk membuat Agen AI kita.

## Alat dan Instruksi Pengaturan

### Microsoft Foundry

Untuk akses ke Large Language Models (LLMs) kita akan menggunakan [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Ada biaya terkait penggunaan Foundry jadi pastikan mengikuti instruksi pengaturan akun jika Anda belum memiliki akses.

### Model OpenAI

Contoh kode agen dalam kursus ini disiapkan untuk menggunakan model OpenAI melalui [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Gunakan panduan ini untuk mempelajari cara menerapkan model menggunakan Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Pilih satu model GPT-4.1 atau yang lebih baru untuk kursus ini.

### Microsoft Agent Framework

Seperti disebutkan sebelumnya, kita akan menggunakan [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) untuk membuat dan mengorkestrasi Agen AI kita.

Untuk menginstal Microsoft Agent Framework dan paket lain yang diperlukan, jalankan perintah berikut saat berada di direktori root proyek ini:

```bash
pip install -r requirements.txt
```

### Menyiapkan Variabel .env

Untuk menjalankan contoh kode dalam kursus ini, Anda perlu membuat file `.env` di direktori root proyek ini.

Untuk mempermudah, Anda bisa menyalin file `.env.example` yang disediakan:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->