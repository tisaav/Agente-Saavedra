# Foram encontrados múltiplos títulos para o NSU XXX

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33279907911575-Foram-encontrados-m%C3%BAltiplos-t%C3%ADtulos-para-o-NSU-XXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/33279907911575-Foram-encontrados-m%C3%BAltiplos-t%C3%ADtulos-para-o-NSU-XXX)  
> **ID:** `33279907911575` | **Última Atualização:** 2026-07-22T14:29:08Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279845753879)

 **MENSAGEM:**

Foram encontrados múltiplos títulos para o NSU XXX. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279845754263)

SOLUÇÃO:**Para que o sistema reconheça os registros de maneira adequada, é importante que, no parcelamento, cada título tenha sua parcela correspondente de forma individual.   **

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33335761517207)

 Para validar as duas situações, siga os passos a seguir:** 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279845754519)

 Acesse a tela **"Layout de Processamento de Arquivo"** (Financeiro>> Rotinas >>Layout de Processamento de Arquivo)

- Selecione o layout utilizado;

- Verifique na grade ''**Campos do Registro''**, se a variável ''**NRO_PARCELA''** está presente e se está posicionada corretamente na sequência esperada.

![image (210).png](https://ajuda.sankhya.com.br/hc/article_attachments/33347278024983)

 
**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279907909399)

** Acesse a tela **"Movimentação Financeira" **(Financeiro >> Rotinas >> Movimentação Financeira)

- Consulte o NSU em questão;

- 
Verifique se o campo **''Desdobramento''** está sendo repetido em outras parcelas com o mesmo NSU.
 

![image (220).png](https://ajuda.sankhya.com.br/hc/article_attachments/33347278025623)

 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279845755031)

CAUSA:**

Esse erro acontece quando, na configuração do Layout de Processamento de Arquivo, a variável NRO_PARCELA não foi definida, ou se há mais de um registro com o mesmo NSU e o mesmo Desdobramento (Parcela).