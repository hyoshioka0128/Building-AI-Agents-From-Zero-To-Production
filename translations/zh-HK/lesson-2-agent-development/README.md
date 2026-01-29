# Lesson 2 Agent Development

歡迎來到「從零到生產建立 AI 代理人課程」的第二課！

在本課程中，我們將涵蓋：

- 用於創建 AI 代理人的工具
  
- 我們的開發資源設定說明

- AI 代理人開發最佳實踐
  
- 創建 AI 代理人的程式碼導覽
  
讓我們先來看看將用於創建 AI 代理人的工具。

## 工具與設定說明

### Microsoft Foundry

為了使用大型語言模型（LLMs），我們將使用[Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)。使用 Foundry 是需要支付費用的，因此如果您尚未擁有帳戶，請務必按照帳戶設定說明進行操作。

### OpenAI 模型

本課程中的代理人程式碼範例設置為通過[Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)使用 OpenAI 模型。

請使用此指南瞭解如何透過 Foundry 部署模型：[在 Foundry 入口網站部署 Microsoft Foundry 模型](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

請為本課程選擇一個 GPT-4.1 或更新版本的模型。

### Microsoft Agent Framework

如前所述，我們將使用[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)來創建並協調我們的 AI 代理人。

要安裝 Microsoft Agent Framework 及其他所需套件，請在此專案的根目錄中執行以下指令：

```bash
pip install -r requirements.txt
```

### 設定 .env 變數

要執行本課程的程式碼範例，您需要在此專案的根目錄建立一個 `.env` 檔案。

為方便起見，您可以複製提供的 `.env.example` 檔案：

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。文件的原始版本應被視為權威來源。對於重要資訊，建議聘請專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->