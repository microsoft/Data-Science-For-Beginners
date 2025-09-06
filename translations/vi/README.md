<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5443b88ba402d2ec7b000e4de6cecb8",
  "translation_date": "2025-08-28T17:47:37+00:00",
  "source_file": "README.md",
  "language_code": "vi"
}
-->
# Khoa học Dữ liệu cho Người mới bắt đầu - Một Chương trình Học

Azure Cloud Advocates tại Microsoft rất vui mừng giới thiệu một chương trình học kéo dài 10 tuần, gồm 20 bài học về Khoa học Dữ liệu. Mỗi bài học bao gồm các câu hỏi kiểm tra trước và sau bài học, hướng dẫn chi tiết để hoàn thành bài học, giải pháp và bài tập. Phương pháp học dựa trên dự án của chúng tôi cho phép bạn học thông qua việc thực hành, một cách hiệu quả để các kỹ năng mới được ghi nhớ lâu dài.

**Chân thành cảm ơn các tác giả:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏 Đặc biệt cảm ơn 🙏 các [Đại sứ Sinh viên Microsoft](https://studentambassadors.microsoft.com/) là tác giả, người đánh giá và đóng góp nội dung,** đặc biệt là Aaryan Arora, [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), ChhailBihari Dubey, [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Max Blum](https://www.linkedin.com/in/max-blum-6036a1186/), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Rohit Yadav](https://www.linkedin.com/in/rty2423), Samridhi Sharma, [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [Sheena Narula](https://www.linkedin.com/in/sheena-narua-n/), [Tauqeer Ahmad](https://www.linkedin.com/in/tauqeerahmad5201/), Yogendrasingh Pawar, [Vidushi Gupta](https://www.linkedin.com/in/vidushi-gupta07/), [Jasleen Sondhi](https://www.linkedin.com/in/jasleen-sondhi/)

|![Sketchnote by @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Title.8af36cd35da1ac555b678627fbdc6e320c75f0100876ea41d30ea205d3b08d22.vi.png)|
|:---:|
| Khoa học Dữ liệu cho Người mới bắt đầu - _Sketchnote bởi [@nitya](https://twitter.com/nitya)_ |

### 🌐 Hỗ trợ Đa ngôn ngữ

#### Được hỗ trợ qua GitHub Action (Tự động & Luôn cập nhật)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) | [Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](./README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md) | [Ukrainian](../uk/README.md) | [Burmese (Myanmar)](../my/README.md)

**Nếu bạn muốn có thêm các ngôn ngữ được hỗ trợ, danh sách các ngôn ngữ có sẵn [ở đây](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

#### Tham gia Cộng đồng của Chúng tôi 
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

# Bạn là sinh viên?

Hãy bắt đầu với các tài nguyên sau:

- [Trang Hub Sinh viên](https://docs.microsoft.com/en-gb/learn/student-hub?WT.mc_id=academic-77958-bethanycheum) Tại đây, bạn sẽ tìm thấy các tài nguyên cho người mới bắt đầu, các gói dành cho sinh viên và thậm chí là cách để nhận voucher chứng chỉ miễn phí. Đây là một trang bạn nên đánh dấu và kiểm tra thường xuyên vì nội dung được cập nhật ít nhất hàng tháng.
- [Đại sứ Sinh viên Microsoft](https://studentambassadors.microsoft.com?WT.mc_id=academic-77958-bethanycheum) Tham gia cộng đồng toàn cầu của các đại sứ sinh viên, đây có thể là cơ hội để bạn bước vào Microsoft.

# Bắt đầu

> **Giáo viên**: chúng tôi đã [bao gồm một số gợi ý](for-teachers.md) về cách sử dụng chương trình học này. Chúng tôi rất mong nhận được phản hồi của bạn [trong diễn đàn thảo luận của chúng tôi](https://github.com/microsoft/Data-Science-For-Beginners/discussions)!

> **[Sinh viên](https://aka.ms/student-page)**: để sử dụng chương trình học này một cách độc lập, hãy fork toàn bộ repo và hoàn thành các bài tập theo cách của bạn, bắt đầu với bài kiểm tra trước bài học. Sau đó, đọc bài giảng và hoàn thành các hoạt động còn lại. Hãy cố gắng tạo các dự án bằng cách hiểu bài học thay vì sao chép mã giải pháp; tuy nhiên, mã giải pháp có sẵn trong thư mục /solutions của mỗi bài học dựa trên dự án. Một ý tưởng khác là thành lập nhóm học tập với bạn bè và cùng nhau học qua nội dung. Để học thêm, chúng tôi khuyến nghị [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum).

## Gặp gỡ Đội ngũ

[![Video giới thiệu](../../ds-for-beginners.gif)](https://youtu.be/8mzavjQSMM4 "Video giới thiệu")

**Gif bởi** [Mohit Jaisal](https://www.linkedin.com/in/mohitjaisal)

> 🎥 Nhấp vào hình ảnh trên để xem video về dự án và những người đã tạo ra nó!

## Phương pháp giảng dạy

Chúng tôi đã chọn hai nguyên tắc giảng dạy khi xây dựng chương trình học này: đảm bảo rằng nó dựa trên dự án và bao gồm các câu hỏi kiểm tra thường xuyên. Đến cuối loạt bài này, sinh viên sẽ học được các nguyên tắc cơ bản của khoa học dữ liệu, bao gồm các khái niệm đạo đức, chuẩn bị dữ liệu, các cách làm việc khác nhau với dữ liệu, trực quan hóa dữ liệu, phân tích dữ liệu, các trường hợp sử dụng thực tế của khoa học dữ liệu và nhiều hơn nữa.

Ngoài ra, một bài kiểm tra nhẹ nhàng trước lớp giúp sinh viên tập trung vào việc học một chủ đề, trong khi một bài kiểm tra thứ hai sau lớp đảm bảo sự ghi nhớ lâu dài. Chương trình học này được thiết kế để linh hoạt và thú vị, có thể học toàn bộ hoặc từng phần. Các dự án bắt đầu từ đơn giản và trở nên phức tạp hơn vào cuối chu kỳ 10 tuần.
> Tìm hiểu [Quy tắc ứng xử](CODE_OF_CONDUCT.md), [Hướng dẫn đóng góp](CONTRIBUTING.md), [Hướng dẫn dịch thuật](TRANSLATIONS.md). Chúng tôi rất mong nhận được phản hồi mang tính xây dựng từ bạn!
## Mỗi bài học bao gồm:

- Sketchnote (tùy chọn)
- Video bổ sung (tùy chọn)
- Bài kiểm tra khởi động trước bài học
- Bài học viết
- Đối với các bài học dựa trên dự án, hướng dẫn từng bước để xây dựng dự án
- Kiểm tra kiến thức
- Một thử thách
- Tài liệu đọc bổ sung
- Bài tập
- [Bài kiểm tra sau bài học](https://ff-quizzes.netlify.app/en/)

> **Lưu ý về các bài kiểm tra**: Tất cả các bài kiểm tra được chứa trong thư mục Quiz-App, với tổng cộng 40 bài kiểm tra, mỗi bài gồm ba câu hỏi. Chúng được liên kết từ trong các bài học, nhưng ứng dụng kiểm tra có thể chạy cục bộ hoặc triển khai trên Azure; hãy làm theo hướng dẫn trong thư mục `quiz-app`. Các bài kiểm tra đang dần được bản địa hóa.

## Các bài học

|![ Sketchnote của @sketchthedocs https://sketchthedocs.dev](../../translated_images/00-Roadmap.4905d6567dff47532b9bfb8e0b8980fc6b0b1292eebb24181c1a9753b33bc0f5.vi.png)|
|:---:|
| Khoa học Dữ liệu cho Người mới bắt đầu: Lộ trình - _Sketchnote của [@nitya](https://twitter.com/nitya)_ |

| Số bài học | Chủ đề | Nhóm bài học | Mục tiêu học tập | Liên kết bài học | Tác giả |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 01 | Định nghĩa Khoa học Dữ liệu | [Giới thiệu](1-Introduction/README.md) | Tìm hiểu các khái niệm cơ bản về khoa học dữ liệu và mối liên hệ của nó với trí tuệ nhân tạo, học máy và dữ liệu lớn. | [bài học](1-Introduction/01-defining-data-science/README.md) [video](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 02 | Đạo đức trong Khoa học Dữ liệu | [Giới thiệu](1-Introduction/README.md) | Các khái niệm, thách thức và khung đạo đức dữ liệu. | [bài học](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 03 | Định nghĩa Dữ liệu | [Giới thiệu](1-Introduction/README.md) | Cách phân loại dữ liệu và các nguồn dữ liệu phổ biến. | [bài học](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 04 | Giới thiệu về Thống kê & Xác suất | [Giới thiệu](1-Introduction/README.md) | Các kỹ thuật toán học về xác suất và thống kê để hiểu dữ liệu. | [bài học](1-Introduction/04-stats-and-probability/README.md) [video](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 05 | Làm việc với Dữ liệu Quan hệ | [Làm việc với Dữ liệu](2-Working-With-Data/README.md) | Giới thiệu về dữ liệu quan hệ và các khái niệm cơ bản để khám phá và phân tích dữ liệu quan hệ bằng Ngôn ngữ Truy vấn Có cấu trúc, còn được gọi là SQL (phát âm là “see-quell”). | [bài học](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 06 | Làm việc với Dữ liệu NoSQL | [Làm việc với Dữ liệu](2-Working-With-Data/README.md) | Giới thiệu về dữ liệu phi quan hệ, các loại khác nhau của nó và các khái niệm cơ bản để khám phá và phân tích cơ sở dữ liệu tài liệu. | [bài học](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 07 | Làm việc với Python | [Làm việc với Dữ liệu](2-Working-With-Data/README.md) | Các khái niệm cơ bản về sử dụng Python để khám phá dữ liệu với các thư viện như Pandas. Khuyến nghị có kiến thức cơ bản về lập trình Python. | [bài học](2-Working-With-Data/07-python/README.md) [video](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 08 | Chuẩn bị Dữ liệu | [Làm việc với Dữ liệu](2-Working-With-Data/README.md) | Các chủ đề về kỹ thuật làm sạch và chuyển đổi dữ liệu để xử lý các thách thức như dữ liệu thiếu, không chính xác hoặc không đầy đủ. | [bài học](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 09 | Trực quan hóa Số lượng | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Tìm hiểu cách sử dụng Matplotlib để trực quan hóa dữ liệu về chim 🦆 | [bài học](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| 10 | Trực quan hóa Phân phối Dữ liệu | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Trực quan hóa các quan sát và xu hướng trong một khoảng. | [bài học](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | Trực quan hóa Tỷ lệ | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Trực quan hóa các tỷ lệ phần trăm rời rạc và nhóm. | [bài học](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | Trực quan hóa Mối quan hệ | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Trực quan hóa các kết nối và mối tương quan giữa các tập dữ liệu và các biến của chúng. | [bài học](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | Trực quan hóa Có ý nghĩa | [Trực quan hóa Dữ liệu](3-Data-Visualization/README.md) | Các kỹ thuật và hướng dẫn để làm cho các trực quan hóa của bạn có giá trị trong việc giải quyết vấn đề và cung cấp thông tin chi tiết hiệu quả. | [bài học](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | Giới thiệu về Vòng đời Khoa học Dữ liệu | [Vòng đời](4-Data-Science-Lifecycle/README.md) | Giới thiệu về vòng đời khoa học dữ liệu và bước đầu tiên của nó là thu thập và trích xuất dữ liệu. | [bài học](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | Phân tích | [Vòng đời](4-Data-Science-Lifecycle/README.md) | Giai đoạn này của vòng đời khoa học dữ liệu tập trung vào các kỹ thuật để phân tích dữ liệu. | [bài học](4-Data-Science-Lifecycle/15-analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | Truyền đạt | [Vòng đời](4-Data-Science-Lifecycle/README.md) | Giai đoạn này của vòng đời khoa học dữ liệu tập trung vào việc trình bày các thông tin chi tiết từ dữ liệu theo cách giúp người ra quyết định dễ dàng hiểu hơn. | [bài học](4-Data-Science-Lifecycle/16-communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | Khoa học Dữ liệu trên Đám mây | [Dữ liệu Đám mây](5-Data-Science-In-Cloud/README.md) | Chuỗi bài học này giới thiệu khoa học dữ liệu trên đám mây và các lợi ích của nó. | [bài học](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) và [Maud](https://twitter.com/maudstweets) |
| 18 | Khoa học Dữ liệu trên Đám mây | [Dữ liệu Đám mây](5-Data-Science-In-Cloud/README.md) | Huấn luyện mô hình bằng các công cụ Low Code. |[bài học](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) và [Maud](https://twitter.com/maudstweets) |
| 19 | Khoa học Dữ liệu trên Đám mây | [Dữ liệu Đám mây](5-Data-Science-In-Cloud/README.md) | Triển khai mô hình với Azure Machine Learning Studio. | [bài học](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) và [Maud](https://twitter.com/maudstweets) |
| 20 | Khoa học Dữ liệu trong Thực tế | [Trong Thực tế](6-Data-Science-In-Wild/README.md) | Các dự án khoa học dữ liệu được thúc đẩy trong thế giới thực. | [bài học](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## GitHub Codespaces

Thực hiện các bước sau để mở mẫu này trong Codespace:
1. Nhấp vào menu thả xuống Code và chọn tùy chọn Open with Codespaces.
2. Chọn + New codespace ở cuối bảng.
Để biết thêm thông tin, hãy xem [tài liệu GitHub](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace).

## VSCode Remote - Containers

Thực hiện các bước sau để mở kho lưu trữ này trong một container bằng máy cục bộ của bạn và VSCode với tiện ích mở rộng VS Code Remote - Containers:

1. Nếu đây là lần đầu tiên bạn sử dụng container phát triển, hãy đảm bảo hệ thống của bạn đáp ứng các yêu cầu (ví dụ: đã cài đặt Docker) trong [tài liệu bắt đầu](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started).

Để sử dụng kho lưu trữ này, bạn có thể mở kho lưu trữ trong một volume Docker cách ly:

**Lưu ý**: Ở phía dưới, điều này sẽ sử dụng lệnh Remote-Containers: **Clone Repository in Container Volume...** để sao chép mã nguồn vào một volume Docker thay vì hệ thống tệp cục bộ. [Volumes](https://docs.docker.com/storage/volumes/) là cơ chế được ưu tiên để lưu trữ dữ liệu container.

Hoặc mở một phiên bản đã sao chép hoặc tải xuống cục bộ của kho lưu trữ:

- Sao chép kho lưu trữ này vào hệ thống tệp cục bộ của bạn.
- Nhấn F1 và chọn lệnh **Remote-Containers: Open Folder in Container...**.
- Chọn bản sao đã sao chép của thư mục này, đợi container khởi động và thử nghiệm.

## Truy cập ngoại tuyến

Bạn có thể chạy tài liệu này ngoại tuyến bằng cách sử dụng [Docsify](https://docsify.js.org/#/). Fork kho lưu trữ này, [cài đặt Docsify](https://docsify.js.org/#/quickstart) trên máy cục bộ của bạn, sau đó trong thư mục gốc của kho lưu trữ này, gõ `docsify serve`. Trang web sẽ được phục vụ trên cổng 3000 trên localhost của bạn: `localhost:3000`.

> Lưu ý, các notebook sẽ không được hiển thị qua Docsify, vì vậy khi bạn cần chạy một notebook, hãy thực hiện riêng trong VS Code với kernel Python.

## Các chương trình học khác

Nhóm của chúng tôi sản xuất các chương trình học khác! Hãy xem:

- [Generative AI for Beginners](https://aka.ms/genai-beginners)
- [Generative AI for Beginners .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI with JavaScript](https://github.com/microsoft/generative-ai-with-javascript)
- [Generative AI with Java](https://aka.ms/genaijava)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101) 
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners)
- [Mastering GitHub Copilot for Paired Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.