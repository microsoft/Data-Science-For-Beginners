<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-24T21:08:59+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "es"
}
-->
# Asignación para Procesamiento de Datos en Python

En esta asignación, te pediremos que desarrolles el código que hemos comenzado a crear en nuestros desafíos. La asignación consta de dos partes:

## Modelado de la Propagación del COVID-19

 - [ ] Graficar *R* para 5-6 países diferentes en un solo gráfico para comparación, o utilizando varios gráficos lado a lado.
 - [ ] Analizar cómo el número de muertes y recuperaciones se correlaciona con el número de casos infectados.
 - [ ] Determinar cuánto dura típicamente una enfermedad correlacionando visualmente la tasa de infección y la tasa de muertes, buscando algunas anomalías. Es posible que necesites observar diferentes países para descubrir esto.
 - [ ] Calcular la tasa de mortalidad y cómo cambia con el tiempo. *Es posible que desees tener en cuenta la duración de la enfermedad en días para desplazar una serie temporal antes de realizar los cálculos.*

## Análisis de Artículos sobre COVID-19

- [ ] Construir una matriz de co-ocurrencia de diferentes medicamentos y observar qué medicamentos suelen aparecer juntos (es decir, mencionados en un mismo resumen). Puedes modificar el código para construir la matriz de co-ocurrencia de medicamentos y diagnósticos.
- [ ] Visualizar esta matriz utilizando un mapa de calor.
- [ ] Como objetivo adicional, visualizar la co-ocurrencia de medicamentos utilizando un [diagrama de cuerdas](https://en.wikipedia.org/wiki/Chord_diagram). [Esta biblioteca](https://pypi.org/project/chord/) puede ayudarte a dibujar un diagrama de cuerdas.
- [ ] Como otro objetivo adicional, extraer las dosis de diferentes medicamentos (como **400mg** en *tomar 400mg de cloroquina diariamente*) utilizando expresiones regulares, y construir un dataframe que muestre diferentes dosis para diferentes medicamentos. **Nota**: considera valores numéricos que estén en proximidad textual cercana al nombre del medicamento.

## Rúbrica

Excepcional | Adecuado | Necesita Mejorar
--- | --- | -- |
Todas las tareas están completas, ilustradas gráficamente y explicadas, incluyendo al menos uno de los dos objetivos adicionales | Más de 5 tareas están completas, no se intentaron objetivos adicionales, o los resultados no son claros | Menos de 5 (pero más de 3) tareas están completas, las visualizaciones no ayudan a demostrar el punto

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.