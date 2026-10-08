# Erro ao carregar os metadados da entidade CabecalhoNota: Erro interno. Metadados do campo 'TGFORD->HORAENTRADA' não inicializados.

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43010179699351-Erro-ao-carregar-os-metadados-da-entidade-CabecalhoNota-Erro-interno-Metadados-do-campo-TGFORD-HORAENTRADA-n%C3%A3o-inicializados](https://ajuda.sankhya.com.br/hc/pt-br/articles/43010179699351-Erro-ao-carregar-os-metadados-da-entidade-CabecalhoNota-Erro-interno-Metadados-do-campo-TGFORD-HORAENTRADA-n%C3%A3o-inicializados)  
> **ID:** `43010179699351` | **Última Atualização:** 2026-09-23T11:35:05Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43010231688215)

 **MENSAGEM:**

Erro interno
Não foi possível resolver os metadados da entidade
'CabecalhoNota-pt_BR'.
Erro ao carregar os metadados da entidade CabecalhoNota: Erro interno. Metadados do campo 'TGFORD->HORAENTRADA' não
inicializados.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/43010179671063)

**SITUAÇÃO**

Este erro ocorre ao tentar acessar telas criticas do sistema tais como: **"Portal de Vendas" **e **"Portal de Compras" **após atualização para as versões recentes do Sankhya.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43010231689879)

SOLUÇÃO:**

Deve ser realizada** **a reinicialização da Unidade de Dado da seguinte tabela:

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43010179674391)

 TGFORD**

- OrdemCarga

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43010231692567)

**** ****TGFFIN**

- Financeiro

 

Esse processo deve ser feito usando a tela Dicionário de Dados (Configurações >> Avançado) conforme vídeo abaixo.

![Sankhya Om - Google Chrome 2026-08-26 12-00-37 (1).gif](https://ajuda.sankhya.com.br/hc/article_attachments/43010750439447)