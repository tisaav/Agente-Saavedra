# Agrupar pagamentos na Remessa para um Parceiro não esta funcionando

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043715434-Agrupar-pagamentos-na-Remessa-para-um-Parceiro-n%C3%A3o-esta-funcionando](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043715434-Agrupar-pagamentos-na-Remessa-para-um-Parceiro-n%C3%A3o-esta-funcionando)  
> **ID:** `360043715434` | **Última Atualização:** 2026-07-22T16:00:23Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17175716336023)

 SITUAÇÃO:**

Na geração do Arquivo de Remessa Bancária, ao marcar a opção: 'Agrupar pagamentos', não está agrupando os títulos de um determinado parceiro.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17175748776215)

 SOLUÇÃO:**
Considere o Comportamento da Aplicação, conforme abaixo:

O Sistema considera as seguintes regras para agrupar:

Mesmo Parceiro, Vencimento, Banco, Agência, Conta, radical do CGC e opção: Marque a opção **"Agrupar Pagamentos na geração p/Banco"**, da aba: **"Identificação do Cadastro do Parceiro".**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17175748777111)

 Acesse: Configurações » Cadastros » Parceiros

Aba: **"Identificação"**

Campo **"Agrupar Pagamentos na geração p/Banco"**: marque

Banco: informe um banco, válido

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17175748777751)

 Acesse: Financeiro » EDI Bancário » Geração Arquivo de Remessa

- Configurações Geração do Arquivo:

- 
**"Agrupar Pagamento"**: marque

- Gere novamente o arquivo de Remessa Bancaria

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17175748781079)

 CAUSA:**

Quando o Vencimento, Banco, Conta, Agência ou a marcação de Agrupar Pagamentos na geração p/ Banco não esta marcado, não agrupa os títulos na remessa.