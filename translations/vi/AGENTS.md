<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cc2e18ab65df63e75d3619c4752e9b22",
  "translation_date": "2025-10-03T11:29:52+00:00",
  "source_file": "AGENTS.md",
  "language_code": "vi"
}
-->
# AGENTS.md

## Tổng quan dự án

Data Science for Beginners là một chương trình học toàn diện kéo dài 10 tuần với 20 bài học được tạo bởi Microsoft Azure Cloud Advocates. Kho lưu trữ này là một tài nguyên học tập dạy các khái niệm cơ bản về khoa học dữ liệu thông qua các bài học dựa trên dự án, bao gồm Jupyter notebooks, bài kiểm tra tương tác và bài tập thực hành.

**Công nghệ chính:**
- **Jupyter Notebooks**: Phương tiện học tập chính sử dụng Python 3
- **Thư viện Python**: pandas, numpy, matplotlib để phân tích và trực quan hóa dữ liệu
- **Vue.js 2**: Ứng dụng bài kiểm tra (thư mục quiz-app)
- **Docsify**: Trình tạo trang tài liệu để truy cập ngoại tuyến
- **Node.js/npm**: Quản lý gói cho các thành phần JavaScript
- **Markdown**: Tất cả nội dung bài học và tài liệu

**Kiến trúc:**
- Kho lưu trữ giáo dục đa ngôn ngữ với các bản dịch phong phú
- Được cấu trúc thành các mô-đun bài học (1-Introduction đến 6-Data-Science-In-Wild)
- Mỗi bài học bao gồm README, notebooks, bài tập và bài kiểm tra
- Ứng dụng bài kiểm tra Vue.js độc lập để đánh giá trước/sau bài học
- Hỗ trợ GitHub Codespaces và container phát triển VS Code

## Lệnh thiết lập

### Thiết lập kho lưu trữ
```bash
# Clone the repository (if not already cloned)
git clone https://github.com/microsoft/Data-Science-For-Beginners.git
cd Data-Science-For-Beginners
```

### Thiết lập môi trường Python
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data science libraries (no requirements.txt exists)
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

### Thiết lập ứng dụng bài kiểm tra
```bash
# Navigate to quiz app
cd quiz-app

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint and fix files
npm run lint
```

### Máy chủ tài liệu Docsify
```bash
# Install Docsify globally
npm install -g docsify-cli

# Serve documentation locally
docsify serve

# Documentation will be available at localhost:3000
```

### Thiết lập dự án trực quan hóa
Đối với các dự án trực quan hóa như meaningful-visualizations (bài học 13):
```bash
# Navigate to starter or solution folder
cd 3-Data-Visualization/13-meaningful-visualizations/starter

# Install dependencies
npm install

# Start development server
npm run serve

# Build for production
npm run build

# Lint files
npm run lint
```


## Quy trình phát triển

### Làm việc với Jupyter Notebooks
1. Khởi động Jupyter tại thư mục gốc của kho lưu trữ: `jupyter notebook`
2. Điều hướng đến thư mục bài học mong muốn
3. Mở các tệp `.ipynb` để làm bài tập
4. Notebooks là các tài liệu tự chứa với giải thích và ô mã
5. Hầu hết các notebooks sử dụng pandas, numpy và matplotlib - đảm bảo đã cài đặt chúng

### Cấu trúc bài học
Mỗi bài học thường bao gồm:
- `README.md` - Nội dung chính của bài học với lý thuyết và ví dụ
- `notebook.ipynb` - Bài tập thực hành với Jupyter notebook
- `assignment.ipynb` hoặc `assignment.md` - Bài tập thực hành
- Thư mục `solution/` - Notebook và mã giải pháp
- Thư mục `images/` - Tài liệu hình ảnh hỗ trợ

### Phát triển ứng dụng bài kiểm tra
- Ứng dụng Vue.js 2 với tính năng tải lại nóng trong quá trình phát triển
- Các bài kiểm tra được lưu trong `quiz-app/src/assets/translations/`
- Mỗi ngôn ngữ có thư mục dịch riêng (en, fr, es, v.v.)
- Số thứ tự bài kiểm tra bắt đầu từ 0 và lên đến 39 (tổng cộng 40 bài kiểm tra)

### Thêm bản dịch
- Các bản dịch được đặt trong thư mục `translations/` tại thư mục gốc của kho lưu trữ
- Mỗi ngôn ngữ có cấu trúc bài học đầy đủ giống với tiếng Anh
- Dịch tự động thông qua GitHub Actions (co-op-translator.yml)

## Hướng dẫn kiểm tra

### Kiểm tra ứng dụng bài kiểm tra
```bash
cd quiz-app

# Run lint checks
npm run lint

# Test build process
npm run build

# Manual testing: Start dev server and verify quiz functionality
npm run serve
```

