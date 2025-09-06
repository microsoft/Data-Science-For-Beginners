<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f8e7cdefa096664ae86f795be571580",
  "translation_date": "2025-09-05T18:19:52+00:00",
  "source_file": "5-Data-Science-In-Cloud/17-Introduction/README.md",
  "language_code": "ro"
}
-->
# Introducere în Știința Datelor în Cloud

|![ Sketchnote de [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/17-DataScience-Cloud.png)|
|:---:|
| Știința Datelor în Cloud: Introducere - _Sketchnote de [@nitya](https://twitter.com/nitya)_ |

În această lecție, vei învăța principiile fundamentale ale Cloud-ului, vei descoperi de ce poate fi interesant să folosești servicii Cloud pentru a derula proiecte de știința datelor și vom analiza câteva exemple de proiecte de știința datelor realizate în Cloud.

## [Quiz înainte de lecție](https://ff-quizzes.netlify.app/en/ds/quiz/32)

## Ce este Cloud-ul?

Cloud-ul, sau Cloud Computing, reprezintă livrarea unei game largi de servicii de calcul pe bază de plată pe măsură ce le folosești, găzduite pe o infrastructură prin internet. Serviciile includ soluții precum stocare, baze de date, rețele, software, analize și servicii inteligente.

De obicei, diferențiem între Cloud-ul Public, Privat și Hibrid astfel:

* Cloud public: un cloud public este deținut și operat de un furnizor terț de servicii cloud care livrează resursele sale de calcul prin Internet către public.
* Cloud privat: se referă la resursele de calcul în cloud utilizate exclusiv de o singură afacere sau organizație, cu servicii și o infrastructură menținute pe o rețea privată.
* Cloud hibrid: cloud-ul hibrid este un sistem care combină cloud-urile publice și private. Utilizatorii optează pentru un centru de date local, permițând în același timp ca datele și aplicațiile să fie rulate pe unul sau mai multe cloud-uri publice.

Majoritatea serviciilor de cloud computing se încadrează în trei categorii: Infrastructură ca Serviciu (IaaS), Platformă ca Serviciu (PaaS) și Software ca Serviciu (SaaS).

* Infrastructură ca Serviciu (IaaS): utilizatorii închiriază o infrastructură IT, cum ar fi servere și mașini virtuale (VM-uri), stocare, rețele, sisteme de operare.
* Platformă ca Serviciu (PaaS): utilizatorii închiriază un mediu pentru dezvoltarea, testarea, livrarea și gestionarea aplicațiilor software. Utilizatorii nu trebuie să se preocupe de configurarea sau gestionarea infrastructurii de bază a serverelor, stocării, rețelelor și bazelor de date necesare pentru dezvoltare.
* Software ca Serviciu (SaaS): utilizatorii au acces la aplicații software prin Internet, la cerere și, de obicei, pe bază de abonament. Utilizatorii nu trebuie să se preocupe de găzduirea și gestionarea aplicației software, infrastructura de bază sau întreținerea, cum ar fi actualizările software și patch-urile de securitate.

Unii dintre cei mai mari furnizori de Cloud sunt Amazon Web Services, Google Cloud Platform și Microsoft Azure.

## De ce să alegi Cloud-ul pentru Știința Datelor?

Dezvoltatorii și profesioniștii IT aleg să lucreze cu Cloud-ul din mai multe motive, inclusiv următoarele:

* Inovație: poți alimenta aplicațiile tale prin integrarea serviciilor inovatoare create de furnizorii de Cloud direct în aplicațiile tale.
* Flexibilitate: plătești doar pentru serviciile de care ai nevoie și poți alege dintr-o gamă largă de servicii. De obicei, plătești pe măsură ce folosești și îți adaptezi serviciile în funcție de nevoile tale în evoluție.
* Buget: nu trebuie să faci investiții inițiale pentru achiziționarea de hardware și software, configurarea și operarea centrelor de date locale, ci plătești doar pentru ceea ce folosești.
* Scalabilitate: resursele tale pot fi scalate în funcție de nevoile proiectului, ceea ce înseamnă că aplicațiile tale pot folosi mai mult sau mai puțin putere de calcul, stocare și lățime de bandă, adaptându-se la factorii externi în orice moment.
* Productivitate: te poți concentra pe afacerea ta, în loc să pierzi timp cu sarcini care pot fi gestionate de altcineva, cum ar fi administrarea centrelor de date.
* Fiabilitate: Cloud Computing oferă mai multe modalități de a face backup continuu pentru datele tale și poți configura planuri de recuperare în caz de dezastru pentru a menține afacerea și serviciile funcționale, chiar și în perioade de criză.
* Securitate: poți beneficia de politici, tehnologii și controale care întăresc securitatea proiectului tău.

Acestea sunt câteva dintre cele mai comune motive pentru care oamenii aleg să folosească servicii Cloud. Acum că avem o înțelegere mai bună a ceea ce este Cloud-ul și care sunt principalele sale beneficii, să analizăm mai specific activitatea oamenilor de știința datelor și a dezvoltatorilor care lucrează cu date, și cum Cloud-ul îi poate ajuta să depășească diverse provocări:

* Stocarea unor cantități mari de date: în loc să cumperi, să gestionezi și să protejezi servere mari, poți stoca datele direct în cloud, cu soluții precum Azure Cosmos DB, Azure SQL Database și Azure Data Lake Storage.
* Integrarea datelor: integrarea datelor este o parte esențială a științei datelor, care îți permite să faci tranziția de la colectarea datelor la luarea de măsuri. Cu serviciile de integrare a datelor oferite în cloud, poți colecta, transforma și integra date din diverse surse într-un singur depozit de date, cu Data Factory.
* Procesarea datelor: procesarea unor cantități mari de date necesită multă putere de calcul, iar nu toată lumea are acces la mașini suficient de puternice pentru asta, motiv pentru care mulți aleg să folosească direct puterea de calcul uriașă a cloud-ului pentru a rula și implementa soluțiile lor.
* Utilizarea serviciilor de analiză a datelor: servicii cloud precum Azure Synapse Analytics, Azure Stream Analytics și Azure Databricks te ajută să transformi datele în informații utile.
* Utilizarea serviciilor de învățare automată și inteligență a datelor: în loc să începi de la zero, poți folosi algoritmi de învățare automată oferiți de furnizorul de cloud, cu servicii precum AzureML. De asemenea, poți folosi servicii cognitive precum conversia vorbirii în text, text în vorbire, viziune computerizată și altele.

## Exemple de Știința Datelor în Cloud

Să facem acest lucru mai concret analizând câteva scenarii.

### Analiza sentimentului pe rețelele sociale în timp real
Vom începe cu un scenariu studiat frecvent de cei care încep cu învățarea automată: analiza sentimentului pe rețelele sociale în timp real.

Să presupunem că administrezi un site de știri și vrei să valorifici datele live pentru a înțelege ce conținut ar putea interesa cititorii tăi. Pentru a afla mai multe despre acest lucru, poți construi un program care efectuează analiza sentimentului în timp real a datelor din publicațiile de pe Twitter, pe subiecte relevante pentru cititorii tăi.

Indicatorii cheie pe care îi vei analiza sunt volumul de tweet-uri pe subiecte specifice (hashtag-uri) și sentimentul, care este stabilit folosind instrumente de analiză ce efectuează analiza sentimentului în jurul subiectelor specificate.

Pașii necesari pentru a crea acest proiect sunt următorii:

* Creează un hub de evenimente pentru colectarea datelor de intrare, care va colecta date de pe Twitter.
* Configurează și pornește o aplicație client Twitter, care va apela API-urile de streaming Twitter.
* Creează un job de Stream Analytics.
* Specifică intrarea și interogarea jobului.
* Creează un punct de ieșire și specifică ieșirea jobului.
* Pornește jobul.

Pentru a vedea procesul complet, consultă [documentația](https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?WT.mc_id=academic-77958-bethanycheum&ocid=AID30411099).

### Analiza lucrărilor științifice
Să luăm un alt exemplu de proiect creat de [Dmitry Soshnikov](http://soshnikov.com), unul dintre autorii acestui curriculum.

Dmitry a creat un instrument care analizează lucrările despre COVID. Revizuind acest proiect, vei vedea cum poți crea un instrument care extrage cunoștințe din lucrări științifice, obține informații și ajută cercetătorii să navigheze eficient prin colecții mari de lucrări.

Să vedem pașii utilizați pentru acest lucru:
* Extrage și preprocesează informații cu [Text Analytics for Health](https://docs.microsoft.com/azure/cognitive-services/text-analytics/how-tos/text-analytics-for-health?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Folosește [Azure ML](https://azure.microsoft.com/services/machine-learning?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109) pentru a paraleliza procesarea.
* Stochează și interoghează informații cu [Cosmos DB](https://azure.microsoft.com/services/cosmos-db?WT.mc_id=academic-77958-bethanycheum&ocid=AID3041109).
* Creează un tablou de bord interactiv pentru explorarea și vizualizarea datelor folosind Power BI.

Pentru a vedea procesul complet, vizitează [blogul lui Dmitry](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/).

După cum poți vedea, putem valorifica serviciile Cloud în multe moduri pentru a realiza Știința Datelor.

## Notă de subsol

Surse:
* https://azure.microsoft.com/overview/what-is-cloud-computing?ocid=AID3041109  
* https://docs.microsoft.com/azure/stream-analytics/stream-analytics-twitter-sentiment-analysis-trends?ocid=AID3041109  
* https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/  

## Quiz după lecție

## [Quiz după lecție](https://ff-quizzes.netlify.app/en/ds/quiz/33)

## Temă

[Studiu de piață](assignment.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.