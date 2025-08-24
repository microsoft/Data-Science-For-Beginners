<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4039f1c76548d144a0aee0bf28304ec",
  "translation_date": "2025-08-24T01:21:30+00:00",
  "source_file": "3-Data-Visualization/R/13-meaningful-vizualizations/README.md",
  "language_code": "de"
}
-->
# Erstellung aussagekräftiger Visualisierungen

|![ Sketchnote von [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/13-MeaningfulViz.png)|
|:---:|
| Aussagekräftige Visualisierungen - _Sketchnote von [@nitya](https://twitter.com/nitya)_ |

> "Wenn man Daten lange genug quält, gestehen sie alles." -- [Ronald Coase](https://en.wikiquote.org/wiki/Ronald_Coase)

Eine der grundlegenden Fähigkeiten eines Data Scientists ist die Fähigkeit, eine aussagekräftige Datenvisualisierung zu erstellen, die hilft, Fragen zu beantworten. Bevor Sie Ihre Daten visualisieren, müssen Sie sicherstellen, dass sie bereinigt und vorbereitet wurden, wie Sie es in den vorherigen Lektionen getan haben. Danach können Sie entscheiden, wie Sie die Daten am besten präsentieren.

In dieser Lektion werden Sie Folgendes lernen:

1. Wie man den richtigen Diagrammtyp auswählt  
2. Wie man irreführende Diagramme vermeidet  
3. Wie man mit Farben arbeitet  
4. Wie man Diagramme für bessere Lesbarkeit gestaltet  
5. Wie man animierte oder 3D-Diagrammlösungen erstellt  
6. Wie man eine kreative Visualisierung entwickelt  

## [Quiz vor der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/24)

## Den richtigen Diagrammtyp auswählen

In den vorherigen Lektionen haben Sie mit Matplotlib und Seaborn verschiedene interessante Datenvisualisierungen erstellt. Im Allgemeinen können Sie mit Hilfe dieser Tabelle den [richtigen Diagrammtyp](https://chartio.com/learn/charts/how-to-select-a-data-vizualization/) für die jeweilige Fragestellung auswählen:

| Ziel                          | Empfohlener Diagrammtyp         |
| ----------------------------- | ------------------------------- |
| Datenverläufe über die Zeit zeigen | Liniendiagramm                 |
| Kategorien vergleichen        | Balken-, Kreisdiagramm          |
| Gesamtsummen vergleichen      | Kreis-, gestapeltes Balkendiagramm |
| Beziehungen darstellen        | Streu-, Linien-, Facetten-, Doppelliniendiagramm |
| Verteilungen zeigen           | Streu-, Histogramm-, Boxplot    |
| Proportionen darstellen       | Kreis-, Donut-, Waffeldiagramm  |

> ✅ Je nach Beschaffenheit Ihrer Daten müssen Sie diese möglicherweise von Text in numerische Werte umwandeln, damit ein bestimmtes Diagramm unterstützt wird.

## Irreführung vermeiden

Selbst wenn ein Data Scientist sorgfältig den richtigen Diagrammtyp für die richtigen Daten auswählt, gibt es viele Möglichkeiten, Daten so darzustellen, dass sie eine bestimmte Aussage unterstützen – oft auf Kosten der Datenintegrität. Es gibt zahlreiche Beispiele für irreführende Diagramme und Infografiken!

[![How Charts Lie von Alberto Cairo](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/tornado.png)](https://www.youtube.com/watch?v=oX74Nge8Wkw "How charts lie")

> 🎥 Klicken Sie auf das obige Bild, um einen Vortrag über irreführende Diagramme anzusehen.

Dieses Diagramm kehrt die X-Achse um, um das Gegenteil der Wahrheit darzustellen, basierend auf dem Datum:

![schlechtes Diagramm 1](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/bad-chart-1.png)

[Dieses Diagramm](https://media.firstcoastnews.com/assets/WTLV/images/170ae16f-4643-438f-b689-50d66ca6a8d8/170ae16f-4643-438f-b689-50d66ca6a8d8_1140x641.jpg) ist noch irreführender, da der Blick nach rechts gelenkt wird, um zu schließen, dass die COVID-Fälle in den verschiedenen Landkreisen im Laufe der Zeit zurückgegangen sind. Tatsächlich wurden die Daten jedoch so umgeordnet, dass ein irreführender Abwärtstrend entsteht.

![schlechtes Diagramm 2](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/bad-chart-2.jpg)

Dieses berüchtigte Beispiel verwendet sowohl Farbe als auch eine umgekehrte Y-Achse, um zu täuschen: Statt zu zeigen, dass die Zahl der Waffentoten nach der Verabschiedung waffenfreundlicher Gesetze gestiegen ist, wird der Betrachter getäuscht, das Gegenteil zu glauben:

![schlechtes Diagramm 3](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/bad-chart-3.jpg)

Dieses seltsame Diagramm zeigt, wie Proportionen manipuliert werden können – mit komischem Effekt:

![schlechtes Diagramm 4](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/bad-chart-4.jpg)

Das Vergleichen von Unvergleichbarem ist ein weiterer fragwürdiger Trick. Es gibt eine [wunderbare Website](https://tylervigen.com/spurious-correlations), die 'spurious correlations' zeigt, also 'Fakten', die Dinge wie die Scheidungsrate in Maine und den Margarineverbrauch korrelieren. Eine Reddit-Gruppe sammelt auch die [hässlichen Anwendungen](https://www.reddit.com/r/dataisugly/top/?t=all) von Daten.

Es ist wichtig zu verstehen, wie leicht das Auge durch irreführende Diagramme getäuscht werden kann. Selbst wenn die Absicht des Data Scientists gut ist, kann die Wahl eines ungeeigneten Diagrammtyps, wie z. B. eines Kreisdiagramms mit zu vielen Kategorien, irreführend sein.

## Farbe

Wie im obigen Diagramm zur 'Waffengewalt in Florida' gezeigt, kann Farbe eine zusätzliche Bedeutungsebene in Diagrammen hinzufügen, insbesondere in solchen, die nicht mit Bibliotheken wie ggplot2 und RColorBrewer erstellt wurden, die geprüfte Farbpaletten enthalten. Wenn Sie ein Diagramm manuell erstellen, sollten Sie sich ein wenig mit [Farbtheorie](https://colormatters.com/color-and-design/basic-color-theory) beschäftigen.

> ✅ Beachten Sie bei der Gestaltung von Diagrammen, dass Barrierefreiheit ein wichtiger Aspekt der Visualisierung ist. Einige Ihrer Nutzer könnten farbenblind sein – wird Ihr Diagramm auch für Nutzer mit Sehbehinderungen gut dargestellt?

Seien Sie vorsichtig bei der Auswahl von Farben für Ihr Diagramm, da Farben Bedeutungen vermitteln können, die Sie möglicherweise nicht beabsichtigen. Die 'pink ladies' im obigen 'Höhen'-Diagramm vermitteln eine deutlich 'weibliche' Bedeutung, die zur Absurdität des Diagramms beiträgt.

Während [Farbbedeutungen](https://colormatters.com/color-symbolism/the-meanings-of-colors) in verschiedenen Teilen der Welt unterschiedlich sein können und je nach Farbton variieren, umfassen allgemeine Bedeutungen:

| Farbe  | Bedeutung             |
| ------ | --------------------- |
| rot    | Macht                 |
| blau   | Vertrauen, Loyalität  |
| gelb   | Glück, Vorsicht       |
| grün   | Ökologie, Glück, Neid |
| lila   | Freude                |
| orange | Lebendigkeit          |

Wenn Sie ein Diagramm mit benutzerdefinierten Farben erstellen, stellen Sie sicher, dass Ihre Diagramme sowohl barrierefrei sind als auch die Farben mit der beabsichtigten Bedeutung übereinstimmen.

## Gestaltung von Diagrammen für bessere Lesbarkeit

Diagramme sind nicht aussagekräftig, wenn sie nicht lesbar sind! Nehmen Sie sich einen Moment Zeit, um die Breite und Höhe Ihres Diagramms so zu gestalten, dass es gut zu Ihren Daten passt. Wenn eine Variable (z. B. alle 50 Bundesstaaten) angezeigt werden muss, stellen Sie sie möglichst vertikal auf der Y-Achse dar, um ein horizontal scrollendes Diagramm zu vermeiden.

Beschriften Sie Ihre Achsen, fügen Sie bei Bedarf eine Legende hinzu und bieten Sie Tooltips für ein besseres Verständnis der Daten.

Wenn Ihre Daten textlastig und auf der X-Achse umfangreich sind, können Sie den Text für eine bessere Lesbarkeit schräg stellen. [plot3D](https://cran.r-project.org/web/packages/plot3D/index.html) bietet 3D-Diagramme, wenn Ihre Daten dies unterstützen. Mit dieser Bibliothek können anspruchsvolle Datenvisualisierungen erstellt werden.

![3D-Diagramme](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/3d.png)

## Animation und 3D-Diagramme

Einige der besten Datenvisualisierungen heutzutage sind animiert. Shirley Wu hat beeindruckende Beispiele mit D3 erstellt, wie '[film flowers](http://bl.ocks.org/sxywu/raw/d612c6c653fb8b4d7ff3d422be164a5d/)', bei denen jede Blume eine Visualisierung eines Films darstellt. Ein weiteres Beispiel für den Guardian ist 'bussed out', eine interaktive Erfahrung, die Visualisierungen mit Greensock und D3 kombiniert, um zu zeigen, wie NYC mit Obdachlosen umgeht, indem sie aus der Stadt gebracht werden.

![bussing](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/busing.png)

> "Bussed Out: How America Moves its Homeless" vom [Guardian](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study). Visualisierungen von Nadieh Bremer & Shirley Wu

Auch wenn diese Lektion nicht ausreicht, um diese leistungsstarken Visualisierungsbibliotheken im Detail zu lehren, können Sie mit D3 in einer Vue.js-App experimentieren, um eine Visualisierung des Buches "Gefährliche Liebschaften" als animiertes soziales Netzwerk zu erstellen.

> "Les Liaisons Dangereuses" ist ein Briefroman, der 1782 von Choderlos de Laclos geschrieben wurde. Er erzählt die Geschichte der bösartigen, moralisch bankrotten sozialen Manöver zweier rivalisierender Protagonisten der französischen Aristokratie im späten 18. Jahrhundert, des Vicomte de Valmont und der Marquise de Merteuil. Beide kommen am Ende zu Fall, hinterlassen jedoch erheblichen sozialen Schaden. Der Roman entfaltet sich als eine Reihe von Briefen, die an verschiedene Personen in ihrem Umfeld geschrieben wurden, um Rache zu planen oder einfach nur Ärger zu machen. Erstellen Sie eine Visualisierung dieser Briefe, um die Hauptakteure der Erzählung visuell zu entdecken.

Sie werden eine Web-App fertigstellen, die eine animierte Ansicht dieses sozialen Netzwerks anzeigt. Sie verwendet eine Bibliothek, die entwickelt wurde, um ein [Netzwerk visuell darzustellen](https://github.com/emiliorizzo/vue-d3-network) mit Vue.js und D3. Wenn die App läuft, können Sie die Knoten auf dem Bildschirm verschieben, um die Daten neu anzuordnen.

![liaisons](../../../../../3-Data-Visualization/R/13-meaningful-vizualizations/images/liaisons.png)

## Projekt: Erstellen Sie ein Diagramm, um ein Netzwerk mit D3.js darzustellen

> Dieser Lektionen-Ordner enthält einen `solution`-Ordner, in dem Sie das fertige Projekt als Referenz finden können.

1. Folgen Sie den Anweisungen in der README.md-Datei im Stammordner des Starterpakets. Stellen Sie sicher, dass NPM und Node.js auf Ihrem Computer installiert sind, bevor Sie die Abhängigkeiten Ihres Projekts installieren.

2. Öffnen Sie den Ordner `starter/src`. Dort finden Sie einen `assets`-Ordner mit einer .json-Datei, die alle Briefe des Romans enthält, nummeriert und mit einer 'to'- und 'from'-Annotation versehen.

3. Vervollständigen Sie den Code in `components/Nodes.vue`, um die Visualisierung zu aktivieren. Suchen Sie nach der Methode `createLinks()` und fügen Sie die folgende verschachtelte Schleife hinzu.

Durchlaufen Sie das .json-Objekt, um die 'to'- und 'from'-Daten der Briefe zu erfassen, und erstellen Sie das `links`-Objekt, damit die Visualisierungsbibliothek es verwenden kann:

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

Führen Sie Ihre App über das Terminal aus (`npm run serve`) und genießen Sie die Visualisierung!

## 🚀 Herausforderung

Machen Sie eine Internetrecherche, um irreführende Visualisierungen zu entdecken. Wie täuscht der Autor den Nutzer, und ist dies absichtlich? Versuchen Sie, die Visualisierungen zu korrigieren, um zu zeigen, wie sie aussehen sollten.

## [Quiz nach der Lektion](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/25)

## Rückblick & Selbststudium

Hier sind einige Artikel über irreführende Datenvisualisierungen:

https://gizmodo.com/how-to-lie-with-data-visualization-1563576606

http://ixd.prattsi.org/2017/12/visual-lies-usability-in-deceptive-data-visualizations/

Schauen Sie sich diese interessanten Visualisierungen historischer Objekte und Artefakte an:

https://handbook.pubpub.org/

Lesen Sie diesen Artikel darüber, wie Animationen Ihre Visualisierungen verbessern können:

https://medium.com/@EvanSinar/use-animation-to-supercharge-data-visualization-cd905a882ad4

## Aufgabe

[Erstellen Sie Ihre eigene benutzerdefinierte Visualisierung](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.