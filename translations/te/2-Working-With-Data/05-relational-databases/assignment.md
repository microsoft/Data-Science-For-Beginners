<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-12-19T15:50:41+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "te"
}
-->
# విమానాశ్రయ డేటా ప్రదర్శన

మీకు విమానాశ్రయాల గురించి సమాచారం కలిగిన [డేటాబేస్](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) అందించబడింది, ఇది [SQLite](https://sqlite.org/index.html) పై నిర్మించబడింది. స్కీమా క్రింద చూపబడింది. మీరు [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum)లో [SQLite విస్తరణ](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ఉపయోగించి వివిధ నగరాల విమానాశ్రయాల గురించి సమాచారం ప్రదర్శించవచ్చు.

## సూచనలు

అసైన్‌మెంట్ ప్రారంభించడానికి, మీరు కొన్ని దశలను అనుసరించాలి. మీరు కొంత టూలింగ్ ఇన్‌స్టాల్ చేసి నమూనా డేటాబేస్‌ను డౌన్లోడ్ చేసుకోవాలి.

### మీ సిస్టమ్ సెటప్ చేయండి

మీరు Visual Studio Code మరియు SQLite విస్తరణను ఉపయోగించి డేటాబేస్‌తో ఇంటరాక్ట్ చేయవచ్చు.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) కు వెళ్లి Visual Studio Code ఇన్‌స్టాల్ చేయడానికి సూచనలను అనుసరించండి
1. మార్కెట్‌ప్లేస్ పేజీలో సూచించినట్లుగా [SQLite విస్తరణ](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ఇన్‌స్టాల్ చేయండి

### డేటాబేస్ డౌన్లోడ్ చేసి తెరవండి

తర్వాత మీరు డేటాబేస్‌ను డౌన్లోడ్ చేసి తెరవాలి.

1. [GitHub నుండి డేటాబేస్ ఫైల్ డౌన్లోడ్ చేయండి](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) మరియు దాన్ని ఒక డైరెక్టరీలో సేవ్ చేయండి
1. Visual Studio Code తెరవండి
1. **Ctl-Shift-P** (లేదా Mac లో **Cmd-Shift-P**) నొక్కి `SQLite: Open database` టైప్ చేసి SQLite విస్తరణలో డేటాబేస్ తెరవండి
1. **Choose database from file** ఎంచుకుని మీరు ముందుగా డౌన్లోడ్ చేసిన **airports.db** ఫైల్‌ను తెరవండి
1. డేటాబేస్ తెరవబడిన తర్వాత (స్క్రీన్‌లో అప్‌డేట్ కనిపించదు), కొత్త క్వెరీ విండో సృష్టించడానికి **Ctl-Shift-P** (లేదా Mac లో **Cmd-Shift-P**) నొక్కి `SQLite: New query` టైప్ చేయండి

ఒకసారి తెరవబడిన తర్వాత, కొత్త క్వెరీ విండోను డేటాబేస్‌పై SQL స్టేట్మెంట్లు నడపడానికి ఉపయోగించవచ్చు. డేటాబేస్‌పై క్వెరీలు నడపడానికి **Ctl-Shift-Q** (లేదా Mac లో **Cmd-Shift-Q**) ఆదేశాన్ని ఉపయోగించవచ్చు.

> [!NOTE]  
> SQLite విస్తరణ గురించి మరింత సమాచారం కోసం, మీరు [డాక్యుమెంటేషన్](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ను చూడవచ్చు

## డేటాబేస్ స్కీమా

డేటాబేస్ స్కీమా అనేది దాని పట్టిక రూపకల్పన మరియు నిర్మాణం. **airports** డేటాబేస్‌లో రెండు పట్టికలు ఉన్నాయి, `cities`, ఇది యునైటెడ్ కింగ్‌డమ్ మరియు ఐర్లాండ్‌లోని నగరాల జాబితాను కలిగి ఉంది, మరియు `airports`, ఇది అన్ని విమానాశ్రయాల జాబితాను కలిగి ఉంది. కొన్ని నగరాలకు బహుళ విమానాశ్రయాలు ఉండవచ్చు కాబట్టి, సమాచారం నిల్వ చేయడానికి రెండు పట్టికలు సృష్టించబడ్డాయి. ఈ వ్యాయామంలో మీరు వివిధ నగరాల సమాచారం ప్రదర్శించడానికి జాయిన్లను ఉపయోగిస్తారు.

| Cities           |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Airports                         |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## అసైన్‌మెంట్

క్రింది సమాచారాన్ని తిరిగి ఇవ్వడానికి క్వెరీలు సృష్టించండి:

1. `Cities` పట్టికలోని అన్ని నగరాల పేర్లు
1. `Cities` పట్టికలోని ఐర్లాండ్‌లోని అన్ని నగరాలు
1. వారి నగరం మరియు దేశంతో కూడిన అన్ని విమానాశ్రయాల పేర్లు
1. లండన్, యునైటెడ్ కింగ్‌డమ్‌లోని అన్ని విమానాశ్రయాలు

## రూబ్రిక్

| అద్భుతమైన | సరిపడిన | మెరుగుదల అవసరం |
| --------- | -------- | ----------------- |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->