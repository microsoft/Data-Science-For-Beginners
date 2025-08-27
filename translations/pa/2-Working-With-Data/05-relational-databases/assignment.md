<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-27T16:44:51+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "pa"
}
-->
# ਹਵਾਈ ਅੱਡਿਆਂ ਦੇ ਡਾਟਾ ਨੂੰ ਦਿਖਾਉਣਾ

ਤੁਹਾਨੂੰ ਇੱਕ [ਡਾਟਾਬੇਸ](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ਦਿੱਤਾ ਗਿਆ ਹੈ ਜੋ [SQLite](https://sqlite.org/index.html) 'ਤੇ ਬਣਾਇਆ ਗਿਆ ਹੈ ਅਤੇ ਜਿਸ ਵਿੱਚ ਹਵਾਈ ਅੱਡਿਆਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਹੈ। ਇਸ ਦਾ ਸਕੀਮਾ ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਤੁਸੀਂ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) ਵਿੱਚ [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵੱਖ-ਵੱਖ ਸ਼ਹਿਰਾਂ ਦੇ ਹਵਾਈ ਅੱਡਿਆਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿਖਾਉਣਗੇ।

## ਹਦਾਇਤਾਂ

ਅਸਾਈਨਮੈਂਟ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਕੁਝ ਕਦਮ ਕਰਨੇ ਪੈਣਗੇ। ਤੁਹਾਨੂੰ ਕੁਝ ਟੂਲਿੰਗ ਇੰਸਟਾਲ ਕਰਨੀ ਪਵੇਗੀ ਅਤੇ ਨਮੂਨਾ ਡਾਟਾਬੇਸ ਡਾਊਨਲੋਡ ਕਰਨਾ ਪਵੇਗਾ।

### ਆਪਣੇ ਸਿਸਟਮ ਨੂੰ ਸੈਟਅੱਪ ਕਰੋ

ਤੁਸੀਂ ਡਾਟਾਬੇਸ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ Visual Studio Code ਅਤੇ SQLite ਐਕਸਟੈਂਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

1. [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) 'ਤੇ ਜਾਓ ਅਤੇ Visual Studio Code ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
1. [SQLite extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ਐਕਸਟੈਂਸ਼ਨ ਨੂੰ ਮਾਰਕੀਟਪਲੇਸ ਪੇਜ 'ਤੇ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਅਨੁਸਾਰ ਇੰਸਟਾਲ ਕਰੋ

### ਡਾਟਾਬੇਸ ਡਾਊਨਲੋਡ ਕਰੋ ਅਤੇ ਖੋਲ੍ਹੋ

ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਤੁਸੀਂ ਡਾਟਾਬੇਸ ਡਾਊਨਲੋਡ ਕਰਕੇ ਖੋਲ੍ਹੋਗੇ।

1. [GitHub ਤੋਂ ਡਾਟਾਬੇਸ ਫਾਈਲ](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) ਡਾਊਨਲੋਡ ਕਰੋ ਅਤੇ ਇਸਨੂੰ ਕਿਸੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਸੇਵ ਕਰੋ
1. Visual Studio Code ਖੋਲ੍ਹੋ
1. SQLite ਐਕਸਟੈਂਸ਼ਨ ਵਿੱਚ ਡਾਟਾਬੇਸ ਖੋਲ੍ਹਣ ਲਈ **Ctl-Shift-P** (ਜਾਂ Mac 'ਤੇ **Cmd-Shift-P**) ਦਬਾਓ ਅਤੇ `SQLite: Open database` ਲਿਖੋ
1. **Choose database from file** ਚੁਣੋ ਅਤੇ ਉਹ **airports.db** ਫਾਈਲ ਖੋਲ੍ਹੋ ਜੋ ਤੁਸੀਂ ਪਹਿਲਾਂ ਡਾਊਨਲੋਡ ਕੀਤੀ ਸੀ
1. ਡਾਟਾਬੇਸ ਖੋਲ੍ਹਣ ਤੋਂ ਬਾਅਦ (ਤੁਹਾਨੂੰ ਸਕ੍ਰੀਨ 'ਤੇ ਕੋਈ ਅੱਪਡੇਟ ਨਹੀਂ ਦਿਖੇਗਾ), ਇੱਕ ਨਵੀਂ ਕਵੈਰੀ ਵਿੰਡੋ ਬਣਾਓ **Ctl-Shift-P** (ਜਾਂ Mac 'ਤੇ **Cmd-Shift-P**) ਦਬਾ ਕੇ ਅਤੇ `SQLite: New query` ਲਿਖ ਕੇ

ਜਦੋਂ ਨਵੀਂ ਕਵੈਰੀ ਵਿੰਡੋ ਖੁਲ੍ਹ ਜਾਵੇ, ਤੁਸੀਂ ਇਸਨੂੰ ਡਾਟਾਬੇਸ 'ਤੇ SQL ਸਟੇਟਮੈਂਟ ਚਲਾਉਣ ਲਈ ਵਰਤ ਸਕਦੇ ਹੋ। ਤੁਸੀਂ **Ctl-Shift-Q** (ਜਾਂ Mac 'ਤੇ **Cmd-Shift-Q**) ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਾਟਾਬੇਸ 'ਤੇ ਕਵੈਰੀ ਚਲਾ ਸਕਦੇ ਹੋ।

> [!NOTE] SQLite ਐਕਸਟੈਂਸ਼ਨ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਤੁਸੀਂ [ਡਾਕੂਮੈਂਟੇਸ਼ਨ](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) ਨੂੰ ਵੇਖ ਸਕਦੇ ਹੋ।

## ਡਾਟਾਬੇਸ ਸਕੀਮਾ

ਡਾਟਾਬੇਸ ਦਾ ਸਕੀਮਾ ਇਸ ਦੀ ਟੇਬਲ ਡਿਜ਼ਾਈਨ ਅਤੇ ਸਟ੍ਰਕਚਰ ਹੈ। **airports** ਡਾਟਾਬੇਸ ਵਿੱਚ ਦੋ ਟੇਬਲ ਹਨ, `cities`, ਜਿਸ ਵਿੱਚ ਯੂਨਾਈਟਿਡ ਕਿੰਗਡਮ ਅਤੇ ਆਇਰਲੈਂਡ ਦੇ ਸ਼ਹਿਰਾਂ ਦੀ ਸੂਚੀ ਹੈ, ਅਤੇ `airports`, ਜਿਸ ਵਿੱਚ ਸਾਰੇ ਹਵਾਈ ਅੱਡਿਆਂ ਦੀ ਸੂਚੀ ਹੈ। ਕਿਉਂਕਿ ਕੁਝ ਸ਼ਹਿਰਾਂ ਵਿੱਚ ਕਈ ਹਵਾਈ ਅੱਡੇ ਹੋ ਸਕਦੇ ਹਨ, ਇਸ ਲਈ ਜਾਣਕਾਰੀ ਸਟੋਰ ਕਰਨ ਲਈ ਦੋ ਟੇਬਲ ਬਣਾਈਆਂ ਗਈਆਂ। ਇਸ ਅਭਿਆਸ ਵਿੱਚ ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਸ਼ਹਿਰਾਂ ਲਈ ਜਾਣਕਾਰੀ ਦਿਖਾਉਣ ਲਈ ਜੋਇਨ ਦੀ ਵਰਤੋਂ ਕਰੋਗੇ।

| ਸ਼ਹਿਰਾਂ (Cities)   |
| ------------------- |
| id (PK, integer)    |
| city (text)         |
| country (text)      |

| ਹਵਾਈ ਅੱਡੇ (Airports)            |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK to id in **Cities**) |

## ਅਸਾਈਨਮੈਂਟ

ਹੇਠਾਂ ਦਿੱਤੀ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਵੈਰੀਆਂ ਬਣਾਓ:

1. `Cities` ਟੇਬਲ ਵਿੱਚ ਸਾਰੇ ਸ਼ਹਿਰਾਂ ਦੇ ਨਾਮ
1. `Cities` ਟੇਬਲ ਵਿੱਚ ਆਇਰਲੈਂਡ ਦੇ ਸਾਰੇ ਸ਼ਹਿਰ
1. ਸਾਰੇ ਹਵਾਈ ਅੱਡਿਆਂ ਦੇ ਨਾਮ ਉਨ੍ਹਾਂ ਦੇ ਸ਼ਹਿਰ ਅਤੇ ਦੇਸ਼ ਦੇ ਨਾਲ
1. ਲੰਡਨ, ਯੂਨਾਈਟਿਡ ਕਿੰਗਡਮ ਦੇ ਸਾਰੇ ਹਵਾਈ ਅੱਡੇ

## ਰੂਬ੍ਰਿਕ

| ਸ਼ਾਨਦਾਰ (Exemplary) | ਠੀਕ-ਠਾਕ (Adequate) | ਸੁਧਾਰ ਦੀ ਲੋੜ (Needs Improvement) |
| -------------------- | ------------------ | -------------------------------- |

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।