### Kiểm tra notebook
- Không có khung kiểm tra tự động cho notebooks
- Xác thực thủ công: Chạy tất cả các ô theo thứ tự để đảm bảo không có lỗi
- Xác minh các tệp dữ liệu có thể truy cập và đầu ra được tạo đúng cách
- Kiểm tra rằng các hình ảnh trực quan được hiển thị đúng

### Kiểm tra tài liệu
```bash
# Verify Docsify renders correctly
docsify serve

# Check for broken links manually by navigating through content
# Verify all lesson links work in the rendered documentation
```

### Kiểm tra chất lượng mã
```bash
# Vue.js projects (quiz-app and visualization projects)
cd quiz-app  # or visualization project folder
npm run lint

# Python notebooks - manual verification recommended
# Ensure imports work and cells execute without errors
```


## Hướng dẫn về phong cách mã

### Python (Jupyter Notebooks)
- Tuân theo hướng dẫn phong cách PEP 8 cho mã Python
- Sử dụng tên biến rõ ràng để giải thích dữ liệu đang được phân tích
- Bao gồm các ô markdown với giải thích trước các ô mã
- Giữ các ô mã tập trung vào một khái niệm hoặc thao tác duy nhất
- Sử dụng pandas để xử lý dữ liệu, matplotlib để trực quan hóa
- Mẫu nhập phổ biến:
  ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  ```


### JavaScript/Vue.js
- Tuân theo hướng dẫn phong cách Vue.js 2 và các thực hành tốt nhất
- Cấu hình ESLint trong `quiz-app/package.json`
- Sử dụng các thành phần đơn tệp Vue (.vue files)
- Duy trì kiến trúc dựa trên thành phần
- Chạy `npm run lint` trước khi commit thay đổi

### Tài liệu Markdown
- Sử dụng hệ thống tiêu đề rõ ràng (# ## ### v.v.)
- Bao gồm các khối mã với chỉ định ngôn ngữ
- Thêm văn bản thay thế cho hình ảnh
- Liên kết đến các bài học và tài nguyên liên quan
- Giữ độ dài dòng hợp lý để dễ đọc

### Tổ chức tệp
- Nội dung bài học trong các thư mục được đánh số (01-defining-data-science, v.v.)
- Giải pháp trong các thư mục con `solution/` chuyên dụng
- Các bản dịch phản ánh cấu trúc tiếng Anh trong thư mục `translations/`
- Giữ các tệp dữ liệu trong thư mục `data/` hoặc các thư mục bài học cụ thể

## Xây dựng và triển khai

### Triển khai ứng dụng bài kiểm tra
```bash
cd quiz-app

# Build production version
npm run build

# Output is in dist/ folder
# Deploy dist/ folder to static hosting (Azure Static Web Apps, Netlify, etc.)
```

### Triển khai Azure Static Web Apps
Ứng dụng quiz-app có thể được triển khai lên Azure Static Web Apps:
1. Tạo tài nguyên Azure Static Web App
2. Kết nối với kho lưu trữ GitHub
3. Cấu hình cài đặt xây dựng:
   - Vị trí ứng dụng: `quiz-app`
   - Vị trí đầu ra: `dist`
4. Workflow GitHub Actions sẽ tự động triển khai khi có thay đổi

### Trang tài liệu
```bash
# Build PDF from Docsify (optional)
npm run convert

# Docsify documentation is served directly from markdown files
# No build step required for deployment
# Deploy repository to static hosting with Docsify
```

### GitHub Codespaces
- Kho lưu trữ bao gồm cấu hình container phát triển
- Codespaces tự động thiết lập môi trường Python và Node.js
- Mở kho lưu trữ trong Codespace qua giao diện GitHub
- Tất cả các phụ thuộc được cài đặt tự động

## Hướng dẫn Pull Request

### Trước khi gửi
```bash
# For Vue.js changes in quiz-app
cd quiz-app
npm run lint
npm run build

