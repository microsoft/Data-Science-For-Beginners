<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cfb068050337a36e348debaa502a24fa",
  "translation_date": "2025-09-05T18:10:26+00:00",
  "source_file": "3-Data-Visualization/13-meaningful-visualizations/README.md",
  "language_code": "sk"
}
-->
# Tvorba zmysluplných vizualizácií

|![ Sketchnote od [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Zmysluplné vizualizácie - _Sketchnote od [@nitya](https://twitter.com/nitya)_ |

> "Ak budete mučiť dáta dostatočne dlho, priznajú sa k čomukoľvek" -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Jednou zo základných zručností dátového vedca je schopnosť vytvoriť zmysluplnú vizualizáciu dát, ktorá pomáha odpovedať na otázky, ktoré máte. Predtým, než začnete vizualizovať svoje dáta, je potrebné zabezpečiť, aby boli vyčistené a pripravené, ako ste to robili v predchádzajúcich lekciách. Potom môžete začať rozhodovať, ako najlepšie prezentovať dáta.

V tejto lekcii si prejdete:

1. Ako vybrať správny typ grafu
2. Ako sa vyhnúť klamlivým grafom
3. Ako pracovať s farbami
4. Ako upraviť grafy pre lepšiu čitateľnosť
5. Ako vytvoriť animované alebo 3D grafy
6. Ako vytvoriť kreatívnu vizualizáciu

## [Kvíz pred lekciou](https://ff-quizzes.netlify.app/en/ds/quiz/24)

## Vyberte správny typ grafu

V predchádzajúcich lekciách ste experimentovali s vytváraním rôznych zaujímavých vizualizácií dát pomocou knižníc Matplotlib a Seaborn. Vo všeobecnosti môžete vybrať [správny typ grafu](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) pre otázku, ktorú si kladiete, pomocou tejto tabuľky:

| Potrebujete:               | Mali by ste použiť:            |
| -------------------------- | ------------------------------- |
| Ukázať trendy dát v čase   | Čiarový graf                    |
| Porovnať kategórie         | Stĺpcový, Koláčový graf         |
| Porovnať celkové hodnoty   | Koláčový, Stohovaný stĺpcový    |
| Ukázať vzťahy              | Bodový, Čiarový, Facet, Dual Line |
| Ukázať distribúcie         | Bodový, Histogram, Boxplot      |
| Ukázať proporcie           | Koláčový, Donut, Waffle         |

> ✅ V závislosti od zloženia vašich dát môže byť potrebné previesť ich z textového formátu na numerický, aby ste mohli použiť konkrétny typ grafu.

## Vyhnite sa klamlivým grafom

Aj keď dátový vedec starostlivo vyberie správny graf pre správne dáta, existuje mnoho spôsobov, ako môžu byť dáta prezentované tak, aby podporili určitý názor, často na úkor samotných dát. Existuje veľa príkladov klamlivých grafov a infografík!

[![Ako klamú grafy od Alberta Caira](../../../../3-Data-Visualization/13-meaningful-visualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "Ako klamú grafy")

> 🎥 Kliknite na obrázok vyššie pre konferenčný prejav o klamlivých grafoch

Tento graf otočil os X, aby ukázal opak pravdy, na základe dátumu:

![zlý graf 1](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-1.png)

[Tento graf](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) je ešte klamlivejší, pretože oko je priťahované doprava, aby dospelo k záveru, že počet prípadov COVIDu v rôznych okresoch časom klesol. Ak sa však pozriete bližšie na dátumy, zistíte, že boli preusporiadané, aby vytvorili tento klamlivý klesajúci trend.

![zlý graf 2](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-2.jpg)

Tento notoricky známy príklad používa farbu A otočenú os Y na oklamanie: namiesto záveru, že počet úmrtí na strelné zbrane vzrástol po prijatí legislatívy podporujúcej zbrane, oko je oklamané, aby si myslelo, že opak je pravdou:

![zlý graf 3](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-3.jpg)

Tento zvláštny graf ukazuje, ako môže byť proporcia manipulovaná, a to až do komického efektu:

![zlý graf 4](../../../../3-Data-Visualization/13-meaningful-visualizations/images/bad-chart-4.jpg)

Porovnávanie neporovnateľného je ďalší pochybný trik. Existuje [úžasná webová stránka](https://tylervigen.com/spurious-correlations) venovaná 'falošným koreláciám', ktorá zobrazuje 'fakty' korelujúce veci ako rozvodovosť v Maine a spotrebu margarínu. Skupina na Reddit tiež zbiera [škaredé použitia](https://www.reddit.com/r/dataisugly/top/?t=all) dát.

Je dôležité pochopiť, ako ľahko môže byť oko oklamané klamlivými grafmi. Aj keď je zámer dátového vedca dobrý, výber zlého typu grafu, ako napríklad koláčového grafu s príliš veľa kategóriami, môže byť klamlivý.

## Farba

Ako ste videli na grafe 'Florida gun violence', farba môže poskytnúť ďalšiu vrstvu významu grafom, najmä tým, ktoré nie sú navrhnuté pomocou knižníc ako Matplotlib a Seaborn, ktoré obsahujú rôzne overené farebné knižnice a palety. Ak vytvárate graf ručne, trochu si naštudujte [teóriu farieb](https://colormatters.com/color-and-design/basic-color-theory).

> ✅ Pri navrhovaní grafov si uvedomte, že prístupnosť je dôležitým aspektom vizualizácie. Niektorí vaši používatelia môžu byť farboslepí - zobrazuje sa váš graf dobre pre používateľov so zrakovým postihnutím?

Buďte opatrní pri výbere farieb pre váš graf, pretože farba môže prenášať význam, ktorý ste možno nezamýšľali. 'Ružové dámy' na grafe 'výška' vyššie prenášajú výrazne 'ženský' pridelený význam, ktorý pridáva k bizarnosti samotného grafu.

Zatiaľ čo [význam farieb](https://colormatters.com/color-symbolism/the-meanings-of-colors) môže byť odlišný v rôznych častiach sveta a má tendenciu meniť sa podľa odtieňa, vo všeobecnosti zahŕňa:

| Farba  | Význam              |
| ------ | ------------------- |
| červená| sila                |
| modrá  | dôvera, lojalita    |
| žltá   | šťastie, opatrnosť  |
| zelená | ekológia, šťastie, závisť |
| fialová| šťastie             |
| oranžová| živelnosť          |

Ak máte za úlohu vytvoriť graf s vlastnými farbami, zabezpečte, aby vaše grafy boli prístupné a farba, ktorú vyberiete, zodpovedala významu, ktorý sa snažíte preniesť.

## Úprava grafov pre čitateľnosť

Grafy nie sú zmysluplné, ak nie sú čitateľné! Venujte chvíľu úprave šírky a výšky vášho grafu, aby dobre zodpovedali vašim dátam. Ak je potrebné zobraziť jednu premennú (napríklad všetkých 50 štátov), zobrazte ich vertikálne na osi Y, ak je to možné, aby ste sa vyhli horizontálne posúvanému grafu.

Označte svoje osi, poskytnite legendu, ak je to potrebné, a ponúknite tooltipy pre lepšie pochopenie dát.

Ak sú vaše dáta textové a rozsiahle na osi X, môžete text nakloniť pre lepšiu čitateľnosť. [Matplotlib](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html) ponúka 3D grafy, ak vaše dáta podporujú tento formát. Sofistikované vizualizácie dát je možné vytvoriť pomocou `mpl_toolkits.mplot3d`.

![3D grafy](../../../../3-Data-Visualization/13-meaningful-visualizations/images/3d.png)

## Animácia a 3D zobrazenie grafov

Niektoré z najlepších vizualizácií dát dnes sú animované. Shirley Wu má úžasné vizualizácie vytvorené pomocou D3, ako napríklad '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', kde každá kvetina je vizualizáciou filmu. Ďalší príklad pre Guardian je 'bussed out', interaktívna skúsenosť kombinujúca vizualizácie s Greensock a D3 plus formát článku 'scrollytelling', ktorý ukazuje, ako NYC rieši problém bezdomovcov tým, že ich posiela autobusmi mimo mesta.

![busing](../../../../3-Data-Visualization/13-meaningful-visualizations/images/busing.png)

> "Bussed Out: Ako Amerika presúva svojich bezdomovcov" od [Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Vizualizácie od Nadieh Bremer & Shirley Wu

Aj keď táto lekcia nie je dostatočne podrobná na to, aby vás naučila tieto výkonné knižnice vizualizácií, vyskúšajte si D3 v aplikácii Vue.js pomocou knižnice na zobrazenie vizualizácie knihy "Nebezpečné známosti" ako animovanej sociálnej siete.

> "Les Liaisons Dangereuses" je epistolárny román, alebo román prezentovaný ako séria listov. Napísaný v roku 1782 Choderlosom de Laclosom, rozpráva príbeh zlomyseľných, morálne zbankrotovaných spoločenských manévrov dvoch súperiacich protagonistov francúzskej aristokracie koncom 18. storočia, vikomta de Valmonta a markízy de Merteuil. Obaja nakoniec zahynú, ale nie bez toho, aby spôsobili veľké spoločenské škody. Román sa rozvíja ako séria listov napísaných rôznym ľuďom v ich kruhoch, plánujúcich pomstu alebo jednoducho spôsobujúcich problémy. Vytvorte vizualizáciu týchto listov, aby ste objavili hlavné postavy príbehu vizuálne.

Dokončíte webovú aplikáciu, ktorá zobrazí animovaný pohľad na túto sociálnu sieť. Používa knižnicu, ktorá bola vytvorená na [vizualizáciu siete](https://github.com/emiliorizzo/vue-d3-network) pomocou Vue.js a D3. Keď aplikácia beží, môžete ťahať uzly po obrazovke a presúvať dáta.

![liaisons](../../../../3-Data-Visualization/13-meaningful-visualizations/images/liaisons.png)

## Projekt: Vytvorte graf na zobrazenie siete pomocou D3.js

> Táto zložka lekcie obsahuje zložku `solution`, kde nájdete dokončený projekt na vašu referenciu.

1. Postupujte podľa pokynov v súbore README.md v koreňovom adresári zložky starter. Uistite sa, že máte na svojom počítači nainštalované NPM a Node.js pred inštaláciou závislostí projektu.

2. Otvorte zložku `starter/src`. Nájdete tam zložku `assets`, kde je .json súbor so všetkými listami z románu, očíslovanými, s anotáciou 'to' a 'from'.

3. Dokončite kód v `components/Nodes.vue`, aby ste umožnili vizualizáciu. Nájdite metódu nazvanú `createLinks()` a pridajte nasledujúcu vnorenú slučku.

Prejdite cez objekt .json, aby ste zachytili údaje 'to' a 'from' pre listy a vytvorili objekt `links`, ktorý môže knižnica vizualizácie spotrebovať:

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

Spustite svoju aplikáciu z terminálu (npm run serve) a užite si vizualizáciu!

## 🚀 Výzva

Prejdite si internet a objavte klamlivé vizualizácie. Ako autor klame používateľa a je to úmyselné? Skúste opraviť vizualizácie, aby ste ukázali, ako by mali vyzerať.

## [Kvíz po lekcii](https://ff-quizzes.netlify.app/en/ds/quiz/25)

## Prehľad a samostatné štúdium

Tu sú niektoré články na čítanie o klamlivých vizualizáciách dát:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Pozrite si tieto zaujímavé vizualizácie historických aktív a artefaktov:

https://handbook.pubpub.org/

Prejdite si tento článok o tom, ako animácia môže zlepšiť vaše vizualizácie:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Zadanie

[Vytvorte vlastnú vizualizáciu](assignment.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.