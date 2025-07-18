# Định nghĩa dữ liệu
Dữ liệu là các sự thật, thông tin, quan sát và phép đo được sử dụng để khám phá và hỗ trợ các quyết định có cơ sở. Một điểm dữ liệu là một đơn vị dữ liệu riêng lẻ nằm trong một tập dữ liệu — tức là tập hợp các điểm dữ liệu. Tập dữ liệu có thể có nhiều định dạng và cấu trúc khác nhau, thường phụ thuộc vào nguồn gốc của nó hoặc nơi dữ liệu được tạo ra. Ví dụ, thu nhập hàng tháng của một công ty có thể được lưu trong bảng tính, còn dữ liệu nhịp tim theo từng giờ từ một chiếc đồng hồ thông minh có thể có định dạng JSON. Các nhà khoa học dữ liệu thường làm việc với nhiều loại dữ liệu khác nhau trong cùng một tập dữ liệu.

Bài học này tập trung vào việc xác định và phân loại dữ liệu dựa trên đặc điểm và nguồn gốc của nó.

## [Câu hỏi trước buổi học](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/4)

## Dữ Liệu được mô tả như thế nào
### Dữ liệu thô
Dữ liệu thô là dữ liệu vừa được lấy từ nguồn gốc ban đầu của nó và chưa được phân tích hay sắp xếp. Để có thể hiểu rõ những gì đang diễn ra trong một tập dữ liệu, dữ liệu cần được tổ chức lại thành một định dạng có thể dễ dàng được con người tiếp thu cũng như được công nghệ sử dụng để phân tích thêm. Cấu trúc của một tập dữ liệu mô tả cách nó được sắp xếp và có thể được phân loại thành có cấu trúc, phi cấu trúc và bán cấu trúc. Các kiểu cấu trúc này sẽ khác nhau tùy theo nguồn dữ liệu, nhưng cuối cùng sẽ thuộc một trong ba loại kể trên.

### Dữ liệu định lượng

Dữ liệu định lượng là những quan sát có dạng số trong một tập dữ liệu và thường có thể được phân tích, đo lường và sử dụng theo cách toán học. Một vài ví dụ về dữ liệu định lượng là: dân số của một quốc gia, chiều cao của một người hoặc lợi nhuận hàng quý của một công ty. Với một số phân tích bổ sung, dữ liệu định lượng có thể được sử dụng để khám phá xu hướng theo mùa của Chỉ số Chất lượng Không khí (AQI) hoặc ước tính xác suất tắc nghẽn giao thông vào giờ cao điểm trong một ngày làm việc điển hình.

### Dữ liệu định tính

Dữ liệu định tính, còn được gọi là dữ liệu phân loại, là loại dữ liệu không thể đo lường một cách khách quan như các quan sát trong dữ liệu định lượng. Đây thường là những dạng dữ liệu mang tính chủ quan, dùng để phản ánh chất lượng của một sản phẩm hoặc quy trình nào đó. Đôi khi, dữ liệu định tính có thể là những con số, nhưng không được sử dụng theo cách toán học thông thường — ví dụ như số điện thoại hoặc dấu thời gian.

Một vài ví dụ về dữ liệu định tính bao gồm: bình luận dưới video, hãng và mẫu xe, hoặc màu yêu thích của những người bạn thân nhất của bạn. Dữ liệu định tính có thể được sử dụng để tìm hiểu sản phẩm nào được người tiêu dùng ưa chuộng nhất, hoặc để xác định các từ khóa phổ biến trong hồ sơ xin việc.

### Dữ liệu có cấu trúc

Dữ liệu có cấu trúc là dữ liệu được tổ chức dưới dạng hàng và cột, trong đó mỗi hàng sẽ có cùng một bộ cột. Các cột đại diện cho một loại giá trị cụ thể và thường được đặt tên để mô tả giá trị đó là gì, còn các hàng thì chứa các giá trị thực tế. Các cột thường có một tập hợp quy tắc hoặc giới hạn nhất định đối với giá trị, nhằm đảm bảo rằng giá trị phản ánh đúng bản chất của cột đó. Ví dụ, hãy tưởng tượng một bảng tính chứa thông tin khách hàng, trong đó mỗi hàng bắt buộc phải có số điện thoại và các số điện thoại này không bao giờ được chứa ký tự chữ cái. Có thể áp dụng quy tắc cho cột số điện thoại để đảm bảo rằng nó không bị bỏ trống và chỉ chứa số.

Một lợi ích của dữ liệu có cấu trúc là nó có thể được tổ chức để dễ dàng liên kết với các dữ liệu có cấu trúc khác. Tuy nhiên, vì dữ liệu được thiết kế theo một cách sắp xếp cụ thể, nên việc thay đổi cấu trúc tổng thể của nó có thể đòi hỏi nhiều công sức. Ví dụ, nếu bạn muốn thêm một cột địa chỉ email vào bảng khách hàng và cột này không được phép để trống, bạn sẽ phải nghĩ cách điền giá trị cho toàn bộ các hàng đã có sẵn trong tập dữ liệu.

Ví dụ về dữ liệu có cấu trúc: bảng tính, cơ sở dữ liệu quan hệ, số điện thoại, sao kê ngân hàng.

### Dữ liệu không có cấu trúc

