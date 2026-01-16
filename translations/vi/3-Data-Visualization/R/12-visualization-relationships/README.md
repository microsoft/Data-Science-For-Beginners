<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a33c5d4b4156a2b41788d8720b6f724c",
  "translation_date": "2025-08-28T18:33:04+00:00",
  "source_file": "3-Data-Visualization/R/12-visualization-relationships/README.md",
  "language_code": "vi"
}
-->
# Hình ảnh hóa Mối quan hệ: Tất cả về Mật ong 🍯

|![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Hình ảnh hóa Mối quan hệ - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

Tiếp tục với trọng tâm nghiên cứu về thiên nhiên, hãy khám phá các cách hình ảnh hóa thú vị để thể hiện mối quan hệ giữa các loại mật ong khác nhau, dựa trên một tập dữ liệu từ [Bộ Nông nghiệp Hoa Kỳ](https://www.nass.usda.gov/About_NASS/index.php).

Tập dữ liệu này gồm khoảng 600 mục, hiển thị sản lượng mật ong ở nhiều bang của Hoa Kỳ. Ví dụ, bạn có thể xem số lượng đàn ong, sản lượng mỗi đàn, tổng sản lượng, lượng tồn kho, giá mỗi pound, và giá trị mật ong được sản xuất ở một bang từ năm 1998-2012, với mỗi hàng đại diện cho một năm của từng bang.

Sẽ rất thú vị khi hình ảnh hóa mối quan hệ giữa sản lượng của một bang trong một năm nhất định và, ví dụ, giá mật ong ở bang đó. Ngoài ra, bạn cũng có thể hình ảnh hóa mối quan hệ giữa sản lượng mật ong mỗi đàn của các bang. Khoảng thời gian này bao gồm sự kiện 'CCD' hay 'Hội chứng Sụp đổ Đàn ong' lần đầu tiên được ghi nhận vào năm 2006 (http://npic.orst.edu/envir/ccd.html), vì vậy đây là một tập dữ liệu đáng để nghiên cứu. 🐝

## [Câu hỏi trước bài học](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

Trong bài học này, bạn có thể sử dụng ggplot2, thư viện mà bạn đã sử dụng trước đây, để hình ảnh hóa mối quan hệ giữa các biến. Đặc biệt thú vị là việc sử dụng hàm `geom_point` và `qplot` của ggplot2, cho phép tạo biểu đồ phân tán và biểu đồ đường để nhanh chóng hình ảnh hóa '[mối quan hệ thống kê](https://ggplot2.tidyverse.org/)', giúp nhà khoa học dữ liệu hiểu rõ hơn về cách các biến liên quan đến nhau.

## Biểu đồ phân tán

Sử dụng biểu đồ phân tán để hiển thị cách giá mật ong thay đổi theo năm, từng bang. ggplot2, với `ggplot` và `geom_point`, thuận tiện nhóm dữ liệu theo bang và hiển thị các điểm dữ liệu cho cả dữ liệu phân loại và dữ liệu số.

Hãy bắt đầu bằng cách nhập dữ liệu và Seaborn:

```r
honey=read.csv('../../data/honey.csv')
head(honey)
```
Bạn sẽ nhận thấy rằng dữ liệu mật ong có một số cột thú vị, bao gồm năm và giá mỗi pound. Hãy khám phá dữ liệu này, được nhóm theo bang của Hoa Kỳ:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |
| FL    | 230000 | 98          |22540000   | 4508000  | 0.64       | 14426000  | 1998 |

Tạo một biểu đồ phân tán cơ bản để hiển thị mối quan hệ giữa giá mỗi pound mật ong và bang xuất xứ của nó. Làm cho trục `y` đủ cao để hiển thị tất cả các bang:

```r
library(ggplot2)
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(colour = "blue")
```
![scatterplot 1](../../../../../translated_images/vi/scatter1.86b8900674d88b26dd3353a83fe604e9ab3722c4680cc40ee9beb452ff02cdea.png)

Bây giờ, hiển thị cùng dữ liệu với bảng màu mật ong để thể hiện cách giá thay đổi theo năm. Bạn có thể làm điều này bằng cách thêm tham số 'scale_color_gradientn' để hiển thị sự thay đổi theo năm:

> ✅ Tìm hiểu thêm về [scale_color_gradientn](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.1/topics/scale_colour_gradientn) - thử một bảng màu cầu vồng đẹp mắt!

```r
ggplot(honey, aes(x = priceperlb, y = state, color=year)) +
  geom_point()+scale_color_gradientn(colours = colorspace::heat_hcl(7))
```
![scatterplot 2](../../../../../translated_images/vi/scatter2.4d1cbc693bad20e2b563888747eb6bdf65b73ce449d903f7cd4068a78502dcff.png)

Với sự thay đổi bảng màu này, bạn có thể thấy rõ ràng rằng có một sự tiến triển mạnh mẽ theo năm về giá mật ong mỗi pound. Thực tế, nếu bạn xem xét một tập mẫu trong dữ liệu để xác minh (chọn một bang cụ thể, ví dụ Arizona), bạn có thể thấy một xu hướng tăng giá theo năm, với một vài ngoại lệ:

| state | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Một cách khác để hình ảnh hóa sự tiến triển này là sử dụng kích thước thay vì màu sắc. Đối với người dùng bị mù màu, đây có thể là một lựa chọn tốt hơn. Chỉnh sửa hình ảnh hóa của bạn để hiển thị sự tăng giá bằng cách tăng chu vi của các điểm:

```r
ggplot(honey, aes(x = priceperlb, y = state)) +
  geom_point(aes(size = year),colour = "blue") +
  scale_size_continuous(range = c(0.25, 3))
```
Bạn có thể thấy kích thước của các điểm tăng dần.

![scatterplot 3](../../../../../translated_images/vi/scatter3.722d21e6f20b3ea2e18339bb9b10d75906126715eb7d5fdc88fe74dcb6d7066a.png)

Đây có phải là một trường hợp đơn giản của cung và cầu? Do các yếu tố như biến đổi khí hậu và sự sụp đổ của đàn ong, liệu có ít mật ong hơn để mua theo năm, dẫn đến giá tăng?

Để khám phá mối tương quan giữa một số biến trong tập dữ liệu này, hãy cùng tìm hiểu một số biểu đồ đường.

## Biểu đồ đường

Câu hỏi: Có sự tăng rõ ràng về giá mật ong mỗi pound theo năm không? Bạn có thể dễ dàng khám phá điều này bằng cách tạo một biểu đồ đường đơn:

```r
qplot(honey$year,honey$priceperlb, geom='smooth', span =0.5, xlab = "year",ylab = "priceperlb")
```
Trả lời: Có, với một số ngoại lệ vào khoảng năm 2003:

![line chart 1](../../../../../translated_images/vi/line1.299b576fbb2a59e60a59e7130030f59836891f90302be084e4e8d14da0562e2a.png)

Câu hỏi: Vậy vào năm 2003, liệu chúng ta có thể thấy sự tăng đột biến trong nguồn cung mật ong không? Nếu bạn xem xét tổng sản lượng theo năm thì sao?

```python
qplot(honey$year,honey$totalprod, geom='smooth', span =0.5, xlab = "year",ylab = "totalprod")
```

![line chart 2](../../../../../translated_images/vi/line2.3b18fcda7176ceba5b6689eaaabb817d49c965e986f11cac1ae3f424030c34d8.png)

Trả lời: Không hẳn. Nếu bạn xem xét tổng sản lượng, thực tế nó dường như đã tăng trong năm đó, mặc dù nhìn chung lượng mật ong được sản xuất đang giảm trong những năm này.

Câu hỏi: Trong trường hợp đó, điều gì có thể đã gây ra sự tăng giá mật ong vào khoảng năm 2003?

Để khám phá điều này, bạn có thể sử dụng lưới facet.

## Lưới facet

Lưới facet lấy một khía cạnh của tập dữ liệu của bạn (trong trường hợp này, bạn có thể chọn 'năm' để tránh tạo quá nhiều facet). Seaborn sau đó có thể tạo một biểu đồ cho mỗi facet của các tọa độ x và y bạn chọn để so sánh dễ dàng hơn. Liệu năm 2003 có nổi bật trong loại so sánh này?

Tạo một lưới facet bằng cách sử dụng `facet_wrap` như được khuyến nghị bởi [tài liệu của ggplot2](https://ggplot2.tidyverse.org/reference/facet_wrap.html).

```r
ggplot(honey, aes(x=yieldpercol, y = numcol,group = 1)) + 
  geom_line() + facet_wrap(vars(year))
```
Trong hình ảnh hóa này, bạn có thể so sánh sản lượng mỗi đàn và số lượng đàn ong theo năm, cạnh nhau với wrap được đặt là 3 cho các cột:

![facet grid](../../../../../translated_images/vi/facet.491ad90d61c2a7cc69b50c929f80786c749e38217ccedbf1e22ed8909b65987c.png)

Đối với tập dữ liệu này, không có điều gì đặc biệt nổi bật liên quan đến số lượng đàn ong và sản lượng của chúng theo năm và theo bang. Liệu có cách khác để tìm mối tương quan giữa hai biến này?

## Biểu đồ đường kép

Thử một biểu đồ đường kép bằng cách chồng hai biểu đồ đường lên nhau, sử dụng hàm `par` và `plot` của R. Chúng ta sẽ vẽ năm trên trục x và hiển thị hai trục y. Vì vậy, hiển thị sản lượng mỗi đàn và số lượng đàn ong, chồng lên nhau:

```r
par(mar = c(5, 4, 4, 4) + 0.3)              
plot(honey$year, honey$numcol, pch = 16, col = 2,type="l")              
par(new = TRUE)                             
plot(honey$year, honey$yieldpercol, pch = 17, col = 3,              
     axes = FALSE, xlab = "", ylab = "",type="l")
axis(side = 4, at = pretty(range(y2)))      
mtext("colony yield", side = 4, line = 3)   
```
![superimposed plots](../../../../../translated_images/vi/dual-line.fc4665f360a54018d7df9bc6abcc26460112e17dcbda18d3b9ae6109b32b36c3.png)

Mặc dù không có điều gì nổi bật vào khoảng năm 2003, điều này cho phép chúng ta kết thúc bài học với một ghi chú vui vẻ hơn: mặc dù số lượng đàn ong đang giảm, số lượng đàn ong đang ổn định ngay cả khi sản lượng mỗi đàn đang giảm.

Cố lên, ong nhé!

🐝❤️
## 🚀 Thử thách

Trong bài học này, bạn đã học thêm về các cách sử dụng biểu đồ phân tán và lưới đường, bao gồm lưới facet. Thử thách bản thân tạo một lưới facet bằng cách sử dụng một tập dữ liệu khác, có thể là một tập dữ liệu bạn đã sử dụng trước đây trong các bài học này. Lưu ý thời gian tạo và cẩn thận về số lượng lưới bạn cần vẽ bằng các kỹ thuật này.
## [Câu hỏi sau bài học](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Ôn tập & Tự học

Biểu đồ đường có thể đơn giản hoặc khá phức tạp. Hãy đọc thêm trong [tài liệu ggplot2](https://ggplot2.tidyverse.org/reference/geom_path.html#:~:text=geom_line()%20connects%20them%20in,which%20cases%20are%20connected%20together) về các cách khác nhau bạn có thể xây dựng chúng. Thử cải thiện các biểu đồ đường bạn đã tạo trong bài học này bằng các phương pháp khác được liệt kê trong tài liệu.
## Bài tập

[Khám phá tổ ong](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.