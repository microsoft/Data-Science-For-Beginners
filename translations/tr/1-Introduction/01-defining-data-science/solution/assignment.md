<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8f79b9c0484c35b4f26e8aec7fc4d56",
  "translation_date": "2025-08-28T11:24:53+00:00",
  "source_file": "1-Introduction/01-defining-data-science/solution/assignment.md",
  "language_code": "tr"
}
-->
# Ödev: Veri Bilimi Senaryoları

Bu ilk ödevde, farklı problem alanlarında gerçek hayattaki bir süreç veya problemi düşünmenizi ve Veri Bilimi sürecini kullanarak bunu nasıl geliştirebileceğinizi değerlendirmenizi istiyoruz. Şunları düşünün:

1. Hangi verileri toplayabilirsiniz?
1. Bu verileri nasıl toplarsınız?
1. Veriyi nasıl saklarsınız? Verinin boyutu ne kadar büyük olabilir?
1. Bu verilerden hangi içgörüler elde edilebilir? Verilere dayanarak hangi kararlar alınabilir?

3 farklı problem/süreç düşünmeye çalışın ve her bir problem alanı için yukarıdaki noktaları açıklayın.

İşte düşünmeye başlamanız için bazı problem alanları ve problemler:

1. Veriyi nasıl kullanarak okullardaki çocuklar için eğitim sürecini geliştirebilirsiniz?
1. Veriyi nasıl kullanarak pandemi sırasında aşılamayı kontrol edebilirsiniz?
1. Veriyi nasıl kullanarak işte verimli olduğunuzdan emin olabilirsiniz?

## Talimatlar

Aşağıdaki tabloyu doldurun (gerekirse önerilen problem alanlarını kendi alanlarınızla değiştirin):

| Problem Alanı | Problem | Hangi veriler toplanacak | Veriyi nasıl saklayacağız | Hangi içgörüler/kararlar alınabilir | 
|----------------|---------|--------------------------|---------------------------|-------------------------------------|
| Eğitim | Üniversitede genellikle derslere düşük katılım oluyor ve derslere katılan öğrencilerin sınavlarda daha iyi performans gösterdiği hipotezimiz var. Katılımı teşvik etmek ve hipotezi test etmek istiyoruz. | Katılımı sınıftaki güvenlik kamerası tarafından çekilen fotoğraflar veya sınıftaki öğrenci mobil telefonlarının bluetooth/wifi adreslerini takip ederek izleyebiliriz. Sınav verileri zaten üniversite veritabanında mevcut. | Güvenlik kamerası görüntülerini takip edersek - sınıf sırasında birkaç (5-10) fotoğraf saklamamız gerekir (yapılandırılmamış veri) ve ardından öğrencilerin yüzlerini tanımlamak için yapay zeka kullanırız (veriyi yapılandırılmış forma dönüştürürüz). | Her öğrenci için ortalama katılım verilerini hesaplayabilir ve sınav notlarıyla herhangi bir korelasyon olup olmadığını görebiliriz. Korelasyon hakkında daha fazla bilgiyi [olasılık ve istatistik](../../04-stats-and-probability/README.md) bölümünde konuşacağız. Öğrenci katılımını teşvik etmek için haftalık katılım sıralamasını okul portalında yayınlayabilir ve en yüksek katılıma sahip olanlar arasında ödüller dağıtabiliriz. |
| Aşılama | | | | |
| Verimlilik | | | | |

> *Sadece bir cevabı örnek olarak sağlıyoruz, böylece bu ödevde ne beklendiğini anlayabilirsiniz.*

## Değerlendirme Ölçütleri

Örnek Niteliğinde | Yeterli | Geliştirme Gerekiyor
--- | --- | -- |
Tüm problem alanları için makul veri kaynakları, veri saklama yöntemleri ve olası kararlar/içgörüler belirlenmiş | Çözümün bazı yönleri detaylandırılmamış, veri saklama tartışılmamış, en az 2 problem alanı açıklanmış | Veri çözümünün sadece bazı bölümleri açıklanmış, sadece bir problem alanı ele alınmış.

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.