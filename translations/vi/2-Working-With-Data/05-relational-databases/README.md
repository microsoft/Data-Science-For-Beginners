<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T20:21:43+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "vi"
}
-->
# Làm việc với dữ liệu: Cơ sở dữ liệu quan hệ

|![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Làm việc với dữ liệu: Cơ sở dữ liệu quan hệ - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

Có lẽ bạn đã từng sử dụng bảng tính để lưu trữ thông tin. Bạn có một tập hợp các hàng và cột, trong đó các hàng chứa thông tin (hoặc dữ liệu), và các cột mô tả thông tin (đôi khi được gọi là siêu dữ liệu). Cơ sở dữ liệu quan hệ được xây dựng dựa trên nguyên tắc cốt lõi này của các cột và hàng trong bảng, cho phép bạn lưu trữ thông tin trên nhiều bảng. Điều này giúp bạn làm việc với dữ liệu phức tạp hơn, tránh trùng lặp và có sự linh hoạt trong cách khám phá dữ liệu. Hãy cùng tìm hiểu các khái niệm về cơ sở dữ liệu quan hệ.

## [Câu hỏi trước bài giảng](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Mọi thứ bắt đầu từ các bảng

Cơ sở dữ liệu quan hệ có cốt lõi là các bảng. Giống như bảng tính, một bảng là tập hợp các cột và hàng. Hàng chứa dữ liệu hoặc thông tin mà chúng ta muốn làm việc, chẳng hạn như tên của một thành phố hoặc lượng mưa. Các cột mô tả dữ liệu mà chúng lưu trữ.

Hãy bắt đầu khám phá bằng cách tạo một bảng để lưu trữ thông tin về các thành phố. Chúng ta có thể bắt đầu với tên và quốc gia của chúng. Bạn có thể lưu trữ thông tin này trong một bảng như sau:

| Thành phố | Quốc gia       |
| --------- | ------------- |
| Tokyo     | Nhật Bản       |
| Atlanta   | Hoa Kỳ         |
| Auckland  | New Zealand    |

Lưu ý rằng tên các cột **thành phố**, **quốc gia** và **dân số** mô tả dữ liệu được lưu trữ, và mỗi hàng chứa thông tin về một thành phố.

## Hạn chế của cách tiếp cận một bảng

Có lẽ bảng trên trông khá quen thuộc với bạn. Hãy bắt đầu thêm một số dữ liệu bổ sung vào cơ sở dữ liệu đang phát triển của chúng ta - lượng mưa hàng năm (tính bằng milimet). Chúng ta sẽ tập trung vào các năm 2018, 2019 và 2020. Nếu chúng ta thêm dữ liệu cho Tokyo, nó có thể trông như thế này:

| Thành phố | Quốc gia | Năm  | Lượng mưa |
| --------- | ------- | ---- | --------- |
| Tokyo     | Nhật Bản | 2020 | 1690      |
| Tokyo     | Nhật Bản | 2019 | 1874      |
| Tokyo     | Nhật Bản | 2018 | 1445      |

Bạn nhận thấy gì về bảng của chúng ta? Có thể bạn nhận thấy chúng ta đang lặp lại tên và quốc gia của thành phố nhiều lần. Điều này có thể chiếm khá nhiều dung lượng lưu trữ và phần lớn là không cần thiết. Rốt cuộc, Tokyo chỉ có một tên mà chúng ta quan tâm.

Được rồi, hãy thử một cách khác. Hãy thêm các cột mới cho mỗi năm:

| Thành phố | Quốc gia       | 2018 | 2019 | 2020 |
| --------- | ------------- | ---- | ---- | ---- |
| Tokyo     | Nhật Bản       | 1445 | 1874 | 1690 |
| Atlanta   | Hoa Kỳ         | 1779 | 1111 | 1683 |
| Auckland  | New Zealand    | 1386 | 942  | 1176 |

Mặc dù cách này tránh được việc lặp lại các hàng, nhưng nó lại mang đến một số thách thức khác. Chúng ta sẽ cần thay đổi cấu trúc của bảng mỗi khi có một năm mới. Ngoài ra, khi dữ liệu của chúng ta tăng lên, việc có các năm làm cột sẽ khiến việc truy xuất và tính toán giá trị trở nên khó khăn hơn.

Đây là lý do tại sao chúng ta cần nhiều bảng và các mối quan hệ. Bằng cách chia nhỏ dữ liệu, chúng ta có thể tránh trùng lặp và có sự linh hoạt hơn trong cách làm việc với dữ liệu.

## Các khái niệm về mối quan hệ

Hãy quay lại dữ liệu của chúng ta và xác định cách chúng ta muốn chia nhỏ. Chúng ta biết rằng chúng ta muốn lưu trữ tên và quốc gia của các thành phố, vì vậy điều này có thể hoạt động tốt nhất trong một bảng.

| Thành phố | Quốc gia       |
| --------- | ------------- |
| Tokyo     | Nhật Bản       |
| Atlanta   | Hoa Kỳ         |
| Auckland  | New Zealand    |

Nhưng trước khi chúng ta tạo bảng tiếp theo, chúng ta cần tìm cách tham chiếu từng thành phố. Chúng ta cần một dạng định danh, ID hoặc (trong thuật ngữ cơ sở dữ liệu kỹ thuật) một khóa chính. Khóa chính là một giá trị được sử dụng để xác định một hàng cụ thể trong bảng. Mặc dù điều này có thể dựa trên một giá trị cụ thể (chúng ta có thể sử dụng tên của thành phố, chẳng hạn), nó gần như luôn luôn nên là một số hoặc định danh khác. Chúng ta không muốn ID thay đổi vì nó sẽ phá vỡ mối quan hệ. Trong hầu hết các trường hợp, khóa chính hoặc ID sẽ là một số được tạo tự động.

> ✅ Khóa chính thường được viết tắt là PK

### cities

| city_id | Thành phố | Quốc gia       |
| ------- | --------- | ------------- |
| 1       | Tokyo     | Nhật Bản       |
| 2       | Atlanta   | Hoa Kỳ         |
| 3       | Auckland  | New Zealand    |

> ✅ Bạn sẽ nhận thấy chúng ta sử dụng các thuật ngữ "id" và "khóa chính" thay thế cho nhau trong bài học này. Các khái niệm này cũng áp dụng cho DataFrames, mà bạn sẽ khám phá sau. DataFrames không sử dụng thuật ngữ "khóa chính", tuy nhiên bạn sẽ nhận thấy chúng hoạt động tương tự.

Với bảng **cities** đã được tạo, hãy lưu trữ lượng mưa. Thay vì lặp lại toàn bộ thông tin về thành phố, chúng ta có thể sử dụng ID. Chúng ta cũng nên đảm bảo bảng mới tạo có một cột *id*, vì tất cả các bảng nên có một ID hoặc khóa chính.

### rainfall

| rainfall_id | city_id | Năm  | Lượng mưa |
| ----------- | ------- | ---- | --------- |
| 1           | 1       | 2018 | 1445      |
| 2           | 1       | 2019 | 1874      |
| 3           | 1       | 2020 | 1690      |
| 4           | 2       | 2018 | 1779      |
| 5           | 2       | 2019 | 1111      |
| 6           | 2       | 2020 | 1683      |
| 7           | 3       | 2018 | 1386      |
| 8           | 3       | 2019 | 942       |
| 9           | 3       | 2020 | 1176      |

Lưu ý cột **city_id** trong bảng **rainfall** mới tạo. Cột này chứa các giá trị tham chiếu đến các ID trong bảng **cities**. Trong thuật ngữ dữ liệu quan hệ kỹ thuật, đây được gọi là **khóa ngoại**; nó là khóa chính từ một bảng khác. Bạn có thể nghĩ về nó như một tham chiếu hoặc con trỏ. **city_id** 1 tham chiếu đến Tokyo.

> [!NOTE] Khóa ngoại thường được viết tắt là FK

## Truy xuất dữ liệu

Với dữ liệu của chúng ta được chia thành hai bảng, bạn có thể thắc mắc làm thế nào để truy xuất nó. Nếu chúng ta sử dụng một cơ sở dữ liệu quan hệ như MySQL, SQL Server hoặc Oracle, chúng ta có thể sử dụng một ngôn ngữ gọi là Structured Query Language hoặc SQL. SQL (đôi khi được phát âm là "sequel") là một ngôn ngữ tiêu chuẩn được sử dụng để truy xuất và sửa đổi dữ liệu trong cơ sở dữ liệu quan hệ.

Để truy xuất dữ liệu, bạn sử dụng lệnh `SELECT`. Về cơ bản, bạn **chọn** các cột bạn muốn xem **từ** bảng chứa chúng. Nếu bạn muốn hiển thị chỉ tên các thành phố, bạn có thể sử dụng câu lệnh sau:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` là nơi bạn liệt kê các cột, và `FROM` là nơi bạn liệt kê các bảng.

> [NOTE] Cú pháp SQL không phân biệt chữ hoa chữ thường, nghĩa là `select` và `SELECT` có nghĩa giống nhau. Tuy nhiên, tùy thuộc vào loại cơ sở dữ liệu bạn đang sử dụng, các cột và bảng có thể phân biệt chữ hoa chữ thường. Vì vậy, một thực hành tốt là luôn coi mọi thứ trong lập trình như phân biệt chữ hoa chữ thường. Khi viết các truy vấn SQL, quy ước phổ biến là viết các từ khóa bằng chữ hoa.

Câu lệnh trên sẽ hiển thị tất cả các thành phố. Hãy tưởng tượng chúng ta chỉ muốn hiển thị các thành phố ở New Zealand. Chúng ta cần một dạng bộ lọc. Từ khóa SQL cho điều này là `WHERE`, hoặc "nơi điều gì đó đúng".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Kết hợp dữ liệu

Cho đến nay chúng ta đã truy xuất dữ liệu từ một bảng duy nhất. Bây giờ chúng ta muốn kết hợp dữ liệu từ cả **cities** và **rainfall**. Điều này được thực hiện bằng cách *kết hợp* chúng lại với nhau. Bạn sẽ tạo một liên kết giữa hai bảng và ghép các giá trị từ một cột của mỗi bảng.

Trong ví dụ của chúng ta, chúng ta sẽ ghép cột **city_id** trong **rainfall** với cột **city_id** trong **cities**. Điều này sẽ ghép giá trị lượng mưa với thành phố tương ứng. Loại kết hợp mà chúng ta sẽ thực hiện được gọi là *inner join*, nghĩa là nếu bất kỳ hàng nào không khớp với bất kỳ hàng nào từ bảng khác, chúng sẽ không được hiển thị. Trong trường hợp của chúng ta, mỗi thành phố đều có lượng mưa, vì vậy mọi thứ sẽ được hiển thị.

Hãy truy xuất lượng mưa năm 2019 cho tất cả các thành phố của chúng ta.

Chúng ta sẽ thực hiện điều này theo từng bước. Bước đầu tiên là kết hợp dữ liệu lại với nhau bằng cách chỉ định các cột để liên kết - **city_id** như đã nêu trước đó.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Chúng ta đã chỉ định hai cột mà chúng ta muốn, và thực tế rằng chúng ta muốn kết hợp các bảng lại với nhau bằng **city_id**. Bây giờ chúng ta có thể thêm câu lệnh `WHERE` để lọc chỉ năm 2019.

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

Cơ sở dữ liệu quan hệ tập trung vào việc chia thông tin thành nhiều bảng, sau đó được kết hợp lại để hiển thị và phân tích. Điều này cung cấp mức độ linh hoạt cao để thực hiện các tính toán và thao tác dữ liệu. Bạn đã thấy các khái niệm cốt lõi của cơ sở dữ liệu quan hệ, và cách thực hiện kết hợp giữa hai bảng.

## 🚀 Thử thách

Có rất nhiều cơ sở dữ liệu quan hệ có sẵn trên internet. Bạn có thể khám phá dữ liệu bằng cách sử dụng các kỹ năng bạn đã học ở trên.

## Câu hỏi sau bài giảng

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ds/)

## Ôn tập & Tự học

Có nhiều tài nguyên có sẵn trên [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) để bạn tiếp tục khám phá các khái niệm về SQL và cơ sở dữ liệu quan hệ

- [Mô tả các khái niệm về dữ liệu quan hệ](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Bắt đầu truy vấn với Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL là một phiên bản của SQL)
- [Nội dung SQL trên Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Bài tập

[Tiêu đề bài tập](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.