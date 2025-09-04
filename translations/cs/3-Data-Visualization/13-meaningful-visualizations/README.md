<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b380bb6d34102bb061eb41de23d9834",
  "translation_date": "2025-09-04T21:46:01+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "cs"
}
-->
# Vytváření smysluplných vizualizací

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Smysluplné vizualizace - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

> "Pokud budete data mučit dostatečně dlouho, přiznají cokoliv." -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Jednou ze základních dovedností datového vědce je schopnost vytvořit smysluplnou vizualizaci dat, která pomůže odpovědět na otázky, které si kladete. Před vizualizací dat je nutné zajistit, aby byla vyčištěna a připravena, jak jste se naučili v předchozích lekcích. Poté můžete začít rozhodovat, jak nejlépe data prezentovat.

V této lekci si projdete:

1. Jak vybrat správný typ grafu  
2. Jak se vyhnout zavádějícím grafům  
3. Jak pracovat s barvami  
4. Jak stylizovat grafy pro lepší čitelnost  
5. Jak vytvořit animované nebo 3D grafy  
6. Jak vytvořit kreativní vizualizaci  

## [Kvíz před lekcí](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Vyberte správný typ grafu

V předchozích lekcích jste experimentovali s vytvářením různých zajímavých vizualizací dat pomocí knihoven Matplotlib a Seaborn. Obecně můžete vybrat [správný typ grafu](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) pro otázku, kterou si kladete, pomocí této tabulky:

| Potřebujete:               | Použijte:                      |
| -------------------------- | ------------------------------ |
| Ukázat trendy v čase       | Čárový graf                   |
| Porovnat kategorie         | Sloupcový, Koláčový graf      |
| Porovnat celkové hodnoty   | Koláčový, Stohovaný sloupcový |
| Ukázat vztahy              | Bodový, Čárový, Facet, Dual Line |
| Ukázat rozložení           | Bodový, Histogram, Krabicový  |
| Ukázat proporce            | Koláčový, Donut, Waffle       |

> ✅ V závislosti na povaze vašich dat může být nutné převést je z textového formátu na číselný, aby je daný graf podporoval.

## Vyhněte se zavádění

I když datový vědec pečlivě vybere správný graf pro správná data, existuje mnoho způsobů, jak mohou být data prezentována tak, aby podpořila určitý názor, často na úkor samotných dat. Existuje mnoho příkladů zavádějících grafů a infografik!

