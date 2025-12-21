<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "25b37acdfb2452917c1aa2e2ca44317a",
  "translation_date": "2025-12-19T15:52:02+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "kn"
}
-->
# ವಿಮಾನ ನಿಲ್ದಾಣದ ಡೇಟಾ ಪ್ರದರ್ಶನ

ನೀವು ವಿಮಾನ ನಿಲ್ದಾಣಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿಯನ್ನು ಹೊಂದಿರುವ [ಡೇಟಾಬೇಸ್](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ಅನ್ನು [SQLite](https://sqlite.org/index.html) ಆಧಾರಿತವಾಗಿ ಒದಗಿಸಲಾಗಿದೆ. ಕೆಳಗಿನಂತೆ ಸ್ಕೀಮಾ ಪ್ರದರ್ಶಿಸಲಾಗಿದೆ. ನೀವು [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ನಲ್ಲಿ [SQLite ವಿಸ್ತರಣೆ](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ಬಳಸಿ ವಿವಿಧ ನಗರಗಳ ವಿಮಾನ ನಿಲ್ದಾಣಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿಯನ್ನು ಪ್ರದರ್ಶಿಸುವಿರಿ.

## ಸೂಚನೆಗಳು

ಕಾರ್ಯವನ್ನು ಪ್ರಾರಂಭಿಸಲು, ನೀವು ಕೆಲವು ಹಂತಗಳನ್ನು ಅನುಸರಿಸಬೇಕಾಗುತ್ತದೆ. ನೀವು ಕೆಲವು ಉಪಕರಣಗಳನ್ನು ಸ್ಥಾಪಿಸಿ ಮಾದರಿ ಡೇಟಾಬೇಸ್ ಅನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಬೇಕಾಗುತ್ತದೆ.

### ನಿಮ್ಮ ವ್ಯವಸ್ಥೆಯನ್ನು ಸಿದ್ಧಪಡಿಸಿ

ನೀವು Visual Studio Code ಮತ್ತು SQLite ವಿಸ್ತರಣೆಯನ್ನು ಡೇಟಾಬೇಸ್ ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ಬಳಸಬಹುದು.

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ಗೆ ಹೋಗಿ ಮತ್ತು Visual Studio Code ಅನ್ನು ಸ್ಥಾಪಿಸಲು ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ
1. ಮಾರ್ಕೆಟ್‌ಪ್ಲೇಸ್ ಪುಟದಲ್ಲಿ ಸೂಚಿಸಿದಂತೆ [SQLite ವಿಸ್ತರಣೆ](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ವಿಸ್ತರಣೆಯನ್ನು ಸ್ಥಾಪಿಸಿ

### ಡೇಟಾಬೇಸ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ತೆರೆಯಿರಿ

ಮುಂದೆ ನೀವು ಡೇಟಾಬೇಸ್ ಅನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ತೆರೆಯುತ್ತೀರಿ.

1. [GitHub ನಿಂದ ಡೇಟಾಬೇಸ್ ಫೈಲ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ಮತ್ತು ಅದನ್ನು ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಉಳಿಸಿ
1. Visual Studio Code ತೆರೆಯಿರಿ
1. **Ctl-Shift-P** (ಅಥವಾ Mac ನಲ್ಲಿ **Cmd-Shift-P**) ಒತ್ತಿ ಮತ್ತು `SQLite: Open database` ಟೈಪ್ ಮಾಡಿ SQLite ವಿಸ್ತರಣೆಯಲ್ಲಿ ಡೇಟಾಬೇಸ್ ತೆರೆಯಿರಿ
1. **Choose database from file** ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ನೀವು ಹಿಂದಿನ ಹಂತದಲ್ಲಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿದ **airports.db** ಫೈಲ್ ತೆರೆಯಿರಿ
1. ಡೇಟಾಬೇಸ್ ತೆರೆಯಲಾದ ನಂತರ (ಸ್ಕ್ರೀನ್‌ನಲ್ಲಿ ಯಾವುದೇ ಅಪ್ಡೇಟ್ ಕಾಣಿಸುವುದಿಲ್ಲ), **Ctl-Shift-P** (ಅಥವಾ Mac ನಲ್ಲಿ **Cmd-Shift-P**) ಒತ್ತಿ ಮತ್ತು `SQLite: New query` ಟೈಪ್ ಮಾಡಿ ಹೊಸ ಕ್ವೇರಿ ವಿಂಡೋವನ್ನು ರಚಿಸಿ

ಒಮ್ಮೆ ತೆರೆಯಾದ ಮೇಲೆ, ಹೊಸ ಕ್ವೇರಿ ವಿಂಡೋವನ್ನು ಡೇಟಾಬೇಸ್ ವಿರುದ್ಧ SQL ಹೇಳಿಕೆಗಳನ್ನು ಚಲಾಯಿಸಲು ಬಳಸಬಹುದು. ನೀವು **Ctl-Shift-Q** (ಅಥವಾ Mac ನಲ್ಲಿ **Cmd-Shift-Q**) ಬಳಸಿ ಡೇಟಾಬೇಸ್ ವಿರುದ್ಧ ಕ್ವೆರಿಗಳನ್ನು ಚಲಾಯಿಸಬಹುದು.

> [!NOTE]  
> SQLite ವಿಸ್ತರಣೆಯ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ, ನೀವು [ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ಅನ್ನು ಪರಿಶೀಲಿಸಬಹುದು

## ಡೇಟಾಬೇಸ್ ಸ್ಕೀಮಾ

ಡೇಟಾಬೇಸ್ ಸ್ಕೀಮಾ ಎಂದರೆ ಅದರ ಟೇಬಲ್ ವಿನ್ಯಾಸ ಮತ್ತು ರಚನೆ. **airports** ಡೇಟಾಬೇಸ್ ಎರಡು ಟೇಬಲ್‌ಗಳನ್ನು ಹೊಂದಿದೆ, `cities`, ಇದು ಯುನೈಟೆಡ್ ಕಿಂಗ್‌ಡಮ್ ಮತ್ತು ಐರ್ಲೆಂಡ್‌ನ ನಗರಗಳ ಪಟ್ಟಿ ಹೊಂದಿದೆ, ಮತ್ತು `airports`, ಇದು ಎಲ್ಲಾ ವಿಮಾನ ನಿಲ್ದಾಣಗಳ ಪಟ್ಟಿಯನ್ನು ಹೊಂದಿದೆ. ಕೆಲವು ನಗರಗಳಿಗೆ ಬಹು ವಿಮಾನ ನಿಲ್ದಾಣಗಳಿರಬಹುದು, ಆದ್ದರಿಂದ ಮಾಹಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸಲು ಎರಡು ಟೇಬಲ್‌ಗಳನ್ನು ರಚಿಸಲಾಗಿದೆ. ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ನೀವು ವಿವಿಧ ನಗರಗಳ ಮಾಹಿತಿಯನ್ನು ಪ್ರದರ್ಶಿಸಲು ಜೋಡಣೆಗಳನ್ನು ಬಳಸುತ್ತೀರಿ.

| ನಗರಗಳು           |
| ---------------- |
| id (PK, ಪೂರ್ಣಾಂಕ) |
| city (ಪಠ್ಯ)      |
| country (ಪಠ್ಯ)   |

| ವಿಮಾನ ನಿಲ್ದಾಣಗಳು                         |
| -------------------------------- |
| id (PK, ಪೂರ್ಣಾಂಕ)                 |
| name (ಪಠ್ಯ)                      |
| code (ಪಠ್ಯ)                      |
| city_id (FK to id in **Cities**) |

## ಕಾರ್ಯ

ಕೆಳಗಿನ ಮಾಹಿತಿಯನ್ನು ಹಿಂತಿರುಗಿಸಲು ಕ್ವೆರಿಗಳನ್ನು ರಚಿಸಿ:

1. `Cities` ಟೇಬಲ್‌ನಲ್ಲಿನ ಎಲ್ಲಾ ನಗರಗಳ ಹೆಸರುಗಳು
1. `Cities` ಟೇಬಲ್‌ನಲ್ಲಿನ ಐರ್ಲೆಂಡ್‌ನ ಎಲ್ಲಾ ನಗರಗಳು
1. ಎಲ್ಲಾ ವಿಮಾನ ನಿಲ್ದಾಣಗಳ ಹೆಸರುಗಳು ಮತ್ತು ಅವುಗಳ ನಗರ ಮತ್ತು ದೇಶ
1. ಲಂಡನ್, ಯುನೈಟೆಡ್ ಕಿಂಗ್‌ಡಮ್‌ನಲ್ಲಿನ ಎಲ್ಲಾ ವಿಮಾನ ನಿಲ್ದಾಣಗಳು

## ಮೌಲ್ಯಮಾಪನ

| ಅತ್ಯುತ್ತಮ | ಸಮರ್ಪಕ | ಸುಧಾರಣೆಯ ಅಗತ್ಯವಿದೆ |
| --------- | -------- | ----------------- |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->