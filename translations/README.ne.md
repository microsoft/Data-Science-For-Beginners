# सुरुआतिका लागी Data Science - पाठ्यक्रम

Microsoft मा Azure Cloud अधिवक्ताहरु एक १०-हप्ता, २०-पाठ पाठ्यक्रम सबै Data Science को बारे मा प्रस्ताव गर्न पाउँदा खुसी छन्। प्रत्येक पाठ पूर्व पाठ र पछि पाठ क्विज, पाठ, एक समाधान, र एक काम पूरा गर्न को लागी लिखित निर्देश शामिल छ। हाम्रो परियोजना आधारित शिक्षाशास्त्रले तपाइँलाई निर्माण गर्न को लागी जान्न को लागी अनुमति दिन्छ साथै नयाँ कौशल को लागी 'stick' हुने तरीका सिकाउदछ ।

**हाम्रा लेखकहरुलाई हार्दिक धन्यवाद:** [Jasmine Greenaway](https://www.twitter.com/paladique), [Dmitry Soshnikov](http://soshnikov.com), [Nitya Narasimhan](https://twitter.com/nitya), [Jalen McGee](https://twitter.com/JalenMcG), [Jen Looper](https://twitter.com/jenlooper), [Maud Levy](https://twitter.com/maudstweets), [Tiffany Souterre](https://twitter.com/TiffanySouterre), [Christopher Harrison](https://www.twitter.com/geektrainer).

**🙏विशेष धन्यवाद 🙏 हाम्रा Microsoft Learn Student Ambassadorका लेखक, समीक्षक र सामग्री योगदानकर्ता,** विशेष गरी [Raymond Wangsa Putra](https://www.linkedin.com/in/raymond-wp/), [Ankita Singh](https://www.linkedin.com/in/ankitasingh007), [Rohit Yadav](https://www.linkedin.com/in/rty2423), [Arpita Das](https://www.linkedin.com/in/arpitadas01/), [Mohamma Iftekher (Iftu) Ebne Jalal](https://twitter.com/iftu119), [Dishita Bhasin](https://www.linkedin.com/in/dishita-bhasin-7065281bb), [Miguel Correa](https://www.linkedin.com/in/miguelmque/), [Nawrin Tabassum](https://www.linkedin.com/in/nawrin-tabassum), [Sanya Sinha](https://www.linkedin.com/mwlite/in/sanya-sinha-13aab1200), [Majd Safi](https://www.linkedin.com/in/majd-s/), [Sheena Narula](https://www.linkedin.com/in/sheena-narula-n/), [Anupam Mishra](https://www.linkedin.com/in/anupam--mishra/), [Dibri Nsofor](https://www.linkedin.com/in/dibrinsofor), [Aditya Garg](https://github.com/AdityaGarg00), [Alondra Sanchez](https://www.linkedin.com/in/alondra-sanchez-molina/), Yogendrasingh Pawar, Max Blum, Samridhi Sharma, Tauqeer Ahmad, Aaryan Arora, ChhailBihari Dubey

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../sketchnotes/00-Title.png)|
|:---:|
|सुरुआतिका लागी Data Science - _स्केचनोट [@nitya](https://twitter.com/nitya) द्वारा_ |


# सुरु गर्नका लागी

> **शिक्षकहरु**, हामीले कसरी यो पाठ्यक्रम को उपयोग गर्न [केहि सुझावहरु ](for-teachers.md) मा समावेस गरेका छौ । हामी तपाइँको प्रतिक्रिया [हाम्रो Discussion Forum](https://github.com/microsoft/Data-Science-For-Beginners/discussions) मा सुन्न आतुर छौ !

> **विद्यार्थी**, यो पाठ्यक्रम आफ्नै शैलिमा प्रयोग गर्नका लागी यो Repo लाई  fork गर्नुहोस् र एक पूर्व व्याख्यान प्रश्नोत्तरी संग शुरू गरी  त्यसपछि गतिविधिहरु को बाकी पूरा लेक्चर पढी   अभ्यास पूरा गर्नुहोस् । समाधान कोड प्रतिलिपि गर्नुको सट्टा पाठ बुझेर परियोजनाहरु बनाउन को लागी प्रयास गर्नुहोस्; जे होस् कि कोड प्रत्येक परियोजना उन्मुख पाठ मा /solution फोल्डरहरु मा उपलब्ध छ। अर्को विचार साथीहरु संग एक साथ सामग्री को माध्यम बाट जाने संग एक अध्ययन समूह गठन गर्न को लागी हुनेछ। थप अध्ययन को लागी, हामी [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/qprpajyoy3x0g7?WT.mc_id=academic-77958-bethanycheum)सिफारिश गर्दछौं ।  

### टोलीलाई भेट्नुहोस्

[![प्रोमो भिडियो](screenshot.png)]( "Promo video")

> 🎥 यो Project मा काम गर्नुहुने माहानुभाभरुको भिडियो हेर्ने माथी को image क्लिक गर्नुहोस्

## शिक्षाशास्त्र

यो पाठ्यक्रम निर्माण गर्दा हामीले दुई शैक्षिक सिद्धान्त छनौट गरेका छौं: यो Project आधारित छ र यीमा  बारम्बार क्विजहरु सामेल छन्। यस श्रृंखला को अन्त सम्म, विद्यार्थीहरु नैतिक अवधारणाहरु, डाटा तयारी, डाटा संग काम गर्ने बिभिन्न तरीकाहरु, डाटा दृश्य, डाटा विश्लेषण, डाटा विज्ञान को वास्तविक दुनिया को उपयोग को मामलाहरु, र अधिक सहित डेटा विज्ञान को आधारभूत सिद्धान्तहरु सिक्ने छन ।

यसबाहेक, एक कम दांव क्विज एक कक्षा भन्दा पहिले गर्नाले एक विषय सिक्न को लागी विद्यार्थी को इरादा सेट गर्दछ, जबकि कक्षा पछि एक दोस्रो प्रश्नोत्तरी थप अवधारण सुनिश्चित गर्दछ। यो पाठ्यक्रम लचिलो र रमाईलो हुन को लागी डिजाइन गरीएको छ  र सम्पूर्ण वा आंशिक रूपमा लिन सकिन्छ। Project सुरु हुँदै १० हप्ता  को अन्त्य सम्म जटिलता बढ्दै जादछ ।

> हाम्रो [आचार संहिता](CODE_OF_CONDUCT.md), [योगदान](CONTRIBUTING.md), [अनुवाद](TRANSLATIONS.md) दिशानिर्देश पाउनुहोस्। हामी तपाइँको रचनात्मक प्रतिक्रिया स्वागत गर्दछौं!

## प्रत्येक पाठ समावेश छ:

- वैकल्पिक स्केचनोट
- वैकल्पिक पूरक भिडियो
- पूर्व पाठ वार्मअप प्रश्नोत्तरी
- लिखित पाठ
-परियोजना आधारित पाठ को लागी, कसरी परियोजना निर्माण गर्न को लागी चरण-दर-चरण गाइड
- ज्ञान जाँच
- चुनौती
- पूरक पठन
- असाइनमेन्ट
- पोस्ट पाठ प्रश्नोत्तरी

> ** क्विजहरु को बारे मा एक नोट **: सबै क्विज  [यो एप मा](https://red-water-0103e7a0f.azurestaticapps.net/) निहित छन्, प्रत्येक तीन प्रश्नहरु को ४० कुल क्विज को लागी। तिनीहरू पाठ भित्र बाट जोडिएका छन् तर प्रश्नोत्तरी अनुप्रयोग स्थानीय स्तर मा चलाउन सकिन्छ; 'क्विज- app' फोल्डर मा निर्देशन पालना गर्नुहोस्। उनीहरु बिस्तारै स्थानीयकृत हुँदैछन्।


## पाठ


|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](./sketchnotes/00-Roadmap.png)|
|:---:|
| शुरुआती को लागी डाटा विज्ञान: गाइड - _स्केचनोट [@nitya](https://twitter.com/nitya)_ द्वारा|


| पाठ नम्बर | विषय | पाठ समूह | सिक्ने उद्देश्यहरू | लिन्कड पाठ | लेखक |
| :-----------: | :----------------------------------------: | :--------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------: | :----: |
| 0१ | डाटा विज्ञान को परिभाषा | [परिचय](1-Introduction/README.md) | डाटा विज्ञान को पछाडि आधारभूत अवधारणाहरु जान्नुहोस् र यो कसरी Artificial Intelligence, Machine Learning, र Big Data संग सम्बन्धित छ। | [पाठ](1-Introduction/01-defining-data-science/README.md) [भिडियो](https://youtu.be/beZ7Mb_oz9I) | [Dmitry](http://soshnikov.com) |
| 0२ | डाटा विज्ञान नैतिकता | [परिचय](1-Introduction/README.md) | डाटा नैतिक अवधारणाहरु, चुनौतिहरु र फ्रेमवर्क | [पाठ](1-Introduction/02-ethics/README.md) | [Nitya](https://twitter.com/nitya) |
| 0३ | डाटा परिभाषा | [परिचय](1-Introduction/README.md) | कसरी डाटा वर्गीकृत र यसको सामान्य स्रोत हो। | [पाठ](1-Introduction/03-defining-data/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 0४ | Probability र Statistics को परिचय | [परिचय](1-Introduction/README.md) |Probability र Statistics को गणितीय प्रविधि डाटा बुझ्न को लागी।| [पाठ](1-Introduction/04-stats-and-probability/README.md) [भिडिय](https://youtu.be/Z5Zy85g4Yjw) | [Dmitry](http://soshnikov.com) |
| 0५ | Relational Data मा काम | [डाटासंग काम](2-Working-With-Data/README.md) | रिलेशनल डाटा को परिचय र स्ट्रक्चर्ड क्वेरी भाषा संग रिलेशनल डाटा को अन्वेषण र विश्लेषण को मूल कुराहरु, जसलाई SQL को रूप मा पनि जानिन्छ (उच्चारण "see-quell") | [पाठ](2-Working-With-Data/05-relational-databases/README.md) | [Christopher](https://www.twitter.com/geektrainer) | | |
| 0६ | NoSQL Data मा काम  | [डाटासंग काम](2-Working-With-Data/README.md) | नन रिलेशनल  डाटा को परिचय, यसको विभिन्न प्रकार र अन्वेषण र कागजात डाटाबेस को विश्लेषण को आधारभूत। | [पाठ](2-Working-With-Data/06-non-relational/README.md) | [Jasmine](https://twitter.com/paladique)|
| 0७ | Python मा काम | [डाटासंग काम](2-Working-With-Data/README.md) | Pandas जस्तै libraries संग डाटा अन्वेषण को लागी अजगर को उपयोग को आधारभूत। पाइथन प्रोग्रामिंग को आधारभूत समझ सिफारिश गरीएको छ। | [पाठ](2-Working-With-Data/07-python/README.md) [भिडियो](https://youtu.be/dZjWOGbsN4Y) | [Dmitry](http://soshnikov.com) |
| 0८ | डाटा तयारी | [डाटासंग काम](2-Working-With-Data/README.md) | सफा गर्न र हराइरहेको, गलत, वा अपूर्ण डाटा को चुनौतिहरु लाई सम्हाल्न को लागी डाटा रूपान्तरण को लागी डाटा प्रविधि मा विषय। | [पाठ](2-Working-With-Data/08-data-preparation/README.md) | [Jasmine](https://www.twitter.com/paladique) |
| 0९ | मात्रा को दृश्य | [डाटा दृश्यता](3-Data-Visualization/README.md) | जान्नुहोस् कसरी Matplotlibमा  चरा डाटा चित्रण  गर्ने 🦆 | [पाठ](3-Data-Visualization/09-visualization-quantities/README.md) | [Jen](https://twitter.com/jenlooper) |
| १० | डाटा को वितरण दृश्य | [डाटा दृश्यता](3-Data-Visualization/README.md) | एक अन्तराल भित्र अवलोकन र प्रवृत्ति दृश्य। | [पाठ](3-Data-Visualization/10-visualization-distributions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 11 | अनुपात दृश्य | [डाटा दृश्यता](3-Data-Visualization/README.md) | अलग र समूहीकृत प्रतिशत दृश्य। | [पाठ](3-Data-Visualization/11-visualization-proportions/README.md) | [Jen](https://twitter.com/jenlooper) |
| 12 | सम्बन्ध को दृश्य | [डाटा दृश्यता](3-Data-Visualization/README.md) | भिजुअलाइजिंग कनेक्शन र डाटा को सेट र उनीहरुको variables को बीच सम्बन्ध। | [पाठ](3-Data-Visualization/12-visualization-relationships/README.md) | [Jen](https://twitter.com/jenlooper) |
| 13 | सार्थक दृश्य | [डाटा दृश्यत](3-Data-Visualization/README.md) | प्रभावकारी समस्या को समाधान र अंतर्दृष्टि को लागी तपाइँको दृश्य बहुमूल्य बनाउन को लागी प्रविधि र मार्गदर्शन। | [पाठ](3-Data-Visualization/13-meaningful-visualizations/README.md) | [Jen](https://twitter.com/jenlooper) |
| 14 | डाटा विज्ञान जीवनचक्र को परिचय | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | डाटा विज्ञान जीवनचक्र को परिचय र डाटा प्राप्त गर्ने र निकाल्ने यसको पहिलो चरण। | [पाठ](4-Data-Science-Lifecycle/14-Introduction/README.md) | [Jasmine](https://twitter.com/paladique) |
| 15 | विश्लेषण  | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | डाटा विज्ञान जीवनचक्र को यो चरण डाटा को विश्लेषण गर्न को लागी टेक्नीक मा केन्द्रित छ। | [पाठ](4-Data-Science-Lifecycle/15-Analyzing/README.md) | [Jasmine](https://twitter.com/paladique) | | |
| 16 | सञ्चार | [जीवनचक्र](4-Data-Science-Lifecycle/README.md) | डाटा विज्ञान जीवनचक्रको यो चरण डेटा बाट अन्तरदृष्टि प्रस्तुत गर्ने तरीका मा ध्यान केन्द्रित गर्दछ कि यो निर्णय निर्माताहरु लाई बुझ्न को लागी सजिलो बनाउँछ। | [पाठ](4-Data-Science-Lifecycle/16-Communication/README.md) | [Jalen](https://twitter.com/JalenMcG) | | |
| 17 | क्लाउड मा डाटा विज्ञान | [क्लाउड डाटा ](5-Data-Science-In-Cloud/README.md) | पाठ को यो श्रृंखला क्लाउड र यसको लाभ मा डाटा विज्ञान को परिचय। | [पाठ](5-Data-Science-In-Cloud/17-Introduction/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) र [Maud](https://twitter.com/maudstweets) |
| 18 | क्लाउड मा डाटा विज्ञान | [क्लाउड डाटा](5-Data-Science-In-Cloud/README.md) | कम कोड उपकरण को उपयोग गरी प्रशिक्षण मोडेल। |[पाठ](5-Data-Science-In-Cloud/18-Low-Code/README.md) | [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 19 | क्लाउड मा डाटा विज्ञान | [क्लाउड डाटा](5-Data-Science-In-Cloud/README.md) | Azure Machine Learning Studio संग मोडेल परिनियोजन। | [पाठ](5-Data-Science-In-Cloud/19-Azure/README.md)| [Tiffany](https://twitter.com/TiffanySouterre) and [Maud](https://twitter.com/maudstweets) |
| 20 | जंगलमा डाटा विज्ञान| [जंगलम](6-Data-Science-In-Wild/README.md) | वास्तविक दुनिया मा डाटा विज्ञान संचालित परियोजनाहरु। | [पाठ](6-Data-Science-In-Wild/20-Real-World-Examples/README.md) | [Nitya](https://twitter.com/nitya) |

## अफलाइन पहुँच

तपाइँ यो कागजात अफलाइन चलाउन सक्नुहुन्छ [Docsify] (https://docsify.js.org/#/) को उपयोग गरेर। यो Repo Fork गर्नुहोस्, [तपाइँको Docsify स्थापना गर्नुहोस् (https://docsify.js.org/#/quickstart) तपाइँको स्थानीय मेसिन मा, तब यो रेपो को मूल फोल्डर मा, `docsify serve`  टाइप गर्नुहोस्। वेबसाइट तपाइँको स्थानीय होस्ट मा पोर्ट 3000 मा सेवा दिइनेछ: `localhost: 3000`।

> नोट, नोटबुक Docsify को माध्यम बाट रेन्डर गरिनेछैन, त्यसैले जब तपाइँ एक नोटबुक चलाउन को लागी आवश्यक छ, VS Code मा एक अजगर कर्नेल चलिरहेको छुट्टै गर्नुहोस्।

##PDF

सबै पाठ को एक पीडीएफ [यहाँ पाउन सकिन्छ](https://microsoft.github.io/Data-Science-For-Beginners/pdf/readme.pdf)

## सहयोग चाहियो!

यदि तपाइँ पाठ्यक्रम को सबै वा अंश अनुवाद गर्न चाहानुहुन्छ, कृपया हाम्रो [अनुवाद](TRANSLATIONS.md) गाइड को पालन गर्नुहोस्।

## अन्य पाठ्यक्रम

हाम्रो टोली अन्य पाठ्यक्रम उत्पादन! यहाँ हेर्नुहोस :

- [शुरुआतीहरुको लागी Machine Learning](https://aka.ms/ml-beginners)
- [शुरुआती को लागी IoT](https://aka.ms/iot-beginners)
- [शुरुआतीहरुको लागि Web Dev](https://aka.ms/webdev-beginners)
