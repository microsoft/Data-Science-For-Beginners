<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a20467e046d312809d008395051fc7",
  "translation_date": "2025-09-05T23:41:02+00:00",
  "source_file": "3-Data-Visualization/10-visualization-distributions/README.md",
  "language_code": "vi"
}
-->
# Hình dung Phân phối

|![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/10-Visualizing-Distributions.png)|
|:---:|
| Hình dung Phân phối - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

Trong bài học trước, bạn đã tìm hiểu một số thông tin thú vị về tập dữ liệu liên quan đến các loài chim ở Minnesota. Bạn đã phát hiện một số dữ liệu sai lệch bằng cách hình dung các giá trị ngoại lai và xem xét sự khác biệt giữa các loại chim dựa trên chiều dài tối đa của chúng.

## [Câu hỏi trước bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/18)
## Khám phá tập dữ liệu về các loài chim

Một cách khác để tìm hiểu dữ liệu là xem xét phân phối của nó, hoặc cách dữ liệu được tổ chức dọc theo một trục. Ví dụ, có thể bạn muốn tìm hiểu về phân phối chung, trong tập dữ liệu này, của sải cánh tối đa hoặc khối lượng cơ thể tối đa của các loài chim ở Minnesota.

Hãy khám phá một số thông tin về phân phối dữ liệu trong tập dữ liệu này. Trong tệp _notebook.ipynb_ ở thư mục gốc của bài học này, hãy nhập Pandas, Matplotlib và dữ liệu của bạn:

```python
import pandas as pd
import matplotlib.pyplot as plt
birds = pd.read_csv('../../data/birds.csv')
birds.head()
```

|      | Tên                          | Tên khoa học           | Loại                  | Bộ           | Họ       | Chi         | Tình trạng bảo tồn | Chiều dài tối thiểu | Chiều dài tối đa | Khối lượng cơ thể tối thiểu | Khối lượng cơ thể tối đa | Sải cánh tối thiểu | Sải cánh tối đa |
| ---: | :--------------------------- | :--------------------- | :-------------------- | :----------- | :------- | :---------- | :----------------- | ------------------: | ---------------: | -------------------------: | -----------------------: | -----------------: | ---------------: |
|    0 | Vịt huýt sáo bụng đen        | Dendrocygna autumnalis | Vịt/Ngan/Nước         | Anseriformes | Anatidae | Dendrocygna | LC                 |                  47 |              56 |                      652 |                    1020 |                 76 |               94 |
|    1 | Vịt huýt sáo hung            | Dendrocygna bicolor    | Vịt/Ngan/Nước         | Anseriformes | Anatidae | Dendrocygna | LC                 |                  45 |              53 |                      712 |                    1050 |                 85 |               93 |
|    2 | Ngỗng tuyết                  | Anser caerulescens     | Vịt/Ngan/Nước         | Anseriformes | Anatidae | Anser       | LC                 |                  64 |              79 |                     2050 |                    4050 |                135 |              165 |
|    3 | Ngỗng Ross                   | Anser rossii           | Vịt/Ngan/Nước         | Anseriformes | Anatidae | Anser       | LC                 |                57.3 |              64 |                     1066 |                    1567 |                113 |              116 |
|    4 | Ngỗng trán trắng lớn         | Anser albifrons        | Vịt/Ngan/Nước         | Anseriformes | Anatidae | Anser       | LC                 |                  64 |              81 |                     1930 |                    3310 |                130 |              165 |

Nhìn chung, bạn có thể nhanh chóng xem cách dữ liệu được phân phối bằng cách sử dụng biểu đồ phân tán như chúng ta đã làm trong bài học trước:

```python
birds.plot(kind='scatter',x='MaxLength',y='Order',figsize=(12,8))

plt.title('Max Length per Order')
plt.ylabel('Order')
plt.xlabel('Max Length')

plt.show()
```
![chiều dài tối đa theo bộ](../../../../3-Data-Visualization/10-visualization-distributions/images/scatter-wb.png)

Điều này cung cấp một cái nhìn tổng quan về phân phối chung của chiều dài cơ thể theo từng Bộ của chim, nhưng đây không phải là cách tối ưu để hiển thị các phân phối thực sự. Nhiệm vụ này thường được thực hiện bằng cách tạo biểu đồ Histogram.

## Làm việc với biểu đồ Histogram

