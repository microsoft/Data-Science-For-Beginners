<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11b166fbcb7eaf82308cdc24b562f687",
  "translation_date": "2025-09-04T13:54:34+00:00",
  "source_file": "2-Working-With-Data/05-relational-databases/README.md",
  "language_code": "es"
}
-->
# Trabajando con Datos: Bases de Datos Relacionales

|![ Sketchnote por [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/05-RelationalData.png)|
|:---:|
| Trabajando con Datos: Bases de Datos Relacionales - _Sketchnote por [@nitya](https://twitter.com/nitya)_ |

Es probable que hayas usado una hoja de cálculo en el pasado para almacenar información. Tenías un conjunto de filas y columnas, donde las filas contenían la información (o datos) y las columnas describían la información (a veces llamada metadatos). Una base de datos relacional se basa en este principio central de columnas y filas en tablas, permitiéndote tener información distribuida en múltiples tablas. Esto te permite trabajar con datos más complejos, evitar duplicaciones y tener flexibilidad en la forma en que exploras los datos. Vamos a explorar los conceptos de una base de datos relacional.

## [Cuestionario previo a la clase](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/8)

## Todo comienza con tablas

Una base de datos relacional tiene como núcleo las tablas. Al igual que en la hoja de cálculo, una tabla es una colección de columnas y filas. La fila contiene los datos o información con la que queremos trabajar, como el nombre de una ciudad o la cantidad de lluvia. Las columnas describen los datos que almacenan.

Comencemos nuestra exploración creando una tabla para almacenar información sobre ciudades. Podríamos empezar con su nombre y país. Podrías almacenar esto en una tabla como la siguiente:

| Ciudad   | País          |
| -------- | ------------- |
| Tokio    | Japón         |
| Atlanta  | Estados Unidos|
| Auckland | Nueva Zelanda |

Nota que los nombres de las columnas **ciudad**, **país** y **población** describen los datos que se están almacenando, y cada fila tiene información sobre una ciudad.

## Las limitaciones de un enfoque de tabla única

Es probable que la tabla anterior te parezca relativamente familiar. Comencemos a agregar algunos datos adicionales a nuestra incipiente base de datos: la lluvia anual (en milímetros). Nos enfocaremos en los años 2018, 2019 y 2020. Si lo agregáramos para Tokio, podría verse algo así:

| Ciudad | País   | Año  | Cantidad |
| ------ | ------ | ---- | -------- |
| Tokio  | Japón  | 2020 | 1690     |
| Tokio  | Japón  | 2019 | 1874     |
| Tokio  | Japón  | 2018 | 1445     |

¿Qué notas sobre nuestra tabla? Podrías notar que estamos duplicando el nombre y el país de la ciudad una y otra vez. Eso podría ocupar bastante espacio de almacenamiento y es en gran medida innecesario tener múltiples copias. Después de todo, Tokio tiene solo un nombre que nos interesa.

Bien, intentemos algo diferente. Agreguemos nuevas columnas para cada año:

| Ciudad   | País          | 2018 | 2019 | 2020 |
| -------- | ------------- | ---- | ---- | ---- |
| Tokio    | Japón         | 1445 | 1874 | 1690 |
| Atlanta  | Estados Unidos| 1779 | 1111 | 1683 |
| Auckland | Nueva Zelanda | 1386 | 942  | 1176 |

Aunque esto evita la duplicación de filas, agrega un par de otros desafíos. Tendríamos que modificar la estructura de nuestra tabla cada vez que haya un nuevo año. Además, a medida que nuestros datos crecen, tener los años como columnas hará que sea más complicado recuperar y calcular valores.

Por eso necesitamos múltiples tablas y relaciones. Al dividir nuestros datos podemos evitar duplicaciones y tener más flexibilidad en cómo trabajamos con ellos.

## Los conceptos de relaciones

Volvamos a nuestros datos y determinemos cómo queremos dividirlos. Sabemos que queremos almacenar el nombre y el país de nuestras ciudades, por lo que esto probablemente funcionará mejor en una tabla.

| Ciudad   | País          |
| -------- | ------------- |
| Tokio    | Japón         |
| Atlanta  | Estados Unidos|
| Auckland | Nueva Zelanda |

Pero antes de crear la siguiente tabla, necesitamos averiguar cómo referenciar cada ciudad. Necesitamos algún tipo de identificador, ID o (en términos técnicos de bases de datos) una clave primaria. Una clave primaria es un valor utilizado para identificar una fila específica en una tabla. Aunque esto podría basarse en un valor en sí mismo (podríamos usar el nombre de la ciudad, por ejemplo), casi siempre debería ser un número u otro identificador. No queremos que el ID cambie nunca, ya que rompería la relación. En la mayoría de los casos, la clave primaria o ID será un número generado automáticamente.

> ✅ La clave primaria se abrevia frecuentemente como PK

### ciudades

| ciudad_id | Ciudad   | País          |
| --------- | -------- | ------------- |
| 1         | Tokio    | Japón         |
| 2         | Atlanta  | Estados Unidos|
| 3         | Auckland | Nueva Zelanda |

> ✅ Notarás que usamos los términos "id" y "clave primaria" de manera intercambiable durante esta lección. Los conceptos aquí se aplican a DataFrames, que explorarás más adelante. Los DataFrames no usan la terminología de "clave primaria", sin embargo notarás que se comportan de manera muy similar.

Con nuestra tabla de ciudades creada, almacenemos la lluvia. En lugar de duplicar la información completa sobre la ciudad, podemos usar el ID. También debemos asegurarnos de que la tabla recién creada tenga una columna *id*, ya que todas las tablas deben tener un ID o clave primaria.

### lluvia

| lluvia_id | ciudad_id | Año  | Cantidad |
| --------- | --------- | ---- | -------- |
| 1         | 1         | 2018 | 1445     |
| 2         | 1         | 2019 | 1874     |
| 3         | 1         | 2020 | 1690     |
| 4         | 2         | 2018 | 1779     |
| 5         | 2         | 2019 | 1111     |
| 6         | 2         | 2020 | 1683     |
| 7         | 3         | 2018 | 1386     |
| 8         | 3         | 2019 | 942      |
| 9         | 3         | 2020 | 1176     |

Nota la columna **ciudad_id** dentro de la tabla recién creada **lluvia**. Esta columna contiene valores que hacen referencia a los IDs en la tabla **ciudades**. En términos técnicos de datos relacionales, esto se llama una **clave foránea**; es una clave primaria de otra tabla. Puedes pensar en ella como una referencia o un puntero. **ciudad_id** 1 hace referencia a Tokio.

> [!NOTE] La clave foránea se abrevia frecuentemente como FK

## Recuperando los datos

Con nuestros datos separados en dos tablas, podrías preguntarte cómo los recuperamos. Si estamos usando una base de datos relacional como MySQL, SQL Server u Oracle, podemos usar un lenguaje llamado Structured Query Language o SQL. SQL (a veces pronunciado "sequel") es un lenguaje estándar utilizado para recuperar y modificar datos en una base de datos relacional.

Para recuperar datos usas el comando `SELECT`. En su núcleo, **seleccionas** las columnas que quieres ver **de** la tabla en la que están contenidas. Si quisieras mostrar solo los nombres de las ciudades, podrías usar lo siguiente:

```sql
SELECT city
FROM cities;

-- Output:
-- Tokyo
-- Atlanta
-- Auckland
```

`SELECT` es donde enumeras las columnas, y `FROM` es donde enumeras las tablas.

> [NOTE] La sintaxis de SQL no distingue entre mayúsculas y minúsculas, lo que significa que `select` y `SELECT` significan lo mismo. Sin embargo, dependiendo del tipo de base de datos que estés usando, las columnas y tablas podrían ser sensibles a mayúsculas y minúsculas. Como resultado, es una buena práctica tratar siempre todo en programación como si fuera sensible a mayúsculas y minúsculas. Al escribir consultas SQL, la convención común es poner las palabras clave en letras mayúsculas.

La consulta anterior mostrará todas las ciudades. Imaginemos que solo queremos mostrar las ciudades en Nueva Zelanda. Necesitamos algún tipo de filtro. La palabra clave de SQL para esto es `WHERE`, o "donde algo es verdadero".

```sql
SELECT city
FROM cities
WHERE country = 'New Zealand';

-- Output:
-- Auckland
```

## Uniendo datos

Hasta ahora hemos recuperado datos de una sola tabla. Ahora queremos reunir los datos de **ciudades** y **lluvia**. Esto se hace *uniéndolos* juntos. Efectivamente crearás una conexión entre las dos tablas y emparejarás los valores de una columna de cada tabla.

En nuestro ejemplo, emparejaremos la columna **ciudad_id** en **lluvia** con la columna **ciudad_id** en **ciudades**. Esto emparejará el valor de lluvia con su respectiva ciudad. El tipo de unión que realizaremos se llama *inner join*, lo que significa que si alguna fila no coincide con nada de la otra tabla, no se mostrará. En nuestro caso, cada ciudad tiene datos de lluvia, por lo que todo se mostrará.

Recuperemos la lluvia de 2019 para todas nuestras ciudades.

Vamos a hacerlo en pasos. El primer paso es unir los datos indicando las columnas para la conexión - **ciudad_id** como se destacó antes.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
```

Hemos destacado las dos columnas que queremos, y el hecho de que queremos unir las tablas por **ciudad_id**. Ahora podemos agregar la declaración `WHERE` para filtrar solo el año 2019.

```sql
SELECT cities.city
    rainfall.amount
FROM cities
    INNER JOIN rainfall ON cities.city_id = rainfall.city_id
WHERE rainfall.year = 2019

-- Output

-- city     | amount
-- -------- | ------
-- Tokyo    | 1874
-- Atlanta  | 1111
-- Auckland |  942
```

## Resumen

Las bases de datos relacionales se centran en dividir la información entre múltiples tablas que luego se reúnen para su visualización y análisis. Esto proporciona un alto grado de flexibilidad para realizar cálculos y manipular datos. Has visto los conceptos centrales de una base de datos relacional y cómo realizar una unión entre dos tablas.

## 🚀 Desafío

Existen numerosas bases de datos relacionales disponibles en internet. Puedes explorar los datos utilizando las habilidades que has aprendido anteriormente.

## Cuestionario posterior a la clase

## [Cuestionario posterior a la clase](https://ff-quizzes.netlify.app/en/ds/)

## Revisión y Autoestudio

Hay varios recursos disponibles en [Microsoft Learn](https://docs.microsoft.com/learn?WT.mc_id=academic-77958-bethanycheum) para que continúes tu exploración de SQL y conceptos de bases de datos relacionales.

- [Describir conceptos de datos relacionales](https://docs.microsoft.com//learn/modules/describe-concepts-of-relational-data?WT.mc_id=academic-77958-bethanycheum)
- [Comienza a consultar con Transact-SQL](https://docs.microsoft.com//learn/paths/get-started-querying-with-transact-sql?WT.mc_id=academic-77958-bethanycheum) (Transact-SQL es una versión de SQL)
- [Contenido de SQL en Microsoft Learn](https://docs.microsoft.com/learn/browse/?products=azure-sql-database%2Csql-server&expanded=azure&WT.mc_id=academic-77958-bethanycheum)

## Tarea

[Título de la tarea](assignment.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.