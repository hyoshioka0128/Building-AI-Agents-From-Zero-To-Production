<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5990c2d40039586841ab255e3395d805",
  "translation_date": "2026-01-27T11:06:28+00:00",
  "source_file": "lesson-2-agent-development/README.md",
  "language_code": "zh"
}
-->
# Lesson 2 代理开发

欢迎来到“从零到生产构建 AI 代理课程”的第二课！

在本课中，我们将涵盖：

- 创建 AI 代理的工具
  
- 开发资源的设置说明

- AI 代理开发最佳实践
  
- 创建 AI 代理的代码讲解
  
让我们首先看看将用来创建 AI 代理的工具。

## 工具和设置说明

### Microsoft Foundry

为了访问大型语言模型（LLM），我们将使用[Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)。使用 Foundry 会产生费用，因此如果您还没有访问权限，请务必按照账户设置说明操作。

### OpenAI 模型

本课程中的代理代码示例设置为通过[Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry)使用 OpenAI 模型。

请使用此指南了解如何通过 Foundry 部署模型：[在 Foundry 门户中部署 Microsoft Foundry 模型](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

请为本课程选择一个 GPT-4.1 或更高版本的模型。

### Microsoft Agent Framework

如前所述，我们将使用[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)来创建和编排我们的 AI 代理。

要安装 Microsoft Agent Framework 及其他必需的包，请在本项目的根目录中运行以下命令：

```bash
pip install -r requirements.txt
```

### 设置 .env 变量

要运行本课程中的代码示例，您需要在本项目的根目录中创建一个 `.env` 文件。

为方便起见，您可以复制提供的 `.env.example` 文件：

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文档由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而导致的任何误解或曲解，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->