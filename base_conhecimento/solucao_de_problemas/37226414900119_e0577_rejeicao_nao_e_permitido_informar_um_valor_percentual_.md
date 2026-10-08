# E0577 Rejeição: Não é permitido informar um valor percentual de redução de base de cálculo do ISSQN por benefício municipal, se o código de identificação do Benefício Municipal não corresponder ao tipo de redução por valor percentual.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226414900119-E0577-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-um-valor-percentual-de-redu%C3%A7%C3%A3o-de-base-de-c%C3%A1lculo-do-ISSQN-por-benef%C3%ADcio-municipal-se-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-n%C3%A3o-corresponder-ao-tipo-de-redu%C3%A7%C3%A3o-por-valor-percentual](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226414900119-E0577-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-um-valor-percentual-de-redu%C3%A7%C3%A3o-de-base-de-c%C3%A1lculo-do-ISSQN-por-benef%C3%ADcio-municipal-se-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-n%C3%A3o-corresponder-ao-tipo-de-redu%C3%A7%C3%A3o-por-valor-percentual)  
> **ID:** `37226414900119` | **Última Atualização:** 2026-07-22T14:14:58Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226400282391)

 **MENSAGEM**

E0577 Rejeição: Não é permitido informar um valor percentual de redução de base de cálculo do ISSQN por benefício municipal, se o código de identificação do Benefício Municipal não corresponder ao tipo de redução por valor percentual.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226400282775)

 **SITUAÇÃO**

A **NFS-e (Nota Fiscal de Serviços Eletrônica) **foi emitida com a informação de** redução percentual da base de cálculo do ISSQN** vinculada a um benefício municipal incompatível com esse tipo de redução no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226400284311)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226414885399)

 Acesse as telas** ''Alíquotas de IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e localize a alíquota utilizada na operação que gerou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38266662163991)

 Na aba **''Tributação''**, verifique se o campo** ''Código de Classificação Tributária'' **informado está correto e se corresponde ao **''% da Redução de Alíquota Municipal''** conforme a legislação municipal aplicável.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226414890647)

 Caso o código de benefício não corresponda ao tipo de redução percentual, realize uma das seguintes ações:

- 

Altere o **''% da Redução de Alíquota Municipal'' **para um código que corresponda ao tipo de redução por valor percentual;

- 

Ou remova o **percentual de redução do ISSQN**, caso o benefício municipal não permita esse tipo de redução.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226400290967)

 Consulte seu **contador ou a legislação municipal** para confirmar qual é o código de benefício correto e o tipo de redução aplicável à operação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226400292247)

 Após realizar os ajustes necessários, salve as alterações e emita novamente a **NFS-e**.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226400293271)

 **CAUSA**

A rejeição ocorre porque a **Sefaz valida a consistência entre o código de benefício municipal informado e o tipo de redução aplicado**. Quando o sistema identifica que o **código de benefício não corresponde ao tipo de redução por valor percentual**, a nota é rejeitada para garantir que as informações fiscais estejam em conformidade com a legislação tributária municipal. Essa validação evita que sejam aplicados benefícios fiscais de forma incorreta ou incompatível com as regras estabelecidas pelo município.