# Pelajaran 2 Pembangunan Ejen

Selamat datang ke pelajaran kedua Kursus "Membina Ejen AI dari Kosong ke Pengeluaran"!

Dalam pelajaran ini kita akan membincangkan:

- Alat untuk Mencipta Ejen AI kami
  
- Arahan Persediaan untuk Sumber Pembangunan kami

- Amalan Terbaik Pembangunan Ejen AI
  
- Penjelasan Kod untuk Mencipta Ejen AI kami
  
Mari kita mula dengan melihat alat yang akan kita gunakan untuk mencipta Ejen AI kita.

## Alat dan Arahan Persediaan

### Microsoft Foundry

Untuk akses kepada Model Bahasa Besar (LLM) kita akan menggunakan [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Terdapat kos yang berkaitan dengan penggunaan Foundry jadi sila pastikan untuk mengikuti arahan untuk persediaan akaun jika anda belum mempunyai akses.

### Model OpenAI

Contoh kod ejen dalam kursus ini disediakan untuk menggunakan model OpenAI melalui [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Gunakan panduan ini untuk belajar cara meng-deploy model menggunakan Foundry: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Pilih satu model siri GPT-5 (contohnya `gpt-5.1`) untuk kursus ini. Elakkan model yang telah digugurkan seperti GPT-4o dan GPT-4.1, yang akan mencapai akhir hayat pada tahun 2026.

### Rangka Kerja Ejen Microsoft

Seperti yang disebutkan tadi, kita akan menggunakan [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) untuk mencipta dan menyelaras Ejen AI kita.

Anda memerlukan **Python 3.12 atau ke atas**. Untuk memasang Microsoft Agent Framework dan pakej lain yang diperlukan, jalankan arahan berikut ketika berada dalam direktori akar projek ini:

```bash
pip install -r requirements.txt
```

### Pengesahan dengan Azure

Ejen mengesahkan kepada Microsoft Foundry menggunakan kelayakan Azure CLI anda
(`AzureCliCredential`), jadi anda mesti log masuk sebelum menjalankan sebarang contoh:

```bash
az login
# Jika anda mempunyai lebih daripada satu langganan, pilih yang mempunyai projek Foundry anda:
az account set --subscription "<your-subscription-id>"
```

Pastikan akaun anda mempunyai peranan **Azure AI User** (atau setaraf) pada projek Foundry
supaya ia boleh memanggil API model dan ejen.

### Tetapkan Pembolehubah .env

Untuk menjalankan contoh kod dalam kursus ini, anda perlu mencipta fail `.env` dalam direktori akar projek ini. 

Untuk memudahkan, anda boleh salin fail `.env.example` yang disediakan:

```bash
cp .env.example .env
``` 

Kemudian isikan dua pembolehubah yang dibaca oleh ejen (yang `FoundryChatClient` akan ambil
secara automatik):

| Pembolehubah | Apa itu | Di mana untuk cari |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Titik akhir projek **Foundry** anda, berakhir dengan `/api/projects/<project>` | Portal Foundry → projek anda → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | Nama peng-deploy-an model yang digunakan ejen anda (contohnya `gpt-5.1`) | Portal Foundry → **Models + endpoints** |

### Cipta stor vektor pekerja

Satu contoh — **Employee Search Agent** — mencari direktori pekerja yang disimpan dalam
Microsoft Foundry **vector store**. Cipta satu kali dan salin ID yang dicetak ke dalam `.env`
sebagai `VECTOR_STORE_ID` (jalankan dari akar repositori supaya ia mengambil `.env` anda):

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### Jalankan contoh

Setiap ejen menjalankan DevUI tempatan sendiri. Contohnya:

```bash
python lesson-2-agent-development/employee-search-agent.py
```

Kemudian buka URL `http://localhost:<port>` yang dicetak dalam pelayar anda untuk bersembang dengan ejen.

## Ejen dalam pelajaran ini

Setiap contoh adalah ejen berdiri sendiri yang dibina dengan Microsoft Agent Framework. Bersama-sama mereka
melaksanakan senario yang anda reka dalam [Pelajaran 1](../lesson-1-agent-design/README.md):

| Contoh | Senario Pelajaran 1 | Alat digunakan | Port |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | Senario 1 — Carian Pekerja | Carian **fail** melalui stor vektor yang dihoskan di Foundry | 8090 |
| `task-recommendation-agent.py` | Senario 2 — Cadangan Tugasan | Pelayan **GitHub MCP** (alat MCP dihoskan) | 8095 |
| `azure-learning-agent.py` | Senario 3 — Penolong Kod (penyelidikan) | Pelayan **Microsoft Learn MCP** (alat MCP dihoskan) | 8092 |
| `coding-agent.py` | Senario 3 — Penolong Kod (kod) | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | Ejen sokongan | Learn MCP + penalaran | 8091 |
| `agent-orchestration.py` | Mengikat senario-senario bersama | Orkestrasi **penyerahan** multi-ejen | 8094 |

> **Nota mengenai Ejen Cadangan Tugasan.** `task-recommendation-agent.py` memerlukan
> `GITHUB_PERSONAL_ACCESS_TOKEN` dalam `.env` anda (cipta satu di
> <https://github.com/settings/personal-access-tokens/new>). Ia membaca aktiviti
> terkini pembangun di GitHub dan mencadangkan 1–3 isu terbuka yang sepadan — tepat seperti reka bentuk Senario 2.
> Ini adalah satu-satunya contoh yang memanggil GitHub; yang lain hanya memerlukan projek Foundry anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->