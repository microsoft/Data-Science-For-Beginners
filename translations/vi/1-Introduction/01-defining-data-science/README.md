<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8141e7195841682914be03ef930fe43d",
  "translation_date": "2025-09-03T20:22:50+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "vi"
}
-->
# Định nghĩa Khoa học Dữ liệu

| ![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Định nghĩa Khoa học Dữ liệu - _Sketchnote của [@nitya](https://twitter.com/nitya)_         |

---

[![Video Định nghĩa Khoa học Dữ liệu](../../../../translated_images/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.vi.png)](https://youtu.be/beZ7Mb_oz9I)

## [Câu hỏi trước bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/0)

## Dữ liệu là gì?
Trong cuộc sống hàng ngày, chúng ta luôn được bao quanh bởi dữ liệu. Văn bản bạn đang đọc bây giờ là dữ liệu. Danh sách số điện thoại của bạn bè trong điện thoại thông minh của bạn là dữ liệu, cũng như thời gian hiện tại hiển thị trên đồng hồ của bạn. Là con người, chúng ta tự nhiên làm việc với dữ liệu bằng cách đếm tiền mình có hoặc viết thư cho bạn bè.

Tuy nhiên, dữ liệu trở nên quan trọng hơn nhiều với sự ra đời của máy tính. Vai trò chính của máy tính là thực hiện các phép tính, nhưng chúng cần dữ liệu để hoạt động. Do đó, chúng ta cần hiểu cách máy tính lưu trữ và xử lý dữ liệu.

Với sự xuất hiện của Internet, vai trò của máy tính như các thiết bị xử lý dữ liệu đã tăng lên. Nếu bạn nghĩ về điều đó, chúng ta ngày càng sử dụng máy tính nhiều hơn để xử lý và giao tiếp dữ liệu, thay vì chỉ thực hiện các phép tính. Khi chúng ta viết email cho bạn bè hoặc tìm kiếm thông tin trên Internet - chúng ta thực chất đang tạo, lưu trữ, truyền tải và thao tác dữ liệu.
> Bạn có nhớ lần cuối cùng bạn sử dụng máy tính để thực sự tính toán điều gì đó không?

## Khoa học Dữ liệu là gì?

Theo [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **Khoa học Dữ liệu** được định nghĩa là *một lĩnh vực khoa học sử dụng các phương pháp khoa học để trích xuất kiến thức và thông tin từ dữ liệu có cấu trúc và không có cấu trúc, và áp dụng kiến thức và thông tin có thể hành động từ dữ liệu vào nhiều lĩnh vực ứng dụng khác nhau*.

Định nghĩa này nhấn mạnh các khía cạnh quan trọng sau của khoa học dữ liệu:

* Mục tiêu chính của khoa học dữ liệu là **trích xuất kiến thức** từ dữ liệu, nói cách khác - **hiểu** dữ liệu, tìm ra các mối quan hệ ẩn và xây dựng một **mô hình**.
* Khoa học dữ liệu sử dụng các **phương pháp khoa học**, chẳng hạn như xác suất và thống kê. Thực tế, khi thuật ngữ *khoa học dữ liệu* lần đầu tiên được giới thiệu, một số người cho rằng khoa học dữ liệu chỉ là một cái tên mới mẻ cho thống kê. Ngày nay, rõ ràng rằng lĩnh vực này rộng lớn hơn nhiều.
* Kiến thức thu được nên được áp dụng để tạo ra các **thông tin có thể hành động**, tức là những thông tin thực tiễn mà bạn có thể áp dụng vào các tình huống kinh doanh thực tế.
* Chúng ta cần có khả năng làm việc với cả dữ liệu **có cấu trúc** và **không có cấu trúc**. Chúng ta sẽ quay lại thảo luận về các loại dữ liệu khác nhau sau trong khóa học.
* **Lĩnh vực ứng dụng** là một khái niệm quan trọng, và các nhà khoa học dữ liệu thường cần ít nhất một mức độ chuyên môn nhất định trong lĩnh vực vấn đề, ví dụ: tài chính, y học, tiếp thị, v.v.

> Một khía cạnh quan trọng khác của Khoa học Dữ liệu là nó nghiên cứu cách dữ liệu có thể được thu thập, lưu trữ và xử lý bằng máy tính. Trong khi thống kê cung cấp nền tảng toán học, khoa học dữ liệu áp dụng các khái niệm toán học để thực sự rút ra thông tin từ dữ liệu.

Một trong những cách (được gán cho [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) để nhìn nhận khoa học dữ liệu là coi nó như một mô hình khoa học riêng biệt:
* **Thực nghiệm**, trong đó chúng ta chủ yếu dựa vào quan sát và kết quả của các thí nghiệm
* **Lý thuyết**, nơi các khái niệm mới xuất hiện từ kiến thức khoa học hiện có
* **Tính toán**, nơi chúng ta khám phá các nguyên tắc mới dựa trên một số thí nghiệm tính toán
* **Dựa trên dữ liệu**, dựa trên việc khám phá các mối quan hệ và mẫu trong dữ liệu  

## Các lĩnh vực liên quan khác

Vì dữ liệu có mặt ở khắp mọi nơi, khoa học dữ liệu cũng là một lĩnh vực rộng lớn, liên quan đến nhiều ngành khác.
Bạn có thể tranh luận rằng cách tiếp cận này không lý tưởng, vì các mô-đun có thể có độ dài khác nhau. Có lẽ sẽ công bằng hơn nếu chia thời gian theo độ dài của mô-đun (tính bằng số ký tự) và so sánh các giá trị đó thay thế.
Khi chúng ta bắt đầu phân tích kết quả của các bài kiểm tra trắc nghiệm, chúng ta có thể cố gắng xác định những khái niệm mà học sinh gặp khó khăn trong việc hiểu, và sử dụng thông tin đó để cải thiện nội dung. Để làm được điều này, chúng ta cần thiết kế các bài kiểm tra sao cho mỗi câu hỏi liên kết với một khái niệm hoặc một phần kiến thức nhất định.

Nếu muốn phân tích phức tạp hơn, chúng ta có thể vẽ biểu đồ thời gian hoàn thành từng mô-đun so với nhóm tuổi của học sinh. Chúng ta có thể phát hiện rằng đối với một số nhóm tuổi, thời gian hoàn thành mô-đun quá dài hoặc học sinh bỏ dở trước khi hoàn thành. Điều này có thể giúp chúng ta đưa ra khuyến nghị về độ tuổi phù hợp cho mô-đun và giảm thiểu sự không hài lòng của mọi người do kỳ vọng sai lệch.

## 🚀 Thử thách

Trong thử thách này, chúng ta sẽ cố gắng tìm các khái niệm liên quan đến lĩnh vực Khoa học Dữ liệu bằng cách xem xét các văn bản. Chúng ta sẽ lấy một bài viết trên Wikipedia về Khoa học Dữ liệu, tải xuống và xử lý văn bản, sau đó tạo một đám mây từ như hình dưới đây:

![Đám mây từ cho Khoa học Dữ liệu](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.vi.png)

Truy cập [`notebook.ipynb`](../../../../../../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') để đọc qua mã. Bạn cũng có thể chạy mã và xem cách nó thực hiện tất cả các chuyển đổi dữ liệu trong thời gian thực.

> Nếu bạn không biết cách chạy mã trong Jupyter Notebook, hãy xem [bài viết này](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ds/)

## Bài tập

* **Nhiệm vụ 1**: Sửa đổi mã trên để tìm các khái niệm liên quan đến các lĩnh vực **Dữ liệu lớn** và **Học máy**
* **Nhiệm vụ 2**: [Suy nghĩ về các kịch bản Khoa học Dữ liệu](assignment.md)

## Tín dụng

Bài học này được viết với ♥️ bởi [Dmitry Soshnikov](http://soshnikov.com)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.