<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T17:43:48+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "cs"
}
-->
# Úvod do datové vědy v cloudu

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Datová věda v cloudu: Úvod - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

V této lekci se naučíte základní principy cloudu, zjistíte, proč může být zajímavé využívat cloudové služby pro vaše projekty datové vědy, a podíváme se na několik příkladů projektů datové vědy realizovaných v cloudu.

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Co je cloud?

Cloud, nebo cloud computing, je poskytování široké škály výpočetních služeb na principu „pay-as-you-go“, které jsou hostovány na infrastruktuře přes internet. Mezi služby patří řešení jako úložiště, databáze, sítě, software, analytika a inteligentní služby.

Obvykle rozlišujeme veřejný, soukromý a hybridní cloud následovně:

* Veřejný cloud: veřejný cloud je vlastněn a provozován třetí stranou, poskytovatelem cloudových služeb, který poskytuje své výpočetní zdroje přes internet veřejnosti.
* Soukromý cloud: označuje výpočetní zdroje cloudu používané výhradně jedním podnikem nebo organizací, přičemž služby a infrastruktura jsou spravovány na soukromé síti.
* Hybridní cloud: hybridní cloud je systém, který kombinuje veřejné a soukromé cloudy. Uživatelé si zvolí datové centrum na místě, zatímco umožní, aby data a aplikace běžely na jednom nebo více veřejných cloudech.

Většina služeb cloud computingu spadá do tří kategorií: infrastruktura jako služba (IaaS), platforma jako služba (PaaS) a software jako služba (SaaS).

* Infrastruktura jako služba (IaaS): uživatelé si pronajímají IT infrastrukturu, jako jsou servery a virtuální stroje (VMs), úložiště, sítě, operační systémy.
* Platforma jako služba (PaaS): uživatelé si pronajímají prostředí pro vývoj, testování, doručování a správu softwarových aplikací. Uživatelé se nemusí starat o nastavení nebo správu základní infrastruktury serverů, úložiště, sítí a databází potřebných pro vývoj.
* Software jako služba (SaaS): uživatelé získávají přístup k softwarovým aplikacím přes internet, na vyžádání a obvykle na základě předplatného. Uživatelé se nemusí starat o hosting a správu softwarové aplikace, základní infrastrukturu nebo údržbu, jako jsou aktualizace softwaru a bezpečnostní záplaty.

Mezi největší poskytovatele cloudových služeb patří Amazon Web Services, Google Cloud Platform a Microsoft Azure.

## Proč zvolit cloud pro datovou vědu?

Vývojáři a IT profesionálové si vybírají práci s cloudem z mnoha důvodů, včetně následujících:

* Inovace: můžete pohánět své aplikace integrací inovativních služeb vytvořených poskytovateli cloudu přímo do svých aplikací.
* Flexibilita: platíte pouze za služby, které potřebujete, a můžete si vybrat z široké škály služeb. Obvykle platíte podle potřeby a přizpůsobujete své služby podle svých měnících se potřeb.
* Rozpočet: nemusíte dělat počáteční investice do nákupu hardwaru a softwaru, nastavení a provozu datových center na místě, a můžete platit pouze za to, co používáte.
* Škálovatelnost: vaše zdroje se mohou přizpůsobit potřebám vašeho projektu, což znamená, že vaše aplikace mohou využívat více nebo méně výpočetního výkonu, úložiště a šířky pásma, přizpůsobené externím faktorům v daném okamžiku.
* Produktivita: můžete se soustředit na své podnikání místo trávení času úkoly, které může spravovat někdo jiný, jako je správa datových center.
* Spolehlivost: cloud computing nabízí několik způsobů, jak nepřetržitě zálohovat vaše data, a můžete nastavit plány obnovy po havárii, aby vaše podnikání a služby pokračovaly i v době krize.
* Bezpečnost: můžete využívat politiky, technologie a kontroly, které posilují bezpečnost vašeho projektu.

