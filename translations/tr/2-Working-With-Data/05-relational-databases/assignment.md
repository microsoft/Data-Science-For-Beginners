<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:55:26+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "tr"
}
-->
# Havaalanı Verilerini Görüntüleme

Size havaalanları hakkında bilgi içeren [SQLite](https://sqlite.org/index.html) tabanlı bir [veritabanı](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) sağlandı. Şema aşağıda gösterilmiştir. Farklı şehirlerin havaalanları hakkında bilgi görüntülemek için [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) içindeki [SQLite eklentisini](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) kullanacaksınız.

## Talimatlar

Bu ödeve başlamak için birkaç adımı tamamlamanız gerekecek. Biraz araç kurmanız ve örnek veritabanını indirmeniz gerekiyor.

### Sisteminizi Kurun

Veritabanı ile etkileşimde bulunmak için Visual Studio Code ve SQLite eklentisini kullanabilirsiniz.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) adresine gidin ve Visual Studio Code'u kurma talimatlarını izleyin
1. Marketplace sayfasındaki talimatlara göre [SQLite eklentisini](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) yükleyin

### Veritabanını İndirin ve Açın

Sonraki adımda veritabanını indirip açacaksınız.

1. [GitHub'dan veritabanı dosyasını](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) indirin ve bir dizine kaydedin
1. Visual Studio Code'u açın
1. **Ctl-Shift-P** (Mac'te **Cmd-Shift-P**) tuşlarına basarak ve `SQLite: Open database` yazarak SQLite eklentisinde veritabanını açın
1. **Choose database from file** seçeneğini seçin ve daha önce indirdiğiniz **airports.db** dosyasını açın
1. Veritabanını açtıktan sonra (ekranda bir güncelleme görmeyeceksiniz), **Ctl-Shift-P** (Mac'te **Cmd-Shift-P**) tuşlarına basarak ve `SQLite: New query` yazarak yeni bir sorgu penceresi oluşturun

Açıldıktan sonra, yeni sorgu penceresi veritabanına karşı SQL ifadeleri çalıştırmak için kullanılabilir. Veritabanına karşı sorguları çalıştırmak için **Ctl-Shift-Q** (Mac'te **Cmd-Shift-Q**) komutunu kullanabilirsiniz.

> [!NOTE] 
> SQLite eklentisi hakkında daha fazla bilgi için [belgelere](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) başvurabilirsiniz.

## Veritabanı Şeması

Bir veritabanının şeması, tablo tasarımı ve yapısıdır. **airports** veritabanı, Birleşik Krallık ve İrlanda'daki şehirlerin bir listesini içeren `cities` ve tüm havaalanlarının listesini içeren `airports` olmak üzere iki tabloya sahiptir. Bazı şehirlerde birden fazla havaalanı olabileceğinden, bilgiyi depolamak için iki tablo oluşturulmuştur. Bu alıştırmada, farklı şehirler için bilgi görüntülemek amacıyla birleştirmeler kullanacaksınız.

| Şehirler          |
| ----------------- |
| id (PK, integer)  |
| city (text)       |
| country (text)    |

| Havaalanları                      |
| --------------------------------- |
| id (PK, integer)                  |
| name (text)                       |
| code (text)                       |
| city_id (**Şehirler** tablosundaki id'ye FK) |

## Ödev

Aşağıdaki bilgileri döndüren sorgular oluşturun:

1. `Cities` tablosundaki tüm şehir isimleri
1. `Cities` tablosundaki İrlanda'daki tüm şehirler
1. Şehir ve ülke bilgileriyle birlikte tüm havaalanı isimleri
1. Londra, Birleşik Krallık'taki tüm havaalanları

## Değerlendirme Ölçütü

| Örnek Çalışma | Yeterli | Geliştirme Gerekiyor |
| ------------- | ------- | -------------------- |

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.