<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-12-19T15:51:22+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "ml"
}
-->
# വിമാനത്താവള ഡാറ്റ പ്രദർശിപ്പിക്കൽ

നിങ്ങൾക്ക് [SQLite](https://sqlite.org/index.html) അടിസ്ഥാനമാക്കിയുള്ള [ഡാറ്റാബേസ്](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ലഭിച്ചിട്ടുണ്ട്, ഇത് വിമാനത്താവളങ്ങളെക്കുറിച്ചുള്ള വിവരങ്ങൾ ഉൾക്കൊള്ളുന്നു. സ്കീമ താഴെ കാണിക്കുന്നു. വ്യത്യസ്ത നഗരങ്ങളിലെ വിമാനത്താവളങ്ങളുടെ വിവരങ്ങൾ പ്രദർശിപ്പിക്കാൻ നിങ്ങൾ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ൽ [SQLite വിപുലീകരണം](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ഉപയോഗിക്കും.

## നിർദ്ദേശങ്ങൾ

അസൈൻമെന്റ് ആരംഭിക്കാൻ, നിങ്ങൾക്ക് ചില ഘട്ടങ്ങൾ നിർവഹിക്കേണ്ടതാണ്. നിങ്ങൾക്ക് ചില ടൂളുകൾ ഇൻസ്റ്റാൾ ചെയ്ത് സാമ്പിൾ ഡാറ്റാബേസ് ഡൗൺലോഡ് ചെയ്യേണ്ടതുണ്ട്.

### നിങ്ങളുടെ സിസ്റ്റം സജ്ജമാക്കുക

ഡാറ്റാബേസുമായി ഇടപഴകാൻ Visual Studio Codeയും SQLite വിപുലീകരണവും ഉപയോഗിക്കാം.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) സന്ദർശിച്ച് Visual Studio Code ഇൻസ്റ്റാൾ ചെയ്യാനുള്ള നിർദ്ദേശങ്ങൾ പിന്തുടരുക
1. മാർക്കറ്റ്പ്ലേസ് പേജിൽ നൽകിയ നിർദ്ദേശങ്ങൾ അനുസരിച്ച് [SQLite വിപുലീകരണം](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ഇൻസ്റ്റാൾ ചെയ്യുക

### ഡാറ്റാബേസ് ഡൗൺലോഡ് ചെയ്ത് തുറക്കുക

അടുത്തതായി, ഡാറ്റാബേസ് ഡൗൺലോഡ് ചെയ്ത് തുറക്കുക.

1. [GitHub-ൽ നിന്നുള്ള ഡാറ്റാബേസ് ഫയൽ](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ഡൗൺലോഡ് ചെയ്ത് ഒരു ഡയറക്ടറിയിൽ സേവ് ചെയ്യുക
1. Visual Studio Code തുറക്കുക
1. **Ctl-Shift-P** (മാക്കിൽ **Cmd-Shift-P**) അമർത്തി `SQLite: Open database` ടൈപ്പ് ചെയ്ത് SQLite വിപുലീകരണത്തിൽ ഡാറ്റാബേസ് തുറക്കുക
1. **Choose database from file** തിരഞ്ഞെടുക്കുക, മുമ്പ് ഡൗൺലോഡ് ചെയ്ത **airports.db** ഫയൽ തുറക്കുക
1. ഡാറ്റാബേസ് തുറന്ന ശേഷം (സ്ക്രീനിൽ അപ്ഡേറ്റ് കാണിക്കില്ല), **Ctl-Shift-P** (മാക്കിൽ **Cmd-Shift-P**) അമർത്തി `SQLite: New query` ടൈപ്പ് ചെയ്ത് പുതിയ ക്വറി വിൻഡോ സൃഷ്ടിക്കുക

തുറന്ന ശേഷം, പുതിയ ക്വറി വിൻഡോ ഡാറ്റാബേസിൽ SQL സ്റ്റേറ്റ്മെന്റുകൾ പ്രവർത്തിപ്പിക്കാൻ ഉപയോഗിക്കാം. **Ctl-Shift-Q** (മാക്കിൽ **Cmd-Shift-Q**) കമാൻഡ് ഉപയോഗിച്ച് ക്വറികൾ പ്രവർത്തിപ്പിക്കാം.

> [!NOTE]  
> SQLite വിപുലീകരണത്തെക്കുറിച്ച് കൂടുതൽ വിവരങ്ങൾക്ക്, നിങ്ങൾ [ഡോക്യുമെന്റേഷൻ](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) കാണാം

## ഡാറ്റാബേസ് സ്കീമ

ഒരു ഡാറ്റാബേസിന്റെ സ്കീമ അതിന്റെ പട്ടിക രൂപകൽപ്പനയും ഘടനയുമാണ്. **airports** ഡാറ്റാബേസിൽ രണ്ട് പട്ടികകൾ ഉണ്ട്, യുണൈറ്റഡ് കിംഗ്ഡം, അയർലൻഡ് എന്നിവയിലെ നഗരങ്ങളുടെ പട്ടികയായ `cities`യും എല്ലാ വിമാനത്താവളങ്ങളുടെ പട്ടികയായ `airports`ഉം. ചില നഗരങ്ങൾക്ക് ഒന്നിലധികം വിമാനത്താവളങ്ങൾ ഉണ്ടാകാമെന്നതിനാൽ, വിവരങ്ങൾ സൂക്ഷിക്കാൻ രണ്ട് പട്ടികകൾ സൃഷ്ടിച്ചു. ഈ അഭ്യാസത്തിൽ, വ്യത്യസ്ത നഗരങ്ങളുടെ വിവരങ്ങൾ പ്രദർശിപ്പിക്കാൻ ജോയിനുകൾ ഉപയോഗിക്കും.

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

## അസൈൻമെന്റ്

താഴെ പറയുന്ന വിവരങ്ങൾ തിരികെ നൽകാൻ ക്വറികൾ സൃഷ്ടിക്കുക:

1. `Cities` പട്ടികയിലെ എല്ലാ നഗരങ്ങളുടെ പേരുകൾ
1. `Cities` പട്ടികയിലെ അയർലൻഡിലെ എല്ലാ നഗരങ്ങളും
1. എല്ലാ വിമാനത്താവളങ്ങളുടെ പേരുകൾ അവയുടെ നഗരം, രാജ്യം എന്നിവയോടൊപ്പം
1. ലണ്ടൻ, യുണൈറ്റഡ് കിംഗ്ഡത്തിലെ എല്ലാ വിമാനത്താവളങ്ങളും

## റൂബ്രിക്

| ഉദാഹരണപരമായ | മതിയായ | മെച്ചപ്പെടുത്തേണ്ടത് |
| --------- | -------- | ----------------- |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->