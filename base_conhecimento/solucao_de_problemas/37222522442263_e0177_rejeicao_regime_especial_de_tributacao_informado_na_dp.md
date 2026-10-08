# E0177 Rejeição: Regime especial de tributação informado na DPS não é admitido na parametrização do município de incidência do ISSQN.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222522442263-E0177-Rejei%C3%A7%C3%A3o-Regime-especial-de-tributa%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-%C3%A9-admitido-na-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222522442263-E0177-Rejei%C3%A7%C3%A3o-Regime-especial-de-tributa%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-%C3%A9-admitido-na-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN)  
> **ID:** `37222522442263` | **Última Atualização:** 2026-07-22T14:17:42Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222522435735)

 **MENSAGEM**

E0177 Rejeição: Regime especial de tributação informado na DPS não é admitido na parametrização do município de incidência do ISSQN.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222507529111)

 **SITUAÇÃO**

Ao emitir uma **NFS-e**, a nota é rejeitada pela prefeitura com a mensagem de erro informando que o **regime especial de tributação** configurado não é permitido para o município de incidência do ISSQN.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222522436887)

 **SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222522437271)

  Acesse a tela **"Empresa"** (Configurações » Empresa » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222507529495)

 Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"** sub-aba **"Geral"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222507529751)

 No campo **"Regime esp. trib. ISS (NFS-e)"**, verifique qual regime especial de tributação está configurado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222522438807)

 Consulte o **manual da prefeitura** do município de incidência do ISSQN para identificar quais regimes especiais de tributação são admitidos. Os regimes disponíveis no sistema podem variar conforme o município, incluindo opções como:

- 

**''Microempresa municipal''**

- 

**''Estimativa''**

- 

**''Sociedade de profissionais''**

- 

**''Cooperativa''**

- 

**''Microempresário e Empresa de Pequeno Porte (ME EPP)''**

- 

**''Microempresário Individual (MEI)''**

- 

**''ISSQN Profissionais Autônomos''**

- 

**''Movimento Mensal''**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222507530647)

 Altere o campo **"Regime esp. trib. ISS (NFS-e)"** para um código de regime especial que seja **compatível com a parametrização do município** de incidência do ISSQN.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37810552623895)

 Salve as alterações e tente emitir novamente a **NFS-e**.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222522439063)

 **CAUSA**

A rejeição ocorre porque o **regime especial de tributação do ISS** configurado nas **Preferências da Empresa** não é permitido pela prefeitura do município de incidência informado na nota fiscal. Cada município possui suas próprias regras e **aceita apenas determinados códigos de regime especial**, conforme sua legislação tributária local.