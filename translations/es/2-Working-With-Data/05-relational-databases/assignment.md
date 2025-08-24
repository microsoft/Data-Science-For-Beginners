<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f2d7693f28e4b2675f275e489dc5aac",
  "translation_date": "2025-08-23T23:25:19+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/assignment.md",
  "language_code": "es"
}
-->
# Mostrando datos de aeropuertos

Se te ha proporcionado una [base de datos](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) construida en [SQLite](https://sqlite.org/index.html) que contiene información sobre aeropuertos. El esquema se muestra a continuación. Utilizarás la [extensión SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) en [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) para mostrar información sobre los aeropuertos de diferentes ciudades.

## Instrucciones

Para comenzar con la tarea, necesitarás realizar algunos pasos. Tendrás que instalar algunas herramientas y descargar la base de datos de ejemplo.

### Configura tu sistema

Puedes usar Visual Studio Code y la extensión SQLite para interactuar con la base de datos.

1. Ve a [code.visualstudio.com](https://code.visualstudio.com?WT.mc_id=academic-77958-bethanycheum) y sigue las instrucciones para instalar Visual Studio Code.
1. Instala la [extensión SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum) como se indica en la página del Marketplace.

### Descarga y abre la base de datos

A continuación, descargarás y abrirás la base de datos.

1. Descarga el [archivo de base de datos desde GitHub](https://raw.githubusercontent.com/Microsoft/Data-Science-For-Beginners/main/2-Working-With-Data/05-relational-databases/airports.db) y guárdalo en un directorio.
1. Abre Visual Studio Code.
1. Abre la base de datos en la extensión SQLite seleccionando **Ctl-Shift-P** (o **Cmd-Shift-P** en una Mac) y escribiendo `SQLite: Open database`.
1. Selecciona **Choose database from file** y abre el archivo **airports.db** que descargaste previamente.
1. Después de abrir la base de datos (no verás una actualización en la pantalla), crea una nueva ventana de consulta seleccionando **Ctl-Shift-P** (o **Cmd-Shift-P** en una Mac) y escribiendo `SQLite: New query`.

Una vez abierta, la nueva ventana de consulta puede ser utilizada para ejecutar sentencias SQL contra la base de datos. Puedes usar el comando **Ctl-Shift-Q** (o **Cmd-Shift-Q** en una Mac) para ejecutar consultas contra la base de datos.

> [!NOTE] Para más información sobre la extensión SQLite, puedes consultar la [documentación](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite&WT.mc_id=academic-77958-bethanycheum).

## Esquema de la base de datos

El esquema de una base de datos es el diseño y la estructura de sus tablas. La base de datos **airports** tiene dos tablas, `cities`, que contiene una lista de ciudades en el Reino Unido e Irlanda, y `airports`, que contiene la lista de todos los aeropuertos. Debido a que algunas ciudades pueden tener múltiples aeropuertos, se crearon dos tablas para almacenar la información. En este ejercicio usarás joins para mostrar información de diferentes ciudades.

| Ciudades         |
| ---------------- |
| id (PK, integer) |
| city (text)      |
| country (text)   |

| Aeropuertos                      |
| -------------------------------- |
| id (PK, integer)                 |
| name (text)                      |
| code (text)                      |
| city_id (FK a id en **Cities**)  |

## Tarea

Crea consultas para devolver la siguiente información:

1. todos los nombres de ciudades en la tabla `Cities`.
1. todas las ciudades en Irlanda en la tabla `Cities`.
1. todos los nombres de aeropuertos con su ciudad y país.
1. todos los aeropuertos en Londres, Reino Unido.

## Rúbrica

| Ejemplar   | Adecuado   | Necesita Mejorar |
| ---------- | ---------- | ---------------- |

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.