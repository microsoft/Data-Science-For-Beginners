<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f546349678757508d69ce9e1d2688446",
  "translation_date": "2025-10-03T15:06:19+00:00",
  "source_file": "USAGE.md",
  "language_code": "vi"
}
-->
# Hướng Dẫn Sử Dụng

Hướng dẫn này cung cấp các ví dụ và quy trình làm việc phổ biến để sử dụng chương trình học "Khoa học Dữ liệu cho Người Mới Bắt Đầu".

## Mục Lục

- [Cách Sử Dụng Chương Trình Học Này](../..)
- [Làm Việc Với Các Bài Học](../..)
- [Làm Việc Với Jupyter Notebooks](../..)
- [Sử Dụng Ứng Dụng Quiz](../..)
- [Quy Trình Làm Việc Phổ Biến](../..)
- [Mẹo Dành Cho Người Tự Học](../..)
- [Mẹo Dành Cho Giáo Viên](../..)

## Cách Sử Dụng Chương Trình Học Này

Chương trình học này được thiết kế linh hoạt và có thể sử dụng theo nhiều cách:

- **Học tự túc**: Tự học các bài học theo tốc độ của riêng bạn
- **Giảng dạy trong lớp học**: Sử dụng như một khóa học có hướng dẫn
- **Nhóm học tập**: Học tập cùng bạn bè
- **Hình thức workshop**: Các buổi học ngắn hạn chuyên sâu

## Làm Việc Với Các Bài Học

Mỗi bài học đều tuân theo một cấu trúc nhất quán để tối ưu hóa việc học:

### Cấu Trúc Bài Học

1. **Quiz trước bài học**: Kiểm tra kiến thức hiện tại của bạn
2. **Sketchnote** (Tùy chọn): Tóm tắt trực quan các khái niệm chính
3. **Video** (Tùy chọn): Nội dung video bổ sung
4. **Bài học viết**: Các khái niệm và giải thích cốt lõi
5. **Jupyter Notebook**: Bài tập thực hành mã hóa
6. **Bài tập**: Thực hành những gì bạn đã học
7. **Quiz sau bài học**: Củng cố sự hiểu biết của bạn

### Quy Trình Ví Dụ Cho Một Bài Học

```bash
# 1. Navigate to the lesson directory
cd 1-Introduction/01-defining-data-science

# 2. Read the README.md
# Open README.md in your browser or editor

# 3. Take the pre-lesson quiz
# Click the quiz link in the README

# 4. Open the Jupyter notebook (if available)
jupyter notebook

# 5. Complete the exercises in the notebook

# 6. Work on the assignment

# 7. Take the post-lesson quiz
```

## Làm Việc Với Jupyter Notebooks

### Khởi Động Jupyter

```bash
# Activate your virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Start Jupyter from the repository root
jupyter notebook
```

### Chạy Các Ô Notebook

1. **Chạy một ô**: Nhấn `Shift + Enter` hoặc nhấp vào nút "Run"
2. **Chạy tất cả các ô**: Chọn "Cell" → "Run All" từ menu
3. **Khởi động lại kernel**: Chọn "Kernel" → "Restart" nếu gặp vấn đề

### Ví Dụ: Làm Việc Với Dữ Liệu Trong Notebook

```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv('data/sample.csv')

# Explore the data
df.head()
df.info()
df.describe()

# Create a visualization
plt.figure(figsize=(10, 6))
plt.plot(df['column_name'])
plt.title('Sample Visualization')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()
```

### Lưu Công Việc Của Bạn

- Jupyter tự động lưu định kỳ
- Lưu thủ công: Nhấn `Ctrl + S` (hoặc `Cmd + S` trên macOS)
- Tiến trình của bạn được lưu trong tệp `.ipynb`

## Sử Dụng Ứng Dụng Quiz

### Chạy Ứng Dụng Quiz Cục Bộ

