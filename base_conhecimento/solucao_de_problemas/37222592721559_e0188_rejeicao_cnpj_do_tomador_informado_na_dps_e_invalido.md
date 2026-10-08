# E0188 Rejeição: CNPJ do tomador informado na DPS é inválido.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222592721559-E0188-Rejei%C3%A7%C3%A3o-CNPJ-do-tomador-informado-na-DPS-%C3%A9-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222592721559-E0188-Rejei%C3%A7%C3%A3o-CNPJ-do-tomador-informado-na-DPS-%C3%A9-inv%C3%A1lido)  
> **ID:** `37222592721559` | **Última Atualização:** 2026-07-22T14:17:40Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222592708631)

 **MENSAGEM**

E0188 Rejeição: CNPJ do tomador informado na DPS é inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222592710423)

 **SITUAÇÃO**

Ao emitir um **Documento Fiscal Eletrônico (DPS)** no contexto da **Reforma Tributária**, o usuário informou o **CNPJ do tomador** do serviço ou da operação com **dados inválidos**. A SEFAZ validou o documento e identificou que o CNPJ apresenta **zeros, está nulo ou possui dígito verificador (DV) incorreto**, resultando na rejeição do documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222592711319)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222576761623)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **cadastro do tomador** informado no documento fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222576762263)

 Verifique o campo **"CNPJ"** do parceiro e certifique-se de que:

- 

O CNPJ **não está preenchido com zeros** (exemplo: 00000000000000);

- 

O CNPJ **não está vazio ou nulo**;

- 

O **dígito verificador (DV) está correto**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222576763031)

 Caso o CNPJ esteja incorreto, **consulte o CNPJ correto** do tomador no site da **Receita Federal** ou no **SINTEGRA** do estado correspondente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222576763671)

 Atualize o campo **"CNPJ"** no cadastro do parceiro com as **informações corretas** e salve as alterações.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222592715415)

 Certifique-se de que a **situação cadastral do parceiro** está **Ativa/Habilitada** na Receita Federal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222576764567)

 Retorne ao **documento fiscal rejeitado**, redigite o cabeçalho da nota e **gere um novo lote** para transmissão à SEFAZ.
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37808533153303)

 OBSERVAÇÃO:** Para parceiros **estrangeiros**, certifique-se de preencher corretamente o parâmetro **"Código do País Brasil" [CODPAISBRASIL]** com o valor **[55]**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222592719639)

 **CAUSA**

A rejeição ocorre quando o **CNPJ do tomador** informado no **Documento Fiscal Eletrônico (DPS)** apresenta uma das seguintes situações:

- 

CNPJ preenchido com **zeros** (exemplo: 00000000000000);

- 

CNPJ **nulo ou vazio**;

- 

**Dígito verificador (DV) inválido**, indicando erro de digitação ou inconsistência cadastral.

Conforme as **regras de validação da SEFAZ** estabelecidas pela **Lei Complementar nº 214/2025** no contexto da **Reforma Tributária**, o CNPJ do tomador deve ser **válido e estar corretamente cadastrado** para que o documento fiscal seja aceito.