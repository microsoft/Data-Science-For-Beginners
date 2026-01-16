<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "47028abaaafa2bcb1079702d20569066",
  "translation_date": "2025-08-28T18:29:15+00:00",
  "source_file": "3-Data-Visualization/R/11-visualization-proportions/README.md",
  "language_code": "vi"
}
-->
# Trực quan hóa tỷ lệ

|![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|Trực quan hóa tỷ lệ - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

Trong bài học này, bạn sẽ sử dụng một bộ dữ liệu tập trung vào thiên nhiên để trực quan hóa tỷ lệ, chẳng hạn như số lượng các loại nấm khác nhau trong một bộ dữ liệu về nấm. Hãy cùng khám phá những loại nấm thú vị này bằng cách sử dụng một bộ dữ liệu từ Audubon, liệt kê chi tiết về 23 loài nấm có mang thuộc họ Agaricus và Lepiota. Bạn sẽ thử nghiệm với các biểu đồ hấp dẫn như:

- Biểu đồ tròn 🥧
- Biểu đồ donut 🍩
- Biểu đồ waffle 🧇

> 💡 Một dự án rất thú vị có tên [Charticulator](https://charticulator.com) của Microsoft Research cung cấp giao diện kéo thả miễn phí để tạo trực quan hóa dữ liệu. Trong một trong các hướng dẫn của họ, họ cũng sử dụng bộ dữ liệu về nấm này! Vì vậy, bạn có thể khám phá dữ liệu và học thư viện cùng lúc: [Hướng dẫn Charticulator](https://charticulator.com/tutorials/tutorial4.html).

## [Câu hỏi trước bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## Tìm hiểu về nấm 🍄

Nấm rất thú vị. Hãy nhập một bộ dữ liệu để nghiên cứu chúng:

```r
mushrooms = read.csv('../../data/mushrooms.csv')
head(mushrooms)
```
Một bảng được in ra với một số dữ liệu tuyệt vời để phân tích:

| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Độc       | Lồi       | Mịn         | Nâu       | Có vết  | Hăng    | Tự do           | Sát nhau     | Hẹp       | Đen        | Phình ra    | Bằng nhau  | Mịn                     | Mịn                     | Trắng                  | Trắng                  | Một phần  | Trắng      | Một         | Treo      | Đen               | Rải rác    | Đô thị  |
| Ăn được   | Lồi       | Mịn         | Vàng      | Có vết  | Hạnh nhân| Tự do           | Sát nhau     | Rộng      | Đen        | Phình ra    | Câu lạc bộ| Mịn                     | Mịn                     | Trắng                  | Trắng                  | Một phần  | Trắng      | Một         | Treo      | Nâu               | Nhiều      | Cỏ      |
| Ăn được   | Chuông    | Mịn         | Trắng     | Có vết  | Hồi     | Tự do           | Sát nhau     | Rộng      | Nâu        | Phình ra    | Câu lạc bộ| Mịn                     | Mịn                     | Trắng                  | Trắng                  | Một phần  | Trắng      | Một         | Treo      | Nâu               | Nhiều      | Đồng cỏ |
| Độc       | Lồi       | Có vảy      | Trắng     | Có vết  | Hăng    | Tự do           | Sát nhau     | Hẹp       | Nâu        | Phình ra    | Bằng nhau  | Mịn                     | Mịn                     | Trắng                  | Trắng                  | Một phần  | Trắng      | Một         | Treo      | Đen               | Rải rác    | Đô thị  |
| Ăn được   | Lồi       | Mịn         | Xanh      | Không có vết | Không có | Tự do       | Đông đúc     | Rộng      | Đen        | Thon lại    | Bằng nhau  | Mịn                     | Mịn                     | Trắng                  | Trắng                  | Một phần  | Trắng      | Một         | Thoáng qua| Nâu               | Dồi dào    | Cỏ      |
| Ăn được   | Lồi       | Có vảy      | Vàng      | Có vết  | Hạnh nhân| Tự do           | Sát nhau     | Rộng      | Nâu        | Phình ra    | Câu lạc bộ| Mịn                     | Mịn                     | Trắng                  | Trắng                  | Một phần  | Trắng      | Một         | Treo      | Đen               | Nhiều      | Cỏ      |

Ngay lập tức, bạn nhận thấy rằng tất cả dữ liệu đều là dạng văn bản. Bạn sẽ phải chuyển đổi dữ liệu này để có thể sử dụng nó trong biểu đồ. Thực tế, hầu hết dữ liệu được biểu diễn dưới dạng đối tượng:

```r
names(mushrooms)
```

Kết quả là:

```output
[1] "class"                    "cap.shape"               
 [3] "cap.surface"              "cap.color"               
 [5] "bruises"                  "odor"                    
 [7] "gill.attachment"          "gill.spacing"            
 [9] "gill.size"                "gill.color"              
[11] "stalk.shape"              "stalk.root"              
[13] "stalk.surface.above.ring" "stalk.surface.below.ring"
[15] "stalk.color.above.ring"   "stalk.color.below.ring"  
[17] "veil.type"                "veil.color"              
[19] "ring.number"              "ring.type"               
[21] "spore.print.color"        "population"              
[23] "habitat"            
```
Hãy lấy dữ liệu này và chuyển đổi cột 'class' thành một danh mục:

```r
library(dplyr)
grouped=mushrooms %>%
  group_by(class) %>%
  summarise(count=n())
```

Bây giờ, nếu bạn in dữ liệu về nấm, bạn có thể thấy rằng nó đã được nhóm thành các danh mục theo lớp độc/ăn được:

```r
View(grouped)
```

| class     | count |
| --------- | --------- |
| Ăn được   | 4208 |
| Độc       | 3916 |

Nếu bạn làm theo thứ tự được trình bày trong bảng này để tạo nhãn danh mục lớp, bạn có thể tạo một biểu đồ tròn.

## Biểu đồ tròn!

```r
pie(grouped$count,grouped$class, main="Edible?")
```
Voila, một biểu đồ tròn hiển thị tỷ lệ của dữ liệu này theo hai lớp nấm. Điều rất quan trọng là phải sắp xếp đúng thứ tự của các nhãn, đặc biệt ở đây, vì vậy hãy chắc chắn kiểm tra thứ tự mà mảng nhãn được xây dựng!

![biểu đồ tròn](../../../../../translated_images/vi/pie1-wb.685df063673751f4b0b82127f7a52c7f9a920192f22ae61ad28412ba9ace97bf.png)

## Biểu đồ donut!

Một biểu đồ tròn thú vị hơn về mặt hình ảnh là biểu đồ donut, là một biểu đồ tròn với một lỗ ở giữa. Hãy xem dữ liệu của chúng ta bằng phương pháp này.

Hãy xem các môi trường sống khác nhau nơi nấm phát triển:

```r
library(dplyr)
habitat=mushrooms %>%
  group_by(habitat) %>%
  summarise(count=n())
View(habitat)
```
Kết quả là:

| habitat   | count |
| --------- | --------- |
| Cỏ        | 2148 |
| Lá        | 832 |
| Đồng cỏ   | 292 |
| Đường mòn | 1144 |
| Đô thị    | 368 |
| Rác thải  | 192 |
| Gỗ        | 3148 |

Ở đây, bạn đang nhóm dữ liệu của mình theo môi trường sống. Có 7 môi trường sống được liệt kê, vì vậy hãy sử dụng chúng làm nhãn cho biểu đồ donut của bạn:

```r
library(ggplot2)
library(webr)
PieDonut(habitat, aes(habitat, count=count))
```

![biểu đồ donut](../../../../../translated_images/vi/donut-wb.34e6fb275da9d834c2205145e39a3de9b6878191dcdba6f7a9e85f4b520449bc.png)

Đoạn mã này sử dụng hai thư viện - ggplot2 và webr. Sử dụng hàm PieDonut của thư viện webr, chúng ta có thể dễ dàng tạo biểu đồ donut!

Biểu đồ donut trong R cũng có thể được tạo chỉ bằng thư viện ggplot2. Bạn có thể tìm hiểu thêm về nó [tại đây](https://www.r-graph-gallery.com/128-ring-or-donut-plot.html) và thử nghiệm.

Bây giờ bạn đã biết cách nhóm dữ liệu của mình và hiển thị nó dưới dạng biểu đồ tròn hoặc donut, bạn có thể khám phá các loại biểu đồ khác. Hãy thử biểu đồ waffle, một cách khác để khám phá số lượng.

## Biểu đồ waffle!

Biểu đồ kiểu 'waffle' là một cách khác để trực quan hóa số lượng dưới dạng mảng 2D các ô vuông. Hãy thử trực quan hóa số lượng màu sắc của mũ nấm trong bộ dữ liệu này. Để làm điều này, bạn cần cài đặt một thư viện hỗ trợ có tên [waffle](https://cran.r-project.org/web/packages/waffle/waffle.pdf) và sử dụng nó để tạo trực quan hóa của bạn:

```r
install.packages("waffle", repos = "https://cinc.rud.is")
```

Chọn một phần dữ liệu của bạn để nhóm:

```r
library(dplyr)
cap_color=mushrooms %>%
  group_by(cap.color) %>%
  summarise(count=n())
View(cap_color)
```

Tạo biểu đồ waffle bằng cách tạo nhãn và sau đó nhóm dữ liệu của bạn:

```r
library(waffle)
names(cap_color$count) = paste0(cap_color$cap.color)
waffle((cap_color$count/10), rows = 7, title = "Waffle Chart")+scale_fill_manual(values=c("brown", "#F0DC82", "#D2691E", "green", 
                                                                                     "pink", "purple", "red", "grey", 
                                                                                     "yellow","white"))
```

Sử dụng biểu đồ waffle, bạn có thể dễ dàng thấy tỷ lệ màu sắc của mũ nấm trong bộ dữ liệu này. Thật thú vị, có rất nhiều nấm có mũ màu xanh lá cây!

![biểu đồ waffle](../../../../../translated_images/vi/waffle.aaa75c5337735a6ef32ace0ffb6506ef49e5aefe870ffd72b1bb080f4843c217.png)

Trong bài học này, bạn đã học ba cách để trực quan hóa tỷ lệ. Đầu tiên, bạn cần nhóm dữ liệu của mình thành các danh mục và sau đó quyết định cách tốt nhất để hiển thị dữ liệu - biểu đồ tròn, donut, hoặc waffle. Tất cả đều hấp dẫn và mang lại cho người dùng một cái nhìn nhanh về bộ dữ liệu.

## 🚀 Thử thách

Hãy thử tạo lại các biểu đồ hấp dẫn này trong [Charticulator](https://charticulator.com).

## [Câu hỏi sau bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## Ôn tập & Tự học

Đôi khi không rõ ràng khi nào nên sử dụng biểu đồ tròn, donut, hoặc waffle. Dưới đây là một số bài viết để đọc về chủ đề này:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

Hãy nghiên cứu thêm để tìm hiểu thêm thông tin về quyết định khó khăn này.

## Bài tập

[Thử nghiệm trong Excel](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.