# AGENTS.md

Hướng dẫn cho các tác nhân mã hóa AI (và những người cộng tác là con người) làm việc trong kho lưu trữ này. Nếu bạn là
một tác nhân tự động thực hiện thay đổi tại đây, hãy đọc file này trước và tuân theo.

## Đây là kho lưu trữ gì

**Xây dựng Tác nhân AI từ Con Số 0 đến Sản phẩm** là một khóa học học tập của Microsoft. Nó dạy các nhà phát triển
cách thiết kế, xây dựng, đánh giá, triển khai và vận hành các tác nhân AI trên **Microsoft Foundry** sử dụng
**Microsoft Agent Framework (MAF)**. Nội dung được tổ chức theo trình tự các bài học, mỗi bài có
file `README.md` và các ví dụ Python có thể chạy được.

```
lesson-1-agent-design/            Use case + how to design effective agents
lesson-2-agent-development/       Build specialised agents with MAF (multiple runnable samples)
lesson-3-agent-evals/             Evaluations and observability
lesson-4-agentdeployment/         Deploy a hosted agent + OpenAI ChatKit front end
lesson-5-hosted-agents-production/ Hosted Agents vs Capability Hosts, BYO storage, governance
lesson-6-toolbox/                 Microsoft Toolbox: define + govern tools centrally
lesson-7-multi-agent-a2a/         Multi-agent orchestration over the A2A protocol
```

Tài liệu gốc: `README.md` (bắt đầu từ đây), `MIGRATION-GUIDE.md` (chi tiết di chuyển SDK), `CHANGELOG.md`.

## Quy tắc vàng

1. **Không bao giờ cam kết bí mật.** Chỉ `*.env.example` được theo dõi; các file `.env` thật sự bị
   git-ignore. Không mã hóa cứng các điểm cuối, khóa, mã thông báo, hoặc chuỗi kết nối trong các ví dụ hoặc tài liệu.
2. **Không đụng tới `translations/` hoặc `translated_images/`.** Chúng được tạo tự động bởi
   một GitHub Action dịch thuật. Không bao giờ chỉnh sửa thủ công; chỉ thực hiện thay đổi nguồn trong các file bài học cấp trên.

3. **Không dùng mô hình lỗi thời.** Sử dụng **`gpt-5.1`** cho chat/đánh giá và **`gpt-5-codex`** cho mã hóa.
   Không **được** giới thiệu `gpt-4o`, `gpt-4.1`, hay bất kỳ mô hình nghỉ hưu nào, và không dùng *GitHub Models*
   (nghỉ hưu ngày 30 tháng 7, 2026) — tất cả mô hình đều được phục vụ qua Microsoft Foundry.
4. **Sử dụng bề mặt SDK hiện tại.** Ví dụ mục tiêu `agent-framework` (khóa phiên bản trong `requirements.txt`)
   với `FoundryChatClient` và **API Phản hồi**. Không tái sử dụng các mẫu cũ
   `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
5. **Giữ thuật ngữ cập nhật**: *Microsoft Foundry* (không phải "Azure AI Foundry"), *Microsoft Agent
   Framework*, *Hosted Agents*, *Capability Hosts*, *Microsoft Toolbox*, *MCP / Hosted MCP*, *A2A*.

## Cài đặt

```bash
python -m venv .venv
# Windows:  .venv\Scripts\Activate.ps1
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt

az login                     # các mẫu xác thực bằng danh tính nhà phát triển của bạn
cp .env.example .env         # sau đó điền điểm cuối dự án Foundry + mô hình của bạn
```

Yêu cầu: **Python 3.12+**, **Azure CLI**, và quyền truy cập vào một dự án **Microsoft Foundry**
với mô hình GPT-5-series đã triển khai. Mỗi README bài học liệt kê các yêu cầu và biến môi trường
cần thiết (xem file `.env.example` cấp bài học nếu có).

## Chạy các ví dụ

Hầu hết các ví dụ bài học 2 khởi chạy **DevUI** cục bộ trên một cổng chuyên dụng (ví dụ từ 8090–8096); máy chủ A2A
trong bài học 7 lắng nghe ở cổng 9000. Kiểm tra docstring/README từng ví dụ để biết lệnh và cổng chính xác.
Vì các ví dụ gọi đến điểm cuối Foundry thật, cần có `.env` hợp lệ và `az login`.

## Xác thực thay đổi

Không có bộ kiểm thử đơn vị; xác thực là tĩnh + trực tiếp:

- **Cổng tĩnh (phải vượt qua trước khi cam kết):** biên dịch byte tất cả ví dụ.
  ```bash
  python -m py_compile $(git ls-files '*.py')
  ```
  Trên Windows PowerShell:
  ```powershell
  git ls-files '*.py' | ForEach-Object { python -m py_compile $_ }
  ```
- **Liên kết Markdown:** công việc CI `static` chạy `markdown-link-check`
  (cấu hình: `.github/workflows/markdown-link-check-config.json`). Xác minh bất kỳ liên kết ngoài mới nào
  trả về (HTTP 200).
- **Kiểm thử nhanh:** `.github/workflows/smoke-test-hosted-agent.yml` chạy hành động Kiểm tra Khói AI
  trên tác nhân được lưu trữ đã triển khai (`workflow_dispatch`, OIDC). Chạy tác nhân trực tiếp cần quyền Azure.

CI (công việc `static`) tự động phát hiện file `.py`, vì vậy các ví dụ mới được bao phủ mà không cần chỉnh sửa
workflow. Không cam kết mã thất bại `py_compile`.

## Quy ước cam kết

- Viết cam kết tập trung với thông điệp rõ ràng, mệnh lệnh.
- Bao gồm phần co-author trên các cam kết có trợ giúp tác nhân:
  ```
  Co-authored-by: Copilot App <223556219+Copilot@users.noreply.github.com>
  ```
- Không cam kết bộ nhớ đệm sinh ra, môi trường ảo, hoặc file `.env` (tất cả đều bị git-ignore).

## Nơi thực hiện các thay đổi cụ thể

| Thay đổi | Vị trí |
|--------|----------|
| Nội dung khóa học / văn bản bài học | `lesson-*/README.md` (chỉ nguồn — không bao giờ chỉnh trong `translations/`) |
| Mã có thể chạy | `lesson-*/**.py`, `setup_vector_store.py` |
| Phụ thuộc | `requirements.txt` (giữ phiên bản cố định) |
| Tài liệu biến môi trường | `.env.example`, `.env.example` ở cấp bài học |
| CI / cổng tĩnh | `.github/workflows/` |
| Kỹ năng khóa học cho trợ lý AI | `.github/skills/` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->