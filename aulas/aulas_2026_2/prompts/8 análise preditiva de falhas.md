Atue como um Especialista em Engenharia de Software e Modelagem Financeira (ROI de QA). Analise a tabela atual e execute uma projeção preditiva detalhada de custos para os próximos 12 meses, considerando as colunas 'Tipo', 'Custo_Hora_QA_Manual_USD', 'Tempo_Execucao_Manual_Min', 'Custo_Setup_Automacao_USD' e 'Tempo_Execucao_Automatizada_Min'.
Para o cálculo, aplique as seguintes regras de negócio:

    Frequência de Execução: Considere que todos os cenários ativos (Existentes + Fictícios acumulados) são executados exatamente 4 vezes por mês (1 vez por semana).
    Crescimento de Escopo: Adicione linearmente os novos cenários fictícios mês a mês, acumulando-os (Mês 1 adiciona os cenários do Mês 1, Mês 2 acumula os Existentes + Mês 1 + Mês 2, e assim por diante).
    Custo Manual Mensal: Calculado por .
    Custo Automatizado Mensal: Considere o custo acumulado de  (pago uma única vez por cenário adicionado) somado ao custo de execução .

Com base nessas regras:

    Crie uma projeção mês a mês (de 1 a 12) comparando o Custo Total Acumulado do Cenário 100% Manual versus o Custo Total Acumulado do Cenário Automatizado.
    Identifique e me informe em qual mês exato ocorre o 'Break-Even' (o ponto de virada onde o custo cumulativo do teste manual supera o custo acumulado de setup + execução da automação).
    Calcule o impacto financeiro (prejuízo ou desperdício de orçamento) no Mês 12 caso a automação não atinja a meta de cobrir pelo menos 75% desses cenários.
    Monte e exiba um gráfico de linhas comparando a curva de 'Custo Manual Acumulado' vs. 'Custo Automatizado Acumulado' ao longo dos 12 meses.