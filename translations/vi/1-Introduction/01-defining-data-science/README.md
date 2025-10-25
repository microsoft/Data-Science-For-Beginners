<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43212cc1ac137b7bb1dcfb37ca06b0f4",
  "translation_date": "2025-10-25T18:59:43+00:00",
  "source_file": "1-Introduction/01-defining-data-science/README.md",
  "language_code": "vi"
}
-->
# Định nghĩa Khoa học Dữ liệu

| ![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/01-Definitions.png) |
| :----------------------------------------------------------------------------------------------------: |
|              Định nghĩa Khoa học Dữ liệu - _Sketchnote của [@nitya](https://twitter.com/nitya)_               |

---

[![Video Định nghĩa Khoa học Dữ liệu](../../../../translated_images/video-def-ds.6623ee2392ef1abf6d7faf3fad10a4163642811749da75f44e35a5bb121de15c.vi.png)](https://youtu.be/beZ7Mb_oz9I)

## [Câu hỏi trước bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/0)

## Dữ liệu là gì?
Trong cuộc sống hàng ngày, chúng ta luôn được bao quanh bởi dữ liệu. Văn bản bạn đang đọc bây giờ là dữ liệu. Danh sách số điện thoại của bạn bè trong điện thoại thông minh của bạn là dữ liệu, cũng như thời gian hiện tại hiển thị trên đồng hồ của bạn. Là con người, chúng ta tự nhiên làm việc với dữ liệu bằng cách đếm tiền mình có hoặc viết thư cho bạn bè.

Tuy nhiên, dữ liệu trở nên quan trọng hơn nhiều với sự ra đời của máy tính. Vai trò chính của máy tính là thực hiện các phép tính, nhưng chúng cần dữ liệu để hoạt động. Do đó, chúng ta cần hiểu cách máy tính lưu trữ và xử lý dữ liệu.

Với sự xuất hiện của Internet, vai trò của máy tính như là thiết bị xử lý dữ liệu đã tăng lên. Nếu bạn nghĩ về điều này, chúng ta hiện nay sử dụng máy tính ngày càng nhiều để xử lý và giao tiếp dữ liệu, thay vì thực hiện các phép tính thực sự. Khi chúng ta viết email cho bạn bè hoặc tìm kiếm thông tin trên Internet - chúng ta thực chất đang tạo, lưu trữ, truyền tải và xử lý dữ liệu.
> Bạn có nhớ lần cuối cùng bạn sử dụng máy tính để thực sự tính toán điều gì đó không?

## Khoa học Dữ liệu là gì?

Theo [Wikipedia](https://en.wikipedia.org/wiki/Data_science), **Khoa học Dữ liệu** được định nghĩa là *một lĩnh vực khoa học sử dụng các phương pháp khoa học để trích xuất kiến thức và thông tin từ dữ liệu có cấu trúc và không có cấu trúc, và áp dụng kiến thức và thông tin có thể hành động từ dữ liệu trong nhiều lĩnh vực ứng dụng khác nhau*.

Định nghĩa này nhấn mạnh các khía cạnh quan trọng sau của khoa học dữ liệu:

* Mục tiêu chính của khoa học dữ liệu là **trích xuất kiến thức** từ dữ liệu, nói cách khác - **hiểu** dữ liệu, tìm ra các mối quan hệ ẩn và xây dựng một **mô hình**.
* Khoa học dữ liệu sử dụng các **phương pháp khoa học**, chẳng hạn như xác suất và thống kê. Thực tế, khi thuật ngữ *khoa học dữ liệu* lần đầu tiên được giới thiệu, một số người cho rằng khoa học dữ liệu chỉ là một tên gọi mới mẻ cho thống kê. Ngày nay, điều này đã trở nên rõ ràng rằng lĩnh vực này rộng lớn hơn nhiều.
* Kiến thức thu được cần được áp dụng để tạo ra **thông tin có thể hành động**, tức là những thông tin thực tiễn mà bạn có thể áp dụng vào các tình huống kinh doanh thực tế.
* Chúng ta cần có khả năng làm việc với cả dữ liệu **có cấu trúc** và **không có cấu trúc**. Chúng ta sẽ quay lại thảo luận về các loại dữ liệu khác nhau sau trong khóa học.
* **Lĩnh vực ứng dụng** là một khái niệm quan trọng, và các nhà khoa học dữ liệu thường cần ít nhất một mức độ chuyên môn nhất định trong lĩnh vực vấn đề, ví dụ: tài chính, y học, tiếp thị, v.v.

> Một khía cạnh quan trọng khác của Khoa học Dữ liệu là nghiên cứu cách dữ liệu có thể được thu thập, lưu trữ và xử lý bằng máy tính. Trong khi thống kê cung cấp nền tảng toán học, khoa học dữ liệu áp dụng các khái niệm toán học để thực sự rút ra thông tin từ dữ liệu.

Một trong những cách (được gán cho [Jim Gray](https://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist))) để nhìn nhận khoa học dữ liệu là coi nó như một mô hình khoa học riêng biệt:
* **Thực nghiệm**, trong đó chúng ta chủ yếu dựa vào quan sát và kết quả của các thí nghiệm
* **Lý thuyết**, nơi các khái niệm mới xuất hiện từ kiến thức khoa học hiện có
* **Tính toán**, nơi chúng ta khám phá các nguyên tắc mới dựa trên một số thí nghiệm tính toán
* **Dựa trên dữ liệu**, dựa vào việc khám phá các mối quan hệ và mẫu trong dữ liệu  

## Các lĩnh vực liên quan khác

Vì dữ liệu phổ biến, bản thân khoa học dữ liệu cũng là một lĩnh vực rộng lớn, liên quan đến nhiều ngành khác.

<dl>
<dt>Cơ sở dữ liệu</dt>
<dd>
Một yếu tố quan trọng là <b>cách lưu trữ</b> dữ liệu, tức là cách cấu trúc nó để cho phép xử lý nhanh hơn. Có nhiều loại cơ sở dữ liệu khác nhau lưu trữ dữ liệu có cấu trúc và không có cấu trúc, điều này <a href="../../2-Working-With-Data/README.md">chúng ta sẽ xem xét trong khóa học</a>.
</dd>
<dt>Dữ liệu lớn</dt>
<dd>
Thường chúng ta cần lưu trữ và xử lý một lượng lớn dữ liệu với cấu trúc tương đối đơn giản. Có những phương pháp và công cụ đặc biệt để lưu trữ dữ liệu đó một cách phân tán trên một cụm máy tính và xử lý nó một cách hiệu quả.
</dd>
<dt>Học máy</dt>
<dd>
Một cách để hiểu dữ liệu là <b>xây dựng một mô hình</b> có thể dự đoán kết quả mong muốn. Việc phát triển các mô hình từ dữ liệu được gọi là <b>học máy</b>. Bạn có thể muốn xem <a href="https://aka.ms/ml-beginners">Chương trình Học Máy cho Người Mới Bắt Đầu</a> của chúng tôi để tìm hiểu thêm về nó.
</dd>
<dt>Trí tuệ nhân tạo</dt>
<dd>
Một lĩnh vực của học máy được gọi là trí tuệ nhân tạo (AI) cũng dựa vào dữ liệu, và nó liên quan đến việc xây dựng các mô hình phức tạp cao mô phỏng quá trình tư duy của con người. Các phương pháp AI thường cho phép chúng ta chuyển đổi dữ liệu không có cấu trúc (ví dụ: ngôn ngữ tự nhiên) thành thông tin có cấu trúc.
</dd>
<dt>Trực quan hóa</dt>
<dd>
Lượng dữ liệu lớn thường khó hiểu đối với con người, nhưng một khi chúng ta tạo ra các hình ảnh trực quan hữu ích từ dữ liệu đó, chúng ta có thể hiểu rõ hơn về dữ liệu và rút ra một số kết luận. Do đó, việc biết nhiều cách để trực quan hóa thông tin là rất quan trọng - điều mà chúng ta sẽ đề cập trong <a href="../../3-Data-Visualization/README.md">Phần 3</a> của khóa học. Các lĩnh vực liên quan cũng bao gồm <b>Đồ họa thông tin</b> và <b>Tương tác Người-Máy tính</b> nói chung.
</dd>
</dl>

## Các loại dữ liệu

Như chúng ta đã đề cập, dữ liệu có mặt ở khắp mọi nơi. Chúng ta chỉ cần thu thập nó đúng cách! Việc phân biệt giữa dữ liệu **có cấu trúc** và **không có cấu trúc** là rất hữu ích. Dữ liệu có cấu trúc thường được biểu diễn dưới dạng có cấu trúc rõ ràng, thường là dưới dạng bảng hoặc nhiều bảng, trong khi dữ liệu không có cấu trúc chỉ là một tập hợp các tệp. Đôi khi chúng ta cũng có thể nói về dữ liệu **bán cấu trúc**, có một số dạng cấu trúc nhưng có thể thay đổi rất nhiều.

| Có cấu trúc                                                                   | Bán cấu trúc                                                                                | Không có cấu trúc                            |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------- |
| Danh sách người với số điện thoại của họ                                      | Các trang Wikipedia với các liên kết                                                       | Văn bản của Bách khoa toàn thư Britannica   |
| Nhiệt độ trong tất cả các phòng của một tòa nhà mỗi phút trong 20 năm qua    | Bộ sưu tập các bài báo khoa học ở định dạng JSON với tác giả, ngày xuất bản và tóm tắt      | Dữ liệu video thô từ camera giám sát        |
| Dữ liệu về tuổi và giới tính của tất cả mọi người vào tòa nhà                | Các trang Internet                                                                         | Dữ liệu video thô từ camera giám sát        |

## Nguồn dữ liệu

Có rất nhiều nguồn dữ liệu có thể có, và sẽ không thể liệt kê hết tất cả! Tuy nhiên, hãy đề cập đến một số nơi điển hình mà bạn có thể lấy dữ liệu:

* **Có cấu trúc**
  - **Internet of Things** (IoT), bao gồm dữ liệu từ các cảm biến khác nhau, chẳng hạn như cảm biến nhiệt độ hoặc áp suất, cung cấp rất nhiều dữ liệu hữu ích. Ví dụ, nếu một tòa nhà văn phòng được trang bị các cảm biến IoT, chúng ta có thể tự động kiểm soát hệ thống sưởi và chiếu sáng để giảm thiểu chi phí.
  - **Khảo sát** mà chúng ta yêu cầu người dùng hoàn thành sau khi mua hàng hoặc sau khi truy cập một trang web.
  - **Phân tích hành vi** có thể, ví dụ, giúp chúng ta hiểu người dùng đi sâu vào trang web như thế nào và lý do phổ biến khiến họ rời khỏi trang web.
* **Không có cấu trúc**
  - **Văn bản** có thể là một nguồn thông tin phong phú, chẳng hạn như điểm số **cảm xúc tổng thể**, hoặc trích xuất từ khóa và ý nghĩa ngữ nghĩa.
  - **Hình ảnh** hoặc **Video**. Một video từ camera giám sát có thể được sử dụng để ước tính lưu lượng giao thông trên đường và thông báo cho mọi người về các tắc nghẽn giao thông tiềm năng.
  - **Nhật ký máy chủ web** có thể được sử dụng để hiểu những trang nào trên trang web của chúng ta được truy cập nhiều nhất và trong bao lâu.
* Bán cấu trúc
  - **Biểu đồ mạng xã hội** có thể là nguồn dữ liệu tuyệt vời về tính cách người dùng và hiệu quả tiềm năng trong việc lan truyền thông tin.
  - Khi chúng ta có một loạt các bức ảnh từ một bữa tiệc, chúng ta có thể cố gắng trích xuất dữ liệu **Động lực nhóm** bằng cách xây dựng một biểu đồ về những người chụp ảnh cùng nhau.

Bằng cách biết các nguồn dữ liệu khác nhau có thể có, bạn có thể cố gắng nghĩ về các kịch bản khác nhau mà các kỹ thuật khoa học dữ liệu có thể được áp dụng để hiểu rõ hơn tình hình và cải thiện quy trình kinh doanh.

## Bạn có thể làm gì với Dữ liệu

Trong Khoa học Dữ liệu, chúng ta tập trung vào các bước sau trong hành trình dữ liệu:

<dl>
<dt>1) Thu thập dữ liệu</dt>
<dd>
Bước đầu tiên là thu thập dữ liệu. Trong nhiều trường hợp, đây có thể là một quá trình đơn giản, như dữ liệu được đưa vào cơ sở dữ liệu từ một ứng dụng web, nhưng đôi khi chúng ta cần sử dụng các kỹ thuật đặc biệt. Ví dụ, dữ liệu từ các cảm biến IoT có thể quá tải, và việc sử dụng các điểm đệm như IoT Hub để thu thập tất cả dữ liệu trước khi xử lý tiếp theo là một thực hành tốt.
</dd>
<dt>2) Lưu trữ dữ liệu</dt>
<dd>
Việc lưu trữ dữ liệu có thể là một thách thức, đặc biệt nếu chúng ta đang nói về dữ liệu lớn. Khi quyết định cách lưu trữ dữ liệu, nên dự đoán cách bạn muốn truy vấn dữ liệu trong tương lai. Có một số cách để lưu trữ dữ liệu:
<ul>
<li>Cơ sở dữ liệu quan hệ lưu trữ một tập hợp các bảng và sử dụng một ngôn ngữ đặc biệt gọi là SQL để truy vấn chúng. Thông thường, các bảng được tổ chức thành các nhóm khác nhau gọi là schema. Trong nhiều trường hợp, chúng ta cần chuyển đổi dữ liệu từ dạng ban đầu để phù hợp với schema.</li>
<li><a href="https://en.wikipedia.org/wiki/NoSQL">Cơ sở dữ liệu NoSQL</a>, chẳng hạn như <a href="https://azure.microsoft.com/services/cosmos-db/?WT.mc_id=academic-77958-bethanycheum">CosmosDB</a>, không áp đặt schema lên dữ liệu và cho phép lưu trữ dữ liệu phức tạp hơn, ví dụ, các tài liệu JSON dạng phân cấp hoặc biểu đồ. Tuy nhiên, các cơ sở dữ liệu NoSQL không có khả năng truy vấn phong phú như SQL và không thể áp đặt tính toàn vẹn tham chiếu, tức là các quy tắc về cách dữ liệu được cấu trúc trong các bảng và quản lý mối quan hệ giữa các bảng.</li>
<li><a href="https://en.wikipedia.org/wiki/Data_lake">Lưu trữ Data Lake</a> được sử dụng cho các bộ sưu tập dữ liệu lớn ở dạng thô, không có cấu trúc. Data Lake thường được sử dụng với dữ liệu lớn, nơi tất cả dữ liệu không thể nằm trên một máy và phải được lưu trữ và xử lý bởi một cụm máy chủ. <a href="https://en.wikipedia.org/wiki/Apache_Parquet">Parquet</a> là định dạng dữ liệu thường được sử dụng cùng với dữ liệu lớn.</li> 
</ul>
</dd>
<dt>3) Xử lý dữ liệu</dt>
<dd>
Đây là phần thú vị nhất của hành trình dữ liệu, bao gồm việc chuyển đổi dữ liệu từ dạng ban đầu sang dạng có thể sử dụng để trực quan hóa/huấn luyện mô hình. Khi xử lý dữ liệu không có cấu trúc như văn bản hoặc hình ảnh, chúng ta có thể cần sử dụng một số kỹ thuật AI để trích xuất <b>đặc điểm</b> từ dữ liệu, do đó chuyển đổi nó thành dạng có cấu trúc.
</dd>
<dt>4) Trực quan hóa / Thông tin từ con người</dt>
<dd>
Thường thì, để hiểu dữ liệu, chúng ta cần trực quan hóa nó. Có nhiều kỹ thuật trực quan hóa khác nhau trong hộp công cụ của chúng ta, chúng ta có thể tìm ra cách hiển thị phù hợp để rút ra thông tin. Thường thì, một nhà khoa học dữ liệu cần "chơi với dữ liệu", trực quan hóa nó nhiều lần và tìm kiếm các mối quan hệ. Ngoài ra, chúng ta có thể sử dụng các kỹ thuật thống kê để kiểm tra giả thuyết hoặc chứng minh mối tương quan giữa các phần dữ liệu khác nhau.
</dd>
<dt>5) Huấn luyện mô hình dự đoán</dt>
<dd>
Vì mục tiêu cuối cùng của khoa học dữ liệu là có thể đưa ra quyết định dựa trên dữ liệu, chúng ta có thể muốn sử dụng các kỹ thuật của <a href="http://github.com/microsoft/ml-for-beginners">Học Máy</a> để xây dựng một mô hình dự đoán. Sau đó, chúng ta có thể sử dụng mô hình này để đưa ra dự đoán bằng cách sử dụng các tập dữ liệu mới có cấu trúc tương tự.
</dd>
</dl>

