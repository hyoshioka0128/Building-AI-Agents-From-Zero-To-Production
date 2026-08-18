# レッスン2 エージェント開発

「ゼロからプロダクションまでの AI エージェント構築コース」の第2回レッスンへようこそ！

このレッスンでは以下を扱います：

- AIエージェント作成に使うツール

- 開発用リソースのセットアップ手順

- AIエージェント開発のベストプラクティス

- AIエージェント作成のコード解説

まずは、AIエージェントを作成するためのツールを見ていきましょう。

## ツールとセットアップ手順

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

### Azureでの認証

エージェントはAzure CLIの資格情報（`AzureCliCredential`）を使用してMicrosoft Foundryに対する認証を行います。そのため、サンプルを実行する前にサインインする必要があります。

```bash
az login
# 複数のサブスクリプションがある場合は、Foundryプロジェクトが含まれるサブスクリプションを選択してください：
az account set --subscription "<your-subscription-id>"
```

モデルやエージェントのAPIを呼び出せるよう、使用するアカウントにFoundryプロジェクトでの**Azure AI User**ロール（または同等の権限）が割り当てられていることを確認してください。

### .env変数の設定

このコースのコードサンプルを実行するには、このプロジェクトのルートディレクトリに `.env` ファイルを作成する必要があります。

簡単にするために、用意された `.env.example` ファイルをコピーしてください：

```bash
cp .env.example .env
```

次に、エージェントが読み取る2つの変数を設定します（`FoundryChatClient` がこれらを自動的に認識します）：

| 変数 | 内容 | 確認場所 |
|----------|------------|------------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Foundry **プロジェクト**のエンドポイント（`/api/projects/<project>` で終わるもの） | Foundryポータル → 対象プロジェクト → **Overview** → *Endpoints* |
| `FOUNDRY_MODEL` | エージェントが実行されるモデルのデプロイ名（例: `gpt-5.1`） | Foundryポータル → **Models + endpoints** |

### 従業員用ベクトルストアの作成

サンプルの一つである**従業員検索エージェント（Employee Search Agent）**は、Microsoft Foundryの**ベクトルストア**に格納された従業員ディレクトリを検索します。ベクトルストアを一度作成し、出力されたIDをコピーして、`.env` ファイルに `VECTOR_STORE_ID` として設定してください（`.env` ファイルを読み込めるよう、リポジトリのルートディレクトリから実行してください）：

```bash
python lesson-2-agent-development/setup_vector_store.py
```

### サンプルの実行

各エージェントは、それぞれ独自のローカルDevUI（開発用UI）で動作します。例：

```bash
python lesson-2-agent-development/employee-search-agent.py
```

その後、表示された `http://localhost:<port>` というURLをブラウザで開き、エージェントとチャットを行います。

## 本レッスンのエージェント

各サンプルは、Microsoft Agent Frameworkを使用して構築された独立したエージェントです。これらを組み合わせることで、[レッスン1](../lesson-1-agent-design/README.md)で設計したシナリオが実装されます：

| サンプル | レッスン1のシナリオ | 使用するツール | ポート |
|--------|-------------------|-----------|------|
| `employee-search-agent.py` | シナリオ1 — 従業員検索 | ベクターストアに対するFoundryホスト型**ファイル検索** | 8090 |
| `task-recommendation-agent.py` | シナリオ2 — タスク推奨 | **GitHub MCP**サーバー（ホスト型MCPツール） | 8095 |
| `azure-learning-agent.py` | シナリオ3 — コードアシスタント（調査） | **Microsoft Learn MCP**サーバー（ホスト型MCPツール） | 8092 |
| `coding-agent.py` | シナリオ3 — コードアシスタント（コーディング） | **Code Interpreter** | 8093 |
| `learning-recommendation-agent.py` | サポート用エージェント | Learn MCP + 推論 | 8091 |
| `agent-orchestration.py` | シナリオの統合 | マルチエージェント**ハンドオフ**・オーケストレーション | 8094 |

> **タスク推奨エージェントに関する注記:** `task-recommendation-agent.py` を動作させるには、
> `.env` ファイルに `GITHUB_PERSONAL_ACCESS_TOKEN` を設定する必要があります
> （トークンは <https://github.com/settings/personal-access-tokens/new> で作成してください）。
> このエージェントは、開発者の最近のGitHubアクティビティを読み取り、
> それに合致するオープンなIssueを1〜3件推奨します。これはまさにシナリオ2の設計そのものです。
> GitHubを呼び出すサンプルはこれだけであり、他のサンプルはFoundryプロジェクトのみを必要とします。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文の言語による文書が公式の情報源として優先されるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当方は一切責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
