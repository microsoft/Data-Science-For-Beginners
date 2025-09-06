<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2baeafe1db4d58ee5b8ec85db9de728a",
  "translation_date": "2025-09-05T23:36:15+00:00",
  "source_file": "4-Data-Science-Lifecycle/15-analyzing/README.md",
  "language_code": "vi"
}
-->
# Vòng đời Khoa học Dữ liệu: Phân tích

|![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/15-Analyzing.png)|
|:---:|
| Vòng đời Khoa học Dữ liệu: Phân tích - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

## Câu hỏi trước bài giảng

## [Câu hỏi trước bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/28)

Giai đoạn phân tích trong vòng đời dữ liệu xác nhận rằng dữ liệu có thể trả lời các câu hỏi được đề xuất hoặc giải quyết một vấn đề cụ thể. Bước này cũng tập trung vào việc xác nhận rằng một mô hình đang giải quyết đúng các câu hỏi và vấn đề đó. Bài học này tập trung vào Phân tích Dữ liệu Khám phá (Exploratory Data Analysis - EDA), bao gồm các kỹ thuật để xác định các đặc điểm và mối quan hệ trong dữ liệu, đồng thời chuẩn bị dữ liệu cho việc xây dựng mô hình.

Chúng ta sẽ sử dụng một tập dữ liệu ví dụ từ [Kaggle](https://www.kaggle.com/balaka18/email-spam-classification-dataset-csv/version/1) để minh họa cách áp dụng điều này với Python và thư viện Pandas. Tập dữ liệu này chứa số lượng một số từ phổ biến được tìm thấy trong email, nguồn gốc của các email này là ẩn danh. Hãy sử dụng [notebook](../../../../4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) trong thư mục này để thực hành theo.

## Phân tích Dữ liệu Khám phá

Giai đoạn thu thập trong vòng đời là nơi dữ liệu được thu thập cùng với các vấn đề và câu hỏi cần giải quyết, nhưng làm thế nào để chúng ta biết rằng dữ liệu có thể hỗ trợ kết quả cuối cùng? 
Hãy nhớ rằng một nhà khoa học dữ liệu có thể đặt ra các câu hỏi sau khi họ thu thập dữ liệu:
- Tôi có đủ dữ liệu để giải quyết vấn đề này không?
- Dữ liệu có chất lượng chấp nhận được cho vấn đề này không?
- Nếu tôi phát hiện thêm thông tin thông qua dữ liệu này, chúng ta có nên xem xét thay đổi hoặc xác định lại mục tiêu không?
Phân tích Dữ liệu Khám phá là quá trình làm quen với dữ liệu và có thể được sử dụng để trả lời các câu hỏi này, cũng như xác định các thách thức khi làm việc với tập dữ liệu. Hãy tập trung vào một số kỹ thuật được sử dụng để đạt được điều này.

## Lập hồ sơ dữ liệu, Thống kê mô tả và Pandas
Làm thế nào để chúng ta đánh giá liệu có đủ dữ liệu để giải quyết vấn đề này không? Lập hồ sơ dữ liệu có thể tóm tắt và thu thập một số thông tin tổng quan về tập dữ liệu của chúng ta thông qua các kỹ thuật thống kê mô tả. Lập hồ sơ dữ liệu giúp chúng ta hiểu những gì có sẵn, và thống kê mô tả giúp chúng ta hiểu có bao nhiêu thứ có sẵn.

Trong một vài bài học trước, chúng ta đã sử dụng Pandas để cung cấp một số thống kê mô tả với [`describe()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html). Hàm này cung cấp số lượng, giá trị lớn nhất và nhỏ nhất, giá trị trung bình, độ lệch chuẩn và các phân vị trên dữ liệu số. Sử dụng các thống kê mô tả như hàm `describe()` có thể giúp bạn đánh giá bạn có bao nhiêu dữ liệu và liệu bạn có cần thêm không.

## Lấy mẫu và Truy vấn
Khám phá toàn bộ một tập dữ liệu lớn có thể rất tốn thời gian và thường là nhiệm vụ dành cho máy tính. Tuy nhiên, lấy mẫu là một công cụ hữu ích để hiểu dữ liệu và cho phép chúng ta có cái nhìn tổng quan hơn về những gì có trong tập dữ liệu và ý nghĩa của nó. Với một mẫu, bạn có thể áp dụng xác suất và thống kê để đưa ra một số kết luận tổng quát về dữ liệu của mình. Mặc dù không có quy tắc cụ thể về lượng dữ liệu bạn nên lấy mẫu, điều quan trọng cần lưu ý là càng lấy mẫu nhiều, bạn càng có thể đưa ra các tổng quát chính xác hơn về dữ liệu. 
Pandas có [`sample()` function trong thư viện của nó](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html), nơi bạn có thể truyền một tham số về số lượng mẫu ngẫu nhiên bạn muốn nhận và sử dụng.

Truy vấn tổng quát dữ liệu có thể giúp bạn trả lời một số câu hỏi và giả thuyết chung mà bạn có thể có. Trái ngược với lấy mẫu, truy vấn cho phép bạn kiểm soát và tập trung vào các phần cụ thể của dữ liệu mà bạn có câu hỏi. 
Hàm [`query()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) trong thư viện Pandas cho phép bạn chọn các cột và nhận các câu trả lời đơn giản về dữ liệu thông qua các hàng được truy xuất.

## Khám phá với Hình ảnh hóa
Bạn không cần phải đợi đến khi dữ liệu được làm sạch và phân tích hoàn toàn để bắt đầu tạo hình ảnh hóa. Thực tế, việc có một biểu diễn trực quan trong khi khám phá có thể giúp xác định các mẫu, mối quan hệ và vấn đề trong dữ liệu. Hơn nữa, hình ảnh hóa cung cấp một phương tiện giao tiếp với những người không tham gia vào việc quản lý dữ liệu và có thể là cơ hội để chia sẻ và làm rõ các câu hỏi bổ sung chưa được giải quyết trong giai đoạn thu thập. Tham khảo [phần về Hình ảnh hóa](../../../../../../../../../3-Data-Visualization) để tìm hiểu thêm về một số cách phổ biến để khám phá trực quan.

## Khám phá để xác định sự không nhất quán
Tất cả các chủ đề trong bài học này có thể giúp xác định các giá trị bị thiếu hoặc không nhất quán, nhưng Pandas cung cấp các hàm để kiểm tra một số điều này. [isna() hoặc isnull()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html) có thể kiểm tra các giá trị bị thiếu. Một phần quan trọng của việc khám phá các giá trị này trong dữ liệu của bạn là tìm hiểu tại sao chúng lại xuất hiện như vậy ngay từ đầu. Điều này có thể giúp bạn quyết định [các hành động cần thực hiện để giải quyết chúng](../../../../../../../../../2-Working-With-Data/08-data-preparation/notebook.ipynb).

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/29)

## Bài tập

[Khám phá để tìm câu trả lời](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.