<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-31T05:40:23+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "lt"
}
-->
# Užduotis duomenų apdorojimui su Python

Šioje užduotyje prašysime jūsų išplėtoti kodą, kurį pradėjome kurti mūsų iššūkiuose. Užduotis susideda iš dviejų dalių:

## COVID-19 plitimo modeliavimas

 - [ ] Nubraižykite *R* grafikus 5-6 skirtingoms šalims viename grafike, kad būtų galima palyginti, arba naudokite kelis grafikus šalia vienas kito.
 - [ ] Išanalizuokite, kaip mirčių ir pasveikimų skaičius koreliuoja su užsikrėtusiųjų skaičiumi.
 - [ ] Išsiaiškinkite, kiek laiko trunka tipinė liga, vizualiai koreliuodami užsikrėtimo ir mirčių rodiklius bei ieškodami tam tikrų anomalijų. Jums gali tekti analizuoti skirtingas šalis, kad tai nustatytumėte.
 - [ ] Apskaičiuokite mirtingumo rodiklį ir kaip jis keičiasi laikui bėgant. *Galbūt norėsite atsižvelgti į ligos trukmę dienomis, kad galėtumėte perkelti vieną laiko seką prieš atlikdami skaičiavimus.*

## COVID-19 mokslinių straipsnių analizė

- [ ] Sukurkite skirtingų vaistų ko-pasirodymo matricą ir pažiūrėkite, kurie vaistai dažnai minimi kartu (t. y. paminėti viename santraukoje). Galite modifikuoti kodą, skirtą ko-pasirodymo matricai kurti vaistams ir diagnozėms.
- [ ] Vizualizuokite šią matricą naudodami šilumos žemėlapį.
- [ ] Papildoma užduotis: vizualizuokite vaistų ko-pasirodymą naudodami [chord diagramą](https://en.wikipedia.org/wiki/Chord_diagram). [Ši biblioteka](https://pypi.org/project/chord/) gali padėti jums nubrėžti chord diagramą.
- [ ] Kita papildoma užduotis: ištraukite skirtingų vaistų dozes (pvz., **400mg** iš *vartokite 400mg chloroquine kasdien*) naudodami reguliarias išraiškas ir sukurkite duomenų rėmelį, kuriame būtų parodytos skirtingos vaistų dozės. **Pastaba**: apsvarstykite skaitines reikšmes, kurios yra arti vaisto pavadinimo tekste.

## Vertinimo kriterijai

Puikiai | Pakankamai | Reikia patobulinimų
--- | --- | -- |
Visos užduotys atliktos, grafiškai iliustruotos ir paaiškintos, įskaitant bent vieną iš dviejų papildomų užduočių | Atlikta daugiau nei 5 užduotys, papildomos užduotys neatliktos arba rezultatai nėra aiškūs | Atlikta mažiau nei 5 (bet daugiau nei 3) užduotys, vizualizacijos nepadeda pademonstruoti esmės

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.