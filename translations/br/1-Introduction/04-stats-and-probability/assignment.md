<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01d1b493e8b51a6ebb42524f6b1bcfff",
  "translation_date": "2025-08-27T17:29:21+00:00",
  "source_file": "1-Introduction/04-stats-and-probability/assignment.md",
  "language_code": "br"
}
-->
# Pequeno Estudo sobre Diabetes

Nesta tarefa, trabalharemos com um pequeno conjunto de dados de pacientes com diabetes retirado de [aqui](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

|   | IDADE | SEXO | IMC | PA | S1 | S2 | S3 | S4 | S5 | S6 | Y  |
|---|-------|------|-----|----|----|----|----|----|----|----|----|
| 0 | 59    | 2    | 32.1 | 101. | 157 | 93.2 | 38.0 | 4. | 4.8598 | 87 | 151 |
| 1 | 48    | 1    | 21.6 | 87.0 | 183 | 103.2 | 70. | 3. | 3.8918 | 69 | 75 |
| 2 | 72    | 2    | 30.5 | 93.0 | 156 | 93.6 | 41.0 | 4.0 | 4. | 85 | 141 |
| ... | ... | ... | ... | ...| ...| ...| ...| ...| ...| ...| ... |

## Instruções

* Abra o [notebook da tarefa](assignment.ipynb) em um ambiente de jupyter notebook
* Complete todas as tarefas listadas no notebook, a saber:
   * [ ] Calcular os valores médios e a variância de todos os valores
   * [ ] Plotar boxplots para IMC, PA e Y dependendo do gênero
   * [ ] Qual é a distribuição das variáveis Idade, Sexo, IMC e Y?
   * [ ] Testar a correlação entre diferentes variáveis e a progressão da doença (Y)
   * [ ] Testar a hipótese de que o grau de progressão do diabetes é diferente entre homens e mulheres
   
## Rubrica

Exemplar | Adequado | Precisa Melhorar
--- | --- | --- |
Todas as tarefas requeridas estão completas, ilustradas graficamente e explicadas | A maioria das tarefas está completa, explicações ou conclusões dos gráficos e/ou valores obtidos estão ausentes | Apenas tarefas básicas como cálculo de média/variância e gráficos básicos estão completas, nenhuma conclusão é feita a partir dos dados

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.