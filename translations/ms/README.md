# Membina Ejen AI dari Kosong ke Pengeluaran

![Building AI Agents from Zero to Production](../../translated_images/ms/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 Sokongan Pelbagai Bahasa

#### Disokong melalui Tindakan GitHub (Automatik & Sentiasa Dikemas Kini)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](./README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Lebih suka Klon Secara Tempatan?**
>
> Repositori ini termasuk lebih daripada 50 terjemahan bahasa yang meningkatkan saiz muat turun dengan ketara. Untuk klon tanpa terjemahan, gunakan sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Ini memberikan anda semua yang anda perlukan untuk menamatkan kursus dengan muat turun yang jauh lebih pantas.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Kursus yang mengajar asas-asas Kitaran Hayat Pembangunan Ejen AI

[![GitHub license](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 Memulakan

Kursus ini mempunyai pelajaran yang merangkumi asas-asas membina dan menerapkan Ejen AI.

Setiap pelajaran dibina berdasarkan pelajaran sebelumnya, jadi kami mengesyorkan bermula dari awal dan meneruskan sehingga akhir.

Jika anda ingin meneroka lebih banyak tentang topik Ejen AI, anda boleh melihat [Kursus Ejen AI untuk Pemula](https://aka.ms/ai-agents-beginners).

### Berjumpa dengan Pelajar Lain, Dapatkan Jawapan kepada Soalan Anda

Jika anda menghadapi masalah atau mempunyai sebarang soalan tentang membina Ejen AI, sertailah Saluran Discord khusus kami di [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6).

### Apa yang Anda Perlukan

Setiap Pelajaran mempunyai sampel kod sendiri yang anda boleh jalankan secara tempatan. Anda boleh [fork repositori ini](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork) untuk membuat salinan anda sendiri.

Kursus ini kini menggunakan perkara berikut:

- [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) — projek dengan model **GPT-5 series** yang diterapkan (contohnya `gpt-5.1`). Jangan gunakan model GPT-4o / GPT-4.1 yang telah dihentikan.
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest) — log masuk dengan `az login` sebelum menjalankan sebarang sampel
- **Python 3.12 atau lebih baru**

Pastikan anda mempunyai akses kepada perkhidmatan ini sebelum memulakan.

> **💰 Kos & pembersihan.** Pelajaran praktikal menghasilkan sumber Azure sebenar — projek Microsoft Foundry,
> satu penyebaran model, stor vektor, dan (dalam Pelajaran 4–6) ejen dan kotak alat yang dihoskan.
> Ini boleh menimbulkan kos selagi ia wujud. Apabila selesai satu pelajaran — atau kursus — padamkan
> sumber yang tidak lagi diperlukan. Cara paling mudah adalah letakkan semuanya dalam satu kumpulan sumber
> khusus dan padam keseluruhan kumpulan apabila selesai:
>
> ```bash
> az group delete --name <your-resource-group> --yes --no-wait
> ```
>
> Anda juga boleh padam agen individu, stor vektor, dan kotak alat dari portal Foundry.

> **Nota mengenai model.** Kursus ini menyajikan semua model melalui **Microsoft Foundry**. Ia **tidak**
> menggunakan *GitHub Models*, yang akan dihentikan pada **30 Julai 2026** — Microsoft Foundry adalah
> laluan migrasi rasmi. Jika anda mempunyai kod lama yang memanggil GitHub Models, arahkan ke penyebaran
> model Foundry sebaliknya.

Pilihan lain berkaitan hosting model dan perkhidmatan akan datang tidak lama lagi.

## 🗃️ Pelajaran

| **Pelajaran**         | **Penerangan**                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| [Reka Bentuk Ejen](./lesson-1-agent-design/README.md)       | Pengenalan kepada Kes Penggunaan Ejen "Pengenalan Pembangun" dan bagaimana mereka bentuk ejen yang berkesan  |
| [Pembangunan Ejen](./lesson-2-agent-development/README.md)  | Menggunakan Microsoft Agent Framework (MAF), bina set ejen khusus untuk membantu pembangun baru memulakan kerja.       |
| [Penilaian Ejen](./lesson-3-agent-evals/README.md)  | Menggunakan Microsoft Foundry, ketahui sejauh mana prestasi Ejen AI kami dan bagaimana memperbaikinya. |
| [Pengeluaran Ejen](./lesson-4-agentdeployment/README.md)   | Menggunakan ejen yang dihoskan Microsoft Foundry dan OpenAI ChatKit, lihat bagaimana untuk menyebarkan Ejen AI ke pengeluaran.       |
| [Ejen Dihoskan dalam Pengeluaran](./lesson-5-hosted-agents-production/README.md)   | Bawa ejen yang dihoskan ke pengeluaran perusahaan: Ejen Dihoskan vs Hos Kebolehan, bawa sendiri storan, memori, dan tadbir urus.       |
| [Kotak Alat Microsoft](./lesson-6-toolbox/README.md)   | Definisikan alat sekali dan tadbir secara pusat: bina kotak alat, gunakan daripadanya daripada ejen melalui satu titik akhir MCP, dan versi alat dengan selamat.       |
| [Multi-Ejen & A2A](./lesson-7-multi-agent-a2a/README.md)   | Susun agen sebagai perkhidmatan berangkaian: dedahkan ejen melalui protokol Terbuka Ejen-ke-Ejen (A2A) dan gunakan ejen jauh sebagai rakan sebaya.       |


## 🎒 Kursus Lain

Pasukan kami menghasilkan kursus lain! Lihat:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Siri AI Generatif

[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Pembelajaran Teras
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Siri Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Kebanyakan sumbangan memerlukan anda bersetuju dengan
Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak untuk, dan sebenarnya, memberikan kami
hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati <https://cla.opensource.microsoft.com>.

Apabila anda mengemukakan permintaan tarikan, bot CLA akan secara automatik menentukan sama ada anda perlu menyediakan
CLA dan menghiasi PR dengan sewajarnya (contohnya, semakan status, komen). Ikuti sahaja arahan
yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali sahaja untuk semua repositori yang menggunakan CLA kami.

Projek ini telah mengguna pakai [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/).
Untuk maklumat lanjut lihat [FAQ Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/) atau
hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Cap Dagang

Projek ini mungkin mengandungi cap dagang atau logo untuk projek, produk, atau perkhidmatan. Penggunaan sah cap dagang atau logo Microsoft
tertakluk kepada dan mesti mengikuti
[Garis Panduan Cap Dagang & Jenama Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Penggunaan cap dagang atau logo Microsoft dalam versi projek yang diubah suai tidak boleh menyebabkan kekeliruan atau memberi implikasi penajaan Microsoft.
Sebarang penggunaan cap dagang atau logo pihak ketiga tertakluk kepada polisi pihak ketiga tersebut.

## Mendapatkan Bantuan

Jika anda menghadapi kesukaran atau mempunyai sebarang soalan tentang membina aplikasi AI, sertai:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

Jika anda mempunyai maklum balas produk atau ralat semasa membina, lawati:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->