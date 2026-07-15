# Nhật ký thay đổi

Tất cả các thay đổi đáng chú ý trong **Xây dựng Các Tác nhân AI từ Con số đến Sản xuất** được ghi lại tại đây.

Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Khóa học này là một chương trình học động thay vì gói phần mềm có phiên bản, do đó các mục được nhóm
theo ngày một tập hợp các thay đổi được áp dụng thay vì theo số phiên bản ngữ nghĩa.

## 13 tháng 7 năm 2026

### Đã thêm
- **Vệ sinh kho lưu trữ để chia sẻ công khai** — củng cố `.gitignore` với phần dành riêng
  cho Python / notebooks / secrets / hệ điều hành (các biến thể tệp env, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), đồng thời giữ được mọi tệp `*.env.example`
  được theo dõi. Đã thêm `CHANGELOG.md` này, một hướng dẫn dành cho cộng tác viên/đại lý `AGENTS.md`,
  và các tệp kỹ năng của khóa học.

### Đã thay đổi
- Chuẩn bị kho lưu trữ để chia sẻ công khai: loại bỏ các định danh cá nhân và môi trường sống
  (tên tài khoản, dự án, nhóm tài nguyên và danh tính) khỏi các tài liệu đã phát hành, và chuyển báo cáo
  hiện đại hóa/phân tích khoảng cách nội bộ ra khỏi kho lưu trữ (tóm tắt dành cho người học nằm trong
  nhật ký thay đổi này).

## [Đổi mới Foundry 2026]

Làm mới hoàn chỉnh về kỹ thuật, thuật ngữ và chương trình giảng dạy phù hợp với nền tảng
**Microsoft Foundry 2026**. Xem `MIGRATION-GUIDE.md` để biết chi tiết di chuyển ở cấp mã.

### Đã thêm
- **Bài 5 – Tác nhân Hosting Sản xuất** (`lesson-5-hosted-agents-production/`): Tác nhân Hosted so với
  Capability Hosts, tùy chọn mang theo Cosmos DB / Storage / AI Search, duy trì bộ nhớ và luồng,
  quy trình phê duyệt MCP Hosted và danh sách kiểm soát quản trị.
- **Bài 6 – Hộp công cụ Microsoft** (`lesson-6-toolbox/`): định nghĩa công cụ một lần và quản lý tập trung,
  cộng với mẫu tiêu dùng có thể chạy được (`toolbox_agent.py`) truy cập tới hộp công cụ qua
  một điểm cuối MCP duy nhất.
- **Bài 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): khai thác một tác nhân qua giao thức
  Agent-to-Agent (A2A) mở (`a2a_server.py`) và tiêu dùng một tác nhân từ xa như một đối tác
  (`a2a_client.py`). Đã xác nhận trực tiếp end-to-end.
- **Tác nhân Đề xuất Nhiệm vụ** (`lesson-2-agent-development/task-recommendation-agent.py`):
  hiện thực Kịch bản Bài 1 Câu 2 sử dụng máy chủ MCP GitHub từ xa như một công cụ.
- **Kịch bản thiết lập kho vector** (`setup_vector_store.py`): tạo và điền dữ liệu cho kho vector
  mà tác nhân tìm kiếm nhân viên phụ thuộc vào (trước đây được tham chiếu nhưng bị thiếu).
- **Kiểm tra CI cơ bản + cổng tĩnh** (`.github/workflows/smoke-test-hosted-agent.yml`): một công việc `static` chạy
  `py_compile` và kiểm tra liên kết markdown trên mọi PR/push; một công việc `smoke` chạy hành động AI Smoke Test
  đối với tác nhân hosted đã triển khai (OIDC, `workflow_dispatch`).
- **Hướng dẫn điều kiện tiên quyết và thiết lập** được thêm vào từng bài học và vào README gốc
  (Python 3.12+, `az login`, hướng dẫn mô hình, chi phí & dọn dẹp).
- **Tài liệu chủ đạo mới**: `MIGRATION-GUIDE.md`.

### Đã thay đổi
- **Đổi thương hiệu**: *Azure AI Foundry* → **Microsoft Foundry** trên toàn bộ khóa học.
- **Di chuyển SDK** sang bề mặt hiện tại của Microsoft Agent Framework — các ví dụ bây giờ sử dụng
  `agent-framework` `1.2.0` với `FoundryChatClient` và **API Phản hồi**, thay thế các mẫu
  trước đó `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
- **Khoá chặt các phụ thuộc**: `requirements.txt` giờ khoá chặt `agent-framework`, `agent-framework-foundry`
  và các gói liên quan thay vì cài đặt các phiên bản tiền phát hành chưa khoá, giúp các ví dụ có thể tái tạo.
- **Biến môi trường** được thống nhất giữa `deploy.py`, `agent.yaml`, `main.py` và
  các tệp `.env.example`.
- Các sơ đồ kiến trúc trong README và danh mục tác nhân/kịch bản được viết lại để phù hợp với mã đã phát hành.

### Đã sửa
- Sửa lỗi liên kết hỏng ROOT README tới Bài 4 (`lesson-4-agentdeployment`).
- Viết README cho Bài 3 trước đây còn trống (đánh giá + khả năng quan sát).
- Thay thế mẫu cũ `asyncio.get_event_loop().run_until_complete` trong
  tác nhân đề xuất học tập.

### Không còn được dùng / Bỏ
- Loại bỏ hoàn toàn việc sử dụng các mô hình cũ **GPT-4o / GPT-4.1**. Các ví dụ chat và đánh giá giờ dùng
  **gpt-5.1**; các ví dụ lập trình dùng **gpt-5-codex**.
- Ghi chú rằng **GitHub Models** đang được ngừng hoạt động (30 tháng 7, 2026); khóa học phục vụ tất cả mô hình
  qua Microsoft Foundry và không phụ thuộc vào GitHub Models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->