# AGENTS.md

Panduan untuk ejen pengekodan AI (dan penyumbang manusia) yang bekerja dalam repositori ini. Jika anda adalah
ejen automatik yang membuat perubahan di sini, baca fail ini dahulu dan ikutinya.

## Apa itu repositori ini

**Membina Ejen AI dari Kosong ke Penghasilan** adalah kursus pembelajaran Microsoft. Ia mengajar pembangun
untuk mereka bentuk, membina, menilai, melaksanakan dan mengendalikan ejen AI pada **Microsoft Foundry** menggunakan
**Microsoft Agent Framework (MAF)**. Kandungan disusun sebagai satu siri pelajaran, setiap satu dengan
`README.md` dan contoh Python yang boleh dijalankan.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Dokumen utama: `README.md` (mula di sini), `MIGRATION-GUIDE.md` (perincian migrasi SDK), `CHANGELOG.md`.

## Peraturan emas

1. **Jangan sekali-kali komit rahsia.** Hanya fail `*.env.example` yang dijejaki; fail `.env` sebenar adalah
   diabaikan oleh git. Jangan kod keras titik akhir, kekunci, token, atau rentetan sambungan dalam contoh atau dokumen.
2. **Jangan sentuh `translations/` atau `translated_images/`.** Ini dijana secara automatik oleh
   GitHub Action terjemahan. Jangan edit secara manual; buat perubahan sumber hanya dalam fail pelajaran
   tahap atas sahaja.
3. **Tiada model yang sudah lapuk.** Gunakan **`gpt-5.1`** untuk chat/eval dan **`gpt-5-codex`** untuk pengkodan.
   Jangan memperkenalkan `gpt-4o`, `gpt-4.1`, atau model yang telah bersara, dan jangan gunakan *Model GitHub*
   (berhenti pada 30 Julai 2026) — semua model disediakan melalui Microsoft Foundry.
4. **Gunakan permukaan SDK yang terkini.** Contoh mensasarkan `agent-framework` (dipin dalam `requirements.txt`)
   dengan `FoundryChatClient` dan **API Respons**. Jangan memperkenalkan semula
   corak lama `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
5. **Kekalkan terminologi semasa**: *Microsoft Foundry* (bukan "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Persediaan

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # sampel mengesahkan dengan identiti pembangun anda
cp .env.example .env         # kemudian isi titik hujung projek Foundry + model anda
```

Keperluan: **Python 3.12+**, **Azure CLI**, dan akses ke projek **Microsoft Foundry**
dengan model siri GPT-5 yang sudah dipasang. Setiap README pelajaran menyenaraikan prasyarat dan pemboleh ubah persekitaran
yang diperlukan (rujuk `.env.example` pada tahap pelajaran jika ada).

## Menjalankan contoh

Kebanyakan contoh pelajaran-2 melancarkan **DevUI** tempatan pada port khusus (contohnya 8090–8096); pelayan A2A
dalam pelajaran 7 mendengar pada port 9000. Semak docstring / README setiap contoh untuk arahan tepat
dan port. Oleh kerana contoh memanggil titik akhir Foundry yang hidup, mereka memerlukan `.env` yang sah dan `az login`.

## Mengesahkan perubahan

Tiada suite ujian unit; pengesahan adalah statik + langsung:

- **Pintu statik (mesti lulus sebelum komit):** byte-compile setiap contoh.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Pada Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Pautan Markdown:** pekerjaan CI `static` menjalankan `markdown-link-check`
  (konfigurasi: `.github/workflows/markdown-link-check-config.json`). Sahkan mana-mana pautan luar baru
  berfungsi (HTTP 200).
- **Ujian asap:** `.github/workflows/smoke-test-hosted-agent.yml` menjalankan aksi Ujian Asap AI
  terhadap ejen hos yang dipasang (`workflow_dispatch`, OIDC). Larian agen hidup memerlukan akses Azure.

CI (pekerjaan `static`) mengesan secara automatik fail `.py`, jadi contoh baru dilindungi tanpa mengedit
workflow. Jangan komit kod yang gagal `py_compile`.

## Konvensyen komit

- Tulis komit fokus dengan mesej yang jelas dan imperatif.
- Sertakan trailer pengarang bersama pada komit yang dibantu ejen:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Jangan komit cache yang dijana, persekitaran maya, atau fail `.env` (semuanya diabaikan git).

## Tempat membuat perubahan tertentu

| Perubahan | Lokasi |
|--------|----------|
| Naratif kursus / teks pelajaran | `lesson-*/README.md` (sumber sahaja — jangan sentuh `translations/`) |
| Kod boleh jalankan | `lesson-*/**.py`, `setup_vector_store.py` |
| Kebergantungan | `requirements.txt` (pastikan versi dipin) |
| Dokumentasi pemboleh ubah persekitaran | `.env.example`, `.env.example` tahap pelajaran |
| CI / pintu statik | `.github/workflows/` |
| Kemahiran kursus untuk pembantu AI | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->