Tất nhiên, tùy thuộc vào dữ liệu thực tế, một số bước có thể bị bỏ qua (ví dụ: khi chúng ta đã có dữ liệu trong cơ sở dữ liệu, hoặc khi chúng ta không cần huấn luyện mô hình), hoặc một số bước có thể được lặp lại nhiều lần (chẳng hạn như xử lý dữ liệu).

## Số hóa và Chuyển đổi số

Trong thập kỷ qua, nhiều doanh nghiệp đã bắt đầu hiểu được tầm quan trọng của dữ liệu khi đưa ra quyết định kinh doanh. Để áp dụng các nguyên tắc khoa học dữ liệu vào việc điều hành doanh nghiệp, trước tiên cần thu thập một số dữ liệu, tức là chuyển đổi các quy trình kinh doanh sang dạng kỹ thuật số. Điều này được gọi là **số hóa**. Việc áp dụng các kỹ thuật khoa học dữ liệu vào dữ liệu này để hướng dẫn quyết định có thể dẫn đến sự gia tăng đáng kể năng suất (hoặc thậm chí thay đổi hướng đi của doanh nghiệp), được gọi là **chuyển đổi số**.

Hãy xem xét một ví dụ. Giả sử chúng ta có một khóa học khoa học dữ liệu (như khóa học này) mà chúng ta cung cấp trực tuyến cho sinh viên, và chúng ta muốn sử dụng khoa học dữ liệu để cải thiện nó. Làm thế nào chúng ta có thể làm điều này?