Dữ liệu phi cấu trúc thường không thể được phân loại thành hàng và cột, và không tuân theo một định dạng hay bộ quy tắc cố định nào. Vì dữ liệu phi cấu trúc có ít giới hạn về mặt cấu trúc nên việc bổ sung thông tin mới sẽ dễ dàng hơn so với dữ liệu có cấu trúc. Ví dụ, nếu một cảm biến đang thu thập dữ liệu về áp suất khí quyển mỗi 2 phút nhận được bản cập nhật cho phép đo và ghi lại nhiệt độ, thì việc này không yêu cầu thay đổi dữ liệu hiện có nếu nó là dữ liệu phi cấu trúc.

Tuy nhiên, đặc điểm này cũng có thể khiến việc phân tích hoặc kiểm tra loại dữ liệu này mất nhiều thời gian hơn. Ví dụ, một nhà khoa học muốn tìm nhiệt độ trung bình của tháng trước từ dữ liệu cảm biến, nhưng phát hiện rằng cảm biến đã ghi lại ký tự “e” trong một số bản ghi để chỉ rằng nó bị hỏng, thay vì ghi lại một con số như thông thường — điều này khiến dữ liệu bị thiếu và không đầy đủ.

Ví dụ về dữ liệu phi cấu trúc: file ký tự, tin nhắn văn bản, file video

### Dữ liệu bán cấu trúc

Dữ liệu bán cấu trúc có các đặc điểm khiến nó trở thành sự kết hợp giữa dữ liệu có cấu trúc và phi cấu trúc. Loại dữ liệu này thường không tuân theo định dạng hàng và cột, nhưng vẫn được tổ chức theo cách có cấu trúc và có thể tuân thủ một định dạng cố định hoặc bộ quy tắc nhất định. Cấu trúc của dữ liệu bán cấu trúc sẽ thay đổi tùy theo nguồn gốc — có thể là một hệ thống phân cấp rõ ràng hoặc một dạng linh hoạt hơn cho phép dễ dàng tích hợp thông tin mới.

Metadata (siêu dữ liệu) là những chỉ báo giúp xác định cách dữ liệu được tổ chức và lưu trữ, và có nhiều tên gọi khác nhau tùy vào loại dữ liệu, chẳng hạn như: tag, element, entity, và attribute. Ví dụ, một email điển hình sẽ có phần tiêu đề, nội dung và danh sách người nhận, và có thể được phân loại theo người gửi hoặc thời điểm gửi.

Ví dụ về dữ liệu bán cấu trúc: HTML, file CSV, JavaScript Object Notation (JSON)

## Nguồn dữ liệu
Nguồn dữ liệu là vị trí ban đầu nơi dữ liệu được tạo ra, hoặc nơi dữ liệu “tồn tại”, và sẽ khác nhau tùy thuộc vào cách thức và thời điểm dữ liệu được thu thập. Dữ liệu được tạo bởi người dùng được gọi là dữ liệu sơ cấp, trong khi dữ liệu thứ cấp đến từ một nguồn đã thu thập dữ liệu để sử dụng chung. Ví dụ, một nhóm nhà khoa học thu thập các quan sát trong rừng nhiệt đới được xem là dữ liệu sơ cấp, còn nếu họ chia sẻ dữ liệu đó với những nhà khoa học khác thì nó sẽ trở thành dữ liệu thứ cấp đối với những người sử dụng nó.

Cơ sở dữ liệu là một nguồn phổ biến và dựa vào hệ quản trị cơ sở dữ liệu để lưu trữ và duy trì dữ liệu, nơi người dùng sử dụng các câu lệnh gọi là truy vấn để khám phá dữ liệu. Tệp tin cũng có thể là nguồn dữ liệu, ví dụ như tệp âm thanh, hình ảnh, video, hoặc bảng tính như Excel. Các nguồn trên Internet là vị trí phổ biến để lưu trữ dữ liệu, nơi có thể tìm thấy cả cơ sở dữ liệu lẫn tệp tin.

Giao diện lập trình ứng dụng (API) cho phép lập trình viên tạo ra các cách để chia sẻ dữ liệu với người dùng bên ngoài thông qua Internet, trong khi quá trình web scraping được sử dụng để trích xuất dữ liệu từ một trang web. 
[Bài học về Làm việc với Dữ liệu](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data) tập trung vào cách sử dụng nhiều loại nguồn dữ liệu khác nhau.

## Kết luận
Trong bài học này, chúng ta đã học về
<ul>
<li>Dữ liệu là gì</li>
<li>Dữ liệu được mô tả như thế nào</li>
<li>Cách dữ liệu được phân loại và tổ chức</li>
<li>Nơi có thể tìm thấy dữ liệu</li>
</ul>

## 🚀 Thử thách
Kaggle là một nguồn tuyệt vời cung cấp các tập dữ liệu mở. Hãy sử dụng [công cụ tìm kiếm tập dữ liệu](https://www.kaggle.com/datasets) để khám phá một vài tập dữ liệu thú vị và phân loại từ 3 đến 5 tập dữ liệu dựa trên các tiêu chí sau:
<ul>
<li>Dữ liệu là định lượng hay định tính?</li>
<li>Dữ liệu có cấu trúc, phi cấu trúc, hay bán cấu trúc</li>
</ul>

## [Câu hỏi sau buổi học](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/5)

## Ôn tập và tự học
<ul><li>Bài học trong Microsoft Learn có tiêu đề "Phân loại Dữ liệu của bạn" chứa phần phân tích chi tiết về dữ liệu có cấu trúc, dữ liệu bán cấu trúc, và dữ liệu phi cấu trúc.</ul>

##  Bài tập về nhà
[Phân loại dữ liệu](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/1-Introduction/03-defining-data/assignment.md)
