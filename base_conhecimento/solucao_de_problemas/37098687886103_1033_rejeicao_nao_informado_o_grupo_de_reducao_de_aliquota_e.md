# 1033 Rejeição: Não informado o grupo de redução de alíquota Estadual [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37098687886103-1033-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Estadual-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37098687886103-1033-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Estadual-nItem-999)  
> **ID:** `37098687886103` | **Última Atualização:** 2026-07-22T14:20:12Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098695793047)

 **MENSAGEM**

1033 Rejeição: Não informado o grupo de redução de alíquota Estadual [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098695793943)

 **SITUAÇÃO**

Ao tenta emitir uma nota fiscal eletrônica (NF-e) com produtos que possuem redução de alíquota estadual do IBS (Imposto sobre Bens e Serviços), não foi informado corretamente o grupo de redução de alíquota estadual no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098687877399)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098695795095)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098695795351)

 Verifique se o **CST **configurado para o produto está correto e se é compatível com a operação que envolve redução de alíquota estadual.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098695795991)

 Certifique-se de que os campos estejam preenchidos com o percentual correto de redução:

- 

CBS: **''% da Redução de Alíquota CBS''**

- 

IBS: **''% da Redução de Alíquota IBS Estadual''**

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098695796759)

 Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098695797655)

 Na seção** ''NF-e''**, verifique se o campo** ''Cód. de Benefício Fiscal na UF''** está preenchido com o código correto conforme legislação da UF.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098687882775)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37968325370903)

 Na aba **"Impostos"**, verifique se a configuração está correta para a operação que envolve redução de alíquota estadual.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37968324133783)

 Após realizar as correções, gere a nota fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37098687883543)

 **CAUSA**

Esta rejeição ocorre devido à implementação da Reforma Tributária (Lei Complementar 214 de 16 de janeiro de 2025), que estabelece a obrigatoriedade de informar o grupo de redução de alíquota estadual do IBS quando aplicável.

Conforme as regras de validação da SEFAZ, quando um produto possui redução de alíquota estadual do IBS, é necessário informar corretamente o grupo de redução no documento fiscal, incluindo o percentual de redução e o código de benefício fiscal correspondente. A ausência dessas informações resulta na rejeição da nota fiscal.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)