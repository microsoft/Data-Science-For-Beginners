<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-27T16:57:13+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "br"
}
-->
# Tarefa de Processamento de Dados em Python

Nesta tarefa, pediremos que você desenvolva o código que começamos a criar em nossos desafios. A tarefa consiste em duas partes:

## Modelagem da Propagação da COVID-19

 - [ ] Plote gráficos de *R* para 5-6 países diferentes em um único gráfico para comparação, ou usando vários gráficos lado a lado.
 - [ ] Veja como o número de mortes e recuperações se correlaciona com o número de casos infectados.
 - [ ] Descubra quanto tempo uma doença típica dura, correlacionando visualmente a taxa de infecção e a taxa de mortes e procurando por algumas anomalias. Pode ser necessário observar diferentes países para descobrir isso.
 - [ ] Calcule a taxa de fatalidade e como ela muda ao longo do tempo. *Você pode querer levar em conta a duração da doença em dias para deslocar uma série temporal antes de fazer os cálculos.*

## Análise de Artigos sobre COVID-19

- [ ] Construa uma matriz de co-ocorrência de diferentes medicamentos e veja quais medicamentos frequentemente aparecem juntos (ou seja, mencionados em um mesmo resumo). Você pode modificar o código para construir a matriz de co-ocorrência de medicamentos e diagnósticos.
- [ ] Visualize essa matriz usando um mapa de calor.
- [ ] Como um objetivo adicional, visualize a co-ocorrência de medicamentos usando [diagrama de cordas](https://en.wikipedia.org/wiki/Chord_diagram). [Esta biblioteca](https://pypi.org/project/chord/) pode ajudar você a desenhar um diagrama de cordas.
- [ ] Como outro objetivo adicional, extraia as dosagens de diferentes medicamentos (como **400mg** em *tomar 400mg de cloroquina diariamente*) usando expressões regulares e construa um dataframe que mostre diferentes dosagens para diferentes medicamentos. **Nota**: considere valores numéricos que estejam em proximidade textual ao nome do medicamento.

## Rubrica

Exemplar | Adequado | Precisa Melhorar
--- | --- | -- |
Todas as tarefas estão completas, ilustradas graficamente e explicadas, incluindo pelo menos um dos dois objetivos adicionais | Mais de 5 tarefas estão completas, nenhum objetivo adicional foi tentado, ou os resultados não estão claros | Menos de 5 (mas mais de 3) tarefas estão completas, as visualizações não ajudam a demonstrar o ponto

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.