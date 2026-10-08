# Erro de metadados ao abrir o Portal de Vendas 'TGFPAR-->ASYCONSULTAID'

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43471435077015-Erro-de-metadados-ao-abrir-o-Portal-de-Vendas-TGFPAR-ASYCONSULTAID](https://ajuda.sankhya.com.br/hc/pt-br/articles/43471435077015-Erro-de-metadados-ao-abrir-o-Portal-de-Vendas-TGFPAR-ASYCONSULTAID)  
> **ID:** `43471435077015` | **Última Atualização:** 2026-09-23T13:50:08Z

---

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43471435067159)

 MENSAGEM**

Erro interno Não foi possível resolver os metadados da entidade 'CabecalhoNota-pt_BR'. Erro ao carregar os metadados da entidade CabecalhoNota: Erro interno: Metadados do campo 'TGFPAR-->ASYCONSULTAID' não inicializados.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/43471435067671)

 **SITUAÇÃO**

Este erro ocorre ao tentar acessar telas criticas do sistema tais como: **"Portal de Vendas" **e **"Portal de Compras" **após atualização para as versões recentes do Sankhya.

 
**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43471435068439)

 SOLUÇÃO**

Deve ser realizada** **a reinicialização das Unidades de Dados das seguintes tabelas e respectivas instâncias:

Esse processo deve ser feito usando a tela **''Dicionário de Dados''** (Configurações » Avançado).

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43471435070487)

 TGFCAB**

- 

CabecalhoNota

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43471469878807)

 TGFVEI**

- 

Veiculo

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43471435074455)

 **TGFPAR**

- 

Parceiro

 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43474701081239)

** Feito os processos, realize a limpeza de cache acessando a 'Administração de servidor >> Descartar Cache'.**