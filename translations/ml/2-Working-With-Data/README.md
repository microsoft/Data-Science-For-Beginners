<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "abc3309ab41bc5a7846f70ee1a055838",
  "translation_date": "2025-12-19T13:29:38+00:00",
  "source_file": "2-Working-With-Data/README.md",
  "language_code": "ml"
}
-->
# ഡാറ്റയുമായി പ്രവർത്തിക്കൽ

![data love](../../../translated_images/data-love.a22ef29e6742c852505ada062920956d3d7604870b281a8ca7c7ac6f37381d5a.ml.jpg)
> ഫോട്ടോ <a href="https://unsplash.com/@swimstaralex?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alexander Sinn</a> യുടെ <a href="https://unsplash.com/s/photos/data?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> ൽ നിന്നാണ്
  
ഈ പാഠങ്ങളിൽ, ഡാറ്റ എങ്ങനെ കൈകാര്യം ചെയ്യാമെന്ന്, മാറ്റം വരുത്താമെന്ന്, ആപ്ലിക്കേഷനുകളിൽ ഉപയോഗിക്കാമെന്ന് നിങ്ങൾ പഠിക്കും. ബന്ധപരമായ (relational) ഡാറ്റാബേസുകളും ബന്ധമില്ലാത്ത (non-relational) ഡാറ്റാബേസുകളും എന്താണെന്ന്, അവയിൽ ഡാറ്റ എങ്ങനെ സൂക്ഷിക്കാമെന്ന് നിങ്ങൾ അറിയും. ഡാറ്റ കൈകാര്യം ചെയ്യാൻ പൈത്തൺ ഉപയോഗിക്കുന്നതിന്റെ അടിസ്ഥാനങ്ങൾ നിങ്ങൾ പഠിക്കും, കൂടാതെ പൈത്തൺ ഉപയോഗിച്ച് ഡാറ്റ കൈകാര്യം ചെയ്യാനും ഡാറ്റയിൽ നിന്ന് വിവരങ്ങൾ കണ്ടെത്താനും ഉള്ള നിരവധി മാർഗങ്ങൾ നിങ്ങൾ കണ്ടെത്തും.  
### വിഷയങ്ങൾ

1. [ബന്ധപരമായ ഡാറ്റാബേസുകൾ](05-relational-databases/README.md)
2. [ബന്ധമില്ലാത്ത ഡാറ്റാബേസുകൾ](06-non-relational/README.md)
3. [പൈത്തൺ ഉപയോഗിച്ച് പ്രവർത്തിക്കൽ](07-python/README.md)
4. [ഡാറ്റ തയ്യാറാക്കൽ](08-data-preparation/README.md)

### ക്രെഡിറ്റുകൾ

ഈ പാഠങ്ങൾ ❤️ ഉപയോഗിച്ച് എഴുതിയത് [Christopher Harrison](https://twitter.com/geektrainer), [Dmitry Soshnikov](https://twitter.com/shwars) എന്നിവരും [Jasmine Greenaway](https://twitter.com/paladique) യും ആണ്

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->