<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f9a704f7494ca2d185ded59ba3da99ef",
  "translation_date": "2025-10-24T09:15:44+00:00",
  "source_file": "README.md",
  "language_code": "vi"
}
-->
# Khoa học Dữ liệu cho Người mới bắt đầu - Chương trình học

Azure Cloud Advocates tại Microsoft rất vui mừng giới thiệu chương trình học kéo dài 10 tuần, gồm 20 bài học về Khoa học Dữ liệu. Mỗi bài học bao gồm các bài kiểm tra trước và sau bài học, hướng dẫn viết để hoàn thành bài học, giải pháp và bài tập. Phương pháp học tập dựa trên dự án cho phép bạn học trong khi thực hành, một cách hiệu quả để kỹ năng mới được ghi nhớ lâu dài.

**Trân trọng cảm ơn các tác giả:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Đặc biệt cảm ơn 🙏 các [Đại sứ Sinh viên Microsoft](https://studentambassadors.microsoft.com/) là tác giả, người đánh giá và đóng góp nội dung,** đặc biệt là Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200),
[Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar , [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.vi.png)|
|:---:|
| Khoa học Dữ liệu cho Người mới bắt đầu - _Sketchnote bởi [@nitya](https://twitter.com/nitya)_ |

### 🌐 Hỗ trợ đa ngôn ngữ

#### Được hỗ trợ qua GitHub Action (Tự động & Luôn cập nhật)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](./README.md)

**Nếu bạn muốn có thêm các ngôn ngữ dịch, danh sách các ngôn ngữ được hỗ trợ có thể tìm thấy [tại đây](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Tham gia cộng đồng của chúng tôi 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://aka.ms/ds4beginners/discord)

Chúng tôi có một chuỗi học tập với AI trên Discord đang diễn ra, tìm hiểu thêm và tham gia cùng chúng tôi tại [Learn with AI Series](https://aka.ms/learnwithai/discord) từ ngày 18 - 30 tháng 9, 2025. Bạn sẽ nhận được mẹo và thủ thuật sử dụng GitHub Copilot cho Khoa học Dữ liệu.

![Learn with AI series](../../translated_images/1.2b28cdc6205e26fef6a21817fe5d83ae8b50fbd0a33e9fed0df05845da5b30b6.vi.jpg)

# Bạn là sinh viên?

Bắt đầu với các tài nguyên sau:

- [Trang Hub Sinh viên](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Trong trang này, bạn sẽ tìm thấy các tài nguyên dành cho người mới bắt đầu, gói dành cho sinh viên và thậm chí là cách nhận voucher chứng chỉ miễn phí. Đây là một trang bạn nên đánh dấu và kiểm tra thường xuyên vì chúng tôi thay đổi nội dung ít nhất hàng tháng.
- [Đại sứ Sinh viên Microsoft Learn](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Tham gia cộng đồng toàn cầu của các đại sứ sinh viên, đây có thể là cách bạn bước vào Microsoft.

# Bắt đầu

## 📚 Tài liệu

- **[Hướng dẫn Cài đặt](INSTALLATION.md)** - Hướng dẫn cài đặt từng bước cho người mới bắt đầu
- **[Hướng dẫn Sử dụng](USAGE.md)** - Ví dụ và quy trình làm việc phổ biến
- **[Khắc phục sự cố](TROUBLESHOOTING.md)** - Giải pháp cho các vấn đề thường gặp
- **[Hướng dẫn Đóng góp](CONTRIBUTING.md)** - Cách đóng góp cho dự án này
- **[Dành cho Giáo viên](for-teachers.md)** - Hướng dẫn giảng dạy và tài nguyên lớp học

## 👨‍🎓 Dành cho Sinh viên
> **Người mới bắt đầu hoàn toàn**: Mới làm quen với khoa học dữ liệu? Bắt đầu với [các ví dụ thân thiện với người mới bắt đầu](examples/README.md)! Những ví dụ đơn giản, được chú thích rõ ràng này sẽ giúp bạn hiểu những điều cơ bản trước khi đi sâu vào chương trình học đầy đủ.
> **[Sinh viên](https://aka.ms/student-page)**: để sử dụng chương trình học này một cách độc lập, hãy sao chép toàn bộ kho lưu trữ và hoàn thành các bài tập theo cách của bạn, bắt đầu với bài kiểm tra trước bài học. Sau đó, đọc bài giảng và hoàn thành các hoạt động còn lại. Hãy cố gắng tạo các dự án bằng cách hiểu bài học thay vì sao chép mã giải pháp; tuy nhiên, mã đó có sẵn trong các thư mục /solutions của mỗi bài học theo hướng dự án. Một ý tưởng khác là tạo nhóm học tập với bạn bè và cùng nhau đi qua nội dung. Để học thêm, chúng tôi khuyến nghị [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum).

**Bắt đầu nhanh:**
1. Kiểm tra [Hướng dẫn Cài đặt](INSTALLATION.md) để thiết lập môi trường của bạn
2. Xem lại [Hướng dẫn Sử dụng](USAGE.md) để học cách làm việc với chương trình học
3. Bắt đầu với Bài học 1 và làm việc theo thứ tự
4. Tham gia cộng đồng [Discord của chúng tôi](https://aka.ms/ds4beginners/discord) để được hỗ trợ

## 👩‍🏫 Dành cho Giáo viên

> **Giáo viên**: chúng tôi đã [bao gồm một số gợi ý](for-teachers.md) về cách sử dụng chương trình học này. Chúng tôi rất mong nhận được phản hồi của bạn [trong diễn đàn thảo luận của chúng tôi](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

## Gặp gỡ đội ngũ

[![Video giới thiệu](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Video giới thiệu")

**Gif bởi** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 Nhấp vào hình ảnh trên để xem video về dự án và những người đã tạo ra nó!

## Phương pháp học tập
Chúng tôi đã chọn hai nguyên tắc giáo dục khi xây dựng chương trình học này: đảm bảo rằng nó dựa trên dự án và bao gồm các bài kiểm tra thường xuyên. Đến cuối loạt bài này, học sinh sẽ học được các nguyên tắc cơ bản của khoa học dữ liệu, bao gồm các khái niệm đạo đức, chuẩn bị dữ liệu, các cách làm việc khác nhau với dữ liệu, trực quan hóa dữ liệu, phân tích dữ liệu, các trường hợp sử dụng thực tế của khoa học dữ liệu, và nhiều hơn nữa.

Ngoài ra, một bài kiểm tra với mức độ áp lực thấp trước buổi học sẽ giúp học sinh định hướng học tập về một chủ đề, trong khi bài kiểm tra thứ hai sau buổi học đảm bảo việc ghi nhớ lâu dài hơn. Chương trình học này được thiết kế linh hoạt và thú vị, có thể học toàn bộ hoặc từng phần. Các dự án bắt đầu từ nhỏ và trở nên phức tạp hơn vào cuối chu kỳ 10 tuần.

> Tìm [Quy tắc ứng xử](CODE_OF_CONDUCT.md), [Hướng dẫn đóng góp](CONTRIBUTING.md), [Hướng dẫn dịch thuật](TRANSLATIONS.md). Chúng tôi hoan nghênh phản hồi mang tính xây dựng của bạn!

## Mỗi bài học bao gồm:

- Ghi chú hình ảnh tùy chọn
- Video bổ sung tùy chọn
- Bài kiểm tra khởi động trước bài học
- Bài học viết
- Đối với các bài học dựa trên dự án, hướng dẫn từng bước về cách xây dựng dự án
- Kiểm tra kiến thức
- Một thử thách
- Đọc thêm tài liệu bổ sung
- Bài tập
- [Bài kiểm tra sau bài học](https://ff-quizzes.netlify.app/en/)

> **Lưu ý về bài kiểm tra**: Tất cả các bài kiểm tra được chứa trong thư mục Quiz-App, với tổng cộng 40 bài kiểm tra, mỗi bài gồm ba câu hỏi. Chúng được liên kết từ trong các bài học, nhưng ứng dụng kiểm tra có thể chạy cục bộ hoặc triển khai lên Azure; làm theo hướng dẫn trong thư mục `quiz-app`. Các bài kiểm tra đang dần được bản địa hóa.

## 🎓 Ví dụ thân thiện với người mới bắt đầu

**Mới làm quen với Khoa học Dữ liệu?** Chúng tôi đã tạo một [thư mục ví dụ](examples/README.md) đặc biệt với mã đơn giản, được chú thích rõ ràng để giúp bạn bắt đầu:

- 🌟 **Hello World** - Chương trình khoa học dữ liệu đầu tiên của bạn
- 📂 **Tải dữ liệu** - Học cách đọc và khám phá các tập dữ liệu
- 📊 **Phân tích đơn giản** - Tính toán thống kê và tìm kiếm các mẫu
- 📈 **Trực quan hóa cơ bản** - Tạo biểu đồ và đồ thị
- 🔬 **Dự án thực tế** - Quy trình hoàn chỉnh từ đầu đến cuối

Mỗi ví dụ đều có các chú thích chi tiết giải thích từng bước, rất phù hợp cho người mới bắt đầu!

👉 **[Bắt đầu với các ví dụ](examples/README.md)** 👈

## Các bài học


|![ Ghi chú hình ảnh của @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.vi.png)|
|:---:|
| Khoa học Dữ liệu cho Người mới bắt đầu: Lộ trình - _Ghi chú hình ảnh của [@nitya](https://twitter.com/nitya)_ |


| Số bài học | Chủ đề | Nhóm bài học | Mục tiêu học tập | Liên kết bài học | Tác giả |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Định nghĩa Khoa học Dữ liệu | [Giới thiệu](1-Introduction/README.md) | Tìm hiểu các khái niệm cơ bản về khoa học dữ liệu và cách nó liên quan đến trí tuệ nhân tạo, học máy, và dữ liệu lớn. | [bài học](1-Introduction/01-defining-data-science/README.md) [video](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Đạo đức Khoa học Dữ liệu | [Giới thiệu](1-Introduction/README.md) | Các khái niệm đạo đức dữ liệu, thách thức và khung làm việc. | [bài học](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Định nghĩa Dữ liệu | [Giới thiệu](1-Introduction/README.md) | Cách phân loại dữ liệu và các nguồn phổ biến của nó. | [bài học](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Giới thiệu về Thống kê & Xác suất | [Giới thiệu](1-Introduction/README.md) | Các kỹ thuật toán học về xác suất và thống kê để hiểu dữ liệu. | [bài học](1-Introduction/04-stats-and-probability/README.md) [video](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Làm việc với Dữ liệu Quan hệ | [Làm việc với Dữ liệu](2-Working-With-Data/README.md) | Giới thiệu về dữ liệu quan hệ và các nguyên tắc cơ bản để khám phá và phân tích dữ liệu quan hệ với Ngôn ngữ Truy vấn Có cấu trúc, còn được gọi là SQL (phát âm là “see-quell”). | [bài học](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | Làm việc với Dữ liệu NoSQL | [Làm việc với Dữ liệu](2-Working-With-Data/README.md) | Giới thiệu về dữ liệu phi quan hệ, các loại khác nhau của nó và các nguyên tắc cơ bản để khám phá và phân tích cơ sở dữ liệu tài liệu. | [bài học](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Làm việc với Python | [Làm việc với Dữ liệu](2-Working-With-Data/README.md) | Các nguyên tắc cơ bản về sử dụng Python để khám phá dữ liệu với các thư viện như Pandas. Hiểu biết cơ bản về lập trình Python được khuyến nghị. | [bài học](2-Working-With-Data/07-python/README.md) [video](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Chuẩn bị Dữ liệu | [Làm việc với Dữ liệu](2-Working-With-Data/README.md) | Các chủ đề về kỹ thuật dữ liệu để làm sạch và chuyển đổi dữ liệu nhằm xử lý các thách thức về dữ liệu thiếu, không chính xác hoặc không đầy đủ. | [bài học](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Trực quan hóa Số lượng | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Học cách sử dụng Matplotlib để trực quan hóa dữ liệu về chim 🦆 | [bài học](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Trực quan hóa Phân bố Dữ liệu | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Trực quan hóa các quan sát và xu hướng trong một khoảng thời gian. | [bài học](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Trực quan hóa Tỷ lệ | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Trực quan hóa các phần trăm riêng lẻ và nhóm. | [bài học](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Trực quan hóa Mối quan hệ | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Trực quan hóa các kết nối và tương quan giữa các tập dữ liệu và các biến của chúng. | [bài học](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Trực quan hóa Có ý nghĩa | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Các kỹ thuật và hướng dẫn để làm cho các trực quan hóa của bạn có giá trị trong việc giải quyết vấn đề và cung cấp thông tin chi tiết hiệu quả. | [bài học](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Giới thiệu về vòng đời Khoa học Dữ liệu | [Vòng đời](4-Data-Science-Lifecycle/README.md) | Giới thiệu về vòng đời khoa học dữ liệu và bước đầu tiên của nó là thu thập và trích xuất dữ liệu. | [bài học](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Phân tích | [Vòng đời](4-Data-Science-Lifecycle/README.md) | Giai đoạn này của vòng đời khoa học dữ liệu tập trung vào các kỹ thuật phân tích dữ liệu. | [bài học](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Giao tiếp | [Vòng đời](4-Data-Science-Lifecycle/README.md) | Giai đoạn này của vòng đời khoa học dữ liệu tập trung vào việc trình bày các thông tin chi tiết từ dữ liệu theo cách giúp người ra quyết định dễ hiểu hơn. | [bài học](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Khoa học Dữ liệu trên Đám mây | [Dữ liệu Đám mây](5-Data-Science-In-Cloud/README.md) | Loạt bài học này giới thiệu về khoa học dữ liệu trên đám mây và các lợi ích của nó. | [bài học](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) và [Maud](https://twitter.com/maudstweets) |
| 18 | Khoa học Dữ liệu trên Đám mây | [Dữ liệu Đám mây](5-Data-Science-In-Cloud/README.md) | Huấn luyện mô hình bằng các công cụ Low Code. |[bài học](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) và [Maud](https://twitter.com/maudstweets) |
| 19 | Khoa học Dữ liệu trên Đám mây | [Dữ liệu Đám mây](5-Data-Science-In-Cloud/README.md) | Triển khai mô hình với Azure Machine Learning Studio. | [bài học](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) và [Maud](https://twitter.com/maudstweets) |
| 20 | Khoa học Dữ liệu trong Thực tế | [Trong Thực tế](6-Data-Science-In-Wild/README.md) | Các dự án khoa học dữ liệu được dẫn dắt bởi dữ liệu trong thế giới thực. | [bài học](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Làm theo các bước sau để mở mẫu này trong Codespace:
1. Nhấp vào menu thả xuống Code và chọn tùy chọn Open with Codespaces.
2. Chọn + New codespace ở dưới cùng của bảng.
Để biết thêm thông tin, hãy xem [tài liệu GitHub](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers
Làm theo các bước sau để mở kho lưu trữ này trong một container bằng máy tính cục bộ của bạn và VSCode sử dụng tiện ích mở rộng VS Code Remote - Containers:

1. Nếu đây là lần đầu tiên bạn sử dụng container phát triển, hãy đảm bảo hệ thống của bạn đáp ứng các yêu cầu trước (ví dụ: đã cài đặt Docker) trong [tài liệu bắt đầu](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

Để sử dụng kho lưu trữ này, bạn có thể mở kho lưu trữ trong một volume Docker độc lập:

**Lưu ý**: Bên dưới, điều này sẽ sử dụng lệnh Remote-Containers: **Clone Repository in Container Volume...** để sao chép mã nguồn trong một volume Docker thay vì hệ thống tệp cục bộ. [Volumes](https://docs.docker.com/storage/volumes/) là cơ chế ưu tiên để lưu trữ dữ liệu container.

Hoặc mở một phiên bản đã sao chép hoặc tải xuống cục bộ của kho lưu trữ:

- Sao chép kho lưu trữ này vào hệ thống tệp cục bộ của bạn.
- Nhấn F1 và chọn lệnh **Remote-Containers: Open Folder in Container...**.
- Chọn bản sao đã sao chép của thư mục này, chờ container khởi động, và thử nghiệm.

## Truy cập ngoại tuyến

Bạn có thể chạy tài liệu này ngoại tuyến bằng cách sử dụng [Docsify](https://docsify.js.org/#/). Fork kho lưu trữ này, [cài đặt Docsify](https://docsify.js.org/#/quickstart) trên máy tính cục bộ của bạn, sau đó trong thư mục gốc của kho lưu trữ này, gõ `docsify serve`. Trang web sẽ được phục vụ trên cổng 3000 trên localhost của bạn: `localhost:3000`.

> Lưu ý, các notebook sẽ không được hiển thị qua Docsify, vì vậy khi bạn cần chạy một notebook, hãy thực hiện riêng trong VS Code với kernel Python.

## Các chương trình học khác

Nhóm của chúng tôi sản xuất các chương trình học khác! Hãy xem:

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP cho Người Mới Bắt Đầu](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Tác Nhân AI cho Người Mới Bắt Đầu](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Chuỗi AI Tạo Sinh  
[![AI Tạo Sinh cho Người Mới Bắt Đầu](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI Tạo Sinh (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![AI Tạo Sinh (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![AI Tạo Sinh (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Học Tập Cốt Lõi  
[![Học Máy cho Người Mới Bắt Đầu](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Khoa Học Dữ Liệu cho Người Mới Bắt Đầu](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI cho Người Mới Bắt Đầu](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![An Ninh Mạng cho Người Mới Bắt Đầu](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Phát Triển Web cho Người Mới Bắt Đầu](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT cho Người Mới Bắt Đầu](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![Phát Triển XR cho Người Mới Bắt Đầu](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Chuỗi Copilot  
[![Copilot cho Lập Trình Đôi AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot cho C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Cuộc Phiêu Lưu Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Nhận Hỗ Trợ  

**Gặp vấn đề?** Hãy kiểm tra [Hướng Dẫn Khắc Phục Sự Cố](TROUBLESHOOTING.md) để tìm giải pháp cho các vấn đề thường gặp.

Nếu bạn gặp khó khăn hoặc có câu hỏi về việc xây dựng ứng dụng AI, hãy tham gia:  

[![Discord Azure AI Foundry](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Nếu bạn có phản hồi về sản phẩm hoặc gặp lỗi trong quá trình xây dựng, hãy truy cập:  

[![Diễn Đàn Nhà Phát Triển Azure AI Foundry](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính xác nhất. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.