<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cad419b574d5c35eaa417e9abfdcb0c8",
  "translation_date": "2025-08-24T01:06:40+00:00",
  "source_file": "3-Data-Visualization/12-visualization-relationships/README.md",
  "language_code": "pl"
}
-->
# Wizualizacja relacji: Wszystko o miodzie 🍯

|![ Sketchnote autorstwa [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/12-Visualizing-Relationships.png)|
|:---:|
|Wizualizacja relacji - _Sketchnote autorstwa [@nitya](https://twitter.com/nitya)_ |

Kontynuując nasz fokus na naturę w badaniach, odkryjmy ciekawe wizualizacje, które pokazują relacje między różnymi rodzajami miodu, zgodnie z danymi pochodzącymi z [Departamentu Rolnictwa Stanów Zjednoczonych](https://www.nass.usda.gov/About_NASS/index.php).

Ten zbiór danych, zawierający około 600 pozycji, przedstawia produkcję miodu w wielu stanach USA. Na przykład można przeanalizować liczbę kolonii, wydajność na kolonię, całkowitą produkcję, zapasy, cenę za funt oraz wartość wyprodukowanego miodu w danym stanie w latach 1998-2012, z jednym wierszem na rok dla każdego stanu.

Ciekawie będzie zwizualizować relację między produkcją danego stanu w danym roku a, na przykład, ceną miodu w tym stanie. Alternatywnie, można zwizualizować relację między wydajnością miodu na kolonię w różnych stanach. Ten zakres lat obejmuje niszczycielski 'CCD' lub 'Colony Collapse Disorder', który po raz pierwszy zaobserwowano w 2006 roku (http://npic.orst.edu/envir/ccd.html), co czyni ten zbiór danych szczególnie interesującym do analizy. 🐝

## [Quiz przed wykładem](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/22)

W tej lekcji możesz użyć biblioteki Seaborn, którą już wcześniej stosowałeś, jako świetnego narzędzia do wizualizacji relacji między zmiennymi. Szczególnie interesująca jest funkcja `relplot` w Seaborn, która umożliwia tworzenie wykresów punktowych i liniowych, szybko wizualizując '[relacje statystyczne](https://seaborn.pydata.org/tutorial/relational.html?highlight=relationships)', co pozwala naukowcom danych lepiej zrozumieć, jak zmienne się ze sobą wiążą.

## Wykresy punktowe

Użyj wykresu punktowego, aby pokazać, jak cena miodu zmieniała się rok po roku w poszczególnych stanach. Seaborn, korzystając z `relplot`, wygodnie grupuje dane stanowe i wyświetla punkty danych zarówno dla danych kategorycznych, jak i liczbowych.

Zacznijmy od zaimportowania danych i biblioteki Seaborn:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
honey = pd.read_csv('../../data/honey.csv')
honey.head()
```
Zauważasz, że dane o miodzie zawierają kilka interesujących kolumn, w tym rok i cenę za funt. Zbadajmy te dane, pogrupowane według stanów USA:

| state | numcol | yieldpercol | totalprod | stocks   | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | -------- | ---------- | --------- | ---- |
| AL    | 16000  | 71          | 1136000   | 159000   | 0.72       | 818000    | 1998 |
| AZ    | 55000  | 60          | 3300000   | 1485000  | 0.64       | 2112000   | 1998 |
| AR    | 53000  | 65          | 3445000   | 1688000  | 0.59       | 2033000   | 1998 |
| CA    | 450000 | 83          | 37350000  | 12326000 | 0.62       | 23157000  | 1998 |
| CO    | 27000  | 72          | 1944000   | 1594000  | 0.7        | 1361000   | 1998 |

Stwórz podstawowy wykres punktowy, aby pokazać relację między ceną za funt miodu a stanem jego pochodzenia. Ustaw oś `y` wystarczająco wysoką, aby wyświetlić wszystkie stany:

```python
sns.relplot(x="priceperlb", y="state", data=honey, height=15, aspect=.5);
```
![scatterplot 1](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter1.png)

Teraz pokaż te same dane z kolorystyką inspirowaną miodem, aby zobrazować, jak cena zmienia się na przestrzeni lat. Możesz to zrobić, dodając parametr 'hue', który pokazuje zmiany rok po roku:

> ✅ Dowiedz się więcej o [paletach kolorów dostępnych w Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html) - wypróbuj piękną tęczową paletę kolorów!

```python
sns.relplot(x="priceperlb", y="state", hue="year", palette="YlOrBr", data=honey, height=15, aspect=.5);
```
![scatterplot 2](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter2.png)

Dzięki tej zmianie kolorystyki widać wyraźnie silny postęp w cenach na przestrzeni lat. Rzeczywiście, jeśli spojrzysz na próbkę danych, aby to zweryfikować (wybierz na przykład stan Arizona), możesz zauważyć wzorzec wzrostu cen rok po roku, z nielicznymi wyjątkami:

| state | numcol | yieldpercol | totalprod | stocks  | priceperlb | prodvalue | year |
| ----- | ------ | ----------- | --------- | ------- | ---------- | --------- | ---- |
| AZ    | 55000  | 60          | 3300000   | 1485000 | 0.64       | 2112000   | 1998 |
| AZ    | 52000  | 62          | 3224000   | 1548000 | 0.62       | 1999000   | 1999 |
| AZ    | 40000  | 59          | 2360000   | 1322000 | 0.73       | 1723000   | 2000 |
| AZ    | 43000  | 59          | 2537000   | 1142000 | 0.72       | 1827000   | 2001 |
| AZ    | 38000  | 63          | 2394000   | 1197000 | 1.08       | 2586000   | 2002 |
| AZ    | 35000  | 72          | 2520000   | 983000  | 1.34       | 3377000   | 2003 |
| AZ    | 32000  | 55          | 1760000   | 774000  | 1.11       | 1954000   | 2004 |
| AZ    | 36000  | 50          | 1800000   | 720000  | 1.04       | 1872000   | 2005 |
| AZ    | 30000  | 65          | 1950000   | 839000  | 0.91       | 1775000   | 2006 |
| AZ    | 30000  | 64          | 1920000   | 902000  | 1.26       | 2419000   | 2007 |
| AZ    | 25000  | 64          | 1600000   | 336000  | 1.26       | 2016000   | 2008 |
| AZ    | 20000  | 52          | 1040000   | 562000  | 1.45       | 1508000   | 2009 |
| AZ    | 24000  | 77          | 1848000   | 665000  | 1.52       | 2809000   | 2010 |
| AZ    | 23000  | 53          | 1219000   | 427000  | 1.55       | 1889000   | 2011 |
| AZ    | 22000  | 46          | 1012000   | 253000  | 1.79       | 1811000   | 2012 |

Innym sposobem wizualizacji tego postępu jest użycie rozmiaru zamiast koloru. Dla osób z daltonizmem może to być lepsza opcja. Zmień swoją wizualizację, aby pokazać wzrost ceny poprzez zwiększenie obwodu punktów:

```python
sns.relplot(x="priceperlb", y="state", size="year", data=honey, height=15, aspect=.5);
```
Widać, że rozmiar punktów stopniowo się zwiększa.

![scatterplot 3](../../../../3-Data-Visualization/12-visualization-relationships/images/scatter3.png)

Czy to prosty przypadek podaży i popytu? Z powodu takich czynników jak zmiany klimatyczne i zanik kolonii, czy dostępność miodu na sprzedaż zmniejsza się rok po roku, a co za tym idzie, cena wzrasta?

Aby odkryć korelację między niektórymi zmiennymi w tym zbiorze danych, przeanalizujmy wykresy liniowe.

## Wykresy liniowe

Pytanie: Czy istnieje wyraźny wzrost ceny miodu za funt rok po roku? Najłatwiej to odkryć, tworząc pojedynczy wykres liniowy:

```python
sns.relplot(x="year", y="priceperlb", kind="line", data=honey);
```
Odpowiedź: Tak, z pewnymi wyjątkami w okolicach roku 2003:

![line chart 1](../../../../3-Data-Visualization/12-visualization-relationships/images/line1.png)

✅ Ponieważ Seaborn agreguje dane wokół jednej linii, wyświetla "wiele pomiarów dla każdej wartości x, rysując średnią i 95% przedział ufności wokół średniej". [Źródło](https://seaborn.pydata.org/tutorial/relational.html). To czasochłonne zachowanie można wyłączyć, dodając `ci=None`.

Pytanie: Cóż, czy w 2003 roku można również zauważyć wzrost podaży miodu? Co jeśli spojrzysz na całkowitą produkcję rok po roku?

```python
sns.relplot(x="year", y="totalprod", kind="line", data=honey);
```

![line chart 2](../../../../3-Data-Visualization/12-visualization-relationships/images/line2.png)

Odpowiedź: Niekoniecznie. Jeśli spojrzysz na całkowitą produkcję, wydaje się, że faktycznie wzrosła w tym konkretnym roku, mimo że ogólnie rzecz biorąc ilość produkowanego miodu maleje w tych latach.

Pytanie: W takim razie, co mogło spowodować ten wzrost ceny miodu w okolicach roku 2003?

Aby to odkryć, możesz przeanalizować siatkę wykresów.

## Siatki wykresów

Siatki wykresów biorą jeden aspekt twojego zbioru danych (w naszym przypadku możesz wybrać 'rok', aby uniknąć zbyt wielu wygenerowanych wykresów). Seaborn może następnie stworzyć wykres dla każdego z tych aspektów, używając wybranych współrzędnych x i y, co ułatwia porównanie. Czy rok 2003 wyróżnia się w tego typu porównaniu?

Stwórz siatkę wykresów, kontynuując użycie `relplot`, zgodnie z zaleceniami [dokumentacji Seaborn](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid#seaborn.FacetGrid).

```python
sns.relplot(
    data=honey, 
    x="yieldpercol", y="numcol",
    col="year", 
    col_wrap=3,
    kind="line"
```
W tej wizualizacji możesz porównać wydajność na kolonię i liczbę kolonii rok po roku, obok siebie, z ustawioną liczbą kolumn na 3:

![facet grid](../../../../3-Data-Visualization/12-visualization-relationships/images/facet.png)

Dla tego zbioru danych nic szczególnego nie wyróżnia się w odniesieniu do liczby kolonii i ich wydajności rok po roku oraz stan po stanie. Czy istnieje inny sposób na znalezienie korelacji między tymi dwoma zmiennymi?

## Wykresy z dwiema liniami

Spróbuj wykresu wieloliniowego, nakładając na siebie dwa wykresy liniowe, używając funkcji 'despine' w Seaborn, aby usunąć górne i prawe osie, oraz `ax.twinx` [pochodzącego z Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html). Twinx pozwala wykresowi dzielić oś x i wyświetlać dwie osie y. Wyświetl wydajność na kolonię i liczbę kolonii, nałożone na siebie:

```python
fig, ax = plt.subplots(figsize=(12,6))
lineplot = sns.lineplot(x=honey['year'], y=honey['numcol'], data=honey, 
                        label = 'Number of bee colonies', legend=False)
sns.despine()
plt.ylabel('# colonies')
plt.title('Honey Production Year over Year');

ax2 = ax.twinx()
lineplot2 = sns.lineplot(x=honey['year'], y=honey['yieldpercol'], ax=ax2, color="r", 
                         label ='Yield per colony', legend=False) 
sns.despine(right=False)
plt.ylabel('colony yield')
ax.figure.legend();
```
![superimposed plots](../../../../3-Data-Visualization/12-visualization-relationships/images/dual-line.png)

Chociaż nic szczególnego nie rzuca się w oczy w okolicach roku 2003, pozwala nam to zakończyć tę lekcję na nieco bardziej optymistycznej nucie: mimo że ogólnie liczba kolonii maleje, liczba kolonii stabilizuje się, nawet jeśli ich wydajność na kolonię spada.

Brawo, pszczoły, brawo!

🐝❤️
## 🚀 Wyzwanie

W tej lekcji dowiedziałeś się nieco więcej o innych zastosowaniach wykresów punktowych i siatek wykresów, w tym siatek wykresów. Podejmij wyzwanie, tworząc siatkę wykresów, używając innego zbioru danych, może takiego, który używałeś wcześniej w tych lekcjach. Zwróć uwagę, jak długo zajmuje ich tworzenie i jak musisz być ostrożny, ile siatek musisz narysować, używając tych technik.
## [Quiz po wykładzie](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/23)

## Przegląd i samodzielna nauka

Wykresy liniowe mogą być proste lub dość złożone. Przeczytaj trochę w [dokumentacji Seaborn](https://seaborn.pydata.org/generated/seaborn.lineplot.html) o różnych sposobach ich budowy. Spróbuj ulepszyć wykresy liniowe, które stworzyłeś w tej lekcji, za pomocą innych metod wymienionych w dokumentacji.
## Zadanie

[Zanurz się w ulu](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.