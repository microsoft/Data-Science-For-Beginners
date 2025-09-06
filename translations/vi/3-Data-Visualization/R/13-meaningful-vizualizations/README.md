<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-28T18:37:04+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "vi"
}
-->
# Tạo Các Biểu Đồ Trực Quan Có Ý Nghĩa

|![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Biểu Đồ Trực Quan Có Ý Nghĩa - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

> "Nếu bạn tra tấn dữ liệu đủ lâu, nó sẽ thú nhận bất cứ điều gì" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Một trong những kỹ năng cơ bản của một nhà khoa học dữ liệu là khả năng tạo ra các biểu đồ trực quan có ý nghĩa, giúp trả lời các câu hỏi mà bạn có thể có. Trước khi trực quan hóa dữ liệu, bạn cần đảm bảo rằng dữ liệu đã được làm sạch và chuẩn bị, như bạn đã làm trong các bài học trước. Sau đó, bạn có thể bắt đầu quyết định cách tốt nhất để trình bày dữ liệu.

Trong bài học này, bạn sẽ xem xét:

1. Cách chọn loại biểu đồ phù hợp  
2. Cách tránh biểu đồ gây hiểu lầm  
3. Cách làm việc với màu sắc  
4. Cách định dạng biểu đồ để dễ đọc  
5. Cách tạo biểu đồ động hoặc 3D  
6. Cách tạo biểu đồ sáng tạo  

## [Câu hỏi trước bài học](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Chọn loại biểu đồ phù hợp

Trong các bài học trước, bạn đã thử nghiệm xây dựng nhiều loại biểu đồ trực quan thú vị bằng Matplotlib và Seaborn. Nói chung, bạn có thể chọn [loại biểu đồ phù hợp](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) cho câu hỏi bạn đang đặt ra bằng cách sử dụng bảng sau:

| Bạn cần:                   | Bạn nên sử dụng:                |
| -------------------------- | ------------------------------- |
| Hiển thị xu hướng theo thời gian | Đường (Line)                  |
| So sánh các danh mục       | Cột (Bar), Tròn (Pie)           |
| So sánh tổng số            | Tròn (Pie), Cột xếp chồng       |
| Hiển thị mối quan hệ       | Điểm (Scatter), Đường, Facet, Đường kép |
| Hiển thị phân phối         | Điểm (Scatter), Histogram, Box  |
| Hiển thị tỷ lệ             | Tròn (Pie), Donut, Waffle       |

> ✅ Tùy thuộc vào cấu trúc dữ liệu của bạn, bạn có thể cần chuyển đổi dữ liệu từ dạng văn bản sang số để biểu đồ hỗ trợ.

## Tránh gây hiểu lầm

Ngay cả khi một nhà khoa học dữ liệu cẩn thận chọn đúng biểu đồ cho dữ liệu, vẫn có nhiều cách để dữ liệu được trình bày nhằm chứng minh một quan điểm, thường là làm tổn hại đến tính chính xác của dữ liệu. Có rất nhiều ví dụ về các biểu đồ và đồ họa thông tin gây hiểu lầm!

[![How Charts Lie của Alberto Cairo](../../../../../translated_images/tornado.2880ffc7f135f82b5e5328624799010abefd1080ae4b7ecacbdc7d792f1d8849.vi.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Nhấp vào hình ảnh trên để xem một bài nói chuyện về các biểu đồ gây hiểu lầm

Biểu đồ này đảo ngược trục X để hiển thị điều ngược lại với sự thật, dựa trên ngày tháng:

![bad chart 1](../../../../../translated_images/bad-chart-1.596bc93425a8ac301a28b8361f59a970276e7b961658ce849886aa1fed427341.vi.png)

[Biểu đồ này](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) thậm chí còn gây hiểu lầm hơn, vì mắt người bị thu hút về phía bên phải để kết luận rằng, theo thời gian, số ca COVID đã giảm ở các quận khác nhau. Thực tế, nếu bạn nhìn kỹ vào các ngày tháng, bạn sẽ thấy chúng đã được sắp xếp lại để tạo ra xu hướng giảm giả.

![bad chart 2](../../../../../translated_images/bad-chart-2.62edf4d2f30f4e519f5ef50c07ce686e27b0196a364febf9a4d98eecd21f9f60.vi.jpg)

Ví dụ nổi tiếng này sử dụng màu sắc VÀ trục Y bị lật để đánh lừa: thay vì kết luận rằng số ca tử vong do súng tăng vọt sau khi thông qua luật thân thiện với súng, mắt người lại bị đánh lừa để nghĩ điều ngược lại:

![bad chart 3](../../../../../translated_images/bad-chart-3.e201e2e915a230bc2cde289110604ec9abeb89be510bd82665bebc1228258972.vi.jpg)

Biểu đồ kỳ lạ này cho thấy cách tỷ lệ có thể bị thao túng, dẫn đến hiệu ứng hài hước:

![bad chart 4](../../../../../translated_images/bad-chart-4.8872b2b881ffa96c3e0db10eb6aed7793efae2cac382c53932794260f7bfff07.vi.jpg)

So sánh những thứ không thể so sánh là một thủ thuật mờ ám khác. Có một [trang web tuyệt vời](https://tylervigen.com/spurious-correlations) về 'mối tương quan giả' hiển thị các 'sự thật' như tỷ lệ ly hôn ở Maine và mức tiêu thụ bơ thực vật. Một nhóm trên Reddit cũng thu thập [các ví dụ xấu](https://www.reddit.com/r/dataisugly/top/?t=all) về việc sử dụng dữ liệu.

Điều quan trọng là phải hiểu mắt người dễ bị đánh lừa bởi các biểu đồ gây hiểu lầm như thế nào. Ngay cả khi ý định của nhà khoa học dữ liệu là tốt, việc chọn sai loại biểu đồ, chẳng hạn như biểu đồ tròn với quá nhiều danh mục, cũng có thể gây hiểu lầm.

## Màu sắc

Bạn đã thấy trong biểu đồ 'bạo lực súng ở Florida' ở trên rằng màu sắc có thể cung cấp một lớp ý nghĩa bổ sung cho biểu đồ, đặc biệt là những biểu đồ không được thiết kế bằng các thư viện như ggplot2 và RColorBrewer, vốn đi kèm với các thư viện và bảng màu đã được kiểm chứng. Nếu bạn tự tạo biểu đồ, hãy nghiên cứu một chút về [lý thuyết màu sắc](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Hãy lưu ý, khi thiết kế biểu đồ, rằng khả năng tiếp cận là một khía cạnh quan trọng của trực quan hóa. Một số người dùng của bạn có thể bị mù màu - liệu biểu đồ của bạn có hiển thị tốt cho những người dùng bị suy giảm thị lực không?

Hãy cẩn thận khi chọn màu sắc cho biểu đồ của bạn, vì màu sắc có thể truyền tải ý nghĩa mà bạn không mong muốn. Các 'quý cô màu hồng' trong biểu đồ 'chiều cao' ở trên truyền tải một ý nghĩa 'nữ tính' rõ ràng, làm tăng thêm sự kỳ quặc của chính biểu đồ.

Mặc dù [ý nghĩa màu sắc](https://colormatters.com/color-symbolism/the-meanings-of-colors) có thể khác nhau ở các khu vực khác nhau trên thế giới và có xu hướng thay đổi theo sắc thái, nhưng nói chung, ý nghĩa màu sắc bao gồm:

| Màu sắc | Ý nghĩa               |
| ------- | --------------------- |
| đỏ      | quyền lực             |
| xanh    | tin cậy, trung thành  |
| vàng    | hạnh phúc, cảnh báo   |
| xanh lá | sinh thái, may mắn, ghen tị |
| tím     | hạnh phúc             |
| cam     | sôi động              |

Nếu bạn được giao nhiệm vụ tạo biểu đồ với màu sắc tùy chỉnh, hãy đảm bảo rằng biểu đồ của bạn vừa dễ tiếp cận vừa phù hợp với ý nghĩa mà bạn muốn truyền tải.

## Định dạng biểu đồ để dễ đọc

Biểu đồ sẽ không có ý nghĩa nếu chúng không dễ đọc! Hãy dành một chút thời gian để cân nhắc định dạng chiều rộng và chiều cao của biểu đồ sao cho phù hợp với dữ liệu của bạn. Nếu một biến (chẳng hạn như tất cả 50 bang) cần được hiển thị, hãy hiển thị chúng theo chiều dọc trên trục Y nếu có thể để tránh biểu đồ cuộn ngang.

Gắn nhãn các trục, cung cấp chú giải nếu cần thiết và cung cấp các công cụ hỗ trợ như tooltip để giúp hiểu dữ liệu tốt hơn.

Nếu dữ liệu của bạn là văn bản và dài dòng trên trục X, bạn có thể xoay góc văn bản để dễ đọc hơn. [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) cung cấp khả năng vẽ biểu đồ 3D nếu dữ liệu của bạn hỗ trợ. Các biểu đồ trực quan phức tạp có thể được tạo ra bằng cách sử dụng nó.

![3d plots](../../../../../translated_images/3d.db1734c151eee87d924989306a00e23f8cddac6a0aab122852ece220e9448def.vi.png)

## Biểu đồ động và hiển thị 3D

Một số biểu đồ trực quan tốt nhất hiện nay là biểu đồ động. Shirley Wu có những biểu đồ tuyệt vời được thực hiện bằng D3, chẳng hạn như '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', nơi mỗi bông hoa là một biểu đồ trực quan của một bộ phim. Một ví dụ khác cho Guardian là 'bussed out', một trải nghiệm tương tác kết hợp biểu đồ trực quan với Greensock và D3 cùng với định dạng bài viết cuộn để kể câu chuyện về cách NYC xử lý vấn đề người vô gia cư bằng cách đưa họ ra khỏi thành phố.

![busing](../../../../../translated_images/busing.8157cf1bc89a3f65052d362a78c72f964982ceb9dcacbe44480e35909c3dce62.vi.png)

> "Bussed Out: How America Moves its Homeless" từ [the Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Biểu đồ trực quan bởi Nadieh Bremer & Shirley Wu

Mặc dù bài học này không đủ để đi sâu vào việc dạy các thư viện trực quan hóa mạnh mẽ này, hãy thử sử dụng D3 trong một ứng dụng Vue.js bằng cách sử dụng một thư viện để hiển thị biểu đồ trực quan của cuốn sách "Dangerous Liaisons" dưới dạng một mạng xã hội động.

> "Les Liaisons Dangereuses" là một tiểu thuyết dưới dạng thư từ, hoặc một tiểu thuyết được trình bày dưới dạng một loạt các bức thư. Được viết vào năm 1782 bởi Choderlos de Laclos, nó kể câu chuyện về những mưu đồ xã hội độc ác và vô đạo đức của hai nhân vật chính đối đầu nhau trong giới quý tộc Pháp cuối thế kỷ 18, Vicomte de Valmont và Marquise de Merteuil. Cả hai đều gặp kết cục bi thảm nhưng không trước khi gây ra rất nhiều tổn hại xã hội. Tiểu thuyết diễn ra dưới dạng một loạt các bức thư được viết cho nhiều người khác nhau trong vòng tròn của họ, âm mưu trả thù hoặc đơn giản là để gây rắc rối. Hãy tạo một biểu đồ trực quan về những bức thư này để khám phá các nhân vật chính của câu chuyện, một cách trực quan.

Bạn sẽ hoàn thành một ứng dụng web hiển thị một cái nhìn động về mạng xã hội này. Nó sử dụng một thư viện được xây dựng để tạo [biểu đồ mạng](https://github.com/emiliorizzo/vue-d3-network) bằng Vue.js và D3. Khi ứng dụng đang chạy, bạn có thể kéo các nút trên màn hình để sắp xếp lại dữ liệu.

![liaisons](../../../../../translated_images/liaisons.90ce7360bcf8476558f700bbbaf198ad697d5b5cb2829ba141a89c0add7c6ecd.vi.png)

## Dự án: Tạo biểu đồ hiển thị mạng bằng D3.js

> Thư mục bài học này bao gồm một thư mục `solution` nơi bạn có thể tìm thấy dự án hoàn chỉnh để tham khảo.

1. Làm theo hướng dẫn trong tệp README.md trong thư mục gốc của thư mục starter. Đảm bảo rằng bạn đã cài đặt NPM và Node.js trên máy của mình trước khi cài đặt các phụ thuộc của dự án.

2. Mở thư mục `starter/src`. Bạn sẽ thấy một thư mục `assets` nơi có tệp .json chứa tất cả các bức thư từ tiểu thuyết, được đánh số, với chú thích 'to' và 'from'.

3. Hoàn thành mã trong `components/Nodes.vue` để kích hoạt biểu đồ trực quan. Tìm phương thức có tên `createLinks()` và thêm vòng lặp lồng nhau sau.

Duyệt qua đối tượng .json để lấy dữ liệu 'to' và 'from' cho các bức thư và xây dựng đối tượng `links` để thư viện biểu đồ trực quan có thể sử dụng:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Chạy ứng dụng của bạn từ terminal (npm run serve) và tận hưởng biểu đồ trực quan!

## 🚀 Thử thách

Khám phá trên internet để tìm các biểu đồ trực quan gây hiểu lầm. Tác giả đã đánh lừa người dùng như thế nào, và điều đó có phải là cố ý không? Hãy thử chỉnh sửa các biểu đồ để hiển thị chúng đúng cách.

## [Câu hỏi sau bài học](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Ôn tập & Tự học

Dưới đây là một số bài viết để đọc về biểu đồ dữ liệu gây hiểu lầm:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Hãy xem các biểu đồ trực quan thú vị về tài sản và hiện vật lịch sử:

https://handbook.pubpub.org/

Xem qua bài viết này về cách hoạt hình có thể nâng cao biểu đồ trực quan của bạn:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Bài tập

[Tự tạo biểu đồ trực quan của riêng bạn](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.