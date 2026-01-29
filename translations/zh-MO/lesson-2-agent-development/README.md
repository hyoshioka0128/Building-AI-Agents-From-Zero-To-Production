# Lesson 2 Agent Development

歡迎來到「從零到生產打造 AI 代理課程」的第二課！

在本課中，我們將涵蓋：

- 建立我們的 AI 代理所需的工具
  
- 我們的開發資源的設定指引

- AI 代理開發最佳實踐
  
- 建立我們的 AI 代理的代碼解說
  
讓我們先來看看用於建立我們 AI 代理的工具。

## 工具與設定指引

### Microsoft Foundry

為了取得大型語言模型 (LLMs) 的使用權，我們將使用 [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)。使用 Foundry 會涉及費用，因此如果您尚未取得使用權，請務必遵照帳號設定指引。

### OpenAI 模型

本課程中的代理程式碼範例設定使用透過 [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) 的 OpenAI 模型。

請使用此指南學習如何透過 Foundry 部署模型：[在 Foundry 入口網站部署 Microsoft Foundry 模型](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

請為本課程選擇一個 GPT-4.1 或更新版本的模型。

### Microsoft Agent Framework

如前所述，我們將使用 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) 來建立並協調我們的 AI 代理。

要安裝 Microsoft Agent Framework 及其他所需套件，請於本專案根目錄執行以下指令：

```bash
pip install -r requirements.txt
```

### 設定 .env 變數

要執行本課程的程式碼範例，您需要在本專案根目錄建立 `.env` 檔案。

為了簡化操作，您可以複製提供的 `.env.example` 檔案：

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或誤譯概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->