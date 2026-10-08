# A TOP da Baixa deve ser informada. Financeiro de Nro Único: XXXXX

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044213993-A-TOP-da-Baixa-deve-ser-informada-Financeiro-de-Nro-%C3%9Anico-XXXXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044213993-A-TOP-da-Baixa-deve-ser-informada-Financeiro-de-Nro-%C3%9Anico-XXXXX)  
> **ID:** `360044213993` | **Última Atualização:** 2026-07-22T16:00:45Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17291148395287)

 MENSAGEM:**

[ORA-20101]: A TOP da Baixa deve ser informada. Financeiro de Nro Único: XXXXX.
[ORA-06512]: em "NOMEBANCO.TRG_UPT_TGFFIN", line 585
[ORA-04088]: erro durante a execução do gatilho 'NOMEBANCO.TRG_UPT_TGFFIN'

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17291148405271)

 SOLUÇÃO:**

Para correção, siga  os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17291133552023)

 Acesse o cadastro de Parâmetros em: Configurações » Avançado » Preferências

Informe em cada parâmetro o código da Top de Baixa para Receita e Despesa, respectivamente. Para que no processo de compensação de devolução o sistema efetua as devidas baixas nos títulos em aberto.

- 
**"TOPBAIRECDEV-TOP baixa da receita na compensação de devolução": **parâmetro para registrar o código da TOP que será gravada no título de receita gerado pela devolução de compras;

- 
**"TOPBAIDESPDEV -TOP baixa da despesa na compensação de devolução": **parâmetro para registrar o código da TOP que será gravada no título de despesa gerado pela devolução de vendas.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17291133554327)

 CAUSA:**

- Ocorre quando não estão devidamente configurados os parâmetros de Top de compensação de devolução de compras e devolução de vendas;

- Aceita-se somente 1 (um) código de Top em cada parâmetro; 

- As TOPs devem ser de Recebimento (Tipo de Movimento - R-Recebimento)  e Pagamento (Tipo de Movimento = G-Pagamento)