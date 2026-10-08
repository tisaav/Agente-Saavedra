# Comissão múltipla não gera financeiro na tela Fechamento de Comissão

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14045554294807-Comiss%C3%A3o-m%C3%BAltipla-n%C3%A3o-gera-financeiro-na-tela-Fechamento-de-Comiss%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/14045554294807-Comiss%C3%A3o-m%C3%BAltipla-n%C3%A3o-gera-financeiro-na-tela-Fechamento-de-Comiss%C3%A3o)  
> **ID:** `14045554294807` | **Última Atualização:** 2026-07-22T14:59:36Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867765328791)

 SITUAÇÃO:**

Comissão múltipla não gera financeiro na tela Fechamento de Comissão.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867758240663)

CAUSA:**

Ocorre devido a configurações divergentes.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867758233239)

SOLUÇÃO:**

Verifique as seguintes configurações abaixo:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450702420631)

 Tela **Vendedores/compradores** *(Configurações » Cadastros » Vendedores/Compradores)*, aba **"Geral"**, campo **"Tipo de fechamento de Comissão":** Financeiro

 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16867765338391)

** Observações: **

A configuração do Tipo de Fechamento de Comissão sofre influência quando se usa o parâmetro  **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"**, da seguinte forma:

 

 **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"** - Ligado: busca o tipo de fechamento na tela **"Fórmula de Comissão",** aba **"Integração"**, campo Tipo de Integração, ou seja, se estiver ligado acesse a tela Fórmula de comissão campo "Tipo de Integração" na aba Integração deve estar marcado como Financeiro.

 **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"** - Desligado: desconsidera a premiação e verifica o parâmetro **"Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"**.

 

**Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"**. - Ligado: olha no cadastro do vendedor, campo Tipo de fechamento de Comissão, então se não trabalha com premiação basta ligar esse parâmetro para que o financeiro seja gerado.

 

**Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"**. - Desligado: Não olha o Tipo de fechamento de Comissão e o financeiro não será gerado.