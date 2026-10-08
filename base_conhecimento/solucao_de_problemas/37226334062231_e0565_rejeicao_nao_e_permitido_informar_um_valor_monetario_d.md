# E0565 Rejeição: Não é permitido informar um valor monetário de redução de base de cálculo do ISSQN por benefício municipal, se o código de identificação do Benefício Municipal não corresponder ao tipo de redução por valor monetário.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226334062231-E0565-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-um-valor-monet%C3%A1rio-de-redu%C3%A7%C3%A3o-de-base-de-c%C3%A1lculo-do-ISSQN-por-benef%C3%ADcio-municipal-se-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-n%C3%A3o-corresponder-ao-tipo-de-redu%C3%A7%C3%A3o-por-valor-monet%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226334062231-E0565-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-um-valor-monet%C3%A1rio-de-redu%C3%A7%C3%A3o-de-base-de-c%C3%A1lculo-do-ISSQN-por-benef%C3%ADcio-municipal-se-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-n%C3%A3o-corresponder-ao-tipo-de-redu%C3%A7%C3%A3o-por-valor-monet%C3%A1rio)  
> **ID:** `37226334062231` | **Última Atualização:** 2026-07-22T14:15:03Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226334051863)

 **MENSAGEM**

E0565 Rejeição: Não é permitido informar um valor monetário de redução de base de cálculo do ISSQN por benefício municipal, se o código de identificação do Benefício Municipal não corresponder ao tipo de redução por valor monetário.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226351034519)

 **SITUAÇÃO**

A rejeição está relacionada à emissão de uma NF-e ou NFC-e com informação de benefício fiscal municipal para redução da base de cálculo do ISSQN, em que o benefício informado não corresponde ao tipo de redução aplicado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226334053655)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226334054167)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e localize a alíquota utilizada na operação que gerou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226351035799)

 Verifique o campo **''Código de Classificação Tributária'' **e certifique-se de que o campo **"% Redução Alíquota"** está preenchido com o percentual correto.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226351036695)

 Caso o código do benefício não seja do tipo redução por valor monetário, realize uma das seguintes ações: 

- 

Altere o **"Código de identificação do Benefício Municipal"** para um código que corresponda ao tipo de redução por valor monetário, conforme estabelecido pela legislação municipal, ou

- 

Ou remova o valor monetário de redução da base de cálculo do ISSQN, caso o benefício cadastrado seja de outro tipo (como redução percentual).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226334057879)

 Consulte seu **contador ou a legislação municipal** para confirmar qual é o código correto do benefício fiscal e o tipo de redução aplicável à operação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226334058391)

 Após realizar os ajustes necessários, salve as alterações e **reemita o documento fiscal**. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226334058903)

 **CAUSA**

A rejeição ocorre porque a **Sefaz valida a consistência entre o tipo de benefício fiscal municipal informado e a forma de redução da base de cálculo do ISSQN** aplicada no documento. Quando é informado um **valor monetário de redução**, o código do benefício municipal deve ser especificamente do tipo que permite redução por valor monetário. Se o código informado corresponder a outro tipo de benefício (como redução percentual ou isenção), a validação falha e a nota é rejeitada com a mensagem E0565.