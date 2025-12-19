<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11739c7b40e7c6b16ad29e3df4e65862",
  "translation_date": "2025-12-19T11:46:19+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "vi"
}
-->
# Làm việc với Dữ liệu: Cơ sở dữ liệu Quan hệ

|![ Sketchnote bởi [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Làm việc với Dữ liệu: Cơ sở dữ liệu Quan hệ - _Sketchnote bởi [@nitya](https://twitter.com/nitya)_ |

Có thể bạn đã từng sử dụng bảng tính trong quá khứ để lưu trữ thông tin. Bạn có một tập hợp các hàng và cột, trong đó các hàng chứa thông tin (hoặc dữ liệu), và các cột mô tả thông tin đó (đôi khi gọi là siêu dữ liệu). Một cơ sở dữ liệu quan hệ được xây dựng dựa trên nguyên tắc cốt lõi này của các cột và hàng trong các bảng, cho phép bạn có thông tin phân bố trên nhiều bảng khác nhau. Điều này cho phép bạn làm việc với dữ liệu phức tạp hơn, tránh trùng lặp, và có sự linh hoạt trong cách bạn khám phá dữ liệu. Hãy cùng khám phá các khái niệm của cơ sở dữ liệu quan hệ.

## [Bài kiểm tra trước bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/8)

## Mọi thứ bắt đầu với các bảng

Một cơ sở dữ liệu quan hệ có cốt lõi là các bảng. Giống như với bảng tính, một bảng là tập hợp các cột và hàng. Hàng chứa dữ liệu hoặc thông tin mà chúng ta muốn làm việc, chẳng hạn như tên một thành phố hoặc lượng mưa. Các cột mô tả dữ liệu mà chúng lưu trữ.

Hãy bắt đầu khám phá bằng cách tạo một bảng để lưu trữ thông tin về các thành phố. Chúng ta có thể bắt đầu với tên và quốc gia của chúng. Bạn có thể lưu trữ điều này trong một bảng như sau:

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Chú ý tên các cột **city**, **country** và **population** mô tả dữ liệu được lưu trữ, và mỗi hàng có thông tin về một thành phố.

## Những hạn chế của cách tiếp cận một bảng duy nhất

Có thể bảng trên có vẻ khá quen thuộc với bạn. Hãy bắt đầu thêm một số dữ liệu bổ sung vào cơ sở dữ liệu đang phát triển của chúng ta - lượng mưa hàng năm (tính bằng milimét). Chúng ta sẽ tập trung vào các năm 2018, 2019 và 2020. Nếu chúng ta thêm cho Tokyo, nó có thể trông như sau:

| City  | Country | Year | Amount |
| ----- | ------- | ---- | ------ |
| Tokyo | Japan   | 2020 | 1690   |
| Tokyo | Japan   | 2019 | 1874   |
| Tokyo | Japan   | 2018 | 1445   |

Bạn nhận thấy gì về bảng của chúng ta? Bạn có thể nhận thấy chúng ta đang lặp lại tên và quốc gia của thành phố nhiều lần. Điều đó có thể chiếm khá nhiều dung lượng lưu trữ, và phần lớn là không cần thiết phải có nhiều bản sao. Rốt cuộc, Tokyo chỉ có một tên mà chúng ta quan tâm.

OK, hãy thử một cách khác. Hãy thêm các cột mới cho mỗi năm:

| City     | Country       | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokyo    | Japan         | 1445 | 1874 | 1690 |
| Atlanta  | United States | 1779 | 1111 | 1683 |
| Auckland | New Zealand   | 1386 | 942  | 1176 |

Mặc dù cách này tránh được việc lặp lại hàng, nhưng nó lại tạo ra một vài thách thức khác. Chúng ta sẽ cần phải sửa đổi cấu trúc bảng mỗi khi có một năm mới. Thêm vào đó, khi dữ liệu của chúng ta tăng lên, việc có các năm làm cột sẽ khiến việc truy xuất và tính toán giá trị trở nên khó khăn hơn.

Đó là lý do tại sao chúng ta cần nhiều bảng và các mối quan hệ. Bằng cách tách dữ liệu ra, chúng ta có thể tránh trùng lặp và có nhiều sự linh hoạt hơn trong cách làm việc với dữ liệu.

## Các khái niệm về mối quan hệ

Hãy quay lại với dữ liệu của chúng ta và xác định cách chúng ta muốn phân chia. Chúng ta biết muốn lưu trữ tên và quốc gia cho các thành phố, vì vậy điều này có lẽ sẽ phù hợp nhất trong một bảng.

| City     | Country       |
| -------- | ------------- |
| Tokyo    | Japan         |
| Atlanta  | United States |
| Auckland | New Zealand   |

Nhưng trước khi tạo bảng tiếp theo, chúng ta cần tìm cách tham chiếu đến từng thành phố. Chúng ta cần một dạng định danh, ID hoặc (theo thuật ngữ kỹ thuật cơ sở dữ liệu) là khóa chính. Khóa chính là một giá trị dùng để xác định một hàng cụ thể trong bảng. Mặc dù điều này có thể dựa trên một giá trị cụ thể (ví dụ như tên thành phố), nhưng nó hầu như luôn phải là một số hoặc định danh khác. Chúng ta không muốn id thay đổi vì điều đó sẽ phá vỡ mối quan hệ. Trong hầu hết các trường hợp, khóa chính hoặc id sẽ là một số được tạo tự động.

> ✅ Khóa chính thường được viết tắt là PK

### cities

| city_id | City     | Country       |
| ------- | -------- | ------------- |
| 1       | Tokyo    | Japan         |
| 2       | Atlanta  | United States |
| 3       | Auckland | New Zealand   |

> ✅ Bạn sẽ nhận thấy chúng ta sử dụng các thuật ngữ "id" và "khóa chính" thay thế cho nhau trong bài học này. Các khái niệm ở đây cũng áp dụng cho DataFrames, mà bạn sẽ khám phá sau. DataFrames không sử dụng thuật ngữ "khóa chính", tuy nhiên bạn sẽ nhận thấy chúng hoạt động tương tự.

Với bảng cities đã tạo, hãy lưu trữ lượng mưa. Thay vì lặp lại toàn bộ thông tin về thành phố, chúng ta có thể sử dụng id. Chúng ta cũng nên đảm bảo bảng mới tạo có một cột *id* nữa, vì tất cả các bảng nên có id hoặc khóa chính.

### rainfall

| rainfall_id | city_id | Year | Amount |
| ----------- | ------- | ---- | ------ |
| 1           | 1       | 2018 | 1445   |
| 2           | 1       | 2019 | 1874   |
| 3           | 1       | 2020 | 1690   |
| 4           | 2       | 2018 | 1779   |
| 5           | 2       | 2019 | 1111   |
| 6           | 2       | 2020 | 1683   |
| 7           | 3       | 2018 | 1386   |
| 8           | 3       | 2019 | 942    |
| 9           | 3       | 2020 | 1176   |

Chú ý cột **city_id** trong bảng **rainfall** mới tạo. Cột này chứa các giá trị tham chiếu đến các ID trong bảng **cities**. Theo thuật ngữ dữ liệu quan hệ kỹ thuật, đây được gọi là **khóa ngoại**; nó là khóa chính từ một bảng khác. Bạn có thể nghĩ đơn giản nó như một tham chiếu hoặc con trỏ. **city_id** 1 tham chiếu đến Tokyo.

> [!NOTE]  
> Khóa ngoại thường được viết tắt là FK

## Truy xuất dữ liệu

Với dữ liệu được tách thành hai bảng, bạn có thể thắc mắc làm thế nào để truy xuất nó. Nếu chúng ta sử dụng cơ sở dữ liệu quan hệ như MySQL, SQL Server hoặc Oracle, chúng ta có thể dùng một ngôn ngữ gọi là Structured Query Language hay SQL. SQL (đôi khi phát âm là sequel) là ngôn ngữ chuẩn dùng để truy xuất và sửa đổi dữ liệu trong cơ sở dữ liệu quan hệ.

Để truy xuất dữ liệu, bạn dùng lệnh `SELECT`. Về cơ bản, bạn **chọn** các cột bạn muốn xem **từ** bảng chứa chúng. Nếu bạn chỉ muốn hiển thị tên các thành phố, bạn có thể dùng câu lệnh sau:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` là nơi bạn liệt kê các cột, và `FROM` là nơi bạn liệt kê các bảng.

> [!NOTE]  
> Cú pháp SQL không phân biệt chữ hoa chữ thường, nghĩa là `select` và `SELECT` có nghĩa như nhau. Tuy nhiên, tùy thuộc vào loại cơ sở dữ liệu bạn đang dùng, các cột và bảng có thể phân biệt chữ hoa chữ thường. Do đó, tốt nhất là luôn coi mọi thứ trong lập trình như phân biệt chữ hoa chữ thường. Khi viết truy vấn SQL, quy ước phổ biến là viết các từ khóa bằng chữ hoa.

Truy vấn trên sẽ hiển thị tất cả các thành phố. Giả sử chúng ta chỉ muốn hiển thị các thành phố ở New Zealand. Chúng ta cần một dạng bộ lọc. Từ khóa SQL cho điều này là `WHERE`, hay "nơi mà điều gì đó đúng".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Kết hợp dữ liệu

Cho đến nay chúng ta đã truy xuất dữ liệu từ một bảng duy nhất. Bây giờ chúng ta muốn kết hợp dữ liệu từ cả hai bảng **cities** và **rainfall**. Điều này được thực hiện bằng cách *kết nối* chúng với nhau. Bạn sẽ tạo ra một mối nối giữa hai bảng, và ghép các giá trị từ một cột của mỗi bảng.

Trong ví dụ của chúng ta, chúng ta sẽ ghép cột **city_id** trong **rainfall** với cột **city_id** trong **cities**. Điều này sẽ ghép giá trị lượng mưa với thành phố tương ứng. Loại kết nối chúng ta sẽ thực hiện gọi là *inner* join, nghĩa là nếu có hàng nào không khớp với bất kỳ hàng nào từ bảng kia thì sẽ không được hiển thị. Trong trường hợp của chúng ta, mỗi thành phố đều có lượng mưa, nên tất cả sẽ được hiển thị.

Hãy truy xuất lượng mưa cho năm 2019 của tất cả các thành phố.

Chúng ta sẽ làm điều này theo các bước. Bước đầu tiên là kết nối dữ liệu bằng cách chỉ định các cột làm mối nối - **city_id** như đã nhấn mạnh trước đó.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Chúng ta đã đánh dấu hai cột muốn lấy, và việc muốn kết nối các bảng với nhau bằng **city_id**. Bây giờ chúng ta có thể thêm câu lệnh `WHERE` để lọc chỉ lấy năm 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Tóm tắt

Cơ sở dữ liệu quan hệ tập trung vào việc chia thông tin thành nhiều bảng rồi kết hợp lại để hiển thị và phân tích. Điều này cung cấp sự linh hoạt cao để thực hiện các phép tính và thao tác dữ liệu khác. Bạn đã thấy các khái niệm cốt lõi của cơ sở dữ liệu quan hệ, và cách thực hiện kết nối giữa hai bảng.

## 🚀 Thử thách

Có rất nhiều cơ sở dữ liệu quan hệ có sẵn trên internet. Bạn có thể khám phá dữ liệu bằng cách sử dụng các kỹ năng bạn đã học ở trên.

## Bài kiểm tra sau bài giảng

## [Bài kiểm tra sau bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/9)

## Ôn tập & Tự học

Có nhiều tài nguyên có sẵn trên [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) để bạn tiếp tục khám phá SQL và các khái niệm cơ sở dữ liệu quan hệ

- [Mô tả các khái niệm về dữ liệu quan hệ](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Bắt đầu truy vấn với Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL là một phiên bản của SQL)
- [Nội dung SQL trên Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Bài tập

[Hiển thị dữ liệu sân bay](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->