Matplotlib cung cấp các cách rất tốt để hình dung phân phối dữ liệu bằng cách sử dụng biểu đồ Histogram. Loại biểu đồ này giống như biểu đồ cột, nơi phân phối có thể được nhìn thấy qua sự tăng giảm của các cột. Để tạo một biểu đồ Histogram, bạn cần dữ liệu số. Để tạo biểu đồ Histogram, bạn có thể vẽ một biểu đồ với loại được định nghĩa là 'hist' cho Histogram. Biểu đồ này hiển thị phân phối của MaxBodyMass cho toàn bộ phạm vi dữ liệu số của tập dữ liệu. Bằng cách chia mảng dữ liệu được cung cấp thành các "bins" nhỏ hơn, nó có thể hiển thị phân phối các giá trị của dữ liệu:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 10, figsize = (12,12))
plt.show()
```
![phân phối trên toàn bộ tập dữ liệu](../../../../3-Data-Visualization/10-visualization-distributions/images/dist1-wb.png)

Như bạn có thể thấy, hầu hết hơn 400 loài chim trong tập dữ liệu này nằm trong phạm vi dưới 2000 cho Khối lượng Cơ thể Tối đa của chúng. Hiểu rõ hơn về dữ liệu bằng cách thay đổi tham số `bins` thành một số lớn hơn, chẳng hạn như 30:

```python
birds['MaxBodyMass'].plot(kind = 'hist', bins = 30, figsize = (12,12))
plt.show()
```
![phân phối trên toàn bộ tập dữ liệu với tham số bins lớn hơn](../../../../3-Data-Visualization/10-visualization-distributions/images/dist2-wb.png)

Biểu đồ này hiển thị phân phối chi tiết hơn một chút. Một biểu đồ ít lệch về bên trái hơn có thể được tạo bằng cách đảm bảo rằng bạn chỉ chọn dữ liệu trong một phạm vi nhất định:

Lọc dữ liệu của bạn để chỉ lấy những loài chim có khối lượng cơ thể dưới 60 và hiển thị 40 `bins`:

```python
filteredBirds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]      
filteredBirds['MaxBodyMass'].plot(kind = 'hist',bins = 40,figsize = (12,12))
plt.show()     
```
![biểu đồ histogram đã lọc](../../../../3-Data-Visualization/10-visualization-distributions/images/dist3-wb.png)

✅ Thử một số bộ lọc và điểm dữ liệu khác. Để xem toàn bộ phân phối của dữ liệu, hãy loại bỏ bộ lọc `['MaxBodyMass']` để hiển thị các phân phối có nhãn.

Biểu đồ Histogram cũng cung cấp một số cải tiến về màu sắc và nhãn để thử nghiệm:

Tạo một biểu đồ Histogram 2D để so sánh mối quan hệ giữa hai phân phối. Hãy so sánh `MaxBodyMass` và `MaxLength`. Matplotlib cung cấp một cách tích hợp để hiển thị sự hội tụ bằng cách sử dụng các màu sáng hơn:

```python
x = filteredBirds['MaxBodyMass']
y = filteredBirds['MaxLength']

fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(x, y)
```
Có vẻ như có một mối tương quan dự kiến giữa hai yếu tố này dọc theo một trục dự kiến, với một điểm hội tụ đặc biệt mạnh:

![biểu đồ 2D](../../../../3-Data-Visualization/10-visualization-distributions/images/2D-wb.png)

Biểu đồ Histogram hoạt động tốt theo mặc định cho dữ liệu số. Vậy nếu bạn cần xem phân phối theo dữ liệu văn bản thì sao?

## Khám phá tập dữ liệu để tìm phân phối sử dụng dữ liệu văn bản

Tập dữ liệu này cũng bao gồm thông tin tốt về loại chim và chi, loài, họ của chúng cũng như tình trạng bảo tồn. Hãy tìm hiểu thông tin bảo tồn này. Phân phối của các loài chim theo tình trạng bảo tồn của chúng là gì?

> ✅ Trong tập dữ liệu, một số từ viết tắt được sử dụng để mô tả tình trạng bảo tồn. Những từ viết tắt này đến từ [Danh mục Đỏ IUCN](https://www.iucnredlist.org/), một tổ chức chuyên phân loại tình trạng của các loài.
> 
> - CR: Cực kỳ nguy cấp
> - EN: Nguy cấp
> - EX: Tuyệt chủng
> - LC: Ít quan tâm
> - NT: Gần bị đe dọa
> - VU: Dễ bị tổn thương

Đây là các giá trị dựa trên văn bản, vì vậy bạn sẽ cần thực hiện một chuyển đổi để tạo biểu đồ Histogram. Sử dụng dataframe filteredBirds, hiển thị tình trạng bảo tồn của nó cùng với Sải cánh Tối thiểu. Bạn thấy gì?

```python
x1 = filteredBirds.loc[filteredBirds.ConservationStatus=='EX', 'MinWingspan']
x2 = filteredBirds.loc[filteredBirds.ConservationStatus=='CR', 'MinWingspan']
x3 = filteredBirds.loc[filteredBirds.ConservationStatus=='EN', 'MinWingspan']
x4 = filteredBirds.loc[filteredBirds.ConservationStatus=='NT', 'MinWingspan']
x5 = filteredBirds.loc[filteredBirds.ConservationStatus=='VU', 'MinWingspan']
x6 = filteredBirds.loc[filteredBirds.ConservationStatus=='LC', 'MinWingspan']

kwargs = dict(alpha=0.5, bins=20)

plt.hist(x1, **kwargs, color='red', label='Extinct')
plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
plt.hist(x3, **kwargs, color='yellow', label='Endangered')
plt.hist(x4, **kwargs, color='green', label='Near Threatened')
plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
plt.hist(x6, **kwargs, color='gray', label='Least Concern')

plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
plt.legend();
```

![sải cánh và tình trạng bảo tồn](../../../../3-Data-Visualization/10-visualization-distributions/images/histogram-conservation-wb.png)

Dường như không có mối tương quan tốt giữa sải cánh tối thiểu và tình trạng bảo tồn. Thử nghiệm các yếu tố khác của tập dữ liệu bằng phương pháp này. Bạn có thể thử các bộ lọc khác nhau. Bạn có tìm thấy mối tương quan nào không?

## Biểu đồ mật độ

Bạn có thể nhận thấy rằng các biểu đồ Histogram mà chúng ta đã xem xét cho đến nay có dạng 'bậc thang' và không trơn tru theo một cung. Để hiển thị biểu đồ mật độ mượt mà hơn, bạn có thể thử biểu đồ mật độ.

Để làm việc với biểu đồ mật độ, hãy làm quen với một thư viện vẽ biểu đồ mới, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html).

Tải Seaborn, thử một biểu đồ mật độ cơ bản:

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(filteredBirds['MinWingspan'])
plt.show()
```
![Biểu đồ mật độ](../../../../3-Data-Visualization/10-visualization-distributions/images/density1.png)

Bạn có thể thấy cách biểu đồ này phản ánh biểu đồ trước đó về dữ liệu Sải cánh Tối thiểu; nó chỉ mượt mà hơn một chút. Theo tài liệu của Seaborn, "So với biểu đồ Histogram, KDE có thể tạo ra một biểu đồ ít lộn xộn và dễ hiểu hơn, đặc biệt khi vẽ nhiều phân phối. Nhưng nó có thể gây ra biến dạng nếu phân phối cơ bản bị giới hạn hoặc không mượt mà. Giống như biểu đồ Histogram, chất lượng của biểu diễn cũng phụ thuộc vào việc chọn các tham số làm mượt tốt." [nguồn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) Nói cách khác, các giá trị ngoại lai như thường lệ sẽ làm cho biểu đồ của bạn hoạt động không đúng.

Nếu bạn muốn xem lại đường MaxBodyMass gồ ghề trong biểu đồ thứ hai mà bạn đã tạo, bạn có thể làm mượt nó rất tốt bằng cách tạo lại nó bằng phương pháp này:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'])
plt.show()
```
![đường khối lượng cơ thể mượt mà](../../../../3-Data-Visualization/10-visualization-distributions/images/density2.png)

Nếu bạn muốn một đường mượt mà, nhưng không quá mượt, hãy chỉnh sửa tham số `bw_adjust`:

```python
sns.kdeplot(filteredBirds['MaxBodyMass'], bw_adjust=.2)
plt.show()
```
![đường khối lượng cơ thể ít mượt hơn](../../../../3-Data-Visualization/10-visualization-distributions/images/density3.png)

✅ Đọc về các tham số có sẵn cho loại biểu đồ này và thử nghiệm!

Loại biểu đồ này cung cấp các hình ảnh minh họa rất rõ ràng. Với một vài dòng mã, ví dụ, bạn có thể hiển thị mật độ khối lượng cơ thể tối đa theo từng Bộ của chim:

```python
sns.kdeplot(
   data=filteredBirds, x="MaxBodyMass", hue="Order",
   fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0,
)
```

![khối lượng cơ thể theo bộ](../../../../3-Data-Visualization/10-visualization-distributions/images/density4.png)

Bạn cũng có thể ánh xạ mật độ của nhiều biến trong một biểu đồ. Thử nghiệm MaxLength và MinLength của một loài chim so với tình trạng bảo tồn của chúng:

```python
sns.kdeplot(data=filteredBirds, x="MinLength", y="MaxLength", hue="ConservationStatus")
```

![nhiều mật độ, chồng lên nhau](../../../../3-Data-Visualization/10-visualization-distributions/images/multi.png)

Có lẽ đáng để nghiên cứu xem cụm các loài chim 'Dễ bị tổn thương' theo chiều dài của chúng có ý nghĩa hay không.

## 🚀 Thử thách

Biểu đồ Histogram là một loại biểu đồ tinh vi hơn so với các biểu đồ phân tán, biểu đồ cột hoặc biểu đồ đường cơ bản. Hãy tìm kiếm trên internet để tìm các ví dụ tốt về việc sử dụng biểu đồ Histogram. Chúng được sử dụng như thế nào, chúng thể hiện điều gì, và chúng thường được sử dụng trong các lĩnh vực hoặc lĩnh vực nghiên cứu nào?

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/19)

## Ôn tập & Tự học

Trong bài học này, bạn đã sử dụng Matplotlib và bắt đầu làm việc với Seaborn để hiển thị các biểu đồ tinh vi hơn. Hãy nghiên cứu về `kdeplot` trong Seaborn, một "đường cong mật độ xác suất liên tục trong một hoặc nhiều chiều". Đọc qua [tài liệu](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) để hiểu cách nó hoạt động.

## Bài tập

[Áp dụng kỹ năng của bạn](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.