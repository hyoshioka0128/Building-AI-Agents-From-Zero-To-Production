# Pelajaran 2 Pengembangan Agen

Selamat datang di pelajaran kedua dari "Kursus Membangun Agen AI dari Nol hingga Produksi"!

Dalam pelajaran ini kami akan membahas:

- Alat untuk Membuat Agen AI kita
  
- Instruksi Pengaturan untuk Sumber Daya Pengembangan kita

- Praktik Terbaik Pengembangan Agen AI
  
- Penelusuran Kode untuk Membuat Agen AI kita
  
Mari mulai dengan melihat alat yang akan kita gunakan untuk membuat Agen AI kita.

## Alat dan Instruksi Pengaturan

### Microsoft Foundry

Untuk akses ke Large Language Models (LLM) kita akan menggunakan [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Ada biaya yang terkait dengan penggunaan Foundry jadi pastikan untuk mengikuti instruksi pengaturan akun jika Anda belum memiliki akses.

### Model OpenAI

Contoh kode agen dalam kursus ini diatur untuk menggunakan model OpenAI melalui [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Gunakan panduan ini untuk mempelajari cara menerapkan model menggunakan Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Pilih satu model seri GPT-5 (misalnya `gpt-5.1`) untuk kursus ini. Hindari model yang sudah pensiun seperti GPT-4o dan GPT-4.1, yang mencapai akhir masa pakai pada tahun 2026.

### Microsoft Agent Framework

Seperti disebutkan sebelumnya, kita akan menggunakan [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) untuk membuat dan mengorkestrasi Agen AI kita.

Anda akan membutuhkan **Python 3.12 atau yang lebih baru**. Untuk menginstal Microsoft Agent Framework dan paket lain yang diperlukan, jalankan perintah berikut saat berada di direktori root proyek ini:

```bash
pip install -r requirements.txt
```

### Autentikasi dengan Azure

Agen mengautentikasi ke Microsoft Foundry menggunakan kredensial Azure CLI Anda
(`AzureCliCredential`), jadi Anda harus masuk terlebih dahulu sebelum menjalankan contoh apapun:

```bash
az login
# Jika Anda memiliki lebih dari satu langganan, pilih yang memiliki proyek Foundry Anda:
az account set --subscription "<your-subscription-id>"
```

Pastikan akun Anda memiliki peran **Azure AI User** (atau setara) pada proyek Foundry
sehingga dapat memanggil API model dan agen.

### Pengaturan Variabel .env

Untuk menjalankan contoh kode dalam kursus ini, Anda perlu membuat file `.env` di direktori root proyek ini.

Untuk memudahkan, Anda bisa menyalin file `.env.example` yang disediakan:

```bash
cp .env.example .env
``` 

Kemudian isi dua variabel yang dibaca oleh agen ( `FoundryChatClient` mengambilnya
secara otomatis):

| Variabel | Apa itu | Dimana menemukannya |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Endpoint **proyek** Foundry Anda, diakhiri dengan `/api/projects/<project>` | Portal Foundry → proyek Anda → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | Nama penerapan model yang dijalankan oleh agen (misalnya `gpt-5.1`) | Portal Foundry → **Models + endpoints** |

### Buat penyimpanan vektor karyawan

Salah satu contoh — **Employee Search Agent** — mencari direktori karyawan yang disimpan dalam
Microsoft Foundry **penyimpanan vektor**. Buat sekali dan salin ID yang dicetak ke dalam `.env`
sebagai `VECTOR_STORE_ID` (jalankan dari root repositori agar dapat membaca `.env` Anda):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Jalankan sebuah contoh

Setiap agen menjalankan DevUI lokalnya sendiri. Misalnya:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Kemudian buka URL `http://localhost:<port>` yang dicetak di browser Anda untuk mengobrol dengan agen.

## Agen dalam pelajaran ini

Setiap contoh adalah agen mandiri yang dibangun dengan Microsoft Agent Framework. Bersama-sama mereka
mengimplementasikan skenario yang Anda rancang di [Pelajaran 1](../lesson-1-agent-design/README.md):

| Contoh | Skenario Pelajaran 1 | Alat yang digunakan | Port |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Skenario 1 — Pencarian Karyawan | Pencarian **file** yang dihosting Foundry di atas penyimpanan vektor | 8090 |
| `task-recommendation-agent.py` | Skenario 2 — Rekomendasi Tugas | Server **GitHub MCP** (alat MCP terhosting) | 8095 |
| `azure-learning-agent.py` | Skenario 3 — Asisten Kode (riset) | Server **Microsoft Learn MCP** (alat MCP terhosting) | 8092 |
| `coding-agent.py` | Skenario 3 — Asisten Kode (kode) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Agen pendukung | Learn MCP + penalaran | 8091 |
| `agent-orchestration.py` | Mengikat skenario bersama | Orkestrasi **handoff** multi-agen | 8094 |

> **Catatan tentang Task Recommendation Agent.** `task-recommendation-agent.py` membutuhkan
> `GITHUB_PERSONAL_ACCESS_TOKEN` dalam `.env` Anda (buat token di
> <https://github.com/settings/personal-access-tokens/new>). Agen ini membaca aktivitas GitHub terakhir seorang pengembang
> dan merekomendasikan 1–3 isu terbuka yang sesuai — tepat seperti desain Skenario 2.
> Ini adalah satu-satunya contoh yang memanggil GitHub; yang lain hanya memerlukan proyek Foundry Anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->