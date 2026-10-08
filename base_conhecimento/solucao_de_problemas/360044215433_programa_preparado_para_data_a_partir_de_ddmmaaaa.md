# Programa preparado para data a partir de DD/MM/AAAA

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044215433-Programa-preparado-para-data-a-partir-de-DD-MM-AAAA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044215433-Programa-preparado-para-data-a-partir-de-DD-MM-AAAA)  
> **ID:** `360044215433` | **Última Atualização:** 2026-07-22T16:00:38Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199373226391)

 MENSAGEM:**

Programa preparado para data a partir de DD/MM/AAAA.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199329253655)

 SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199373233175)

 A retroação máxima permitida para data de implantação de saldo bancário é **1 ano**.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458154813847)

 **EXEMPLO:**

Dia 28/03/2019 criada Conta Bancária 79, ao tentar implantar um saldo bancário com a data 25/03/2018 é apresentada a mensagem:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/12826552847639)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199373239319)

 Não trata-se de um "erro de sistema" ou uma configuração a ser ajustada. É um  comportamento default que enquadra-se nas** melhores práticas**, de forma a impedir inconsistências em fechamentos contábeis/fiscais anuais.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199373241111)

 Como solução, ajuste a data informada em **"Referência p/aceitar lançamentos"** para uma data no **máximo 365 dias anteriores** a data atual.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16199373243543)

 CAUSA:**

Ocorre quando ao tentar implantar um saldo em conta é informado uma data maior que 365 da data de criação da conta bancaria.