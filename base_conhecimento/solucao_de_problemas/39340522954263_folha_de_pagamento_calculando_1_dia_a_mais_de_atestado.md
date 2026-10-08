# Folha de Pagamento Calculando 1 Dia a Mais de Atestado

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39340522954263-Folha-de-Pagamento-Calculando-1-Dia-a-Mais-de-Atestado](https://ajuda.sankhya.com.br/hc/pt-br/articles/39340522954263-Folha-de-Pagamento-Calculando-1-Dia-a-Mais-de-Atestado)  
> **ID:** `39340522954263` | **Última Atualização:** 2026-08-10T15:10:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340514292119)

 **MENSAGEM**

O sistema está calculando dias a mais de atestado na folha de pagamento. 
Por exemplo, ao calcular a folha mensal, o sistema considera 30 dias de salário base mais os dia de atestado lançado, totalizando a quantidade de dias superior ao devido. 
 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340514293911)

 **SITUAÇÃO**

Ao calcular a folha de pagamento mensal para funcionários que possuem atestado médico, o sistema está considerando incorretamente o(s) dia(s) do atestado adicional no cálculo. Isso ocorre mesmo quando o funcionário deveria ter apenas 30 dias computados no mês.
 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340522942615)

 **SOLUÇÃO**

Para corrigir este problema, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340514294935)

 Acesse a tela **"Ocorrências"** (Pessoal+ » Rotinas Folha » Ocorrências) e localize a ocorrência de atestado utilizada para o funcionário;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340514295575)

 Verifique se a opção **"Reduz Dias Trabalhados"** está marcada na configuração da ocorrência. 
Caso esteja desmarcada, realize a marcação e salve as alterações;

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41123071425815)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340522947095)

 Acesse a "Regra de Cálculo" e verifique se a marcação "Calcula resíduo de afastamento em meses que não possuem 30 dias" também está marcada. 
Caso esteja marcada, realize a desmarcação e salve as alterações;

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41142138812695)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340522948247)

 Realize o calculo da folha novamente; 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340522948887)

 Valide se o cálculo agora está considerando corretamente os 30 dias, sem o dia adicional de atestado;

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39340514299031)

 **CAUSA**

O problema ocorre porque a **"Ocorrência"** estava configurada com a opção **"Reduz Dias Trabalhados"** desmarcada. Quando esta opção não está marcada corretamente, o sistema não computa adequadamente os dias de atestado, resultando no cálculo de um dia a mais na folha de pagamento.
Esta configuração incorreta faz com que o sistema some os dias de atestado aos dias trabalhados, ao invés de considerá-los dentro do período mensal padrão de 30 dias.