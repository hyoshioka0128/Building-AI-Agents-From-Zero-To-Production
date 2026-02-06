# Lesson 2 Agent Development

歡迎來到「從零開始構建 AI 代理到生產課程」的第二課！

在本課中，我們將涵蓋：

- 創建我們的 AI 代理的工具

- 我們開發資源的設置說明

- AI 代理開發最佳實踐

- 建立我們 AI 代理的程式碼演練

讓我們先來看一下用於創建我們 AI 代理的工具。

## Tools and Setup Instructions

### Microsoft Foundry

為了使用大型語言模型（LLMs），我們將使用 [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)。使用 Foundry 會產生費用，因此如果您尚未擁有存取權，請務必遵循帳戶設置說明。

### OpenAI Models

本課程中的代理程式碼範例設定為通過 [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) 使用 OpenAI 模型。

使用此指南了解如何通過 Foundry 部署模型：[Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

本課程請選擇一個 GPT-4.1 或更新版本模型。

### Microsoft Agent Framework

如前所述，我們將使用 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) 來創建並協調我們的 AI 代理。

要安裝 Microsoft Agent Framework 及其他必需套件，請在此專案的根目錄執行以下命令：

```bash
pip install -r requirements.txt
```

### Setup .env Variables

要執行本課程中的程式碼範例，您需要在此專案的根目錄建立 `.env` 檔案。

為了方便起見，您可以複製提供的 `.env.example` 檔案：

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之原文版本應被視為權威依據。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或錯誤詮釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->