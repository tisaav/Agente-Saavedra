# Visualização de boletos não gerada

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7117486338711-Visualiza%C3%A7%C3%A3o-de-boletos-n%C3%A3o-gerada](https://ajuda.sankhya.com.br/hc/pt-br/articles/7117486338711-Visualiza%C3%A7%C3%A3o-de-boletos-n%C3%A3o-gerada)  
> **ID:** `7117486338711` | **Última Atualização:** 2026-07-22T15:14:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490370346519)

  MENSAGEM:**

[CORE_E01374] Visualização de boletos não gerada!

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490370348183)

 CAUSA:**

Mensagem apresentada quando a emissão de boleto não está devidamente configurada e não permite a visualização do respectivo boleto.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490312063895)

 SOLUÇÃO:**

Revise as configurações abaixo, de acordo com o lançamento efetuado, e caso algum deles não seja respeitado, a mensagem será apresentada na tentativa de visualização do boleto:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490312065303)

 Acesse a tela: **"Contas"** *(Caminho de acesso: Configurações » Cadastros » Bancários » Contas):*

Aba: **"Boleto(s)/Duplicatas"**

- Emite: marcado

- Modelo, configure em: '**Financeiro » Relatórios » Modelos de Boleto(s)**', um que seja padrão ou personalizado e vincule em '**Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)**', para ser informado neste campo

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490411528983)

 Acesse a rotina **"Movimentação Financeira" ***(Caminho de acesso: Financeiro » Rotinas » Movimentação Financeira):*

- Certifique-se que o(s) titulo(s) não estejam Baixados. Campo: "Data de Baixa" e **"Valor de Baixa"**  preenchidos e **"Data de Vencimento"** não seja igual data de negociação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16490411532311)

 Após os ajustes, considere efetuar a impressão do boleto novamente