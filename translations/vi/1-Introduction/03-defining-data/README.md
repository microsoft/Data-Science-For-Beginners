<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1228edf3572afca7d7cdcd938b6b4984",
  "translation_date": "2025-09-04T20:28:52+00:00",
  "source_file": "1-Introduction/03-defining-data/README.md",
  "language_code": "vi"
}
-->
# Định nghĩa Dữ liệu

|![ Sketchnote bởi [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Định nghĩa Dữ liệu - _Sketchnote bởi [@nitya](https://twitter.com/nitya)_ |

Dữ liệu là các sự kiện, thông tin, quan sát và đo lường được sử dụng để khám phá và hỗ trợ các quyết định có cơ sở. Một điểm dữ liệu là một đơn vị dữ liệu duy nhất trong một tập dữ liệu, là tập hợp các điểm dữ liệu. Các tập dữ liệu có thể có nhiều định dạng và cấu trúc khác nhau, thường dựa trên nguồn gốc của nó hoặc nơi dữ liệu được thu thập. Ví dụ, thu nhập hàng tháng của một công ty có thể được lưu trong bảng tính, nhưng dữ liệu nhịp tim theo giờ từ một đồng hồ thông minh có thể ở định dạng [JSON](https://stackoverflow.com/a/383699). Các nhà khoa học dữ liệu thường làm việc với nhiều loại dữ liệu khác nhau trong một tập dữ liệu.

Bài học này tập trung vào việc xác định và phân loại dữ liệu dựa trên đặc điểm và nguồn gốc của nó.

## [Câu hỏi trước bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)
## Cách mô tả dữ liệu

### Dữ liệu thô
Dữ liệu thô là dữ liệu đến từ nguồn của nó ở trạng thái ban đầu và chưa được phân tích hay tổ chức. Để hiểu được điều gì đang xảy ra với một tập dữ liệu, nó cần được tổ chức thành một định dạng mà con người cũng như công nghệ họ sử dụng có thể hiểu và phân tích thêm. Cấu trúc của một tập dữ liệu mô tả cách nó được tổ chức và có thể được phân loại thành có cấu trúc, không có cấu trúc và bán cấu trúc. Các loại cấu trúc này sẽ khác nhau tùy thuộc vào nguồn gốc nhưng cuối cùng sẽ thuộc một trong ba loại này.

### Dữ liệu định lượng
Dữ liệu định lượng là các quan sát số trong một tập dữ liệu và thường có thể được phân tích, đo lường và sử dụng trong toán học. Một số ví dụ về dữ liệu định lượng là: dân số của một quốc gia, chiều cao của một người hoặc thu nhập hàng quý của một công ty. Với một số phân tích bổ sung, dữ liệu định lượng có thể được sử dụng để khám phá xu hướng theo mùa của Chỉ số Chất lượng Không khí (AQI) hoặc ước tính xác suất tắc đường vào giờ cao điểm trong một ngày làm việc điển hình.

### Dữ liệu định tính
Dữ liệu định tính, còn được gọi là dữ liệu phân loại, là dữ liệu không thể đo lường một cách khách quan như các quan sát của dữ liệu định lượng. Nó thường là các định dạng dữ liệu chủ quan khác nhau, ghi lại chất lượng của một sản phẩm hoặc quy trình. Đôi khi, dữ liệu định tính là số nhưng không được sử dụng trong toán học, như số điện thoại hoặc dấu thời gian. Một số ví dụ về dữ liệu định tính là: bình luận video, nhãn hiệu và mẫu mã của một chiếc xe hoặc màu sắc yêu thích của những người bạn thân nhất của bạn. Dữ liệu định tính có thể được sử dụng để hiểu sản phẩm nào được người tiêu dùng yêu thích nhất hoặc xác định các từ khóa phổ biến trong hồ sơ xin việc.

### Dữ liệu có cấu trúc
Dữ liệu có cấu trúc là dữ liệu được tổ chức thành các hàng và cột, trong đó mỗi hàng sẽ có cùng một tập hợp các cột. Các cột đại diện cho một giá trị của một loại cụ thể và sẽ được xác định bằng một tên mô tả giá trị đó đại diện cho điều gì, trong khi các hàng chứa các giá trị thực tế. Các cột thường có một tập hợp các quy tắc hoặc hạn chế cụ thể về giá trị, để đảm bảo rằng các giá trị chính xác đại diện cho cột. Ví dụ, hãy tưởng tượng một bảng tính khách hàng, trong đó mỗi hàng phải có một số điện thoại và các số điện thoại không bao giờ chứa ký tự chữ cái. Có thể có các quy tắc áp dụng cho cột số điện thoại để đảm bảo nó không bao giờ trống và chỉ chứa số.

Một lợi ích của dữ liệu có cấu trúc là nó có thể được tổ chức theo cách mà nó có thể liên kết với dữ liệu có cấu trúc khác. Tuy nhiên, vì dữ liệu được thiết kế để được tổ chức theo một cách cụ thể, việc thay đổi cấu trúc tổng thể của nó có thể tốn nhiều công sức. Ví dụ, thêm một cột email vào bảng tính khách hàng mà không thể để trống có nghĩa là bạn sẽ cần tìm cách thêm các giá trị này vào các hàng khách hàng hiện có trong tập dữ liệu.

Ví dụ về dữ liệu có cấu trúc: bảng tính, cơ sở dữ liệu quan hệ, số điện thoại, bảng sao kê ngân hàng.

### Dữ liệu không có cấu trúc
Dữ liệu không có cấu trúc thường không thể được phân loại thành các hàng hoặc cột và không chứa một định dạng hoặc tập hợp các quy tắc để tuân theo. Vì dữ liệu không có cấu trúc có ít hạn chế hơn về cấu trúc của nó, nên việc thêm thông tin mới dễ dàng hơn so với một tập dữ liệu có cấu trúc. Nếu một cảm biến ghi lại dữ liệu áp suất khí quyển mỗi 2 phút nhận được một bản cập nhật cho phép nó đo và ghi lại nhiệt độ, thì không cần phải thay đổi dữ liệu hiện có nếu nó không có cấu trúc. Tuy nhiên, điều này có thể khiến việc phân tích hoặc điều tra loại dữ liệu này mất nhiều thời gian hơn. Ví dụ, một nhà khoa học muốn tìm nhiệt độ trung bình của tháng trước từ dữ liệu của cảm biến, nhưng phát hiện ra rằng cảm biến đã ghi lại một "e" trong một số dữ liệu của nó để ghi chú rằng nó bị hỏng thay vì một số thông thường, điều này có nghĩa là dữ liệu không đầy đủ.

Ví dụ về dữ liệu không có cấu trúc: tệp văn bản, tin nhắn văn bản, tệp video.

### Dữ liệu bán cấu trúc
Dữ liệu bán cấu trúc có các đặc điểm khiến nó trở thành sự kết hợp giữa dữ liệu có cấu trúc và không có cấu trúc. Nó thường không tuân theo định dạng hàng và cột nhưng được tổ chức theo cách được coi là có cấu trúc và có thể tuân theo một định dạng cố định hoặc tập hợp các quy tắc. Cấu trúc sẽ khác nhau giữa các nguồn, chẳng hạn như một hệ thống phân cấp được xác định rõ ràng đến một thứ gì đó linh hoạt hơn cho phép tích hợp thông tin mới dễ dàng. Metadata là các chỉ số giúp quyết định cách dữ liệu được tổ chức và lưu trữ và sẽ có các tên khác nhau, dựa trên loại dữ liệu. Một số tên phổ biến cho metadata là thẻ, phần tử, thực thể và thuộc tính. Ví dụ, một tin nhắn email điển hình sẽ có tiêu đề, nội dung và một tập hợp người nhận và có thể được tổ chức theo người gửi hoặc thời gian gửi.

Ví dụ về dữ liệu bán cấu trúc: HTML, tệp CSV, JavaScript Object Notation (JSON).

## Nguồn dữ liệu 

Nguồn dữ liệu là vị trí ban đầu nơi dữ liệu được tạo ra hoặc nơi nó "tồn tại" và sẽ khác nhau tùy thuộc vào cách và thời điểm nó được thu thập. Dữ liệu được tạo ra bởi người dùng của nó được gọi là dữ liệu sơ cấp, trong khi dữ liệu thứ cấp đến từ một nguồn đã thu thập dữ liệu để sử dụng chung. Ví dụ, một nhóm các nhà khoa học thu thập các quan sát trong một khu rừng nhiệt đới sẽ được coi là dữ liệu sơ cấp và nếu họ quyết định chia sẻ nó với các nhà khoa học khác, nó sẽ được coi là dữ liệu thứ cấp đối với những người sử dụng nó.

Cơ sở dữ liệu là một nguồn phổ biến và dựa vào hệ thống quản lý cơ sở dữ liệu để lưu trữ và duy trì dữ liệu, nơi người dùng sử dụng các lệnh gọi là truy vấn để khám phá dữ liệu. Các tệp như nguồn dữ liệu có thể là tệp âm thanh, hình ảnh và video cũng như bảng tính như Excel. Các nguồn internet là một vị trí phổ biến để lưu trữ dữ liệu, nơi cơ sở dữ liệu cũng như các tệp có thể được tìm thấy. Giao diện lập trình ứng dụng, còn được gọi là API, cho phép các lập trình viên tạo cách chia sẻ dữ liệu với người dùng bên ngoài thông qua internet, trong khi quá trình web scraping trích xuất dữ liệu từ một trang web. [Các bài học trong Làm việc với Dữ liệu](../../../../../../../../../2-Working-With-Data) tập trung vào cách sử dụng các nguồn dữ liệu khác nhau.

## Kết luận

Trong bài học này, chúng ta đã học:

- Dữ liệu là gì
- Cách mô tả dữ liệu
- Cách phân loại và phân nhóm dữ liệu
- Nơi có thể tìm thấy dữ liệu

## 🚀 Thử thách

Kaggle là một nguồn tuyệt vời cho các tập dữ liệu mở. Sử dụng [công cụ tìm kiếm tập dữ liệu](https://www.kaggle.com/datasets) để tìm một số tập dữ liệu thú vị và phân loại 3-5 tập dữ liệu theo tiêu chí sau:

- Dữ liệu là định lượng hay định tính?
- Dữ liệu có cấu trúc, không có cấu trúc hay bán cấu trúc?

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ds/)

## Ôn tập & Tự học

- Đơn vị Microsoft Learn này, có tiêu đề [Phân loại dữ liệu của bạn](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/2-classify-data) có một phân tích chi tiết về dữ liệu có cấu trúc, bán cấu trúc và không có cấu trúc.

## Bài tập

[Phân loại Tập dữ liệu](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.