<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10f86fb29b5407088445ac803b3d0ed1",
  "translation_date": "2025-10-03T14:17:33+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "vi"
}
-->
# Đóng góp cho Data Science for Beginners

Cảm ơn bạn đã quan tâm đến việc đóng góp cho chương trình học Data Science for Beginners! Chúng tôi hoan nghênh sự đóng góp từ cộng đồng.

## Mục lục

- [Quy tắc ứng xử](../..)
- [Làm thế nào để đóng góp?](../..)
- [Bắt đầu](../..)
- [Hướng dẫn đóng góp](../..)
- [Quy trình Pull Request](../..)
- [Hướng dẫn về phong cách](../..)
- [Thỏa thuận cấp phép cho người đóng góp](../..)

## Quy tắc ứng xử

Dự án này đã áp dụng [Quy tắc ứng xử mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Để biết thêm thông tin, hãy xem [Câu hỏi thường gặp về Quy tắc ứng xử](https://opensource.microsoft.com/codeofconduct/faq/)  
hoặc liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu bạn có thêm câu hỏi hoặc ý kiến.

## Làm thế nào để đóng góp?

### Báo cáo lỗi

Trước khi tạo báo cáo lỗi, vui lòng kiểm tra các vấn đề hiện có để tránh trùng lặp. Khi bạn tạo báo cáo lỗi, hãy cung cấp càng nhiều chi tiết càng tốt:

- **Sử dụng tiêu đề rõ ràng và mô tả**
- **Mô tả các bước cụ thể để tái hiện vấn đề**
- **Cung cấp ví dụ cụ thể** (đoạn mã, ảnh chụp màn hình)
- **Mô tả hành vi bạn quan sát được và điều bạn mong đợi**
- **Bao gồm thông tin về môi trường của bạn** (Hệ điều hành, phiên bản Python, trình duyệt)

### Đề xuất cải tiến

Chúng tôi hoan nghênh các đề xuất cải tiến! Khi đề xuất cải tiến:

- **Sử dụng tiêu đề rõ ràng và mô tả**
- **Cung cấp mô tả chi tiết về cải tiến được đề xuất**
- **Giải thích tại sao cải tiến này hữu ích**
- **Liệt kê các tính năng tương tự trong các dự án khác, nếu có**

### Đóng góp cho tài liệu

Cải thiện tài liệu luôn được đánh giá cao:

- **Sửa lỗi chính tả và ngữ pháp**
- **Cải thiện sự rõ ràng của các giải thích**
- **Thêm tài liệu còn thiếu**
- **Cập nhật thông tin lỗi thời**
- **Thêm ví dụ hoặc trường hợp sử dụng**

### Đóng góp mã

Chúng tôi hoan nghênh các đóng góp mã bao gồm:

- **Bài học hoặc bài tập mới**
- **Sửa lỗi**
- **Cải tiến các notebook hiện có**
- **Bộ dữ liệu hoặc ví dụ mới**
- **Cải tiến ứng dụng quiz**

## Bắt đầu

### Yêu cầu

Trước khi đóng góp, hãy đảm bảo bạn có:

1. Tài khoản GitHub
2. Git được cài đặt trên hệ thống của bạn
3. Python 3.7+ và Jupyter được cài đặt
4. Node.js và npm (đối với đóng góp ứng dụng quiz)
5. Hiểu biết về cấu trúc chương trình học

Xem [INSTALLATION.md](INSTALLATION.md) để biết hướng dẫn cài đặt chi tiết.

### Fork và Clone

1. **Fork repository** trên GitHub  
2. **Clone fork của bạn** về máy:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Data-Science-For-Beginners.git
   cd Data-Science-For-Beginners
   ```
3. **Thêm upstream remote**:
   ```bash
   git remote add upstream https://github.com/microsoft/Data-Science-For-Beginners.git
   ```

### Tạo nhánh

Tạo một nhánh mới cho công việc của bạn:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Quy ước đặt tên nhánh:
- `feature/` - Tính năng hoặc bài học mới
- `fix/` - Sửa lỗi
- `docs/` - Thay đổi tài liệu
- `refactor/` - Tái cấu trúc mã

## Hướng dẫn đóng góp

### Đối với nội dung bài học

Khi đóng góp bài học hoặc chỉnh sửa bài học hiện có:

1. **Tuân theo cấu trúc hiện có**:
   - README.md với nội dung bài học
   - Notebook Jupyter với bài tập
   - Bài tập (nếu có)
   - Liên kết đến quiz trước và sau bài học

2. **Bao gồm các yếu tố sau**:
   - Mục tiêu học tập rõ ràng
   - Giải thích từng bước
   - Ví dụ mã với chú thích
   - Bài tập thực hành
   - Liên kết đến tài nguyên bổ sung

3. **Đảm bảo tính dễ tiếp cận**:
   - Sử dụng ngôn ngữ rõ ràng, đơn giản
   - Cung cấp văn bản thay thế cho hình ảnh
   - Bao gồm chú thích mã
   - Cân nhắc các phong cách học tập khác nhau

### Đối với Notebook Jupyter

1. **Xóa tất cả đầu ra** trước khi commit:
   ```bash
   jupyter nbconvert --clear-output --inplace notebook.ipynb
   ```

2. **Bao gồm các ô markdown** với giải thích

3. **Sử dụng định dạng nhất quán**:
   ```python
   # Import libraries at the top
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Use meaningful variable names
   # Add comments for complex operations
   # Follow PEP 8 style guidelines
   ```

4. **Kiểm tra notebook** hoàn toàn trước khi gửi

### Đối với mã Python

Tuân theo hướng dẫn phong cách [PEP 8](https://www.python.org/dev/peps/pep-0008/):

```python
# Good practices
import pandas as pd

def calculate_mean(data):
    """Calculate the mean of a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        float: Mean of the dataset
    """
    return sum(data) / len(data)
```

### Đối với đóng góp ứng dụng quiz

Khi chỉnh sửa ứng dụng quiz:

1. **Kiểm tra cục bộ**:
   ```bash
   cd quiz-app
   npm install
   npm run serve
   ```

2. **Chạy linter**:
   ```bash
   npm run lint
   ```

3. **Xây dựng thành công**:
   ```bash
   npm run build
   ```

4. **Tuân theo hướng dẫn phong cách Vue.js** và các mẫu hiện có

### Đối với bản dịch

Khi thêm hoặc cập nhật bản dịch:

1. Tuân theo cấu trúc trong thư mục `translations/`
2. Sử dụng mã ngôn ngữ làm tên thư mục (ví dụ: `fr` cho tiếng Pháp)
3. Duy trì cấu trúc tệp giống như phiên bản tiếng Anh
4. Cập nhật liên kết quiz để bao gồm tham số ngôn ngữ: `?loc=fr`
5. Kiểm tra tất cả liên kết và định dạng

## Quy trình Pull Request

### Trước khi gửi

1. **Cập nhật nhánh của bạn** với các thay đổi mới nhất:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Kiểm tra các thay đổi của bạn**:
   - Chạy tất cả notebook đã chỉnh sửa
   - Kiểm tra ứng dụng quiz nếu đã chỉnh sửa
   - Xác minh tất cả liên kết hoạt động
   - Kiểm tra lỗi chính tả và ngữ pháp

3. **Commit các thay đổi của bạn**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Viết thông điệp commit rõ ràng:
   - Sử dụng thì hiện tại ("Thêm tính năng" thay vì "Đã thêm tính năng")
   - Sử dụng giọng điệu mệnh lệnh ("Di chuyển con trỏ đến..." thay vì "Di chuyển con trỏ đến...")
   - Giới hạn dòng đầu tiên trong 72 ký tự
   - Tham chiếu các vấn đề và pull request khi cần thiết

4. **Push lên fork của bạn**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Tạo Pull Request

1. Truy cập [repository](https://github.com/microsoft/Data-Science-For-Beginners)  
2. Nhấp vào "Pull requests" → "New pull request"  
3. Nhấp vào "compare across forks"  
4. Chọn fork và nhánh của bạn  
5. Nhấp vào "Create pull request"

### Định dạng tiêu đề PR

Sử dụng tiêu đề rõ ràng, mô tả theo định dạng sau:

```
[Component] Brief description
```

Ví dụ:
- `[Lesson 7] Sửa lỗi import notebook Python`
- `[Quiz App] Thêm bản dịch tiếng Đức`
- `[Docs] Cập nhật README với yêu cầu mới`
- `[Fix] Sửa đường dẫn dữ liệu trong bài học trực quan hóa`

### Mô tả PR

Bao gồm trong mô tả PR của bạn:

- **Cái gì**: Bạn đã thực hiện những thay đổi gì?
- **Tại sao**: Tại sao những thay đổi này cần thiết?
- **Cách thực hiện**: Bạn đã thực hiện thay đổi như thế nào?
- **Kiểm tra**: Bạn đã kiểm tra thay đổi như thế nào?
- **Ảnh chụp màn hình**: Bao gồm ảnh chụp màn hình cho các thay đổi trực quan
- **Vấn đề liên quan**: Liên kết đến các vấn đề liên quan (ví dụ: "Fixes #123")

### Quy trình xem xét

1. **Kiểm tra tự động** sẽ chạy trên PR của bạn  
2. **Người duy trì sẽ xem xét** đóng góp của bạn  
3. **Giải quyết phản hồi** bằng cách thực hiện các commit bổ sung  
4. Khi được chấp thuận, **người duy trì sẽ merge** PR của bạn

### Sau khi PR của bạn được merge

1. Xóa nhánh của bạn:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Cập nhật fork của bạn:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Hướng dẫn về phong cách

### Markdown

- Sử dụng cấp độ tiêu đề nhất quán
- Bao gồm các dòng trống giữa các phần
- Sử dụng khối mã với chỉ định ngôn ngữ:
  ````markdown
  ```python
  import pandas as pd
  ```
  ````
- Thêm văn bản thay thế cho hình ảnh: `![Alt text](../../translated_images/image.4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a.vi.png)`
- Giữ độ dài dòng hợp lý (khoảng 80-100 ký tự)

### Python

- Tuân theo hướng dẫn phong cách PEP 8
- Sử dụng tên biến có ý nghĩa
- Thêm docstring cho các hàm
- Bao gồm gợi ý kiểu khi thích hợp:
  ```python
  def process_data(df: pd.DataFrame) -> pd.DataFrame:
      """Process the input dataframe."""
      return df
  ```

### JavaScript/Vue.js

- Tuân theo hướng dẫn phong cách Vue.js 2
- Sử dụng cấu hình ESLint được cung cấp
- Viết các thành phần mô-đun, có thể tái sử dụng
- Thêm chú thích cho logic phức tạp

### Tổ chức tệp

- Giữ các tệp liên quan cùng nhau
- Sử dụng tên tệp mô tả
- Tuân theo cấu trúc thư mục hiện có
- Không commit các tệp không cần thiết (.DS_Store, .pyc, node_modules, v.v.)

## Thỏa thuận cấp phép cho người đóng góp

Dự án này hoan nghênh các đóng góp và đề xuất. Hầu hết các đóng góp yêu cầu bạn  
đồng ý với Thỏa thuận cấp phép cho người đóng góp (CLA) tuyên bố rằng bạn có quyền,  
và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Để biết chi tiết, hãy truy cập  
https://cla.microsoft.com.

Khi bạn gửi một pull request, CLA-bot sẽ tự động xác định liệu bạn có cần  
cung cấp CLA hay không và trang trí PR một cách thích hợp (ví dụ: nhãn, bình luận). Chỉ cần làm theo  
hướng dẫn được cung cấp bởi bot. Bạn chỉ cần làm điều này một lần trên tất cả các repository sử dụng CLA của chúng tôi.

## Câu hỏi?

- Kiểm tra [Kênh Discord #data-science-for-beginners](https://aka.ms/ds4beginners/discord)  
- Tham gia cộng đồng [Discord của chúng tôi](https://aka.ms/ds4beginners/discord)  
- Xem các [vấn đề hiện có](https://github.com/microsoft/Data-Science-For-Beginners/issues) và [pull request](https://github.com/microsoft/Data-Science-For-Beginners/pulls)

## Cảm ơn!

Sự đóng góp của bạn làm cho chương trình học này tốt hơn cho tất cả mọi người. Cảm ơn bạn đã dành thời gian để đóng góp!

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.