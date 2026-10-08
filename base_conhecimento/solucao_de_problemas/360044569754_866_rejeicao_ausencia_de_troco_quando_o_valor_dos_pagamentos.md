# 866 - Rejeição: Ausência de troco quando o valor dos pagamentos informados for maior que o total da nota.(NT2016/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044569754-866-Rejei%C3%A7%C3%A3o-Aus%C3%AAncia-de-troco-quando-o-valor-dos-pagamentos-informados-for-maior-que-o-total-da-nota-NT2016-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044569754-866-Rejei%C3%A7%C3%A3o-Aus%C3%AAncia-de-troco-quando-o-valor-dos-pagamentos-informados-for-maior-que-o-total-da-nota-NT2016-002)  
> **ID:** `360044569754` | **Última Atualização:** 2026-07-22T15:51:39Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581979403799)

 SITUAÇÃO:**

Ao realizar emissão de NF-e pela tela Central de Vendas no SankhyaW, acessando a opção (...)>>Ver Acompanhamento, é possível consultar o detalhe da Rejeição a seguir.

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581993765271)

 MENSAGEM:**

866-Rejeição: Ausência de troco quando o valor dos pagamentos informados for maior que o total da nota.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581993766423)

 SOLUÇÃO:**

Para correção seguir os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581979408663)

 Comercial » Preferências » Empresa

Aba: NF-e/NFC-e

Campo: Desconsiderar valores de taxas financeiras na geração do XML

Mantendo o campo **desmarcado**, o comportamento do sistema não se altera, incluindo o valor de juros embutidos nas tags vDup e vPag, conforme xml abaixo. Com isso, esses valores ficam maiores que o conteúdo da tag vOrig.

![Desconsidera.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581979410839)

Mantendo o campo **marcado, **as tags vDup e vPag contém apenas o valor da vOrig, sem considerar valores extras do financeiro, no campo valor de juros embutidos.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581979412247)

 Após os ajustes na marcação, deverá excluir ou inutilizar a nota e faturar/gerar novamente e gerar Lote.

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581993773207)

** OBSERVAÇÃO:** 

É possível ter a geração da tag <vtroco> apenas com utilização do TEF.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581979414423)

 CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e o total do pagamento for maior que o total da NF, e não for informado o valor do troco. 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16581993773207)

 OBSERVAÇÃO:**

1- (**NT2016/002**)

Nota Técnica:

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uvfnqOj%20spg=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uvfnqOj%20spg=)