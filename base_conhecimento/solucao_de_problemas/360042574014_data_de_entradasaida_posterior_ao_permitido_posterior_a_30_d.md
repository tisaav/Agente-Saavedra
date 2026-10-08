# Data de Entrada/Saida posterior ao permitido (Posterior a 30 dias)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574014-Data-de-Entrada-Saida-posterior-ao-permitido-Posterior-a-30-dias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574014-Data-de-Entrada-Saida-posterior-ao-permitido-Posterior-a-30-dias)  
> **ID:** `360042574014` | **Última Atualização:** 2026-07-22T16:09:33Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459901887895)

 MENSAGEM:**

504 - Data de Entrada/Saída posterior ao permitido (Posterior a 30 dias)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459901898007)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459901900567)

 Para resolver a rejeição verifique no XML da NF-e a tag <dhSaiEnt> (Data de Entrada/Saída) e veja se ela é posterior a 30 dias da data de autorização (<dhEmi>)

- Portal de Vendas » NF-e »** "Gerar XML em arquivo para conferência"**

- Abra o XML [Bloco de Notas e/ou Internet Explorer]

- Verifique a informação das tags abaixo:

**<dhEmi>***2019-12-26T16:05:58-03:00***</dhEmi>**
**<dhSaiEnt>***2020-01-30T23:59:59-03:00***</dhSaiEnt>**

Conforme exemplo acima, a data entrada/saída (30/01/2020) é mais do que 30 dias posterior a data de emissão (26/12/2019).

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459934009111)

 Na Central de Vendas, ajuste a informação inserida em 'Data Entrada/Saída' e gere um novo lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459934010263)

 CAUSA:**

Se informado Data de Entrada / Saída (dhSaiEnt) e essa data for posterior a 30 dias da data de autorização, será apresentada a rejeição.