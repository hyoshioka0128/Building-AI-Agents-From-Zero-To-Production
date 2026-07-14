# 移行ガイド — Microsoft Foundry Agent Framework（2026年7月）

このガイドは、コースサンプルが最初に対応していたSDKの表面を
<strong>現在の公開済み</strong> Microsoft Agent Frameworkパッケージにマッピングします。以下のすべてのマッピングと
シグネチャは、インストール済みパッケージを調査して検証されています
（`agent-framework 1.2.0`、`agent-framework-foundry 1.2.0`）。

> **なぜ重要か:** <strong>Microsoft Foundry</strong>へのリブランドにより、クライアントの表面は
> `agent_framework.azure`（旧 `AzureAI*` クラス）から **`agent_framework.foundry`**
> （`FoundryChatClient`、`FoundryAgent`）に移行しました。旧トップレベルのホスト型ツールクラス
> （`HostedMCPTool`、`HostedFileSearchTool`、`HostedVectorStoreContent`）は削除されました。ホスト型
> ツールは今や `get_*_tool(...)` ファクトリーメソッドを通じて<strong>クライアントから</strong>作成されます。

---

## 1. インポートとクライアントのマッピング

| 旧（コースサンプル） | 新（Microsoft Foundry） |
|----------------------|-------------------------|
| `from agent_framework.azure import AzureAIClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureAIAgentClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework.azure import AzureOpenAIChatClient` | `from agent_framework.foundry import FoundryChatClient` |
| `from agent_framework import ChatAgent` | `client.as_agent(...)` → 返り値は `Agent` |
| `from agent_framework import HostedMCPTool` | `client.get_mcp_tool(...)` |
| `from agent_framework import HostedFileSearchTool, HostedVectorStoreContent` | `client.get_file_search_tool(vector_store_ids=[...])` |
| `from agent_framework import HandoffBuilder` | `from agent_framework.orchestrations import HandoffBuilder` |
| `MCPStreamableHTTPTool`（クライアント側MCP） | 変更なし — 依然として `from agent_framework import MCPStreamableHTTPTool` |

**資格情報パラメータの名称変更：** 旧クライアントは `async_credential=...` を受け取りましたが、
`FoundryChatClient` は `credential=...` を受け取ります。

---

## 2. 検証済みシグネチャ

```python
FoundryChatClient(
    *, project_endpoint: str | None = None,   # または AZURE_AI_PROJECT_ENDPOINT を設定します
    project_client: AIProjectClient | None = None,
    model: str | None = None,                 # またはモデル環境変数を設定します
    credential=None, ...
)

client.as_agent(*, id=None, name=None, description=None, instructions=None,
                tools=None, context_providers=None, middleware=None, ...) -> Agent

client.get_file_search_tool(*, vector_store_ids: list[str],
                            max_num_results: int | None = None, ...)

client.get_mcp_tool(*, name: str, url: str | None = None,
                    approval_mode: "always_require" | "never_require" | dict | None = None,
                    allowed_tools: list[str] | None = None, ...)

client.get_toolbox(name: str, *, version: str | None = None)   # マイクロソフトツールボックス
client.configure_azure_monitor(enable_sensitive_data: bool = False)  # 可観測性
```

---

## 3. 以前 / 以降 — ホスト型MCPツールを持つ単一エージェントの場合

<strong>以前</strong>（`azure-learning-agent.py`）：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework import HostedMCPTool
from agent_framework.azure import AzureAIClient

client = AzureAIClient(async_credential=AzureCliCredential())
agent = client.create_agent(
    name="LearningPathAgent",
    instructions=AGENT_INSTRUCTIONS,
    tools=HostedMCPTool(
        name="Microsoft Learn MCP",
        url="https://learn.microsoft.com/api/mcp",
        approval_mode="never_require",
    ),
)
```

<strong>以降</strong>（Microsoft Foundry）：

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    name="LearningPathAgent",
    instructions=AGENT_INSTRUCTIONS,
    tools=client.get_mcp_tool(
        name="Microsoft Learn MCP",
        url="https://learn.microsoft.com/api/mcp",
        approval_mode="never_require",
    ),
)
```

---

## 4. 以前 / 以降 — ホスト型ファイル検索（ベクターストア）

<strong>以前</strong>（`employee-search-agent.py`）：

```python
from agent_framework import ChatAgent, HostedFileSearchTool, HostedVectorStoreContent
from agent_framework.azure import AzureAIAgentClient

file_search_tool = HostedFileSearchTool(
    inputs=[HostedVectorStoreContent(vector_store_id=os.environ["VECTOR_STORE_ID"])]
)
agent = ChatAgent(
    chat_client=AzureAIAgentClient(async_credential=AzureCliCredential()),
    instructions="...",
    tools=[file_search_tool],
)
```

<strong>以降</strong>：

```python
from agent_framework.foundry import FoundryChatClient

client = FoundryChatClient(credential=AzureCliCredential())
agent = client.as_agent(
    instructions="...",
    tools=[client.get_file_search_tool(vector_store_ids=[os.environ["VECTOR_STORE_ID"]])],
)
```

---

## 5. 非推奨の非同期パターン

<strong>以前</strong>（`learning-recommendation-agent.py`）：

```python
asyncio.get_event_loop().run_until_complete(learn_mcp_tool.connect())
```

`asyncio.get_event_loop()` は非推奨です。ホスト型の `client.get_mcp_tool(...)`
（手動接続不要）を使用するか、クライアント側の `MCPStreamableHTTPTool` を使う必要がある場合は
`asyncio.run(...)` または `async with` コンテキストでラップしてください。

---

## 6. 本コースで今使う高度な表面

| 機能 | インポート |
|-----------|--------|
| **Microsoft Toolbox** | `client.get_toolbox("<name>")`、`from agent_framework.foundry import select_toolbox_tools, FoundryHostedToolType` |
| **Foundry Memory** | `from agent_framework.foundry import FoundryMemoryProvider` |
| **Observability / eval** | `client.configure_azure_monitor()`、`from agent_framework.foundry import FoundryEvals, evaluate_traces` |
| **Foundry Local** | `from agent_framework.foundry import FoundryLocalClient` |
| **A2A** | `agent-framework-a2a`（`import agent_framework.a2a`） |
| **Hosted-agent runtime** | `agent-framework-foundry-hosting`、`azure.ai.agentserver` |

> **注記:** これらのスニペットは現在のパッケージとインポート・シグネチャを確認済みです。
> エンドツーエンドの実行には、Microsoft Foundryプロジェクト、デプロイ済みチャットモデル、
> （ファイル検索の場合）充填済みのベクターストアがさらに必要です。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->