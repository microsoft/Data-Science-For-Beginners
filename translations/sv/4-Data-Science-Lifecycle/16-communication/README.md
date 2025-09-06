<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "215a3254ba5a222a57c5bb0192cea8e3",
  "translation_date": "2025-09-06T21:06:46+00:00",
  "source_file": "4-Data-Science-Lifecycle/16-communication/README.md",
  "language_code": "sv"
}
-->
# Livscykeln för Data Science: Kommunikation

|![ Sketchnote av [(@sketchthedocs)](https://sketchthedocs.dev)](../../sketchnotes/16-Communicating.png)|
|:---:|
| Livscykeln för Data Science: Kommunikation - _Sketchnote av [@nitya](https://twitter.com/nitya)_ |

## [Quiz före föreläsningen](https://ff-quizzes.netlify.app/en/ds/quiz/30)

Testa dina kunskaper om vad som kommer att tas upp med quizet ovan!

# Introduktion

### Vad är kommunikation?
Låt oss börja denna lektion med att definiera vad det innebär att kommunicera. **Att kommunicera är att förmedla eller utbyta information.** Information kan vara idéer, tankar, känslor, meddelanden, dolda signaler, data – allt som en **_avsändare_** (någon som skickar information) vill att en **_mottagare_** (någon som tar emot information) ska förstå. I denna lektion kommer vi att referera till avsändare som kommunikatörer och mottagare som publiken.

### Datakommunikation & Berättande
Vi förstår att syftet med kommunikation är att förmedla eller utbyta information. Men när det gäller att kommunicera data bör målet inte bara vara att överföra siffror till din publik. Målet bör vara att berätta en historia som baseras på din data – effektiv datakommunikation och berättande går hand i hand. Din publik kommer troligare att minnas en historia du berättar än en siffra du ger. Senare i denna lektion kommer vi att gå igenom några sätt att använda berättande för att kommunicera din data mer effektivt.

### Typer av kommunikation
Under denna lektion kommer två olika typer av kommunikation att diskuteras: Envägskommunikation och Tvåvägskommunikation.

**Envägskommunikation** sker när en avsändare skickar information till en mottagare utan att få någon feedback eller respons. Vi ser exempel på envägskommunikation varje dag – i massutskick via e-post, när nyheterna rapporterar de senaste händelserna, eller när en TV-reklam berättar varför deras produkt är fantastisk. I dessa fall söker avsändaren inte ett informationsutbyte, utan endast att förmedla eller leverera information.

**Tvåvägskommunikation** sker när alla inblandade parter agerar både som avsändare och mottagare. En avsändare börjar med att kommunicera till en mottagare, och mottagaren ger feedback eller en respons. Tvåvägskommunikation är vad vi traditionellt tänker på när vi pratar om kommunikation. Vi tänker oftast på människor som är engagerade i en konversation – antingen personligen, via telefonsamtal, sociala medier eller textmeddelanden.

När du kommunicerar data kommer det att finnas tillfällen då du använder envägskommunikation (tänk på att presentera på en konferens eller för en stor grupp där frågor inte ställs direkt efteråt) och tillfällen då du använder tvåvägskommunikation (tänk på att använda data för att övertyga några intressenter om att investera, eller för att övertyga en kollega om att tid och resurser bör läggas på att bygga något nytt).

# Effektiv kommunikation

### Dina ansvar som kommunikatör
När du kommunicerar är det ditt jobb att se till att dina mottagare tar till sig den information du vill att de ska ta till sig. När du kommunicerar data vill du inte bara att dina mottagare ska ta till sig siffror, du vill att de ska ta till sig en historia som baseras på din data. En bra datakommunikatör är en bra berättare.

Hur berättar du en historia med data? Det finns oändliga sätt – men nedan är 6 som vi kommer att prata om i denna lektion:
1. Förstå din publik, din kanal och din kommunikationsmetod
2. Börja med slutet i åtanke
3. Närma dig det som en riktig berättelse
4. Använd meningsfulla ord och fraser
5. Använd känslor

Varje strategi förklaras mer i detalj nedan.

### 1. Förstå din publik, din kanal och din kommunikationsmetod
Sättet du kommunicerar med familjemedlemmar är förmodligen annorlunda än sättet du kommunicerar med dina vänner. Du använder förmodligen olika ord och fraser som de personer du pratar med är mer benägna att förstå. Du bör ta samma tillvägagångssätt när du kommunicerar data. Tänk på vem du kommunicerar med. Tänk på deras mål och den kontext de har kring situationen du förklarar för dem.

Du kan förmodligen gruppera majoriteten av din publik inom en kategori. I en artikel från _Harvard Business Review_, “[How to Tell a Story with Data](http://blogs.hbr.org/2013/04/how-to-tell-a-story-with-data/)” identifierar Dell Executive Strategist Jim Stikeleather fem kategorier av publik:

 - **Nybörjare**: första exponeringen för ämnet, men vill inte ha
   överförenkling
 - **Generalist**: medveten om ämnet, men söker en översiktlig förståelse och
   huvudteman
 - **Ledare**: djupgående, handlingsbar förståelse av detaljer och
   samband med tillgång till detaljer
 - **Expert**: mer utforskning och upptäckt och mindre berättande med
   stor detaljrikedom
 - **Chef**: har bara tid att förstå betydelsen och slutsatserna av
   sannolikheter

Dessa kategorier kan informera hur du presenterar data för din publik.

Utöver att tänka på din publiks kategori bör du också överväga kanalen du använder för att kommunicera med din publik. Din metod bör vara något annorlunda om du skriver ett memo eller e-post jämfört med att ha ett möte eller presentera på en konferens.

Att förstå din publik och veta hur du kommer att kommunicera med dem (använda envägskommunikation eller tvåvägskommunikation) är också avgörande.

Om du kommunicerar med en majoritet nybörjare och använder envägskommunikation måste du först utbilda publiken och ge dem rätt kontext. Sedan måste du presentera din data för dem och berätta vad din data betyder och varför den är viktig. I detta fall kan det vara viktigt att fokusera på att skapa klarhet, eftersom din publik inte kommer att kunna ställa några direkta frågor.

Om du kommunicerar med en majoritet ledare och använder tvåvägskommunikation behöver du förmodligen inte utbilda din publik eller ge dem mycket kontext. Du kan förmodligen gå direkt in på att diskutera den data du har samlat in och varför den är viktig. I detta scenario bör du dock fokusera på timing och kontrollera din presentation. När du använder tvåvägskommunikation (särskilt med en ledande publik som söker en "handlingsbar förståelse av detaljer och samband med tillgång till detaljer") kan frågor dyka upp under interaktionen som kan ta diskussionen i en riktning som inte relaterar till den historia du försöker berätta. När detta händer kan du agera och föra diskussionen tillbaka på rätt spår med din historia.

### 2. Börja med slutet i åtanke
Att börja med slutet i åtanke innebär att förstå dina avsedda slutsatser för din publik innan du börjar kommunicera med dem. Att vara genomtänkt kring vad du vill att din publik ska ta med sig i förväg kan hjälpa dig att skapa en historia som din publik kan följa. Att börja med slutet i åtanke är lämpligt för både envägskommunikation och tvåvägskommunikation.

Hur börjar du med slutet i åtanke? Innan du kommunicerar din data, skriv ner dina nyckelslutsatser. Sedan, varje steg på vägen när du förbereder den historia du vill berätta med din data, fråga dig själv, "Hur integreras detta i den historia jag berättar?"

Var medveten – även om det är idealiskt att börja med slutet i åtanke, vill du inte bara kommunicera den data som stöder dina avsedda slutsatser. Att göra detta kallas Cherry-Picking, vilket händer när en kommunikatör endast kommunicerar data som stöder den poäng de försöker göra och ignorerar all annan data.

Om all data du samlat in tydligt stöder dina avsedda slutsatser, fantastiskt. Men om det finns data som du samlat in som inte stöder dina slutsatser, eller till och med stöder ett argument mot dina nyckelslutsatser, bör du kommunicera den datan också. Om detta händer, var ärlig med din publik och låt dem veta varför du väljer att hålla fast vid din historia även om all data inte nödvändigtvis stöder den.

### 3. Närma dig det som en riktig berättelse
En traditionell berättelse sker i 5 faser. Du kanske har hört dessa faser uttryckas som Exposition, Rising Action, Climax, Falling Action och Denouement. Eller de lättare att komma ihåg: Kontext, Konflikt, Klimax, Avslutning, Slutsats. När du kommunicerar din data och din historia kan du ta en liknande metod.

Du kan börja med kontext, sätta scenen och se till att din publik är på samma sida. Sedan introducerar du konflikten. Varför behövde du samla in denna data? Vilka problem försökte du lösa? Därefter klimax. Vad är datan? Vad betyder datan? Vilka lösningar säger datan att vi behöver? Sedan kommer du till avslutningen, där du kan upprepa problemet och de föreslagna lösningarna. Slutligen kommer vi till slutsatsen, där du kan sammanfatta dina nyckelslutsatser och de nästa steg du rekommenderar att teamet tar.

### 4. Använd meningsfulla ord och fraser
Om du och jag arbetade tillsammans på en produkt, och jag sa till dig "Våra användare tar lång tid att registrera sig på vår plattform," hur lång tid skulle du uppskatta att "lång tid" är? En timme? En vecka? Det är svårt att veta. Vad om jag sa det till en hel publik? Alla i publiken kan sluta med olika idéer om hur lång tid det tar för användare att registrera sig på vår plattform.

Istället, vad om jag sa "Våra användare tar i genomsnitt 3 minuter att registrera sig och komma igång på vår plattform."

Det budskapet är tydligare. När du kommunicerar data kan det vara lätt att tro att alla i din publik tänker precis som du. Men det är inte alltid fallet. Att skapa klarhet kring din data och vad den betyder är ett av dina ansvar som kommunikatör. Om datan eller din historia inte är tydlig kommer din publik att ha svårt att följa, och det är mindre sannolikt att de förstår dina nyckelslutsatser.

Du kan kommunicera data mer tydligt när du använder meningsfulla ord och fraser istället för vaga. Nedan är några exempel.

 - Vi hade ett *imponerande* år!
	 - En person kan tro att ett imponerande år innebär en ökning av intäkterna med 2% - 3%, och en annan person kan tro att det innebär en ökning med 50% - 60%.
 - Våra användares framgångsgrad ökade *dramatiskt*.
	 - Hur stor ökning är en dramatisk ökning?
 - Detta projekt kommer att kräva *betydande* ansträngning.
	 - Hur mycket ansträngning är betydande?

Att använda vaga ord kan vara användbart som en introduktion till mer data som kommer, eller som en sammanfattning av den historia du just berättat. Men överväg att säkerställa att varje del av din presentation är tydlig för din publik.

### 5. Använd känslor
Känslor är nyckeln i berättande. Det är ännu viktigare när du berättar en historia med data. När du kommunicerar data är allt fokuserat på de slutsatser du vill att din publik ska ha. När du väcker en känsla hos en publik hjälper det dem att känna empati och gör dem mer benägna att agera. Känslor ökar också sannolikheten att en publik kommer att minnas ditt budskap.

Du kanske har stött på detta tidigare med TV-reklamer. Vissa reklamer är mycket allvarsamma och använder en sorglig känsla för att ansluta till sin publik och göra den data de presenterar verkligen framträdande. Eller, vissa reklamer är mycket glada och positiva och kan få dig att associera deras data med en lycklig känsla.

Hur använder du känslor när du kommunicerar data? Nedan är några sätt.

 - Använd vittnesmål och personliga berättelser
	 - När du samlar in data, försök att samla in både kvantitativ och kvalitativ data, och integrera båda typerna av data när du kommunicerar. Om din data är främst kvantitativ, sök berättelser från individer för att lära dig mer om deras erfarenheter med det som din data berättar.
 - Använd bilder
	 - Bilder hjälper en publik att se sig själva i en situation. När du använder bilder kan du styra en publik mot den känsla du tycker att de ska ha om din data.
 - Använd färg
	 - Olika färger väcker olika känslor. Populära färger och de känslor de väcker är nedan. Var medveten om att färger kan ha olika betydelser i olika kulturer.
		 - Blå väcker vanligtvis känslor av lugn och tillit
		 - Grön är vanligtvis relaterad till natur och miljö
		 - Röd är vanligtvis passion och spänning
		 - Gul är vanligtvis optimism och glädje

# Fallstudie: Kommunikation
Emerson är produktchef för en mobilapp. Emerson har märkt att kunder skickar in 42% fler klagomål och buggrapporter under helgerna. Emerson har också märkt att kunder som skickar in ett klagomål som förblir obesvarat efter 48 timmar är 32% mer benägna att ge appen ett betyg på 1 eller 2 i appbutiken.

Efter att ha gjort forskning har Emerson ett par lösningar som kommer att adressera problemet. Emerson bokar ett 30-minuters möte med de tre företagsledarna för att kommunicera datan och de föreslagna lösningarna.

Under detta möte är Emersons mål att få företagsledarna att förstå att de två lösningarna nedan kan förbättra appens betyg, vilket sannolikt kommer att översättas till högre intäkter.

**Lösning 1.** Anställa kundtjänstmedarbetare som arbetar på helger

**Lösning 2.** Köpa ett nytt system för kundtjänstärenden där kundtjänstmedarbetare enkelt kan identifiera vilka klagomål som har varit i kön längst – så att de kan se vilka som ska hanteras mest omedelbart.

Under mötet spenderar Emerson 5 minuter på att förklara varför det är dåligt att ha ett lågt betyg i appbutiken, 10 minuter på att förklara forskningsprocessen och hur trenderna identifierades, 10 minuter på att gå igenom några av de senaste kundklagomålen, och de sista 5 minuterna på att snabbt gå igenom de två potentiella lösningarna.
Var detta ett effektivt sätt för Emerson att kommunicera under detta möte?

Under mötet fokuserade en företagsledare enbart på de 10 minuter av kundklagomål som Emerson gick igenom. Efter mötet var dessa klagomål det enda som denna ledare kom ihåg. En annan företagsledare fokuserade främst på Emersons beskrivning av forskningsprocessen. Den tredje företagsledaren kom ihåg de lösningar som Emerson föreslog, men var osäker på hur dessa lösningar skulle kunna implementeras.

I situationen ovan kan man se att det fanns en betydande skillnad mellan vad Emerson ville att företagsledarna skulle ta med sig och vad de faktiskt tog med sig från mötet. Nedan finns ett annat tillvägagångssätt som Emerson skulle kunna överväga.

Hur kan Emerson förbättra detta tillvägagångssätt?  
Kontext, Konflikt, Klimax, Avslutning, Slutsats  
**Kontext** - Emerson skulle kunna ägna de första 5 minuterna åt att introducera hela situationen och se till att företagsledarna förstår hur problemen påverkar viktiga företagsmått, som intäkter.

Det skulle kunna läggas upp så här: "För närvarande är vårt apps betyg i appbutiken 2,5. Betyg i appbutiken är avgörande för App Store Optimization, vilket påverkar hur många användare som ser vår app i sökningar och hur vår app uppfattas av potentiella användare. Och naturligtvis är antalet användare direkt kopplat till intäkterna."

**Konflikt** Emerson skulle sedan kunna ägna de följande 5 minuterna åt att prata om konflikten.

Det skulle kunna låta så här: "Användare skickar in 42 % fler klagomål och buggrapporter under helgerna. Kunder som skickar in ett klagomål som förblir obesvarat efter 48 timmar är 32 % mindre benägna att ge vår app ett betyg över 2 i appbutiken. Att förbättra vårt apps betyg i appbutiken till 4 skulle förbättra vår synlighet med 20–30 %, vilket jag förutspår skulle öka intäkterna med 10 %." Naturligtvis bör Emerson vara beredd att motivera dessa siffror.

**Klimax** Efter att ha lagt grunden skulle Emerson sedan kunna gå vidare till klimaxet under cirka 5 minuter.

Emerson skulle kunna presentera de föreslagna lösningarna, förklara hur dessa lösningar kommer att adressera de problem som har beskrivits, hur lösningarna kan integreras i befintliga arbetsflöden, vad lösningarna kostar, vad avkastningen på investeringen skulle vara, och kanske till och med visa några skärmdumpar eller wireframes av hur lösningarna skulle se ut om de implementerades. Emerson skulle också kunna dela med sig av användarberättelser från personer vars klagomål tog över 48 timmar att hantera, samt en kommentar från en nuvarande kundtjänstrepresentant inom företaget som har synpunkter på det nuvarande ärendehanteringssystemet.

**Avslutning** Nu kan Emerson ägna 5 minuter åt att återigen beskriva de problem som företaget står inför, gå igenom de föreslagna lösningarna och sammanfatta varför dessa lösningar är de rätta.

**Slutsats** Eftersom detta är ett möte med några intressenter där tvåvägskommunikation kommer att användas, skulle Emerson kunna planera att lämna 10 minuter för frågor, för att säkerställa att allt som var oklart för företagsledarna kan förtydligas innan mötet avslutas.

Om Emerson använde tillvägagångssätt #2 är det mycket mer sannolikt att företagsledarna tar med sig precis det Emerson avsåg – att sättet klagomål och buggar hanteras kan förbättras, och att det finns två lösningar som kan implementeras för att göra denna förbättring möjlig. Detta tillvägagångssätt skulle vara ett mycket mer effektivt sätt att kommunicera den data och den berättelse som Emerson vill förmedla.

# Slutsats  
### Sammanfattning av huvudpunkter  
- Att kommunicera innebär att förmedla eller utbyta information.  
- När du kommunicerar data bör ditt mål inte vara att bara överföra siffror till din publik. Ditt mål bör vara att berätta en historia som baseras på din data.  
- Det finns två typer av kommunikation: envägskommunikation (information förmedlas utan avsikt att få ett svar) och tvåvägskommunikation (information förmedlas fram och tillbaka).  
- Det finns många strategier du kan använda för att berätta en historia med din data. Fem strategier vi har gått igenom är:  
  - Förstå din publik, ditt medium och din kommunikationsmetod  
  - Börja med slutet i åtanke  
  - Närma dig det som en riktig berättelse  
  - Använd meningsfulla ord och fraser  
  - Använd känslor  

### Rekommenderade resurser för självstudier  
[The Five C's of Storytelling - Articulate Persuasion](http://articulatepersuasion.com/the-five-cs-of-storytelling/)  

[1.4 Your Responsibilities as a Communicator – Business Communication for Success (umn.edu)](https://open.lib.umn.edu/businesscommunication/chapter/1-4-your-responsibilities-as-a-communicator/)  

[How to Tell a Story with Data (hbr.org)](https://hbr.org/2013/04/how-to-tell-a-story-with-data)  

[Two-Way Communication: 4 Tips for a More Engaged Workplace (yourthoughtpartner.com)](https://www.yourthoughtpartner.com/blog/bid/59576/4-steps-to-increase-employee-engagement-through-two-way-communication)  

[6 succinct steps to great data storytelling - BarnRaisers, LLC (barnraisersllc.com)](https://barnraisersllc.com/2021/05/02/6-succinct-steps-to-great-data-storytelling/)  

[How to Tell a Story With Data | Lucidchart Blog](https://www.lucidchart.com/blog/how-to-tell-a-story-with-data)  

[6 Cs of Effective Storytelling on Social Media | Cooler Insights](https://coolerinsights.com/2018/06/effective-storytelling-social-media/)  

[The Importance of Emotions In Presentations | Ethos3 - A Presentation Training and Design Agency](https://ethos3.com/2015/02/the-importance-of-emotions-in-presentations/)  

[Data storytelling: linking emotions and rational decisions (toucantoco.com)](https://www.toucantoco.com/en/blog/data-storytelling-dataviz)  

[Emotional Advertising: How Brands Use Feelings to Get People to Buy (hubspot.com)](https://blog.hubspot.com/marketing/emotions-in-advertising-examples)  

[Choosing Colors for Your Presentation Slides | Think Outside The Slide](https://www.thinkoutsidetheslide.com/choosing-colors-for-your-presentation-slides/)  

[How To Present Data [10 Expert Tips] | ObservePoint](https://resources.observepoint.com/blog/10-tips-for-presenting-data)  

[Microsoft Word - Persuasive Instructions.doc (tpsnva.org)](https://www.tpsnva.org/teach/lq/016/persinstr.pdf)  

[The Power of Story for Your Data (thinkhdi.com)](https://www.thinkhdi.com/library/supportworld/2019/power-story-your-data.aspx)  

[Common Mistakes in Data Presentation (perceptualedge.com)](https://www.perceptualedge.com/articles/ie/data_presentation.pdf)  

[Infographic: Here are 15 Common Data Fallacies to Avoid (visualcapitalist.com)](https://www.visualcapitalist.com/here-are-15-common-data-fallacies-to-avoid/)  

[Cherry Picking: When People Ignore Evidence that They Dislike – Effectiviology](https://effectiviology.com/cherry-picking/#How_to_avoid_cherry_picking)  

[Tell Stories with Data: Communication in Data Science | by Sonali Verghese | Towards Data Science](https://towardsdatascience.com/tell-stories-with-data-communication-in-data-science-5266f7671d7)  

[1. Communicating Data - Communicating Data with Tableau [Book] (oreilly.com)](https://www.oreilly.com/library/view/communicating-data-with/9781449372019/ch01.html)  

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ds/quiz/31)  

Gå igenom vad du just har lärt dig med quizet ovan!  

## Uppgift  

[Marknadsundersökning](assignment.md)  

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.