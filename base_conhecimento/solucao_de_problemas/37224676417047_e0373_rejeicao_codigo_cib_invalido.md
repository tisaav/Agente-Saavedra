# E0373 Rejeição: Código CIB inválido.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224676417047-E0373-Rejei%C3%A7%C3%A3o-C%C3%B3digo-CIB-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224676417047-E0373-Rejei%C3%A7%C3%A3o-C%C3%B3digo-CIB-inv%C3%A1lido)  
> **ID:** `37224676417047` | **Última Atualização:** 2026-07-22T14:16:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224651186327)

 **MENSAGEM**

E0373 Rejeição: Código CIB inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224651187351)

 **SITUAÇÃO**

A NF-e ou NFC-e foi emitida com informações dos tributos IBS e CBS, contendo um Código de Identificação do Benefício Fiscal (CIB) que não é reconhecido no layout do documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224667096087)

 **SOLUÇÃO**

Para corrigir a rejeição e permitir a autorização do documento fiscal, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38307729909783)

 Acesse as telas **''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS)** **e** ''Alíquotas de CBS'' **(Livros Fiscais » Cadastros » Aliquotas de CBS)** **e localize o **cadastro de alíquota** utilizado no documento fiscal rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224667098135)

 Verifique se o campo **"Código de Identificação do Benefício Fiscal - CIB"** está preenchido corretamente: 

- 

Confirme se o código informado corresponde a um **CIB válido e homologado** pela Sefaz;

- 

Consulte a **tabela oficial de códigos CIB** disponibilizada pela Receita Federal ou pelo Comitê Gestor do IBS para validar o código;

- 

Certifique-se de que o CIB está **vigente e aplicável** ao tipo de operação e produto da nota fiscal.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224651195543)

 Caso o código esteja **incorreto ou desatualizado**, corrija o campo **"Código de Identificação do Benefício Fiscal - CIB"** com o código válido correspondente ao benefício fiscal aplicável.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224651196311)

 Se o benefício fiscal **não se aplica** à operação, remova o código CIB do cadastro da alíquota, deixando o campo em branco.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224651196695)

 Retorne ao documento fiscal rejeitado e **redigite o cabeçalho** da nota para que as informações atualizadas sejam aplicadas.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224651197975)

 Gere um **novo lote de transmissão** e tente autorizar o documento fiscal novamente. 
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38307704912279)

 OBSERVAÇÃO:** O Código de Identificação do Benefício Fiscal (CIB) é obrigatório quando há **aplicação de benefícios fiscais** relacionados ao IBS e CBS, conforme previsto na **Lei Complementar nº 214/2025**. Certifique-se de que o código utilizado está **devidamente cadastrado e homologado** pelos órgãos competentes.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224667103895)

 **CAUSA**

A rejeição E0373 é causada pelo **preenchimento incorreto ou ausência de validação** do campo **"Código de Identificação do Benefício Fiscal - CIB"** no cadastro de alíquotas IBS e CBS. Isso ocorre quando o código informado **não consta na tabela oficial** da Sefaz, está **desatualizado, inválido** ou foi **digitado incorretamente**, impedindo a validação do documento fiscal pela Receita Federal.