Toto jsou některé z nejběžnějších důvodů, proč lidé volí cloudové služby. Nyní, když máme lepší pochopení toho, co cloud je a jaké jsou jeho hlavní výhody, podívejme se konkrétněji na práci datových vědců a vývojářů pracujících s daty a na to, jak jim cloud může pomoci s několika výzvami, kterým mohou čelit:

* Ukládání velkého množství dat: místo nákupu, správy a ochrany velkých serverů můžete ukládat svá data přímo v cloudu, s řešeními jako Azure Cosmos DB, Azure SQL Database a Azure Data Lake Storage.
* Provádění integrace dat: integrace dat je zásadní součástí datové vědy, která vám umožňuje přejít od sběru dat k činění rozhodnutí. S integračními službami dat nabízenými v cloudu můžete sbírat, transformovat a integrovat data z různých zdrojů do jednoho datového skladu, například pomocí Data Factory.
* Zpracování dat: zpracování velkého množství dat vyžaduje hodně výpočetního výkonu, a ne každý má přístup k dostatečně výkonným strojům, což je důvod, proč mnoho lidí volí přímo využití obrovského výpočetního výkonu cloudu k provozu a nasazení svých řešení.
* Využívání analytických služeb: cloudové služby jako Azure Synapse Analytics, Azure Stream Analytics a Azure Databricks vám pomohou proměnit vaše data v akční poznatky.
* Využívání služeb strojového učení a datové inteligence: místo začínání od nuly můžete využívat algoritmy strojového učení nabízené poskytovatelem cloudu, například pomocí AzureML. Můžete také využívat kognitivní služby, jako je převod řeči na text, text na řeč, počítačové vidění a další.

## Příklady datové vědy v cloudu

Pojďme si to přiblížit pomocí několika scénářů.

### Analýza sentimentu na sociálních sítích v reálném čase
Začneme scénářem, který je běžně studován lidmi začínajícími se strojovým učením: analýza sentimentu na sociálních sítích v reálném čase.

Řekněme, že provozujete zpravodajský web a chcete využít živá data k pochopení, jaký obsah by mohl vaše čtenáře zajímat. Abyste se o tom dozvěděli více, můžete vytvořit program, který provádí analýzu sentimentu v reálném čase na datech z publikací na Twitteru, na témata, která jsou relevantní pro vaše čtenáře.

Klíčové ukazatele, na které se zaměříte, jsou objem tweetů na konkrétní témata (hashtagy) a sentiment, který je stanoven pomocí analytických nástrojů provádějících analýzu sentimentu kolem specifikovaných témat.

Kroky potřebné k vytvoření tohoto projektu jsou následující:

* Vytvořte událostní centrum pro streamování vstupů, které bude sbírat data z Twitteru.
* Nakonfigurujte a spusťte aplikaci klienta Twitteru, která bude volat Twitter Streaming API.
* Vytvořte úlohu Stream Analytics.
* Určete vstup a dotaz úlohy.
* Vytvořte výstupní cíl a určete výstup úlohy.
* Spusťte úlohu.

Pro zobrazení celého procesu si prohlédněte [dokumentaci](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analýza vědeckých článků
Podívejme se na další příklad projektu vytvořeného [Dmitrym Soshnikovem](http://soshnikov.com), jedním z autorů tohoto kurzu.

Dmitry vytvořil nástroj, který analyzuje články o COVIDu. Přezkoumáním tohoto projektu uvidíte, jak můžete vytvořit nástroj, který extrahuje znalosti z vědeckých článků, získává poznatky a pomáhá výzkumníkům efektivně se orientovat ve velkých kolekcích článků.

Podívejme se na různé kroky použité pro tento projekt:

* Extrakce a předzpracování informací pomocí [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Použití [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) k paralelizaci zpracování.
* Ukládání a dotazování informací pomocí [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Vytvoření interaktivního dashboardu pro průzkum a vizualizaci dat pomocí Power BI.

Pro zobrazení celého procesu navštivte [Dmitryho blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

Jak vidíte, cloudové služby můžeme využívat mnoha způsoby k provádění datové vědy.

## Poznámka pod čarou

Zdroje:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Kvíz po přednášce

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Zadání

[Průzkum trhu](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.