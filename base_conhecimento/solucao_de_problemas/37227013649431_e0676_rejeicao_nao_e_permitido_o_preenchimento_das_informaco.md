# E0676 Rejeição: Não é permitido o preenchimento das informações relativas aos tributos federais quando o emitente for identificado como MEI na data de competência informada na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37227013649431-E0676-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-das-informa%C3%A7%C3%B5es-relativas-aos-tributos-federais-quando-o-emitente-for-identificado-como-MEI-na-data-de-compet%C3%AAncia-informada-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37227013649431-E0676-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-das-informa%C3%A7%C3%B5es-relativas-aos-tributos-federais-quando-o-emitente-for-identificado-como-MEI-na-data-de-compet%C3%AAncia-informada-na-DPS)  
> **ID:** `37227013649431` | **Última Atualização:** 2026-09-04T09:30:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227013577367)

 **MENSAGEM**

E0676 Rejeição: Não é permitido o preenchimento das informações relativas aos tributos federais quando o emitente for identificado como MEI na data de competência informada na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227013579287)

 **SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** com informações de **tributos federais** (CBS - Contribuição sobre Bens e Serviços), sendo que a empresa emitente está cadastrada como **Microempreendedor Individual (MEI)** na data de competência informada no documento fiscal, o sistema da Sefaz rejeita a operação com a mensagem E0676.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226999441943)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226999444119)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresa) e localize o cadastro da empresa emitente.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37618384102423)

 Na aba **''Naturezas''**, verifique se a empresta está cadastrada como MEI **(Microempreendedor Individual) **no campo** ''Cód. Regime Tribut'' **ou em campos relacionados ao enquadramento fiscal.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227013608471)

 Caso a empresa seja **MEI**, não preencha as informações de **tributos federais (CBS)** no documento fiscal, pois empresas enquadradas neste regime **não estão sujeitas** à tributação federal nos moldes da Reforma Tributária.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37618384112663)

 Acesse a tela **"Alíquota IBS'' **(Livros Fiscais » Cadastros » Aliquotas de IBS) e** ''Alíquota CBS'' **(Livros Fiscais » Cadastros » Aliquotas de CBS), e verifique se há alíquotas de CBS configuradas para os produtos ou serviços da operação.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37618384114711)

 Remova ou desative as alíquotas de **CBS** vinculadas aos produtos/serviços quando a empresa emitente for **MEI**, garantindo que o campo **"Código de situação tributária'' (CST) **esteja configurado adequadamente para **''não tributação''** ou **''isenção''**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37618430417047)

 Após realizar os ajustes necessários, emita novamente o documento fiscal. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227013632535)

 **CAUSA**

A rejeição ocorre porque **empresas enquadradas como MEI** (Microempreendedor Individual) **não estão sujeitas** ao recolhimento de tributos federais nos moldes da Reforma Tributária, como a **CBS**. Quando o sistema identifica que o emitente é **MEI** na data de competência do documento e detecta o preenchimento de informações de tributos federais, a Sefaz rejeita automaticamente a operação para garantir a conformidade com a legislação tributária vigente.