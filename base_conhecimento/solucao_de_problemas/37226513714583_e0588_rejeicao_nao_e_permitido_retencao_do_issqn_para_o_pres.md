# E0588 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que tenha algum regime especial de tributação na data de competência informada na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226513714583-E0588-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-para-o-prestador-do-servi%C3%A7o-que-tenha-algum-regime-especial-de-tributa%C3%A7%C3%A3o-na-data-de-compet%C3%AAncia-informada-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226513714583-E0588-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-para-o-prestador-do-servi%C3%A7o-que-tenha-algum-regime-especial-de-tributa%C3%A7%C3%A3o-na-data-de-compet%C3%AAncia-informada-na-DPS)  
> **ID:** `37226513714583` | **Última Atualização:** 2026-07-22T14:14:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226499041303)

 **MENSAGEM**

E0588 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que tenha algum regime especial de tributação na data de competência informada na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226499042199)

 **SITUAÇÃO**

Ao tentar emitir uma NFS-e, o sistema apresenta a mensagem de rejeição informando que **não é permitida a retenção do ISSQN** quando o prestador do serviço possui algum **regime especial de tributação** configurado na data de competência da nota.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226513692055)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226499047959)

 Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226513696407)

 Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, verifique o campo **"Regime esp. trib. ISS (NFS-e)" **e identifique qual regime especial está configurado para a empresa.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226513698199)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226513701655)

 Na aba **''Fiscal''**, desabilite o campo **''Retém ISS''**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226513702679)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226499054999)

 Na aba **"NFS-e"**, verifique se o campo **"Cód. Natureza Oper. ISS (NFS-e)"** está configurado corretamente para operações sem retenção.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38223883089815)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38223883091863)

 No rodapé, verifique a aba **''Impostos''**, verifique se o campo** ''****Tipo de Retenção do ISS''** está configurado como **''Não Retido''**.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38223891431191)

 Após realizar os ajustes, tente emitir novamente a NFS-e. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226499055895)

 **CAUSA**

A rejeição ocorre porque a **legislação municipal não permite** que empresas prestadoras de serviço com **regime especial de tributação do ISS** (como Microempresa Municipal, Estimativa, Sociedade de Profissionais, Cooperativa, MEI, Simples Nacional, entre outros) efetuem a **retenção do ISSQN** na nota fiscal. Quando o sistema identifica que a empresa possui um regime especial configurado e, simultaneamente, está marcada a retenção de ISS no cadastro do tomador ou na operação, a nota é rejeitada pela prefeitura.