Chúng ta có thể bắt đầu bằng cách hỏi "Điều gì có thể được số hóa?" Cách đơn giản nhất là đo thời gian mỗi sinh viên hoàn thành mỗi module, và đo kiến thức thu được bằng cách đưa ra bài kiểm tra trắc nghiệm ở cuối mỗi module. Bằng cách tính trung bình thời gian hoàn thành của tất cả sinh viên, chúng ta có thể tìm ra những module nào gây khó khăn nhất cho sinh viên, và làm việc để đơn giản hóa chúng.
> Bạn có thể tranh luận rằng cách tiếp cận này không lý tưởng, vì các mô-đun có thể có độ dài khác nhau. Có lẽ công bằng hơn nếu chia thời gian theo độ dài của mô-đun (tính theo số ký tự) và so sánh các giá trị đó.

Khi chúng ta bắt đầu phân tích kết quả của các bài kiểm tra trắc nghiệm, chúng ta có thể cố gắng xác định những khái niệm mà học sinh gặp khó khăn trong việc hiểu, và sử dụng thông tin đó để cải thiện nội dung. Để làm được điều này, chúng ta cần thiết kế các bài kiểm tra sao cho mỗi câu hỏi tương ứng với một khái niệm hoặc một phần kiến thức nhất định.

Nếu muốn phức tạp hơn, chúng ta có thể vẽ biểu đồ thời gian hoàn thành mỗi mô-đun so với nhóm tuổi của học sinh. Chúng ta có thể phát hiện ra rằng đối với một số nhóm tuổi, thời gian hoàn thành mô-đun là quá dài hoặc học sinh bỏ cuộc trước khi hoàn thành. Điều này có thể giúp chúng ta đưa ra khuyến nghị về độ tuổi phù hợp cho mô-đun và giảm thiểu sự không hài lòng của mọi người do kỳ vọng sai lệch.

