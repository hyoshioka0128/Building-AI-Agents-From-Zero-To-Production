# Lesson 2 Phát triển Đại lý

Chào mừng bạn đến với bài học thứ hai của khóa học "Xây dựng Đại lý AI từ con số 0 đến Sản xuất"!

Trong bài học này, chúng ta sẽ trình bày:

- Các công cụ để tạo Đại lý AI của chúng ta

- Hướng dẫn cài đặt các tài nguyên phát triển của chúng ta

- Các thực hành tốt nhất về phát triển Đại lý AI

- Hướng dẫn mã nguồn tạo Đại lý AI của chúng ta

Hãy bắt đầu bằng việc xem xét các công cụ mà chúng ta sẽ sử dụng để tạo Đại lý AI.

## Công cụ và Hướng dẫn cài đặt

### Microsoft Foundry

Để truy cập các Mô hình Ngôn ngữ Lớn (LLMs), chúng ta sẽ sử dụng [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Có các chi phí liên quan đến việc sử dụng Foundry, vì vậy hãy chắc chắn làm theo hướng dẫn để thiết lập tài khoản nếu bạn chưa có quyền truy cập.

### Mô hình OpenAI

Các ví dụ mã đại lý trong khóa học này được thiết lập để sử dụng các mô hình OpenAI thông qua [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry).

Sử dụng hướng dẫn này để tìm hiểu cách triển khai một mô hình bằng Foundry: [Triển khai Mô hình Microsoft Foundry trong cổng Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Chọn một mô hình GPT-4.1 trở lên cho khóa học này.

### Microsoft Agent Framework

Như đã đề cập trước đó, chúng ta sẽ sử dụng [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) để vừa tạo vừa điều phối các Đại lý AI của chúng ta.

Để cài đặt Microsoft Agent Framework và các gói cần thiết khác, hãy chạy lệnh sau khi ở thư mục gốc của dự án này:

```bash
pip install -r requirements.txt
```

### Thiết lập biến .env

Để chạy các ví dụ mã trong khóa học này, bạn sẽ cần tạo một tệp `.env` trong thư mục gốc của dự án này.

Để dễ dàng hơn, bạn có thể sao chép tệp `.env.example` được cung cấp:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin quý vị lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản của nó nên được coi là nguồn tham khảo đáng tin cậy. Đối với những thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->