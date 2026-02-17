# Lesson 2 Agent Development

「Building AI Agent from Zero to Production Course」第2課へようこそ！

このレッスンでは以下を扱います：

- AIエージェント作成に使うツール

- 開発用リソースのセットアップ手順

- AIエージェント開発のベストプラクティス

- AIエージェント作成のコード解説

まずは、AIエージェントを作成するためのツールを見ていきましょう。

## Tools and Setup Instructions

### Microsoft Foundry

大規模言語モデル（LLM）へのアクセスには [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) を使用します。Foundryの利用には費用が発生するため、まだアクセス権を持っていない場合はアカウント設定の指示に従ってください。

### OpenAI Models

このコースのエージェントコードのサンプルは、[Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) を通じてOpenAIモデルを使用するよう設定されています。

Foundryでモデルをデプロイする方法はこちらのガイドを参照してください: [Deploy Microsoft Foundry Models in the Foundry portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

本コースではGPT-4.1以上のモデルを1つ選択してください。

### Microsoft Agent Framework

前述の通り、AIエージェントの作成とオーケストレーションには [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) を使用します。

Microsoft Agent Frameworkおよびその他必要なパッケージをインストールするには、このプロジェクトのルートディレクトリで次のコマンドを実行してください：

```bash
pip install -r requirements.txt
```

### Setup .env Variables

このコースのコードサンプルを実行するには、このプロジェクトのルートディレクトリに `.env` ファイルを作成する必要があります。

簡単にするために、用意された `.env.example` ファイルをコピーしてください：

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文の言語による文書が公式の情報源として優先されるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当方は一切責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