## 🚀 Thử thách

Trong thử thách này, chúng ta sẽ cố gắng tìm các khái niệm liên quan đến lĩnh vực Khoa học Dữ liệu bằng cách xem xét các văn bản. Chúng ta sẽ lấy một bài viết trên Wikipedia về Khoa học Dữ liệu, tải xuống và xử lý văn bản, sau đó tạo một đám mây từ như thế này:

![Đám mây từ cho Khoa học Dữ liệu](../../../../translated_images/ds_wordcloud.664a7c07dca57de017c22bf0498cb40f898d48aa85b3c36a80620fea12fadd42.vi.png)

Truy cập [`notebook.ipynb`](../../../../1-Introduction/01-defining-data-science/notebook.ipynb ':ignore') để đọc qua mã. Bạn cũng có thể chạy mã và xem cách nó thực hiện tất cả các chuyển đổi dữ liệu trong thời gian thực.

> Nếu bạn không biết cách chạy mã trong Jupyter Notebook, hãy xem [bài viết này](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/1)

## Bài tập

* **Nhiệm vụ 1**: Sửa đổi mã trên để tìm các khái niệm liên quan đến các lĩnh vực **Dữ liệu lớn** và **Học máy**
* **Nhiệm vụ 2**: [Suy nghĩ về các kịch bản Khoa học Dữ liệu](assignment.md)

## Tác giả

Bài học này được viết với ♥️ bởi [Dmitry Soshnikov](http://soshnikov.com)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.