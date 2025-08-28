<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3ade580a06b5f04d57cc83a768a8fb77",
  "translation_date": "2025-08-28T18:15:12+00:00",
  "source_file": "2-Working-With-Data/08-data-preparation/README.md",
  "language_code": "vi"
}
-->
# Làm việc với Dữ liệu: Chuẩn bị Dữ liệu

|![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Chuẩn bị Dữ liệu - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

## [Câu hỏi trước bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)

Tùy thuộc vào nguồn gốc, dữ liệu thô có thể chứa một số điểm không nhất quán gây khó khăn trong việc phân tích và mô hình hóa. Nói cách khác, dữ liệu này có thể được coi là "bẩn" và cần được làm sạch. Bài học này tập trung vào các kỹ thuật làm sạch và chuyển đổi dữ liệu để xử lý các vấn đề như dữ liệu thiếu, không chính xác hoặc không đầy đủ. Các chủ đề được đề cập trong bài học này sẽ sử dụng Python và thư viện Pandas và sẽ được [trình bày trong notebook](notebook.ipynb) trong thư mục này.

## Tầm quan trọng của việc làm sạch dữ liệu

- **Dễ sử dụng và tái sử dụng**: Khi dữ liệu được tổ chức và chuẩn hóa đúng cách, việc tìm kiếm, sử dụng và chia sẻ với người khác trở nên dễ dàng hơn.

- **Tính nhất quán**: Khoa học dữ liệu thường yêu cầu làm việc với nhiều tập dữ liệu, nơi các tập dữ liệu từ các nguồn khác nhau cần được kết hợp lại. Đảm bảo rằng mỗi tập dữ liệu riêng lẻ có tiêu chuẩn chung sẽ đảm bảo rằng dữ liệu vẫn hữu ích khi chúng được hợp nhất thành một tập dữ liệu duy nhất.

- **Độ chính xác của mô hình**: Dữ liệu đã được làm sạch sẽ cải thiện độ chính xác của các mô hình dựa vào nó.

## Các mục tiêu và chiến lược làm sạch phổ biến

- **Khám phá tập dữ liệu**: Khám phá dữ liệu, được đề cập trong một [bài học sau](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing), có thể giúp bạn phát hiện dữ liệu cần được làm sạch. Quan sát trực quan các giá trị trong một tập dữ liệu có thể thiết lập kỳ vọng về phần còn lại của nó hoặc cung cấp ý tưởng về các vấn đề có thể được giải quyết. Khám phá có thể bao gồm truy vấn cơ bản, trực quan hóa và lấy mẫu.

- **Định dạng**: Tùy thuộc vào nguồn, dữ liệu có thể có sự không nhất quán trong cách trình bày. Điều này có thể gây ra vấn đề trong việc tìm kiếm và biểu diễn giá trị, nơi nó được nhìn thấy trong tập dữ liệu nhưng không được biểu diễn đúng cách trong trực quan hóa hoặc kết quả truy vấn. Các vấn đề định dạng phổ biến bao gồm xử lý khoảng trắng, ngày tháng và kiểu dữ liệu. Việc giải quyết các vấn đề định dạng thường phụ thuộc vào người sử dụng dữ liệu. Ví dụ, tiêu chuẩn về cách trình bày ngày tháng và số có thể khác nhau giữa các quốc gia.

- **Trùng lặp**: Dữ liệu có nhiều hơn một lần xuất hiện có thể tạo ra kết quả không chính xác và thường nên được loại bỏ. Đây có thể là một hiện tượng phổ biến khi kết hợp hai hoặc nhiều tập dữ liệu. Tuy nhiên, có những trường hợp trùng lặp trong các tập dữ liệu kết hợp chứa các phần có thể cung cấp thông tin bổ sung và có thể cần được giữ lại.

- **Dữ liệu thiếu**: Dữ liệu thiếu có thể gây ra kết quả không chính xác cũng như kết quả yếu hoặc thiên lệch. Đôi khi điều này có thể được giải quyết bằng cách "tải lại" dữ liệu, điền vào các giá trị thiếu bằng tính toán và mã như Python, hoặc đơn giản là loại bỏ giá trị và dữ liệu tương ứng. Có nhiều lý do khiến dữ liệu bị thiếu và các hành động được thực hiện để giải quyết các giá trị thiếu này có thể phụ thuộc vào cách và lý do tại sao chúng bị thiếu ngay từ đầu.

## Khám phá thông tin DataFrame
> **Mục tiêu học tập:** Sau phần này, bạn sẽ cảm thấy thoải mái khi tìm kiếm thông tin chung về dữ liệu được lưu trữ trong các DataFrame của pandas.

Khi bạn đã tải dữ liệu vào pandas, dữ liệu đó có khả năng sẽ ở dạng DataFrame (tham khảo [bài học trước](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) để có cái nhìn tổng quan chi tiết). Tuy nhiên, nếu tập dữ liệu trong DataFrame của bạn có 60.000 hàng và 400 cột, làm thế nào để bạn bắt đầu hiểu được những gì bạn đang làm việc? May mắn thay, [pandas](https://pandas.pydata.org/) cung cấp một số công cụ tiện lợi để nhanh chóng xem thông tin tổng quan về một DataFrame ngoài các hàng đầu tiên và cuối cùng.

Để khám phá chức năng này, chúng ta sẽ nhập thư viện scikit-learn của Python và sử dụng một tập dữ liệu mang tính biểu tượng: **tập dữ liệu Iris**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: Để bắt đầu, phương thức `info()` được sử dụng để in ra tóm tắt nội dung có trong một `DataFrame`. Hãy xem tập dữ liệu này để xem chúng ta có gì:
```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Từ đây, chúng ta biết rằng tập dữ liệu *Iris* có 150 mục trong bốn cột và không có mục nào bị thiếu. Tất cả dữ liệu được lưu trữ dưới dạng số thực 64-bit.

- **DataFrame.head()**: Tiếp theo, để kiểm tra nội dung thực tế của `DataFrame`, chúng ta sử dụng phương thức `head()`. Hãy xem vài hàng đầu tiên của `iris_df` trông như thế nào:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Ngược lại, để kiểm tra vài hàng cuối cùng của `DataFrame`, chúng ta sử dụng phương thức `tail()`:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Kết luận:** Chỉ cần nhìn vào siêu dữ liệu về thông tin trong một DataFrame hoặc vài giá trị đầu tiên và cuối cùng trong đó, bạn có thể có ngay ý tưởng về kích thước, hình dạng và nội dung của dữ liệu mà bạn đang xử lý.

## Xử lý Dữ liệu Thiếu
> **Mục tiêu học tập:** Sau phần này, bạn sẽ biết cách thay thế hoặc loại bỏ các giá trị null khỏi DataFrame.

Hầu hết thời gian, các tập dữ liệu bạn muốn sử dụng (hoặc phải sử dụng) đều có các giá trị bị thiếu. Cách xử lý dữ liệu thiếu mang theo những sự đánh đổi tinh tế có thể ảnh hưởng đến phân tích cuối cùng và kết quả thực tế.

Pandas xử lý các giá trị thiếu theo hai cách. Cách đầu tiên bạn đã thấy trong các phần trước: `NaN`, hoặc Not a Number. Đây thực chất là một giá trị đặc biệt thuộc về đặc tả số thực IEEE và chỉ được sử dụng để chỉ ra các giá trị số thực bị thiếu.

Đối với các giá trị thiếu không phải số thực, pandas sử dụng đối tượng `None` của Python. Mặc dù có vẻ khó hiểu khi bạn sẽ gặp hai loại giá trị khác nhau để biểu thị cùng một điều, nhưng có những lý do lập trình hợp lý cho thiết kế này và, trên thực tế, cách tiếp cận này cho phép pandas cung cấp một sự thỏa hiệp tốt cho phần lớn các trường hợp. Tuy nhiên, cả `None` và `NaN` đều mang theo những hạn chế mà bạn cần lưu ý liên quan đến cách chúng có thể được sử dụng.

Tìm hiểu thêm về `NaN` và `None` từ [notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb)!

- **Phát hiện giá trị null**: Trong `pandas`, các phương thức `isnull()` và `notnull()` là các phương thức chính để phát hiện dữ liệu null. Cả hai đều trả về mặt nạ Boolean trên dữ liệu của bạn. Chúng ta sẽ sử dụng `numpy` cho các giá trị `NaN`:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Hãy nhìn kỹ vào kết quả. Có điều gì làm bạn ngạc nhiên không? Mặc dù `0` là một null số học, nhưng nó vẫn là một số nguyên hợp lệ và pandas coi nó như vậy. `''` thì tinh tế hơn một chút. Mặc dù chúng ta đã sử dụng nó trong Phần 1 để biểu thị một giá trị chuỗi rỗng, nhưng nó vẫn là một đối tượng chuỗi và không phải là biểu thị null theo quan điểm của pandas.

Bây giờ, hãy đảo ngược điều này và sử dụng các phương thức này theo cách giống như bạn sẽ sử dụng chúng trong thực tế. Bạn có thể sử dụng mặt nạ Boolean trực tiếp như một chỉ mục ``Series`` hoặc ``DataFrame``, điều này có thể hữu ích khi cố gắng làm việc với các giá trị bị thiếu (hoặc có mặt) riêng lẻ.

> **Kết luận**: Cả hai phương thức `isnull()` và `notnull()` đều tạo ra kết quả tương tự khi bạn sử dụng chúng trong `DataFrame`: chúng hiển thị kết quả và chỉ mục của các kết quả đó, điều này sẽ giúp bạn rất nhiều khi xử lý dữ liệu của mình.

- **Loại bỏ giá trị null**: Ngoài việc xác định các giá trị thiếu, pandas cung cấp một phương tiện tiện lợi để loại bỏ các giá trị null khỏi `Series` và `DataFrame`. (Đặc biệt trên các tập dữ liệu lớn, thường nên loại bỏ các giá trị thiếu [NA] khỏi phân tích của bạn hơn là xử lý chúng theo cách khác.) Để thấy điều này trong thực tế, hãy quay lại `example1`:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Lưu ý rằng điều này sẽ giống với kết quả đầu ra từ `example3[example3.notnull()]`. Sự khác biệt ở đây là, thay vì chỉ lập chỉ mục trên các giá trị được che, `dropna` đã loại bỏ các giá trị thiếu khỏi `Series` `example1`.

Vì `DataFrame` có hai chiều, chúng cung cấp nhiều tùy chọn hơn để loại bỏ dữ liệu.

```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Bạn có nhận thấy rằng pandas đã chuyển đổi hai cột thành số thực để phù hợp với các giá trị `NaN` không?)

Bạn không thể loại bỏ một giá trị duy nhất khỏi một `DataFrame`, vì vậy bạn phải loại bỏ toàn bộ hàng hoặc cột. Tùy thuộc vào những gì bạn đang làm, bạn có thể muốn làm một trong hai điều này, và vì vậy pandas cung cấp cho bạn các tùy chọn cho cả hai. Vì trong khoa học dữ liệu, các cột thường đại diện cho các biến và các hàng đại diện cho các quan sát, bạn có nhiều khả năng loại bỏ các hàng dữ liệu hơn; cài đặt mặc định cho `dropna()` là loại bỏ tất cả các hàng chứa bất kỳ giá trị null nào:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Nếu cần, bạn có thể loại bỏ các giá trị NA khỏi các cột. Sử dụng `axis=1` để làm điều đó:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Lưu ý rằng điều này có thể loại bỏ rất nhiều dữ liệu mà bạn có thể muốn giữ lại, đặc biệt là trong các tập dữ liệu nhỏ hơn. Điều gì sẽ xảy ra nếu bạn chỉ muốn loại bỏ các hàng hoặc cột chứa một số hoặc thậm chí tất cả các giá trị null? Bạn có thể chỉ định các cài đặt đó trong `dropna` với các tham số `how` và `thresh`.

Theo mặc định, `how='any'` (nếu bạn muốn tự kiểm tra hoặc xem phương thức này có các tham số nào khác, hãy chạy `example4.dropna?` trong một ô mã). Bạn có thể thay thế chỉ định `how='all'` để chỉ loại bỏ các hàng hoặc cột chứa tất cả các giá trị null. Hãy mở rộng `DataFrame` ví dụ của chúng ta để thấy điều này trong thực tế.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

Tham số `thresh` cung cấp cho bạn sự kiểm soát chi tiết hơn: bạn đặt số lượng giá trị *không null* mà một hàng hoặc cột cần có để được giữ lại:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Ở đây, hàng đầu tiên và cuối cùng đã bị loại bỏ, vì chúng chỉ chứa hai giá trị không null.

- **Điền giá trị null**: Tùy thuộc vào tập dữ liệu của bạn, đôi khi có thể hợp lý hơn khi điền các giá trị null bằng các giá trị hợp lệ thay vì loại bỏ chúng. Bạn có thể sử dụng `isnull` để làm điều này tại chỗ, nhưng điều đó có thể tốn công, đặc biệt nếu bạn có nhiều giá trị cần điền. Vì đây là một nhiệm vụ phổ biến trong khoa học dữ liệu, pandas cung cấp `fillna`, phương thức trả về một bản sao của `Series` hoặc `DataFrame` với các giá trị thiếu được thay thế bằng một giá trị bạn chọn. Hãy tạo một `Series` ví dụ khác để xem cách hoạt động của điều này trong thực tế.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Bạn có thể điền tất cả các mục null bằng một giá trị duy nhất, chẳng hạn như `0`:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Bạn có thể **điền tiến** các giá trị null, tức là sử dụng giá trị hợp lệ cuối cùng để điền vào null:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Bạn cũng có thể **điền lùi** để truyền giá trị hợp lệ tiếp theo ngược lại để điền vào null:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Như bạn có thể đoán, điều này hoạt động tương tự với `DataFrame`, nhưng bạn cũng có thể chỉ định một `axis` dọc theo đó để điền các giá trị null. Sử dụng lại `example2` đã sử dụng trước đó:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
Lưu ý rằng khi không có giá trị trước đó để điền tiến, giá trị null vẫn được giữ lại.
> **Điểm chính:** Có nhiều cách để xử lý giá trị thiếu trong tập dữ liệu của bạn. Chiến lược cụ thể mà bạn sử dụng (loại bỏ, thay thế, hoặc cách bạn thay thế) nên được quyết định bởi đặc điểm của dữ liệu đó. Bạn sẽ phát triển khả năng xử lý giá trị thiếu tốt hơn khi bạn làm việc và tương tác nhiều hơn với các tập dữ liệu.

## Loại bỏ dữ liệu trùng lặp

> **Mục tiêu học tập:** Sau phần này, bạn sẽ cảm thấy thoải mái khi xác định và loại bỏ các giá trị trùng lặp trong DataFrames.

Ngoài dữ liệu thiếu, bạn thường gặp dữ liệu trùng lặp trong các tập dữ liệu thực tế. May mắn thay, `pandas` cung cấp một cách dễ dàng để phát hiện và loại bỏ các mục trùng lặp.

- **Xác định dữ liệu trùng lặp: `duplicated`**: Bạn có thể dễ dàng phát hiện các giá trị trùng lặp bằng phương pháp `duplicated` trong pandas, phương pháp này trả về một mặt nạ Boolean cho biết liệu một mục trong `DataFrame` có trùng lặp với một mục trước đó hay không. Hãy tạo một ví dụ `DataFrame` khác để xem cách hoạt động này.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Loại bỏ dữ liệu trùng lặp: `drop_duplicates`:** chỉ đơn giản trả về một bản sao của dữ liệu mà tất cả các giá trị `duplicated` là `False`:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Cả `duplicated` và `drop_duplicates` mặc định xem xét tất cả các cột, nhưng bạn có thể chỉ định rằng chúng chỉ kiểm tra một tập hợp con các cột trong `DataFrame` của bạn:
```python
example4.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Điểm chính:** Loại bỏ dữ liệu trùng lặp là một phần thiết yếu của hầu hết các dự án khoa học dữ liệu. Dữ liệu trùng lặp có thể làm thay đổi kết quả phân tích của bạn và dẫn đến kết quả không chính xác!


## 🚀 Thử thách

Tất cả các tài liệu đã thảo luận đều được cung cấp dưới dạng [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/2-Working-With-Data/08-data-preparation/notebook.ipynb). Ngoài ra, có các bài tập sau mỗi phần, hãy thử làm chúng!

## [Câu hỏi sau bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## Ôn tập & Tự học

Có nhiều cách để khám phá và tiếp cận việc chuẩn bị dữ liệu của bạn cho phân tích và mô hình hóa, và việc làm sạch dữ liệu là một bước quan trọng mang tính "thực hành". Hãy thử các thử thách này từ Kaggle để khám phá các kỹ thuật mà bài học này chưa đề cập.

- [Thử thách Làm sạch Dữ liệu: Phân tích Ngày tháng](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Thử thách Làm sạch Dữ liệu: Chuẩn hóa và Tỷ lệ hóa Dữ liệu](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Bài tập

[Đánh giá Dữ liệu từ một Biểu mẫu](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.