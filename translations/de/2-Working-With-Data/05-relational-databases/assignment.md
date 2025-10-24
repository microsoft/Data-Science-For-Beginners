<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-10-24T09:52:11+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "de"
}
-->
# Anzeigen von Flughafendaten

Ihnen wurde eine [Datenbank](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) auf Basis von [SQLite](https://sqlite.org/index.html) zur Verfügung gestellt, die Informationen über Flughäfen enthält. Das Schema wird unten angezeigt. Sie werden die [SQLite-Erweiterung](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) in [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) verwenden, um Informationen über Flughäfen in verschiedenen Städten anzuzeigen.

## Anweisungen

Um mit der Aufgabe zu beginnen, müssen Sie einige Schritte ausführen. Sie müssen einige Tools installieren und die Beispieldatenbank herunterladen.

### System einrichten

Sie können Visual Studio Code und die SQLite-Erweiterung verwenden, um mit der Datenbank zu interagieren.

1. Gehen Sie zu [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) und folgen Sie den Anweisungen, um Visual Studio Code zu installieren.
1. Installieren Sie die [SQLite-Erweiterung](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum), wie auf der Marketplace-Seite beschrieben.

### Datenbank herunterladen und öffnen

Als Nächstes laden Sie die Datenbank herunter und öffnen sie.

1. Laden Sie die [Datenbankdatei von GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) herunter und speichern Sie sie in einem Verzeichnis.
1. Öffnen Sie Visual Studio Code.
1. Öffnen Sie die Datenbank in der SQLite-Erweiterung, indem Sie **Strg-Shift-P** (oder **Cmd-Shift-P** auf einem Mac) auswählen und `SQLite: Open database` eingeben.
1. Wählen Sie **Choose database from file** und öffnen Sie die **airports.db**-Datei, die Sie zuvor heruntergeladen haben.
1. Nachdem Sie die Datenbank geöffnet haben (es wird keine Aktualisierung auf dem Bildschirm angezeigt), erstellen Sie ein neues Abfragefenster, indem Sie **Strg-Shift-P** (oder **Cmd-Shift-P** auf einem Mac) auswählen und `SQLite: New query` eingeben.

Sobald das neue Abfragefenster geöffnet ist, können Sie SQL-Anweisungen gegen die Datenbank ausführen. Sie können den Befehl **Strg-Shift-Q** (oder **Cmd-Shift-Q** auf einem Mac) verwenden, um Abfragen gegen die Datenbank auszuführen.

> [!NOTE] 
> Weitere Informationen zur SQLite-Erweiterung finden Sie in der [Dokumentation](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum).

## Datenbankschema

Das Schema einer Datenbank ist ihr Tabellenentwurf und ihre Struktur. Die **airports**-Datenbank hat zwei Tabellen, `cities`, die eine Liste von Städten in Großbritannien und Irland enthält, und `airports`, die die Liste aller Flughäfen enthält. Da einige Städte mehrere Flughäfen haben können, wurden zwei Tabellen erstellt, um die Informationen zu speichern. In dieser Übung werden Sie Joins verwenden, um Informationen für verschiedene Städte anzuzeigen.

| Städte            |
| ----------------- |
| id (PK, integer)  |
| city (text)       |
| country (text)    |

| Flughäfen                        |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK zu id in **Cities**) |

## Aufgabe

Erstellen Sie Abfragen, um die folgenden Informationen zurückzugeben:

1. alle Städtenamen in der Tabelle `Cities`
1. alle Städte in Irland in der Tabelle `Cities`
1. alle Flughafennamen mit ihrer Stadt und ihrem Land
1. alle Flughäfen in London, Vereinigtes Königreich

## Bewertungsrichtlinien

| Vorbildlich | Angemessen | Verbesserungswürdig |
| ----------- | ---------- | ------------------- |

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.