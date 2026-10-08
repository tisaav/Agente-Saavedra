# E0567 Rejeição: É obrigatório informar vRedBCBM quando o código de identificação do Benefício Municipal (nBM) for um benefício do tipo Redução de Base de Cálculo por Valor Monetário.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226372197271-E0567-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-vRedBCBM-quando-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-nBM-for-um-benef%C3%ADcio-do-tipo-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-por-Valor-Monet%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226372197271-E0567-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-vRedBCBM-quando-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-nBM-for-um-benef%C3%ADcio-do-tipo-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-por-Valor-Monet%C3%A1rio)  
> **ID:** `37226372197271` | **Última Atualização:** 2026-07-22T14:15:02Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226372177303)

 **MENSAGEM**

E0567 Rejeição: É obrigatório informar vRedBCBM quando o código de identificação do Benefício Municipal (nBM) for um benefício do tipo Redução de Base de Cálculo por Valor Monetário.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226357687191)

 **SITUAÇÃO**

Rejeição apresentada na emissão de um documento fiscal eletrônico (NF-e ou NFC-e) quando é utilizado um benefício fiscal municipal do tipo **Redução de Base de Cálculo por Valor Monetário** em um dos itens, sem que o valor da redução esteja informado no campo correspondente.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226372184087)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226357691287)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e localize a alíquota vinculada ao produto que está gerando a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226372186007)

 Na aba '**'Tributação''**, verifique se o campo **''Código de Classificação Tributária'' **está preenchido com um código que permite redução, e verifique se o campo **''% de Redução de Alíquota''** possui o percentual configurado corretamente.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38268883729047)

 Salve as alterações.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226357694103)

 Emita novamente o documento fiscal eletrônico para validar se a rejeição foi solucionada.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226357697815)

 **CAUSA**

A rejeição ocorre porque a **legislação fiscal exige** que, quando um benefício municipal for do tipo **"Redução de Base de Cálculo por Valor Monetário"**, o campo **"Valor da Redução da Base de Cálculo (vRedBCBM)"** seja obrigatoriamente informado no documento fiscal. A ausência desta informação impede que a Sefaz valide corretamente o benefício fiscal aplicado, resultando na rejeição do documento.