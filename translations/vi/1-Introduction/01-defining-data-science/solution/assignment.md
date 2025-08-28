<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8f79b9c0484c35b4f26e8aec7fc4d56",
  "translation_date": "2025-08-28T18:58:00+00:00",
  "source_file": "1-Introduction/01-defining-data-science/solution/assignment.md",
  "language_code": "vi"
}
-->
# Bài tập: Các tình huống Khoa học Dữ liệu

Trong bài tập đầu tiên này, chúng tôi yêu cầu bạn suy nghĩ về một quy trình hoặc vấn đề thực tế trong các lĩnh vực khác nhau, và cách bạn có thể cải thiện nó bằng quy trình Khoa học Dữ liệu. Hãy cân nhắc các câu hỏi sau:

1. Bạn có thể thu thập dữ liệu nào?
1. Bạn sẽ thu thập dữ liệu như thế nào?
1. Bạn sẽ lưu trữ dữ liệu ở đâu? Dữ liệu có khả năng lớn đến mức nào?
1. Những thông tin nào bạn có thể rút ra từ dữ liệu này? Những quyết định nào chúng ta có thể đưa ra dựa trên dữ liệu?

Hãy cố gắng suy nghĩ về 3 vấn đề/quy trình khác nhau và mô tả từng điểm trên cho mỗi lĩnh vực.

Dưới đây là một số lĩnh vực và vấn đề để bạn bắt đầu suy nghĩ:

1. Làm thế nào bạn có thể sử dụng dữ liệu để cải thiện quá trình giáo dục cho trẻ em trong trường học?
1. Làm thế nào bạn có thể sử dụng dữ liệu để kiểm soát việc tiêm chủng trong đại dịch?
1. Làm thế nào bạn có thể sử dụng dữ liệu để đảm bảo rằng bạn đang làm việc hiệu quả?

## Hướng dẫn

Điền vào bảng sau (thay thế các lĩnh vực gợi ý bằng các lĩnh vực của riêng bạn nếu cần):

| Lĩnh vực | Vấn đề | Dữ liệu cần thu thập | Cách lưu trữ dữ liệu | Những thông tin/quyết định có thể đưa ra | 
|----------|--------|----------------------|----------------------|------------------------------------------|
| Giáo dục | Trong trường đại học, chúng tôi thường có tỷ lệ tham dự thấp trong các buổi giảng, và chúng tôi có giả thuyết rằng sinh viên tham dự lớp học thường xuyên hơn sẽ làm bài thi tốt hơn. Chúng tôi muốn khuyến khích tham dự và kiểm tra giả thuyết này. | Chúng tôi có thể theo dõi sự tham dự thông qua hình ảnh chụp bởi camera an ninh trong lớp, hoặc bằng cách theo dõi địa chỉ bluetooth/wifi của điện thoại di động của sinh viên trong lớp. Dữ liệu bài thi đã có sẵn trong cơ sở dữ liệu của trường. | Trong trường hợp chúng tôi theo dõi hình ảnh từ camera an ninh - chúng tôi cần lưu trữ một vài (5-10) bức ảnh trong lớp (dữ liệu không có cấu trúc), sau đó sử dụng AI để nhận diện khuôn mặt sinh viên (chuyển dữ liệu sang dạng có cấu trúc). | Chúng tôi có thể tính toán dữ liệu tham dự trung bình cho mỗi sinh viên, và xem liệu có bất kỳ mối tương quan nào với điểm thi hay không. Chúng tôi sẽ nói thêm về tương quan trong phần [xác suất và thống kê](../../04-stats-and-probability/README.md). Để khuyến khích sinh viên tham dự, chúng tôi có thể công bố xếp hạng tham dự hàng tuần trên cổng thông tin của trường, và trao giải thưởng cho những người có tỷ lệ tham dự cao nhất. |
| Tiêm chủng | | | | |
| Hiệu suất làm việc | | | | |

> *Chúng tôi chỉ cung cấp một câu trả lời làm ví dụ, để bạn có thể hình dung những gì được mong đợi trong bài tập này.*

## Tiêu chí đánh giá

Xuất sắc | Đạt yêu cầu | Cần cải thiện
--- | --- | -- |
Có thể xác định các nguồn dữ liệu hợp lý, cách lưu trữ dữ liệu và các quyết định/thông tin có thể rút ra cho tất cả các lĩnh vực | Một số khía cạnh của giải pháp không được chi tiết, cách lưu trữ dữ liệu không được thảo luận, ít nhất 2 lĩnh vực được mô tả | Chỉ mô tả một phần của giải pháp dữ liệu, chỉ xem xét một lĩnh vực.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.