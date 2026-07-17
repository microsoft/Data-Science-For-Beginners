# Định nghĩa Dữ liệu

|![ Sketchnote bởi [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/03-DefiningData.png)|
|:---:|
|Định nghĩa Dữ liệu - _Sketchnote bởi [@nitya](https://twitter.com/nitya)_ |

Dữ liệu là các sự kiện, thông tin, quan sát và đo lường được sử dụng để khám phá và hỗ trợ các quyết định có cơ sở. Một điểm dữ liệu là một đơn vị dữ liệu duy nhất trong một bộ dữ liệu, mà là tập hợp của các điểm dữ liệu. Bộ dữ liệu có thể có các định dạng và cấu trúc khác nhau, và thường dựa trên nguồn gốc hoặc nơi dữ liệu đến. Ví dụ, thu nhập hàng tháng của một công ty có thể ở dạng bảng tính nhưng dữ liệu nhịp tim mỗi giờ từ đồng hồ thông minh có thể ở định dạng [JSON](https://stackoverflow.com/a/383699). Các nhà khoa học dữ liệu thường làm việc với nhiều loại dữ liệu khác nhau trong cùng một bộ dữ liệu.

Bài học này tập trung vào việc nhận diện và phân loại dữ liệu dựa trên đặc điểm và nguồn gốc của nó.

## [Bài kiểm tra trước bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/4)
## Cách Mô tả Dữ liệu

### Dữ liệu thô
Dữ liệu thô là dữ liệu vừa lấy từ nguồn của nó ở trạng thái ban đầu và chưa được phân tích hay tổ chức. Để hiểu được những gì đang xảy ra với một bộ dữ liệu, nó cần được tổ chức theo một định dạng có thể được con người và công nghệ phân tích tiếp. Cấu trúc của một bộ dữ liệu mô tả cách nó được tổ chức và có thể được phân loại thành có cấu trúc, không cấu trúc và bán cấu trúc. Các loại cấu trúc này sẽ khác nhau tùy theo nguồn nhưng cuối cùng sẽ thuộc ba loại này.

### Dữ liệu định lượng
Dữ liệu định lượng là những quan sát dạng số trong một bộ dữ liệu và thường có thể được phân tích, đo lường và sử dụng về mặt toán học. Một số ví dụ về dữ liệu định lượng là: dân số của một quốc gia, chiều cao của một người hoặc thu nhập hàng quý của một công ty. Với một số phân tích thêm, dữ liệu định lượng có thể được dùng để phát hiện các xu hướng theo mùa của Chỉ số Chất lượng Không khí (AQI) hoặc ước tính xác suất tắc đường giờ cao điểm trong một ngày làm việc bình thường.

### Dữ liệu định tính
Dữ liệu định tính, còn gọi là dữ liệu phân loại, là dữ liệu không thể đo lường chính xác như dữ liệu định lượng. Thường là các định dạng khác nhau của dữ liệu chủ quan, thể hiện chất lượng của một thứ gì đó, như sản phẩm hoặc quy trình. Đôi khi, dữ liệu định tính có thể là dạng số nhưng không được dùng cho các phép toán, ví dụ như số điện thoại hoặc dấu thời gian. Một số ví dụ về dữ liệu định tính là: bình luận video, hãng và mẫu xe ô tô hoặc màu sắc yêu thích của những người bạn thân của bạn. Dữ liệu định tính có thể được dùng để hiểu sản phẩm nào người tiêu dùng thích nhất hoặc xác định các từ khóa phổ biến trong hồ sơ xin việc.

### Dữ liệu có cấu trúc
Dữ liệu có cấu trúc là dữ liệu được tổ chức theo hàng và cột, trong đó mỗi hàng sẽ có cùng bộ cột. Các cột đại diện cho giá trị của một loại dữ liệu cụ thể và sẽ được đặt tên mô tả giá trị đó, trong khi các hàng chứa các giá trị thực tế. Các cột thường có bộ quy tắc hoặc hạn chế cụ thể về giá trị để đảm bảo giá trị chính xác mô tả cột đó. Ví dụ, hãy tưởng tượng một bảng tính khách hàng mà mỗi hàng phải có số điện thoại và các số điện thoại không bao giờ chứa ký tự chữ cái. Có thể có các quy tắc áp dụng cho cột số điện thoại để đảm bảo nó không bao giờ trống và chỉ chứa số.

Một lợi ích của dữ liệu có cấu trúc là có thể được tổ chức sao cho liên quan đến các dữ liệu có cấu trúc khác. Tuy nhiên, vì dữ liệu được thiết kế để tổ chức theo một cách cụ thể, việc thay đổi cấu trúc tổng thể có thể tốn nhiều công sức. Ví dụ, thêm một cột email vào bảng khách hàng mà không được để trống thì bạn sẽ phải tìm cách thêm giá trị đó cho các hàng khách hàng hiện có trong bộ dữ liệu.

Ví dụ về dữ liệu có cấu trúc: bảng tính, cơ sở dữ liệu quan hệ, số điện thoại, sao kê ngân hàng

### Dữ liệu không có cấu trúc
Dữ liệu không có cấu trúc thường không thể phân loại thành hàng hoặc cột và không có định dạng hoặc bộ quy tắc nào để theo. Vì dữ liệu không có cấu trúc bị ít hạn chế hơn về cấu trúc nên dễ dàng bổ sung thông tin mới hơn so với bộ dữ liệu có cấu trúc. Nếu một cảm biến đo áp suất khí quyển mỗi 2 phút được cập nhật để đo và ghi lại nhiệt độ, nó không cần thay đổi dữ liệu hiện có nếu dữ liệu là không có cấu trúc. Tuy nhiên, điều này có thể làm cho việc phân tích hoặc kiểm tra loại dữ liệu này mất nhiều thời gian hơn. Ví dụ, một nhà khoa học muốn tìm nhiệt độ trung bình của tháng trước từ dữ liệu cảm biến, nhưng phát hiện cảm biến ghi lại một "e" trong một số dữ liệu để ghi chú rằng thiết bị bị hỏng thay vì số điển hình, điều này nghĩa là dữ liệu không đầy đủ.

Ví dụ về dữ liệu không có cấu trúc: tập tin văn bản, tin nhắn văn bản, tập tin video

### Dữ liệu bán cấu trúc
Dữ liệu bán cấu trúc có các đặc điểm làm cho nó là sự kết hợp giữa dữ liệu có cấu trúc và không có cấu trúc. Nó thường không tuân theo định dạng hàng và cột nhưng được tổ chức theo cách được coi là có cấu trúc và có thể theo một định dạng cố định hoặc bộ quy tắc. Cấu trúc sẽ khác nhau giữa các nguồn, như một hệ thống phân cấp rõ ràng đến một thứ linh hoạt hơn cho phép tích hợp thông tin mới dễ dàng. Metadata là các chỉ báo giúp xác định cách dữ liệu được tổ chức và lưu trữ và sẽ có nhiều tên gọi khác nhau dựa trên loại dữ liệu. Một số tên phổ biến cho metadata là thẻ (tags), phần tử (elements), thực thể (entities) và thuộc tính (attributes). Ví dụ, một email điển hình sẽ có chủ đề, nội dung và danh sách người nhận, và có thể được tổ chức theo người gửi hoặc thời điểm gửi.

Ví dụ về dữ liệu bán cấu trúc: HTML, tập tin CSV, JavaScript Object Notation (JSON)

## Nguồn Dữ liệu

Nguồn dữ liệu là vị trí ban đầu nơi dữ liệu được tạo ra, hoặc nơi dữ liệu "sinh sống", và sẽ khác nhau tùy theo cách và thời điểm thu thập. Dữ liệu do người dùng tạo ra được gọi là dữ liệu sơ cấp trong khi dữ liệu thứ cấp đến từ nguồn đã thu thập dữ liệu để sử dụng chung. Ví dụ, một nhóm nhà khoa học thu thập quan sát trong rừng nhiệt đới được xem là sơ cấp, và nếu họ quyết định chia sẻ với các nhà khoa học khác thì nó sẽ là thứ cấp đối với những người sử dụng dữ liệu đó.

Cơ sở dữ liệu là nguồn phổ biến và dựa trên hệ thống quản lý cơ sở dữ liệu để lưu trữ và duy trì dữ liệu, người dùng sử dụng các lệnh gọi là truy vấn để khám phá dữ liệu. Tập tin là nguồn dữ liệu có thể là tập tin âm thanh, hình ảnh, video cũng như bảng tính như Excel. Nguồn Internet là nơi phổ biến để lưu trữ dữ liệu, nơi có thể tìm thấy cả cơ sở dữ liệu và tập tin. Giao diện lập trình ứng dụng, còn được gọi là API, cho phép lập trình viên tạo cách chia sẻ dữ liệu với người dùng bên ngoài qua Internet, trong khi quy trình lấy dữ liệu từ trang web (web scraping) trích xuất dữ liệu từ một trang web. Các [bài học trong phần Làm việc với Dữ liệu](../../../../../../../../../2-Working-With-Data) tập trung vào cách sử dụng các nguồn dữ liệu khác nhau.

## Kết luận

Trong bài học này chúng ta đã học:

- Dữ liệu là gì
- Cách mô tả dữ liệu
- Cách phân loại và nhóm dữ liệu
- Nơi có thể tìm thấy dữ liệu

## 🚀 Thử thách

Kaggle là nguồn dữ liệu mở tuyệt vời. Sử dụng [công cụ tìm kiếm bộ dữ liệu](https://www.kaggle.com/datasets) để tìm các bộ dữ liệu thú vị và phân loại 3-5 bộ dữ liệu với các tiêu chí sau:

- Dữ liệu là định lượng hay định tính?
- Dữ liệu là có cấu trúc, không có cấu trúc hay bán cấu trúc?

## [Bài kiểm tra sau bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/5)



## Ôn tập & Tự học

- Đơn vị Microsoft Learn này, có tiêu đề [Xác định định dạng dữ liệu](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats?pivots=text) có phần phân tích chi tiết về dữ liệu có cấu trúc, bán cấu trúc và không có cấu trúc.

## Bài tập

[Phân loại Bộ dữ liệu](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->