[![Jak grafy lžou od Alberta Caira](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Jak grafy lžou")

> 🎥 Klikněte na obrázek výše pro konferenční přednášku o zavádějících grafech

Tento graf obrací osu X, aby ukázal opak pravdy na základě data:

![špatný graf 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Tento graf](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) je ještě zavádějící, protože oko je přitahováno doprava, aby dospělo k závěru, že počet případů COVIDu v jednotlivých okresech klesal. Ve skutečnosti, pokud se podíváte pozorně na data, zjistíte, že byla přeuspořádána, aby vytvořila tento zavádějící klesající trend.

![špatný graf 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Tento notoricky známý příklad používá barvy A obrácenou osu Y k oklamání: místo závěru, že počet úmrtí na střelné zbraně vzrostl po přijetí zákonů podporujících zbraně, je oko oklamáno, aby si myslelo opak:

![špatný graf 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Tento podivný graf ukazuje, jak lze manipulovat s proporcemi, a to k humornému efektu:

![špatný graf 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Porovnávání neporovnatelného je další pochybný trik. Existuje [skvělá webová stránka](https://tylervigen.com/spurious-correlations) věnovaná 'falešným korelacím', která ukazuje 'fakta' spojující například rozvodovost v Maine a spotřebu margarínu. Skupina na Redditu také sbírá [ošklivé příklady](https://www.reddit.com/r/dataisugly/top/?t=all) použití dat.

Je důležité pochopit, jak snadno může být oko oklamáno zavádějícími grafy. I když má datový vědec dobré úmysly, volba špatného typu grafu, například koláčového grafu s příliš mnoha kategoriemi, může být zavádějící.

## Barvy

Jak jste viděli na grafu 'Florida gun violence', barvy mohou přidat další vrstvu významu grafům, zejména těm, které nejsou navrženy pomocí knihoven jako Matplotlib a Seaborn, které obsahují různé ověřené barevné palety. Pokud vytváříte graf ručně, věnujte trochu času studiu [teorie barev](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Při navrhování grafů mějte na paměti, že přístupnost je důležitým aspektem vizualizace. Někteří vaši uživatelé mohou být barvoslepí – zobrazuje se váš graf dobře i pro uživatele se zrakovým postižením?

Buďte opatrní při výběru barev pro váš graf, protože barvy mohou nést význam, který jste nezamýšleli. 'Růžové dámy' v grafu výšky výše nesou výrazně 'ženský' význam, který přidává k bizarnosti samotného grafu.

Zatímco [význam barev](https://colormatters.com/color-symbolism/the-meanings-of-colors) se může lišit v různých částech světa a mění se podle jejich odstínu, obecně platí následující významy:

| Barva  | Význam              |
| ------ | ------------------- |
| červená | síla               |
| modrá   | důvěra, loajalita  |
| žlutá   | štěstí, opatrnost  |
| zelená  | ekologie, štěstí, závist |
| fialová | radost             |
| oranžová| energie            |

Pokud máte za úkol vytvořit graf s vlastními barvami, zajistěte, aby vaše grafy byly přístupné a aby barvy odpovídaly významu, který chcete sdělit.

## Stylizace grafů pro čitelnost

Grafy nejsou smysluplné, pokud nejsou čitelné! Věnujte chvíli úpravě šířky a výšky grafu tak, aby odpovídaly vašim datům. Pokud je třeba zobrazit mnoho proměnných (například všech 50 států), zobrazte je vertikálně na ose Y, pokud je to možné, abyste se vyhnuli horizontálnímu posouvání grafu.

Označte osy, poskytněte legendu, pokud je to nutné, a nabídněte popisky pro lepší pochopení dat.

Pokud jsou vaše data textová a na ose X příliš dlouhá, můžete text naklonit pro lepší čitelnost. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) nabízí 3D vykreslování, pokud to vaše data podporují. Sofistikované vizualizace dat lze vytvořit pomocí `mpl_toolkits.mplot3d`.

![3D grafy](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Animace a 3D zobrazení grafů

Některé z nejlepších vizualizací dat dnes jsou animované. Shirley Wu vytvořila úžasné vizualizace pomocí D3, například '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', kde každá květina představuje vizualizaci filmu. Dalším příkladem je projekt pro Guardian 'bussed out', interaktivní zážitek kombinující vizualizace s Greensock a D3 a formát článku 'scrollytelling', který ukazuje, jak NYC řeší problém bezdomovectví tím, že lidi posílá autobusy mimo město.

![busing](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: Jak Amerika přesouvá své bezdomovce" od [Guardianu](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Vizualizace od Nadieh Bremer & Shirley Wu

I když tato lekce není dostatečně podrobná, aby vás naučila používat tyto výkonné knihovny pro vizualizaci, zkuste si práci s D3 v aplikaci Vue.js pomocí knihovny, která zobrazuje vizualizaci knihy "Nebezpečné známosti" jako animovanou sociální síť.

> "Les Liaisons Dangereuses" je epistolární román, tedy román prezentovaný jako série dopisů. Napsal jej v roce 1782 Choderlos de Laclos a vypráví příběh nemorálních intrik dvou protagonistů francouzské aristokracie 18. století, vikomta de Valmont a markýzy de Merteuil. Oba nakonec zahynou, ale ne bez toho, aby způsobili značné společenské škody. Román se odvíjí jako série dopisů psaných různým lidem v jejich kruzích, plánujících pomstu nebo prostě jen způsobujících problémy. Vytvořte vizualizaci těchto dopisů, abyste objevili hlavní postavy příběhu vizuálně.

Dokončíte webovou aplikaci, která zobrazí animovaný pohled na tuto sociální síť. Používá knihovnu vytvořenou pro [vizualizaci sítě](https://github.com/emiliorizzo/vue-d3-network) pomocí Vue.js a D3. Když aplikace běží, můžete uzly na obrazovce přetahovat a měnit uspořádání dat.

![liaisons](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Projekt: Vytvořte graf zobrazující síť pomocí D3.js

> Tato složka lekce obsahuje složku `solution`, kde najdete dokončený projekt pro vaši referenci.

1. Postupujte podle pokynů v souboru README.md v kořenové složce složky starter. Ujistěte se, že máte na svém počítači nainstalované NPM a Node.js před instalací závislostí projektu.

2. Otevřete složku `starter/src`. Najdete zde složku `assets`, kde je .json soubor se všemi dopisy z románu, očíslovanými, s anotacemi 'to' a 'from'.

3. Dokončete kód v `components/Nodes.vue`, abyste umožnili vizualizaci. Najděte metodu nazvanou `createLinks()` a přidejte následující vnořenou smyčku.

Projděte objekt .json, abyste zachytili data 'to' a 'from' pro dopisy a vytvořili objekt `links`, který může knihovna pro vizualizaci zpracovat:

```javascript
//loop through letters
      let f = 0;
      let t = 0;
      for (var i = 0; i < letters.length; i++) {
          for (var j = 0; j < characters.length; j++) {
              
            if (characters[j] == letters[i].from) {
              f = j;
            }
            if (characters[j] == letters[i].to) {
              t = j;
            }
        }
        this.links.push({ sid: f, tid: t });
      }
  ```

Spusťte svou aplikaci z terminálu (npm run serve) a užijte si vizualizaci!

## 🚀 Výzva

Prozkoumejte internet a objevte zavádějící vizualizace. Jak autor klame uživatele a je to záměrné? Zkuste vizualizace opravit, aby ukazovaly, jak by měly vypadat.

## [Kvíz po lekci](https://ff-quizzes.netlify.app/en/ds/)

## Přehled a samostudium

Zde jsou některé články o zavádějících vizualizacích dat:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Podívejte se na tyto zajímavé vizualizace historických aktiv a artefaktů:

https://handbook.pubpub.org/

Projděte si tento článek o tom, jak animace může zlepšit vaše vizualizace:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Zadání

[Vytvořte si vlastní vizualizaci](assignment.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.