# AGENTS.md

Panduan untuk agen pengkodean AI (dan kontributor manusia) yang bekerja dalam repositori ini. Jika Anda adalah
agen otomatis yang membuat perubahan di sini, bacalah file ini terlebih dahulu dan ikuti.

## Apa itu repositori ini

**Membangun Agen AI dari Nol hingga Produksi** adalah kursus pembelajaran Microsoft. Kursus ini mengajarkan pengembang
untuk merancang, membangun, mengevaluasi, menyebarkan, dan mengoperasikan agen AI di **Microsoft Foundry** menggunakan
**Microsoft Agent Framework (MAF)**. Konten disusun sebagai rangkaian pelajaran, masing-masing dengan
`README.md` dan contoh Python yang dapat dijalankan.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Dokumen utama: `README.md` (mulai di sini), `MIGRATION-GUIDE.md` (detail migrasi SDK), `CHANGELOG.md`.

## Aturan emas

1. **Jangan pernah meng-commit rahasia.** Hanya file `*.env.example` yang dilacak; file `.env` asli
   diabaikan oleh git. Jangan memasukkan endpoint, kunci, token, atau string koneksi secara keras dalam contoh atau dokumen.
2. **Jangan sentuh `translations/` atau `translated_images/`.** Folder ini dihasilkan secara otomatis oleh
   GitHub Action terjemahan. Jangan pernah mengedit secara manual; lakukan perubahan sumber hanya pada
   file pelajaran tingkat atas saja.
3. **Jangan gunakan model yang sudah usang.** Gunakan **`gpt-5.1`** untuk chat/evaluasi dan **`gpt-5-codex`** untuk pengkodean.
   Jangan memperkenalkan `gpt-4o`, `gpt-4.1`, atau model yang sudah dihentikan, dan jangan gunakan *GitHub Models*
   (akan dihentikan pada 30 Juli 2026) — semua model disajikan melalui Microsoft Foundry.
4. **Gunakan permukaan SDK saat ini.** Contoh menargetkan `agent-framework` (tertangkap di `requirements.txt`)
   dengan `FoundryChatClient` dan **Responses API**. Jangan mengembalikan pola lama
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
5. **Gunakan terminologi terkini**: *Microsoft Foundry* (bukan "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Setup

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # contoh mengautentikasi dengan identitas pengembang Anda
cp .env.example .env         # kemudian isi endpoint proyek Foundry + model Anda
```

Persyaratan: **Python 3.12+**, **Azure CLI**, dan akses ke proyek **Microsoft Foundry**
dengan model GPT-5-series yang sudah disebarkan. Setiap README pelajaran mencantumkan prasyaratnya sendiri dan variabel lingkungan
yang dibutuhkan (lihat `.env.example` tingkat pelajaran jika tersedia).

## Menjalankan contoh

Sebagian besar contoh pelajaran-2 menjalankan **DevUI** lokal pada port khusus (misalnya 8090–8096); server A2A di pelajaran 7
mendengarkan port 9000. Periksa docstring/README masing-masing contoh untuk perintah dan port yang tepat.
Karena contoh memanggil endpoint Foundry langsung, mereka membutuhkan `.env` yang valid dan `az login`.

## Memvalidasi perubahan

Tidak ada suite unit-test; validasi bersifat statis + langsung:

- **Gerbang statis (harus lolos sebelum commit):** byte-compile setiap contoh.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Pada PowerShell Windows:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Tautan markdown:** pekerjaan CI `static` menjalankan `markdown-link-check`
  (konfigurasi: `.github/workflows/markdown-link-check-config.json`). Verifikasi tautan eksternal baru
  dapat diakses (HTTP 200).
- **Smoke test:** `.github/workflows/smoke-test-hosted-agent.yml` menjalankan aksi AI Smoke Test
  terhadap agen hosted yang sudah disebarkan (`workflow_dispatch`, OIDC). Jalankan agen langsung membutuhkan akses Azure.

CI (pekerjaan `static`) secara otomatis menemukan file `.py`, sehingga contoh baru tercakup tanpa mengubah
workflow. Jangan commit kode yang gagal `py_compile`.

## Konvensi commit

- Tulislah commit yang fokus dengan pesan imperatif yang jelas.
- Sertakan trailer co-author pada commit dengan bantuan agen:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Jangan commit cache yang dihasilkan, lingkungan virtual, atau file `.env` (semua diabaikan git).

## Tempat membuat perubahan spesifik

| Perubahan | Lokasi |
|--------|----------|
| Narasi kursus / teks pelajaran | `lesson-*/README.md` (hanya sumber — jangan `translations/`) |
| Kode yang dapat dijalankan | `lesson-*/**.py`, `setup_vector_store.py` |
| Dependensi | `requirements.txt` (pertahankan versi tetap) |
| Dokumentasi variabel lingkungan | `.env.example`, `.env.example` tingkat pelajaran |
| CI / gerbang statis | `.github/workflows/` |
| Keterampilan kursus untuk asisten AI | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->