# Test changes locally
npm run serve
```

### Định dạng tiêu đề PR
- Sử dụng tiêu đề rõ ràng, mô tả
- Định dạng: `[Component] Mô tả ngắn gọn`
- Ví dụ:
  - `[Lesson 7] Sửa lỗi nhập notebook Python`
  - `[Quiz App] Thêm bản dịch tiếng Đức`
  - `[Docs] Cập nhật README với các yêu cầu mới`

### Kiểm tra bắt buộc
- Đảm bảo tất cả mã chạy không có lỗi
- Xác minh các notebook thực thi hoàn toàn
- Xác nhận các ứng dụng Vue.js xây dựng thành công
- Kiểm tra rằng các liên kết tài liệu hoạt động
- Kiểm tra ứng dụng bài kiểm tra nếu có thay đổi
- Xác minh các bản dịch duy trì cấu trúc nhất quán

### Hướng dẫn đóng góp
- Tuân theo phong cách và mẫu mã hiện có
- Thêm các bình luận giải thích cho logic phức tạp
- Cập nhật tài liệu liên quan
- Kiểm tra thay đổi trên các mô-đun bài học khác nhau nếu áp dụng
- Xem lại tệp CONTRIBUTING.md

## Ghi chú bổ sung

### Các thư viện thường dùng
- **pandas**: Xử lý và phân tích dữ liệu
- **numpy**: Tính toán số học
- **matplotlib**: Trực quan hóa và vẽ biểu đồ dữ liệu
- **seaborn**: Trực quan hóa dữ liệu thống kê (một số bài học)
- **scikit-learn**: Học máy (bài học nâng cao)

### Làm việc với tệp dữ liệu
- Các tệp dữ liệu nằm trong thư mục `data/` hoặc các thư mục bài học cụ thể
- Hầu hết các notebook mong đợi tệp dữ liệu ở đường dẫn tương đối
- Tệp CSV là định dạng dữ liệu chính
- Một số bài học sử dụng JSON cho ví dụ dữ liệu phi quan hệ

### Hỗ trợ đa ngôn ngữ
- Hơn 40 bản dịch ngôn ngữ thông qua GitHub Actions tự động
- Quy trình dịch trong `.github/workflows/co-op-translator.yml`
- Các bản dịch trong thư mục `translations/` với mã ngôn ngữ
- Dịch bài kiểm tra trong `quiz-app/src/assets/translations/`

### Tùy chọn môi trường phát triển
1. **Phát triển cục bộ**: Cài đặt Python, Jupyter, Node.js trên máy
2. **GitHub Codespaces**: Môi trường phát triển tức thì trên đám mây
3. **VS Code Dev Containers**: Phát triển dựa trên container cục bộ
4. **Binder**: Khởi chạy notebook trên đám mây (nếu được cấu hình)

### Hướng dẫn nội dung bài học
- Mỗi bài học độc lập nhưng xây dựng dựa trên các khái niệm trước đó
- Bài kiểm tra trước bài học kiểm tra kiến thức trước đó
- Bài kiểm tra sau bài học củng cố kiến thức
- Bài tập cung cấp thực hành thực tế
- Sketchnotes cung cấp tóm tắt trực quan

### Xử lý sự cố thường gặp

**Vấn đề kernel Jupyter:**
```bash
# Ensure correct kernel is installed
python -m ipykernel install --user --name=datascience
```

**Lỗi cài đặt npm:**
```bash
# Clear npm cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Lỗi nhập trong notebook:**
- Xác minh tất cả các thư viện cần thiết đã được cài đặt
- Kiểm tra khả năng tương thích phiên bản Python (khuyến nghị Python 3.7+)
- Đảm bảo môi trường ảo đã được kích hoạt

**Docsify không tải:**
- Xác minh bạn đang phục vụ từ thư mục gốc của kho lưu trữ
- Kiểm tra rằng `index.html` tồn tại
- Đảm bảo truy cập mạng đúng cách (cổng 3000)

### Cân nhắc về hiệu suất
- Các tập dữ liệu lớn có thể mất thời gian để tải trong notebook
- Việc hiển thị hình ảnh trực quan có thể chậm đối với các biểu đồ phức tạp
- Máy chủ phát triển Vue.js cho phép tải lại nóng để lặp nhanh
- Các bản dựng sản xuất được tối ưu hóa và giảm thiểu

### Ghi chú bảo mật
- Không nên commit dữ liệu nhạy cảm hoặc thông tin đăng nhập
- Sử dụng biến môi trường cho bất kỳ khóa API nào trong các bài học đám mây
- Các bài học liên quan đến Azure có thể yêu cầu thông tin đăng nhập tài khoản Azure
- Giữ các phụ thuộc được cập nhật để vá lỗi bảo mật

## Đóng góp cho bản dịch
- Các bản dịch tự động được quản lý thông qua GitHub Actions
- Chào đón các chỉnh sửa thủ công để đảm bảo độ chính xác của bản dịch
- Tuân theo cấu trúc thư mục dịch hiện có
- Cập nhật liên kết bài kiểm tra để bao gồm tham số ngôn ngữ: `?loc=fr`
- Kiểm tra các bài học đã dịch để đảm bảo hiển thị đúng

## Tài nguyên liên quan
- Chương trình chính: https://aka.ms/datascience-beginners
- Microsoft Learn: https://docs.microsoft.com/learn/
- Student Hub: https://docs.microsoft.com/learn/student-hub
- Diễn đàn thảo luận: https://github.com/microsoft/Data-Science-For-Beginners/discussions
- Các chương trình học khác của Microsoft: ML for Beginners, AI for Beginners, Web Dev for Beginners

## Bảo trì dự án
- Cập nhật thường xuyên để giữ nội dung luôn mới
- Chào đón đóng góp từ cộng đồng
- Các vấn đề được theo dõi trên GitHub
- PRs được xem xét bởi các nhà quản lý chương trình học
- Xem xét và cập nhật nội dung hàng tháng

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.