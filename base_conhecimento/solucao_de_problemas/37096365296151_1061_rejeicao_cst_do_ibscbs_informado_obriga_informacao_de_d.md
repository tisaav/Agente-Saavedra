# 1061 Rejeição: CST do IBS/CBS informado obriga informação de diferimento da CBS [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37096365296151-1061-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-da-CBS-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37096365296151-1061-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-da-CBS-nItem-999)  
> **ID:** `37096365296151` | **Última Atualização:** 2026-08-21T15:26:21Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096396013335)

 **MENSAGEM**

1061 Rejeição: CST do IBS/CBS informado obriga informação de diferimento da CBS [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096396015127)

 **SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e, o documento foi rejeitado pela SEFAZ porque o CST (Código de Situação Tributária) do IBS/CBS utilizado exige a informação do grupo de diferimento da CBS, porém este grupo não foi informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096365288599)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096396016535)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquotas de CBS'' **(Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST configurado para a operação que está gerando a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096365290519)

 Na aba **''Identificação''**, verifique se o CST utilizado possui indicador que exige o uso diferimento (ind_gDif = 1). Neste caso, é obrigatório informar o grupo de diferimento da CBS.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096365291159)

 Na aba **''Tributação''**, na seção ''**Redução e Diferimentos''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096396022935)

 Preencha os campos obrigatórios do grupo de diferimento:

- 

Percentual de diferimento (pDif)

- 

Valor do diferimento (vDif)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096365293591)

 Salve as alterações e tente emitir o documento fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37096396026135)

 **CAUSA**

A rejeição ocorre porque, de acordo com a regra de validação UB59-10 da SEFAZ, quando o CST do IBS/CBS utilizado possui o indicador que exige o uso de diferimento (ind_gDif = 1), é **obrigatório** informar o grupo de diferimento da CBS (grupo: gCBS/gDif) no documento fiscal.

O diferimento é um mecanismo de postergação do pagamento do tributo, transferindo a responsabilidade para uma etapa posterior da cadeia. Quando um CST específico exige o uso de diferimento, todos os campos relacionados a este mecanismo devem ser corretamente preenchidos para que o documento fiscal seja aceito pela SEFAZ.

Cada CST possui indicadores específicos que determinam quais grupos de informações são obrigatórios ou não permitidos.No caso desta rejeição, o CST utilizado possui o indicador ind_gDif = 1, tornando obrigatória a informação do grupo de diferimento da CBS.