# Metadados do campo TCBPLA->CAPEX não inicializados

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/42250379418391-Metadados-do-campo-TCBPLA-CAPEX-n%C3%A3o-inicializados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42250379418391-Metadados-do-campo-TCBPLA-CAPEX-n%C3%A3o-inicializados)  
> **ID:** `42250379418391` | **Última Atualização:** 2026-09-14T13:30:34Z

---

A correção desse erro foi realizada nas versões 4.36b112 e 4.35b811, mas caso não consiga atualizar a base no momento, seguir os passos a baixo para a correção.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42250364876567)

 **Mensagem**
Erro interno
Não foi possível resolver os meladados da entidade
EmpresaFinanceiro-pt_BR
Erro ao carregar os metadados da entidade
EmpresaFinanceiro: Erro interno: Metadados do campo
TCBPLA->CAPEX não inicializados

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/42250364877207)

**SITUAÇÃO**

Este erro ocorre ao tentar acessar telas criticas do sistema tais como: **"Portal de Vendas" **e **"Portal de Compras" **após atualização para as versões recentes do Sankhya.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42250379405207)

 **Solução**
Deve ser realizada** **a reinicialização das Unidades de Dados das seguintes tabelas e respectivas instâncias:

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42250364882967)

 TCBPLA**

- PlanoContaECD

- FINPlanoContaComb

- PlanoConta

- PlanoContaEmpresa

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42250364883351)

 TGFCAB**

- CabecalhoNota

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42250364883863)

 TGFEMP**

- EmpresaFinanceiro

Esse processo deve ser feito usando a tela Dicionário de Dados (Configurações >> Avançado) conforme video abaixo.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42250364885655)