<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dc8f035ce92e4eaa078ab19caa68267a",
  "translation_date": "2025-08-24T21:08:50+00:00",
  "source_file": "2-Working-With-Data/07-python/assignment.md",
  "language_code": "pt"
}
-->
# Tarefa de Processamento de Dados em Python

Nesta tarefa, pedimos que desenvolvas o código que começámos a criar nos nossos desafios. A tarefa consiste em duas partes:

## Modelação da Propagação da COVID-19

 - [ ] Traçar gráficos de *R* para 5-6 países diferentes num único gráfico para comparação, ou utilizando vários gráficos lado a lado.
 - [ ] Ver como o número de mortes e recuperações se correlaciona com o número de casos infetados.
 - [ ] Descobrir quanto tempo dura, em média, a doença, correlacionando visualmente a taxa de infeção e a taxa de mortes, procurando por algumas anomalias. Poderás precisar de analisar diferentes países para descobrir isso.
 - [ ] Calcular a taxa de letalidade e como esta muda ao longo do tempo. *Poderás querer considerar a duração da doença em dias para deslocar uma série temporal antes de fazer os cálculos.*

## Análise de Artigos sobre a COVID-19

- [ ] Construir uma matriz de coocorrência de diferentes medicamentos e verificar quais medicamentos aparecem frequentemente juntos (ou seja, mencionados num mesmo resumo). Podes modificar o código para construir a matriz de coocorrência de medicamentos e diagnósticos.
- [ ] Visualizar esta matriz utilizando um mapa de calor.
- [ ] Como objetivo adicional, visualizar a coocorrência de medicamentos utilizando [diagrama de cordas](https://en.wikipedia.org/wiki/Chord_diagram). [Esta biblioteca](https://pypi.org/project/chord/) pode ajudar-te a desenhar um diagrama de cordas.
- [ ] Como outro objetivo adicional, extrair as dosagens de diferentes medicamentos (como **400mg** em *tomar 400mg de cloroquina diariamente*) utilizando expressões regulares, e construir um dataframe que mostre diferentes dosagens para diferentes medicamentos. **Nota**: considera valores numéricos que estejam em proximidade textual com o nome do medicamento.

## Rubrica

Exemplar | Adequado | Precisa de Melhorias
--- | --- | -- |
Todas as tarefas estão completas, ilustradas graficamente e explicadas, incluindo pelo menos um dos dois objetivos adicionais | Mais de 5 tarefas estão completas, nenhum objetivo adicional foi tentado, ou os resultados não são claros | Menos de 5 (mas mais de 3) tarefas estão completas, as visualizações não ajudam a demonstrar o ponto

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.