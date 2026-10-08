# 1164 Rejeição: Não informado tipo de nota de crédito

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36397201069847-1164-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-tipo-de-nota-de-cr%C3%A9dito](https://ajuda.sankhya.com.br/hc/pt-br/articles/36397201069847-1164-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-tipo-de-nota-de-cr%C3%A9dito)  
> **ID:** `36397201069847` | **Última Atualização:** 2026-07-22T14:23:04Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/36397201028247)

**MENSAGEM**

1164 Rejeição: Não informado tipo de nota de crédito

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/36397192877079)

**SITUAÇÃO**

O usuário enfrenta rejeições pela SEFAZ ao emitir Notas Fiscais com finalidade 5 (Nota de Crédito) ou 6 (Nota de Débito) quando campos obrigatórios específicos (tpNFCredito ou tpNFDebito) não estão preenchidos no sistema.
 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/36397192877975)

**SOLUÇÃO**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/36397201036439)

 Acesse as telas **"Portal de Compras"** (Comercial >> Rotinas >> Portal de Compras) ou **"Portal de Vendas"** (Comercial >> Rotinas >> Portal de Vendas).
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/36397192880791)

 Selecione a nota fiscal que apresentou a rejeição.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/36397201040023)

 Na Central, verifique o campo **"Tipo Operação"** e identifique a TOP utilizada na nota.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/36397201045911)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) e selecione a TOP identificada.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/36397201051671)

 Na aba **"NF-e/NFC-e/CF-e"**, verifique a configuração do campo **"NF-e"**:
 

Para Notas de Crédito: Se selecionada a opção **"Nota de Crédito"**, preencha o campo **"Tipo de Nota Fiscal de Crédito"** conforme o motivo (ex: Multa e juros, Apropriação de crédito presumido, Retorno).
 

Para Notas de Débito: Se selecionada a opção **"Nota de Débito"**, preencha o campo **"Tipo de Nota Fiscal de Débito"** corretamente.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41842394218391)

![6](https://ajuda.sankhya.com.br/hc/article_attachments/36397192888087)

 Salve as alterações.
 

![7](https://ajuda.sankhya.com.br/hc/article_attachments/36397192892055)

Após isso, exclua a nota anterior e gere uma nova.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/36397201058071)

**CAUSA**

A SEFAZ exige que, para as finalidades 5 (Nota de Crédito) e 6 (Nota de Débito), os respectivos campos complementares (tpNFCredito ou tpNFDebito) sejam informados no XML. A ausência de preenchimento, preenchimento indevido, datas de vigência desrespeitadas ou tipo de operação incorreto para o tipo de nota geram as rejeições validadas pela regra fiscal.