```bash
# Navigate to quiz app directory
cd quiz-app

# Start the development server
npm run serve

# Access at http://localhost:8080
```

### Làm Quiz

1. Quiz trước bài học được liên kết ở đầu mỗi bài học
2. Quiz sau bài học được liên kết ở cuối mỗi bài học
3. Mỗi quiz có 3 câu hỏi
4. Quiz được thiết kế để củng cố việc học, không phải để kiểm tra toàn diện

### Đánh Số Quiz

- Quiz được đánh số từ 0-39 (tổng cộng 40 quiz)
- Mỗi bài học thường có một quiz trước và sau
- URL của quiz bao gồm số quiz: `https://ff-quizzes.netlify.app/en/ds/quiz/0`

## Quy Trình Làm Việc Phổ Biến

### Quy Trình 1: Lộ Trình Cho Người Mới Bắt Đầu

```bash
# 1. Set up your environment (see INSTALLATION.md)

# 2. Start with Lesson 1
cd 1-Introduction/01-defining-data-science

# 3. For each lesson:
#    - Take pre-lesson quiz
#    - Read the lesson content
#    - Work through the notebook
#    - Complete the assignment
#    - Take post-lesson quiz

# 4. Progress through all 20 lessons sequentially
```

### Quy Trình 2: Học Theo Chủ Đề

Nếu bạn quan tâm đến một chủ đề cụ thể:

```bash
# Example: Focus on Data Visualization
cd 3-Data-Visualization

# Explore lessons 9-13:
# - Lesson 9: Visualizing Quantities
# - Lesson 10: Visualizing Distributions
# - Lesson 11: Visualizing Proportions
# - Lesson 12: Visualizing Relationships
# - Lesson 13: Meaningful Visualizations
```

### Quy Trình 3: Học Dựa Trên Dự Án

```bash
# 1. Review the Data Science Lifecycle lessons (14-16)
cd 4-Data-Science-Lifecycle

# 2. Work through a real-world example (Lesson 20)
cd ../6-Data-Science-In-Wild/20-Real-World-Examples

# 3. Apply concepts to your own project
```

### Quy Trình 4: Khoa Học Dữ Liệu Trên Đám Mây

```bash
# Learn about cloud data science (Lessons 17-19)
cd 5-Data-Science-In-Cloud

# 17: Introduction to Cloud Data Science
# 18: Low-Code ML Tools
# 19: Azure Machine Learning Studio
```

## Mẹo Dành Cho Người Tự Học

### Giữ Gìn Tổ Chức

```bash
# Create a learning journal
mkdir my-learning-journal

# For each lesson, create notes
echo "# Lesson 1 Notes" > my-learning-journal/lesson-01-notes.md
```

### Luyện Tập Thường Xuyên

- Dành thời gian cố định mỗi ngày hoặc mỗi tuần
- Hoàn thành ít nhất một bài học mỗi tuần
- Ôn lại các bài học trước định kỳ

### Tham Gia Cộng Đồng

