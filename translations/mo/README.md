<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b09df38b3188ffe957c7ac8b055967f5",
  "translation_date": "2026-01-16T08:28:06+00:00",
  "source_file": "README.md",
  "language_code": "mo"
}
-->
# 從零開始打造 AI 代理至生產

![從零開始打造 AI 代理至生產](../../../../translated_images/mo/repo-thumbnail.083b24afed61b6dd.webp)

### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動化及持續更新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯文](../ar/README.md) | [孟加拉文](../bn/README.md) | [保加利亞文](../bg/README.md) | [緬甸文 (緬甸)](../my/README.md) | [中文 (簡體)](../zh/README.md) | [中文 (繁體，香港)](../hk/README.md) | [中文 (繁體，澳門)](./README.md) | [中文 (繁體，台灣)](../tw/README.md) | [克羅地亞文](../hr/README.md) | [捷克文](../cs/README.md) | [丹麥文](../da/README.md) | [荷蘭文](../nl/README.md) | [愛沙尼亞文](../et/README.md) | [芬蘭文](../fi/README.md) | [法文](../fr/README.md) | [德文](../de/README.md) | [希臘文](../el/README.md) | [希伯來文](../he/README.md) | [印地文](../hi/README.md) | [匈牙利文](../hu/README.md) | [印尼文](../id/README.md) | [意大利文](../it/README.md) | [日文](../ja/README.md) | [坎那達文](../kn/README.md) | [韓文](../ko/README.md) | [立陶宛文](../lt/README.md) | [馬來文](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地文](../mr/README.md) | [尼泊爾文](../ne/README.md) | [尼日利亞皮欽語](../pcm/README.md) | [挪威文](../no/README.md) | [波斯文 (法爾西語)](../fa/README.md) | [波蘭文](../pl/README.md) | [葡萄牙文 (巴西)](../br/README.md) | [葡萄牙文 (葡萄牙)](../pt/README.md) | [旁遮普文 (古魯穆奇)](../pa/README.md) | [羅馬尼亞文](../ro/README.md) | [俄文](../ru/README.md) | [塞爾維亞文 (西里爾字母)](../sr/README.md) | [斯洛伐克文](../sk/README.md) | [斯洛文尼亞文](../sl/README.md) | [西班牙文](../es/README.md) | [斯瓦希里文](../sw/README.md) | [瑞典文](../sv/README.md) | [他加祿文 (菲律賓)](../tl/README.md) | [泰米爾文](../ta/README.md) | [泰盧固文](../te/README.md) | [泰文](../th/README.md) | [土耳其文](../tr/README.md) | [烏克蘭文](../uk/README.md) | [烏爾都文](../ur/README.md) | [越南文](../vi/README.md)

> **想要本地複製？**

> 此儲存庫包含 50 多種語言翻譯，會大幅增加下載大小。如欲不含翻譯複製，請使用稀疏擷取：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production.git
> cd Building-AI-Agents-From-Zero-To-Production
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 這樣讓你以更快速度下載並擁有完成課程所需的所有內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 一門教授 AI 代理開發生命周期基礎的課程

[![GitHub 授權](https://img.shields.io/github/license/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/Building-AI-Agents-From-Zero-To-Production.svg)](https://GitHub.com/microsoft/Building-AI-Agents-From-Zero-To-Production/pulls/?WT.mc_id=academic-105485-koreyst)
[![歡迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

## 🌱 入門指南

本課程包含建造及部署 AI 代理的基礎課程。

每課內容均以之前課程為基礎，建議由頭開始依序學習至結束。

如果你想深入了解 AI 代理相關主題，可查看 [AI 代理初學者課程](https://aka.ms/ai-agents-beginners)。

### 認識其他學員，答疑解惑

若你在打造 AI 代理過程中遇到困難或有任何疑問，歡迎加入我們在 [Microsoft Foundry Discord](https://discord.gg/Kuaw3ktsu6) 的專屬 Discord 頻道。

### 你需要準備的東西

每課都有可在本地執行的程式碼範例。你可以[分叉此儲存庫](https://github.com/microsoft/Building-AI-Agents-From-Zero-To-Production/fork)來建立自己的副本。

本課程目前使用以下資源：

- [Microsoft 代理框架 (MAF)](https://aka.ms/ai-agents-beginners/agent-framework)
- [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)
- [Azure OpenAI 服務](https://azure.microsoft.com/products/ai-foundry/models/openai)
- [Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli?view=azure-cli-latest)

請確保你已擁有上述服務的使用權限，才可開始學習。

更多關於模型托管及服務選項將陸續推出。

## 🗃️ 課程列表

| **課程**          | **說明**                                                                                      |
|-------------------|-----------------------------------------------------------------------------------------------|
| [代理設計](./lesson-1-agent-design/README.md)           | 介紹我們的「開發者入門」代理使用案例及如何設計有效代理                                           |
| [代理開發](./lesson-2-agent-development/README.md)      | 使用 Microsoft 代理框架 (MAF)，建立 3 個代理協助新開發者入門                                    |
| [代理評估](./lesson-3-agent-evals/README.md)            | 透過 Microsoft Foundry，了解 AI 代理表現情況及改進方法                                          |
| [代理部署](./lesson-4-agent-deployment/README.md)       | 使用托管代理和 OpenAI Chatkit，學習如何將 AI 代理部署到生產環境                                |

## 🎒 其他課程

我們的團隊也製作其他課程！來看看：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 初學者](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js 初學者](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / 邊緣 / MCP / 代理
[![AZD 初學者](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![邊緣 AI 初學者](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP 初學者](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 代理初學者](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![生成式 AI 初學者](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心學習
[![初學者機器學習](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![初學者數據科學](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![初學者人工智能](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![網絡安全初學者](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![網頁開發初學者](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![物聯網初學者](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR 開發初學者](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot 系列
[![AI 配對編程的 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET 的 Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot 冒險](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 貢獻

本項目歡迎貢獻和建議。大多數貢獻都需要您同意一份貢獻者授權協議（CLA），聲明您有權並且確實授予我們使用您的貢獻的權利。詳情請訪問 <https://cla.opensource.microsoft.com>。

當您提交拉取請求時，CLA 機械人會自動判定您是否需要提供 CLA 並在 PR 上適當標註（例如狀態檢查、評論）。請按照機械人提供的指示操作。您只需在使用我們 CLA 的所有倉庫中執行一次此操作。

本項目已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲知詳情，請參閱 [行為準則常見問題](https://opensource.microsoft.com/codeofconduct/faq/) 或通過 [opencode@microsoft.com](mailto:opencode@microsoft.com) 聯繫我們，有任何其他問題或意見。

## 商標

本項目可能包含項目、產品或服務的商標或標誌。Microsoft 商標或標誌的授權使用需遵守並符合
[Microsoft 商標及品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。
修改版項目中使用 Microsoft 商標或標誌不得引起混淆或暗示 Microsoft 贊助。
任何第三方商標或標誌的使用均需遵守該第三方的政策。

## 尋求幫助

如果您遇到困難或有任何有關構建 AI 應用的問題，歡迎加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/Kuaw3ktsu6)

如果您有產品反饋或在構建過程中遇到錯誤，請訪問：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件經由人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們力求準確，但請注意，機器翻譯可能包含錯誤或不準確之處。原文文件以其母語版本為權威依據。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->