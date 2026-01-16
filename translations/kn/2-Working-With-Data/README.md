<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "abc3309ab41bc5a7846f70ee1a055838",
  "translation_date": "2025-12-19T13:29:56+00:00",
  "source_file": "2-Working-With-Data/README.md",
  "language_code": "kn"
}
-->
# ಡೇಟಾ ಜೊತೆಗೆ ಕೆಲಸ ಮಾಡುವುದು

![data love](../../../translated_images/kn/data-love.a22ef29e6742c852505ada062920956d3d7604870b281a8ca7c7ac6f37381d5a.jpg)
> ಫೋಟೋ <a href="https://unsplash.com/@swimstaralex?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">ಅಲೆಕ್ಸಾಂಡರ್ ಸಿನ್</a> ಅವರಿಂದ <a href="https://unsplash.com/s/photos/data?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">ಅನ್ಸ್ಪ್ಲ್ಯಾಶ್</a> ನಲ್ಲಿ
  
ಈ ಪಾಠಗಳಲ್ಲಿ, ಡೇಟಾವನ್ನು ನಿರ್ವಹಿಸುವ, ತಿದ್ದುಪಡಿ ಮಾಡುವ ಮತ್ತು ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಬಳಸುವ ಕೆಲವು ವಿಧಾನಗಳನ್ನು ನೀವು ಕಲಿಯುತ್ತೀರಿ. ಸಂಬಂಧಿತ ಮತ್ತು ಅಸಂಬಂಧಿತ ಡೇಟಾಬೇಸ್‌ಗಳ ಬಗ್ಗೆ ಮತ್ತು ಅವುಗಳಲ್ಲಿ ಡೇಟಾವನ್ನು ಹೇಗೆ ಸಂಗ್ರಹಿಸಬಹುದು ಎಂಬುದನ್ನು ನೀವು ತಿಳಿದುಕೊಳ್ಳುತ್ತೀರಿ. ಡೇಟಾವನ್ನು ನಿರ್ವಹಿಸಲು ಪೈಥಾನ್‌ನೊಂದಿಗೆ ಕೆಲಸ ಮಾಡುವ ಮೂಲಭೂತಗಳನ್ನು ನೀವು ಕಲಿಯುತ್ತೀರಿ ಮತ್ತು ಪೈಥಾನ್‌ನೊಂದಿಗೆ ಡೇಟಾವನ್ನು ನಿರ್ವಹಿಸುವ ಮತ್ತು ಗಣನೆ ಮಾಡುವ ಅನೇಕ ವಿಧಾನಗಳನ್ನು ನೀವು ಕಂಡುಹಿಡಿಯುತ್ತೀರಿ.  
### ವಿಷಯಗಳು

1. [ಸಂಬಂಧಿತ ಡೇಟಾಬೇಸ್‌ಗಳು](05-relational-databases/README.md)
2. [ಅಸಂಬಂಧಿತ ಡೇಟಾಬೇಸ್‌ಗಳು](06-non-relational/README.md)
3. [ಪೈಥಾನ್ ಜೊತೆಗೆ ಕೆಲಸ ಮಾಡುವುದು](07-python/README.md)
4. [ಡೇಟಾ ತಯಾರಿಕೆ](08-data-preparation/README.md)

### ಕ್ರೆಡಿಟ್ಸ್

ಈ ಪಾಠಗಳನ್ನು ❤️ ಸಹಿತ [ಕ್ರಿಸ್ಟೋಫರ್ ಹ್ಯಾರಿಸನ್](https://twitter.com/geektrainer), [ಡ್ಮಿತ್ರಿ ಸೋಶ್ನಿಕೋವ್](https://twitter.com/shwars) ಮತ್ತು [ಜಾಸ್ಮಿನ್ ಗ್ರೀನವೇ](https://twitter.com/paladique) ರವರು ಬರೆಯಲಾಗಿದೆ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->