- Tham gia [cộng đồng Discord](https://aka.ms/ds4beginners/discord)
- Tham gia kênh #Data-Science-for-Beginners trong Discord [Thảo luận trên Discord](https://aka.ms/ds4beginners/discord)
- Chia sẻ tiến trình của bạn và đặt câu hỏi

### Xây Dựng Dự Án Của Riêng Bạn

Sau khi hoàn thành các bài học, áp dụng các khái niệm vào dự án cá nhân:

```python
# Example: Analyze your own dataset
import pandas as pd

# Load your own data
my_data = pd.read_csv('my-project/data.csv')

# Apply techniques learned
# - Data cleaning (Lesson 8)
# - Exploratory data analysis (Lesson 7)
# - Visualization (Lessons 9-13)
# - Analysis (Lesson 15)
```

## Mẹo Dành Cho Giáo Viên

### Thiết Lập Lớp Học

1. Xem [for-teachers.md](for-teachers.md) để biết hướng dẫn chi tiết
2. Thiết lập môi trường chia sẻ (GitHub Classroom hoặc Codespaces)
3. Tạo kênh giao tiếp (Discord, Slack, hoặc Teams)

### Lập Kế Hoạch Bài Học

**Lịch Trình Gợi Ý 10 Tuần:**

- **Tuần 1-2**: Giới thiệu (Bài học 1-4)
- **Tuần 3-4**: Làm việc với dữ liệu (Bài học 5-8)
- **Tuần 5-6**: Trực quan hóa dữ liệu (Bài học 9-13)
- **Tuần 7-8**: Vòng đời khoa học dữ liệu (Bài học 14-16)
- **Tuần 9**: Khoa học dữ liệu trên đám mây (Bài học 17-19)
- **Tuần 10**: Ứng dụng thực tế & Dự án cuối khóa (Bài học 20)

### Chạy Docsify Để Truy Cập Ngoại Tuyến

```bash
# Serve documentation locally for classroom use
docsify serve

# Students can access at localhost:3000
# No internet required after initial setup
```

### Chấm Điểm Bài Tập

- Xem xét notebook của học sinh để kiểm tra bài tập đã hoàn thành
- Kiểm tra sự hiểu biết thông qua điểm quiz
- Đánh giá dự án cuối khóa dựa trên các nguyên tắc vòng đời khoa học dữ liệu

### Tạo Bài Tập

```python
# Example custom assignment template
"""
Assignment: [Topic]

Objective: [Learning goal]

Dataset: [Provide or have students find one]

Tasks:
1. Load and explore the dataset
2. Clean and prepare the data
3. Create at least 3 visualizations
4. Perform analysis
5. Communicate findings

Deliverables:
- Jupyter notebook with code and explanations
- Written summary of findings
"""
```

## Làm Việc Ngoại Tuyến

### Tải Xuống Tài Nguyên

```bash
# Clone the entire repository
git clone https://github.com/microsoft/Data-Science-For-Beginners.git

# Download datasets in advance
# Most datasets are included in the repository
```

### Chạy Tài Liệu Cục Bộ

```bash
# Serve with Docsify
docsify serve

# Access at localhost:3000
```

### Chạy Ứng Dụng Quiz Cục Bộ

```bash
cd quiz-app
npm run serve
```

## Truy Cập Nội Dung Đã Dịch

Các bản dịch có sẵn trên hơn 40 ngôn ngữ:

```bash
# Access translated lessons
cd translations/fr  # French
cd translations/es  # Spanish
cd translations/de  # German
# ... and many more
```

Mỗi bản dịch giữ nguyên cấu trúc như phiên bản tiếng Anh.

## Tài Nguyên Bổ Sung

### Tiếp Tục Học Tập

- [Microsoft Learn](https://docs.microsoft.com/learn/) - Các lộ trình học bổ sung
- [Student Hub](https://docs.microsoft.com/learn/student-hub) - Tài nguyên dành cho sinh viên
- [Azure AI Foundry](https://aka.ms/foundry/forum) - Diễn đàn cộng đồng

### Chương Trình Học Liên Quan

- [AI cho Người Mới Bắt Đầu](https://aka.ms/ai-beginners)
- [ML cho Người Mới Bắt Đầu](https://aka.ms/ml-beginners)
- [Web Dev cho Người Mới Bắt Đầu](https://aka.ms/webdev-beginners)
- [Generative AI cho Người Mới Bắt Đầu](https://aka.ms/genai-beginners)

## Nhận Trợ Giúp

- Xem [TROUBLESHOOTING.md](TROUBLESHOOTING.md) để biết các vấn đề thường gặp
- Tìm kiếm [GitHub Issues](https://github.com/microsoft/Data-Science-For-Beginners/issues)
- Tham gia [Discord](https://aka.ms/ds4beginners/discord)
- Xem [CONTRIBUTING.md](CONTRIBUTING.md) để báo cáo vấn đề hoặc đóng góp

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.