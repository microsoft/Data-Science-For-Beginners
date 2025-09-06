<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-28T10:52:56+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "tr"
}
-->
# Havaalanı verilerini görüntüleme

Size havaalanları hakkında bilgi içeren [SQLite](https://sqlite.org/index.html) üzerine kurulmuş bir [veritabanı](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) sağlandı. Şema aşağıda gösterilmektedir. Farklı şehirlerin havaalanları hakkında bilgi görüntülemek için [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) içindeki [SQLite eklentisini](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) kullanacaksınız.

## Talimatlar

Görevle başlamak için birkaç adımı tamamlamanız gerekecek. Biraz araç kurmanız ve örnek veritabanını indirmeniz gerekecek.

### Sisteminizi kurun

Veritabanı ile etkileşimde bulunmak için Visual Studio Code ve SQLite eklentisini kullanabilirsiniz.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) adresine gidin ve Visual Studio Code'u yüklemek için talimatları izleyin
1. [SQLite eklentisini](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) Marketplace sayfasındaki talimatlara göre yükleyin

### Veritabanını indirin ve açın

Sonraki adımda veritabanını indirip açacaksınız.

1. [GitHub'dan veritabanı dosyasını](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) indirin ve bir dizine kaydedin
1. Visual Studio Code'u açın
1. SQLite eklentisinde veritabanını açmak için **Ctl-Shift-P** (Mac'te **Cmd-Shift-P**) tuşlarına basın ve `SQLite: Open database` yazın
1. **Choose database from file** seçeneğini seçin ve daha önce indirdiğiniz **airports.db** dosyasını açın
1. Veritabanını açtıktan sonra (ekranda bir güncelleme görmeyeceksiniz), yeni bir sorgu penceresi oluşturmak için **Ctl-Shift-P** (Mac'te **Cmd-Shift-P**) tuşlarına basın ve `SQLite: New query` yazın

Açıldıktan sonra, yeni sorgu penceresi veritabanına karşı SQL ifadeleri çalıştırmak için kullanılabilir. Veritabanına karşı sorguları çalıştırmak için **Ctl-Shift-Q** (Mac'te **Cmd-Shift-Q**) komutunu kullanabilirsiniz.

> [!NOTE] SQLite eklentisi hakkında daha fazla bilgi için [dokümantasyonu](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) inceleyebilirsiniz.

## Veritabanı şeması

Bir veritabanının şeması, tablo tasarımı ve yapısıdır. **airports** veritabanı iki tabloya sahiptir: Birleşik Krallık ve İrlanda'daki şehirlerin listesini içeren `cities` ve tüm havaalanlarının listesini içeren `airports`. Bazı şehirlerde birden fazla havaalanı olabileceğinden, bilgiyi depolamak için iki tablo oluşturulmuştur. Bu alıştırmada, farklı şehirler için bilgi görüntülemek amacıyla birleştirmeler kullanacaksınız.

| Şehirler          |
| ------------------ |
| id (PK, integer)   |
| city (text)        |
| country (text)     |

| Havaalanları                     |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (**Şehirler** tablosundaki id'ye FK) |

## Görev

Aşağıdaki bilgileri döndüren sorgular oluşturun:

1. `Cities` tablosundaki tüm şehir isimleri
1. `Cities` tablosundaki İrlanda'daki tüm şehirler
1. Şehir ve ülke bilgileriyle birlikte tüm havaalanı isimleri
1. Londra, Birleşik Krallık'taki tüm havaalanları

## Değerlendirme

| Örnek Çalışma | Yeterli | Geliştirme Gerekiyor |
| ------------- | ------- | -------------------- |

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.