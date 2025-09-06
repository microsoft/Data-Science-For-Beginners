<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "06bac7959b46b6e8aedcae014278c476",
  "translation_date": "2025-09-05T23:46:14+00:00",
  "source_file": "6-Data-Science-In-Wild/20-Real-World-Examples/README.md",
  "language_code": "vi"
}
-->
# Khoa Học Dữ Liệu Trong Thế Giới Thực

| ![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-RealWorld.png) |
| :--------------------------------------------------------------------------------------------------------------: |
|               Khoa Học Dữ Liệu Trong Thế Giới Thực - _Sketchnote của [@nitya](https://twitter.com/nitya)_               |

Chúng ta gần như đã hoàn thành hành trình học tập này!

Chúng ta đã bắt đầu với các định nghĩa về khoa học dữ liệu và đạo đức, khám phá các công cụ và kỹ thuật phân tích và trực quan hóa dữ liệu, xem xét vòng đời khoa học dữ liệu, và tìm hiểu cách mở rộng và tự động hóa quy trình làm việc khoa học dữ liệu với các dịch vụ điện toán đám mây. Vì vậy, bạn có thể đang tự hỏi: _"Làm thế nào để áp dụng tất cả những kiến thức này vào các bối cảnh thực tế?"_

Trong bài học này, chúng ta sẽ khám phá các ứng dụng thực tế của khoa học dữ liệu trong ngành công nghiệp và đi sâu vào các ví dụ cụ thể trong nghiên cứu, nhân văn số và bền vững. Chúng ta sẽ xem xét các cơ hội dự án cho sinh viên và kết thúc với các tài nguyên hữu ích để giúp bạn tiếp tục hành trình học tập của mình!

## Câu Hỏi Trước Bài Giảng

## [Câu hỏi trước bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/38)

## Khoa Học Dữ Liệu + Ngành Công Nghiệp

Nhờ vào sự dân chủ hóa AI, các nhà phát triển hiện nay dễ dàng hơn trong việc thiết kế và tích hợp các quyết định dựa trên AI và các thông tin chi tiết dựa trên dữ liệu vào trải nghiệm người dùng và quy trình phát triển. Dưới đây là một vài ví dụ về cách khoa học dữ liệu được "ứng dụng" vào các bối cảnh thực tế trong ngành công nghiệp:

 * [Google Flu Trends](https://www.wired.com/2015/10/can-learn-epic-failure-google-flu-trends/) đã sử dụng khoa học dữ liệu để liên kết các thuật ngữ tìm kiếm với xu hướng cúm. Mặc dù cách tiếp cận này có những sai sót, nó đã nâng cao nhận thức về các khả năng (và thách thức) của dự đoán y tế dựa trên dữ liệu.

 * [Dự đoán Tuyến Đường của UPS](https://www.technologyreview.com/2018/11/21/139000/how-ups-uses-ai-to-outsmart-bad-weather/) - giải thích cách UPS sử dụng khoa học dữ liệu và học máy để dự đoán các tuyến đường tối ưu cho việc giao hàng, tính đến điều kiện thời tiết, lưu lượng giao thông, thời hạn giao hàng và nhiều yếu tố khác.

 * [Trực Quan Hóa Tuyến Đường Taxi NYC](http://chriswhong.github.io/nyctaxi/) - dữ liệu thu thập được thông qua [Luật Tự Do Thông Tin](https://chriswhong.com/open-data/foil_nyc_taxi/) đã giúp trực quan hóa một ngày làm việc của các taxi ở NYC, giúp chúng ta hiểu cách họ di chuyển trong thành phố bận rộn, số tiền họ kiếm được, và thời gian của các chuyến đi trong mỗi 24 giờ.

 * [Uber Data Science Workbench](https://eng.uber.com/dsw/) - sử dụng dữ liệu (về địa điểm đón & trả khách, thời gian chuyến đi, tuyến đường ưa thích, v.v.) thu thập từ hàng triệu chuyến đi Uber *hàng ngày* để xây dựng một công cụ phân tích dữ liệu giúp định giá, đảm bảo an toàn, phát hiện gian lận và đưa ra quyết định điều hướng.

 * [Phân Tích Dữ Liệu Trong Thể Thao](https://towardsdatascience.com/scope-of-analytics-in-sports-world-37ed09c39860) - tập trung vào _phân tích dự đoán_ (phân tích đội và cầu thủ - nghĩ đến [Moneyball](https://datasciencedegree.wisconsin.edu/blog/moneyball-proves-importance-big-data-big-ideas/) - và quản lý người hâm mộ) và _trực quan hóa dữ liệu_ (bảng điều khiển đội & người hâm mộ, trò chơi, v.v.) với các ứng dụng như tìm kiếm tài năng, cá cược thể thao và quản lý hàng tồn kho/địa điểm.

 * [Khoa Học Dữ Liệu Trong Ngân Hàng](https://data-flair.training/blogs/data-science-in-banking/) - nhấn mạnh giá trị của khoa học dữ liệu trong ngành tài chính với các ứng dụng từ mô hình rủi ro và phát hiện gian lận, đến phân khúc khách hàng, dự đoán thời gian thực và hệ thống gợi ý. Phân tích dự đoán cũng thúc đẩy các biện pháp quan trọng như [điểm tín dụng](https://dzone.com/articles/using-big-data-and-predictive-analytics-for-credit).

 * [Khoa Học Dữ Liệu Trong Y Tế](https://data-flair.training/blogs/data-science-in-healthcare/) - nhấn mạnh các ứng dụng như hình ảnh y tế (ví dụ: MRI, X-Ray, CT-Scan), gen học (giải trình tự DNA), phát triển thuốc (đánh giá rủi ro, dự đoán thành công), phân tích dự đoán (chăm sóc bệnh nhân & hậu cần cung ứng), theo dõi & phòng ngừa dịch bệnh, v.v.

![Ứng Dụng Khoa Học Dữ Liệu Trong Thế Giới Thực](../../../../6-Data-Science-In-Wild/20-Real-World-Examples/images/data-science-applications.png) Nguồn Hình Ảnh: [Data Flair: 6 Amazing Data Science Applications ](https://data-flair.training/blogs/data-science-applications/)

Hình minh họa các lĩnh vực và ví dụ khác về việc áp dụng các kỹ thuật khoa học dữ liệu. Muốn khám phá thêm các ứng dụng khác? Hãy xem phần [Ôn Tập & Tự Học](../../../../6-Data-Science-In-Wild/20-Real-World-Examples) bên dưới.

## Khoa Học Dữ Liệu + Nghiên Cứu

| ![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Research.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Khoa Học Dữ Liệu & Nghiên Cứu - _Sketchnote của [@nitya](https://twitter.com/nitya)_              |

Trong khi các ứng dụng thực tế thường tập trung vào các trường hợp sử dụng trong ngành công nghiệp ở quy mô lớn, các ứng dụng và dự án _nghiên cứu_ có thể hữu ích từ hai góc độ:

* _cơ hội đổi mới_ - khám phá nguyên mẫu nhanh các khái niệm tiên tiến và thử nghiệm trải nghiệm người dùng cho các ứng dụng thế hệ tiếp theo.
* _thách thức triển khai_ - điều tra các tác hại tiềm ẩn hoặc hậu quả không mong muốn của các công nghệ khoa học dữ liệu trong bối cảnh thực tế.

Đối với sinh viên, các dự án nghiên cứu này có thể cung cấp cả cơ hội học tập và hợp tác, giúp cải thiện sự hiểu biết của bạn về chủ đề, và mở rộng nhận thức cũng như sự tham gia của bạn với những người hoặc nhóm làm việc trong các lĩnh vực quan tâm. Vậy các dự án nghiên cứu trông như thế nào và chúng có thể tạo ra tác động ra sao?

Hãy xem một ví dụ - [Nghiên Cứu Gender Shades của MIT](http://gendershades.org/overview.html) từ Joy Buolamwini (MIT Media Labs) với một [bài báo nghiên cứu nổi bật](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf) đồng tác giả với Timnit Gebru (khi đó tại Microsoft Research) tập trung vào:

 * **Cái gì:** Mục tiêu của dự án nghiên cứu là _đánh giá sự thiên vị trong các thuật toán và tập dữ liệu phân tích khuôn mặt tự động_ dựa trên giới tính và màu da.
 * **Tại sao:** Phân tích khuôn mặt được sử dụng trong các lĩnh vực như thực thi pháp luật, an ninh sân bay, hệ thống tuyển dụng và nhiều lĩnh vực khác - những bối cảnh mà phân loại không chính xác (ví dụ: do thiên vị) có thể gây ra các tác hại kinh tế và xã hội tiềm ẩn cho các cá nhân hoặc nhóm bị ảnh hưởng. Hiểu (và loại bỏ hoặc giảm thiểu) sự thiên vị là chìa khóa để đảm bảo công bằng trong việc sử dụng.
 * **Làm thế nào:** Các nhà nghiên cứu nhận ra rằng các tiêu chuẩn hiện có chủ yếu sử dụng các đối tượng có màu da sáng hơn, và đã tạo ra một tập dữ liệu mới (hơn 1000 hình ảnh) _cân bằng hơn_ về giới tính và màu da. Tập dữ liệu này được sử dụng để đánh giá độ chính xác của ba sản phẩm phân loại giới tính (từ Microsoft, IBM & Face++).

Kết quả cho thấy mặc dù độ chính xác phân loại tổng thể là tốt, nhưng có sự khác biệt đáng kể về tỷ lệ lỗi giữa các nhóm phụ khác nhau - với **sai sót nhận diện giới tính** cao hơn đối với nữ giới hoặc người có màu da tối hơn, cho thấy sự thiên vị.

**Kết Quả Chính:** Nâng cao nhận thức rằng khoa học dữ liệu cần có các _tập dữ liệu đại diện hơn_ (các nhóm phụ cân bằng) và các _nhóm làm việc bao gồm hơn_ (nhiều nền tảng đa dạng) để nhận ra và loại bỏ hoặc giảm thiểu các thiên vị như vậy sớm hơn trong các giải pháp AI. Các nỗ lực nghiên cứu như thế này cũng đóng vai trò quan trọng trong việc nhiều tổ chức định nghĩa các nguyên tắc và thực hành cho _AI có trách nhiệm_ nhằm cải thiện tính công bằng trong các sản phẩm và quy trình AI của họ.

**Muốn tìm hiểu về các nỗ lực nghiên cứu liên quan tại Microsoft?**

* Xem [Dự Án Nghiên Cứu Microsoft](https://www.microsoft.com/research/research-area/artificial-intelligence/?facet%5Btax%5D%5Bmsr-research-area%5D%5B%5D=13556&facet%5Btax%5D%5Bmsr-content-type%5D%5B%5D=msr-project) về Trí Tuệ Nhân Tạo.
* Khám phá các dự án sinh viên từ [Trường Hè Khoa Học Dữ Liệu Microsoft Research](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/).
* Xem dự án [Fairlearn](https://fairlearn.org/) và các sáng kiến [AI Có Trách Nhiệm](https://www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6).

## Khoa Học Dữ Liệu + Nhân Văn

| ![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Humanities.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Khoa Học Dữ Liệu & Nhân Văn Số - _Sketchnote của [@nitya](https://twitter.com/nitya)_              |

Nhân Văn Số [được định nghĩa](https://digitalhumanities.stanford.edu/about-dh-stanford) là "một tập hợp các thực hành và cách tiếp cận kết hợp các phương pháp tính toán với nghiên cứu nhân văn". Các dự án [Stanford](https://digitalhumanities.stanford.edu/projects) như _"tái khởi động lịch sử"_ và _"tư duy thơ ca"_ minh họa mối liên kết giữa [Nhân Văn Số và Khoa Học Dữ Liệu](https://digitalhumanities.stanford.edu/digital-humanities-and-data-science) - nhấn mạnh các kỹ thuật như phân tích mạng, trực quan hóa thông tin, phân tích không gian và văn bản có thể giúp chúng ta xem xét lại các tập dữ liệu lịch sử và văn học để rút ra những hiểu biết và góc nhìn mới.

*Muốn khám phá và mở rộng một dự án trong lĩnh vực này?*

Hãy xem ["Emily Dickinson và Nhịp Điệu Cảm Xúc"](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671) - một ví dụ tuyệt vời từ [Jen Looper](https://twitter.com/jenlooper) đặt câu hỏi làm thế nào chúng ta có thể sử dụng khoa học dữ liệu để xem xét lại thơ ca quen thuộc và đánh giá lại ý nghĩa cũng như đóng góp của tác giả trong các bối cảnh mới. Ví dụ, _chúng ta có thể dự đoán mùa mà một bài thơ được sáng tác bằng cách phân tích giọng điệu hoặc cảm xúc của nó không_ - và điều này nói lên điều gì về trạng thái tinh thần của tác giả trong giai đoạn đó?

Để trả lời câu hỏi đó, chúng ta làm theo các bước của vòng đời khoa học dữ liệu:
 * [`Thu Thập Dữ Liệu`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#acquiring-the-dataset) - để thu thập một tập dữ liệu phù hợp để phân tích. Các lựa chọn bao gồm sử dụng API (ví dụ: [Poetry DB API](https://poetrydb.org/index.html)) hoặc thu thập dữ liệu từ các trang web (ví dụ: [Project Gutenberg](https://www.gutenberg.org/files/12242/12242-h/12242-h.htm)) bằng các công cụ như [Scrapy](https://scrapy.org/).
 * [`Làm Sạch Dữ Liệu`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#clean-the-data) - giải thích cách văn bản có thể được định dạng, làm sạch và đơn giản hóa bằng các công cụ cơ bản như Visual Studio Code và Microsoft Excel.
 * [`Phân Tích Dữ Liệu`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#working-with-the-data-in-a-notebook) - giải thích cách chúng ta có thể nhập tập dữ liệu vào "Notebooks" để phân tích bằng các gói Python (như pandas, numpy và matplotlib) để tổ chức và trực quan hóa dữ liệu.
 * [`Phân Tích Cảm Xúc`](https://gist.github.com/jlooper/ce4d102efd057137bc000db796bfd671#sentiment-analysis-using-cognitive-services) - giải thích cách chúng ta có thể tích hợp các dịch vụ đám mây như Text Analytics, sử dụng các công cụ low-code như [Power Automate](https://flow.microsoft.com/en-us/) cho các quy trình xử lý dữ liệu tự động.

Sử dụng quy trình này, chúng ta có thể khám phá tác động của mùa đối với cảm xúc của các bài thơ, và giúp chúng ta hình thành quan điểm riêng về tác giả. Hãy thử tự mình thực hiện - sau đó mở rộng notebook để đặt các câu hỏi khác hoặc trực quan hóa dữ liệu theo những cách mới!

> Bạn có thể sử dụng một số công cụ trong [Bộ Công Cụ Nhân Văn Số](https://github.com/Digital-Humanities-Toolkit) để theo đuổi các hướng nghiên cứu này.

## Khoa Học Dữ Liệu + Bền Vững

| ![ Sketchnote của [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/20-DataScience-Sustainability.png) |
| :---------------------------------------------------------------------------------------------------------------: |
|              Khoa Học Dữ Liệu & Bền Vững - _Sketchnote của [@nitya](https://twitter.com/nitya)_              |

[Chương Trình Nghị Sự 2030 Vì Phát Triển Bền Vững](https://sdgs.un.org/2030agenda) - được tất cả các thành viên Liên Hợp Quốc thông qua vào năm 2015 - xác định 17 mục tiêu bao gồm các mục tiêu tập trung vào **Bảo Vệ Hành Tinh** khỏi sự suy thoái và tác động của biến đổi khí hậu. Sáng kiến [Bền Vững của Microsoft](https://www.microsoft.com/en-us/sustainability) hỗ trợ các mục tiêu này bằng cách khám phá cách các giải pháp công nghệ có thể hỗ trợ và xây dựng các tương lai bền vững hơn với [trọng tâm vào 4 mục tiêu](https://dev.to/azure/a-visual-guide-to-sustainable-software-engineering-53hh) - trở thành tiêu cực carbon, tích cực nước, không rác thải, và đa dạng sinh học vào năm 2030.

Để giải quyết các thách thức này một cách có quy mô và kịp thời, cần có tư duy quy mô đám mây - và dữ liệu quy mô lớn. Sáng kiến [Máy Tính Hành Tinh](https://planetarycomputer.microsoft.com/) cung cấp 4 thành phần để giúp các nhà khoa học dữ liệu và nhà phát triển trong nỗ lực này:

 * [Danh Mục Dữ Liệu](https://planetarycomputer.microsoft.com/catalog) - với hàng petabyte dữ liệu Hệ Thống Trái Đất (miễn phí & được lưu trữ trên Azure).
 * [API Hành Tinh](https://planetarycomputer.microsoft.com/docs/reference/stac/) - để giúp người dùng tìm kiếm dữ liệu liên quan theo không gian và thời gian.
 * [Hub](https://planetarycomputer.microsoft.com/docs/overview/environment/) - môi trường được quản lý cho các nhà khoa học xử lý các tập dữ liệu địa lý lớn.
 * [Ứng Dụng](https://planetarycomputer.microsoft.com/applications) - trình bày các trường hợp sử dụng & công cụ để có được thông tin chi tiết về bền vững.
**Dự án Planetary Computer hiện đang trong giai đoạn xem trước (tính đến tháng 9 năm 2021)** - đây là cách bạn có thể bắt đầu đóng góp vào các giải pháp bền vững bằng cách sử dụng khoa học dữ liệu.

* [Yêu cầu quyền truy cập](https://planetarycomputer.microsoft.com/account/request) để bắt đầu khám phá và kết nối với các đồng nghiệp.
* [Khám phá tài liệu](https://planetarycomputer.microsoft.com/docs/overview/about) để hiểu các tập dữ liệu và API được hỗ trợ.
* Khám phá các ứng dụng như [Ecosystem Monitoring](https://analytics-lab.org/ecosystemmonitoring/) để tìm cảm hứng cho các ý tưởng ứng dụng.

Hãy suy nghĩ về cách bạn có thể sử dụng trực quan hóa dữ liệu để làm nổi bật hoặc khuếch đại những hiểu biết liên quan đến các lĩnh vực như biến đổi khí hậu và nạn phá rừng. Hoặc suy nghĩ về cách những hiểu biết này có thể được sử dụng để tạo ra các trải nghiệm người dùng mới nhằm thúc đẩy thay đổi hành vi hướng tới lối sống bền vững hơn.

## Khoa học dữ liệu + Sinh viên

Chúng ta đã nói về các ứng dụng thực tế trong ngành công nghiệp và nghiên cứu, đồng thời khám phá các ví dụ ứng dụng khoa học dữ liệu trong nhân văn số và bền vững. Vậy làm thế nào bạn có thể xây dựng kỹ năng và chia sẻ chuyên môn của mình khi là người mới bắt đầu với khoa học dữ liệu?

Dưới đây là một số ví dụ về các dự án khoa học dữ liệu của sinh viên để truyền cảm hứng cho bạn.

 * [Trường hè Khoa học Dữ liệu MSR](https://www.microsoft.com/en-us/research/academic-program/data-science-summer-school/#!projects) với các [dự án](https://github.com/msr-ds3) trên GitHub khám phá các chủ đề như:
    - [Định kiến chủng tộc trong việc sử dụng vũ lực của cảnh sát](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2019-replicating-an-empirical-analysis-of-racial-differences-in-police-use-of-force/) | [Github](https://github.com/msr-ds3/stop-question-frisk)
    - [Độ tin cậy của hệ thống tàu điện ngầm NYC](https://www.microsoft.com/en-us/research/video/data-science-summer-school-2018-exploring-the-reliability-of-the-nyc-subway-system/) | [Github](https://github.com/msr-ds3/nyctransit)
 * [Số hóa Văn hóa Vật chất: Khám phá phân bố kinh tế-xã hội ở Sirkap](https://claremont.maps.arcgis.com/apps/Cascade/index.html?appid=bdf2aef0f45a4674ba41cd373fa23afc) - từ [Ornella Altunyan](https://twitter.com/ornelladotcom) và nhóm tại Claremont, sử dụng [ArcGIS StoryMaps](https://storymaps.arcgis.com/).

## 🚀 Thử thách

Tìm kiếm các bài viết gợi ý các dự án khoa học dữ liệu phù hợp cho người mới bắt đầu - như [50 lĩnh vực chủ đề này](https://www.upgrad.com/blog/data-science-project-ideas-topics-beginners/) hoặc [21 ý tưởng dự án này](https://www.intellspot.com/data-science-project-ideas) hoặc [16 dự án với mã nguồn này](https://data-flair.training/blogs/data-science-project-ideas/) mà bạn có thể phân tích và tái sử dụng. Và đừng quên viết blog về hành trình học tập của bạn và chia sẻ những hiểu biết của bạn với tất cả chúng tôi.

## Câu hỏi kiểm tra sau bài giảng

## [Câu hỏi kiểm tra sau bài giảng](https://ff-quizzes.netlify.app/en/ds/quiz/39)

## Ôn tập & Tự học

Muốn khám phá thêm các trường hợp sử dụng? Dưới đây là một số bài viết liên quan:
 * [17 Ứng dụng và Ví dụ về Khoa học Dữ liệu](https://builtin.com/data-science/data-science-applications-examples) - Tháng 7 năm 2021
 * [11 Ứng dụng Khoa học Dữ liệu Đáng Kinh Ngạc trong Thế Giới Thực](https://myblindbird.com/data-science-applications-real-world/) - Tháng 5 năm 2021
 * [Khoa học Dữ liệu Trong Thế Giới Thực](https://towardsdatascience.com/data-science-in-the-real-world/home) - Bộ sưu tập bài viết
 * Khoa học Dữ liệu Trong: [Giáo dục](https://data-flair.training/blogs/data-science-in-education/), [Nông nghiệp](https://data-flair.training/blogs/data-science-in-agriculture/), [Tài chính](https://data-flair.training/blogs/data-science-in-finance/), [Phim ảnh](https://data-flair.training/blogs/data-science-at-movies/) & nhiều lĩnh vực khác.

## Bài tập

[Khám phá Một Tập Dữ Liệu Planetary Computer](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.