# Documento xxxx: Modelo de impressão de notas/pedidos formatados pelo Ireport deve possuir parâmetro com nome NUNOTA do tipo numérico. Corrija o modelo e tente novamente. (Modelo do Relatório Formatado = xx)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109814-Documento-xxxx-Modelo-de-impress%C3%A3o-de-notas-pedidos-formatados-pelo-Ireport-deve-possuir-par%C3%A2metro-com-nome-NUNOTA-do-tipo-num%C3%A9rico-Corrija-o-modelo-e-tente-novamente-Modelo-do-Relat%C3%B3rio-Formatado-xx](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109814-Documento-xxxx-Modelo-de-impress%C3%A3o-de-notas-pedidos-formatados-pelo-Ireport-deve-possuir-par%C3%A2metro-com-nome-NUNOTA-do-tipo-num%C3%A9rico-Corrija-o-modelo-e-tente-novamente-Modelo-do-Relat%C3%B3rio-Formatado-xx)  
> **ID:** `360044109814` | **Última Atualização:** 2026-08-28T13:51:04Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610664487447)

 MENSAGEM:**

[CORE_E02232] Documento xxxx: Modelo de impressão de notas/pedidos formatados pelo Ireport deve possuir parâmetro com nome NUNOTA do tipo numérico. Corrija o modelo e tente novamente. (Modelo do Relatório Formatado = xx).

[CORE_E02533] Modelo de impressão de notas/pedidos formatados pelo Ireport deve possuir parâmetro com nome NUARQUIVO do tipo numérico. Corrija o modelo e tente novamente. (Modelo do Relatório Formatado = xx)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610664497047)

 CAUSA:**

Ocorre pela falta do Parâmetro $P{NUNOTA} no modelo (jrxml) utilizado na impressão ou usado como modelo para envio de e-mail.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610689260695)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610660453783)

 Identifique onde está configurado o respectivo modelo de impressão, considerando as possibilidades:

- Cadastro do **Tipos de Operação - TOP** *(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)*, aba: 'Impressão' ou 'Emails da TOP', de acordo com a necessidade de cada cliente.

- Modelo de impressão pode estar também em Relatórios Formatados *(Configurações » Avançado » Relatórios Formatados).*

Compreenda que essa mensagem será retornada quando no modelo utilizado falta o parâmetro $P{NUNOTA} no modelo (jrxml) utilizado na impressão ou usado como modelo para envio de e-mail. Para tal é possível baixar o modelo padrão para compreender a configuração desse parâmetro e realizar os devidos ajustes no modelo utilizado:

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610601406487)

 Tela 'Modelo de Impressão (Nota/Pedido)' *(Comercial » Arquivo » Cadastros):*

Através do botão 'Baixar Modelos Padrões', é possível ter modelos que possuem o parâmetro NUNOTA para que possa servir de guia para ajuste no modelo que apresenta o referido erro.

**Importante:**

É preciso ter conhecimento em formatação [Ireport](https://downloads-sankhya-tools.s3-sa-east-1.amazonaws.com/iReport-4.0.1.zip), pois esse ajuste é de responsabilidade do cliente ou um consultor da sua Franquia/Unidade.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18610660464407)

Após os ajustes , efetue a impressão ou envio de e-mail.