# E0392 Rejeição: O grupo de informações de Atividade/Evento não é permitido quando o código de tributação nacional não pertencer ao item 12 da lista de serviços, com exceção do código 99.01.01.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225013461143-E0392-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-Atividade-Evento-n%C3%A3o-%C3%A9-permitido-quando-o-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-nacional-n%C3%A3o-pertencer-ao-item-12-da-lista-de-servi%C3%A7os-com-exce%C3%A7%C3%A3o-do-c%C3%B3digo-99-01-01](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225013461143-E0392-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-Atividade-Evento-n%C3%A3o-%C3%A9-permitido-quando-o-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-nacional-n%C3%A3o-pertencer-ao-item-12-da-lista-de-servi%C3%A7os-com-exce%C3%A7%C3%A3o-do-c%C3%B3digo-99-01-01)  
> **ID:** `37225013461143` | **Última Atualização:** 2026-07-22T14:16:18Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225013432087)

 **MENSAGEM**

E0392 Rejeição: O grupo de informações de Atividade/Evento não é permitido quando o código de tributação nacional não pertencer ao item 12 da lista de serviços, com exceção do código 99.01.01.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225029316119)

 **SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviço Eletrônica), o documento é rejeitado pela Sefaz porque **o grupo de informações de Atividade/Evento foi preenchido** para um serviço cujo **código de tributação nacional não pertence ao item 12 da lista de serviços** e também não é o código 99.01.01.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225029317399)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225013438615)

 Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225013441815)

 Localize o serviço utilizado na nota fiscal rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225013443863)

 Na aba **"Impostos"**, verifique o campo **"Tipo de Serviço"** e confirme qual código de tributação nacional está vinculado ao serviço.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225029323671)

 Confirme se o código pertence ao **item 12 da lista de serviços** ou se corresponde ao **código 99.01.01**.

- 

**Caso o código não pertença ao item 12 e não seja 99.01.01:**
Remova as informações do **grupo Atividade/Evento**, pois elas foram preenchidas indevidamente.

1. 

**Caso o código pertença ao item 12 ou seja 99.01.01:**
Mantenha as informações do **grupo Atividade/Evento**, assegurando que estejam preenchidas corretamente.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225029324823)

 Caso necessário, acesse a tela** “Alíquotas de ISS” **(Configurações » Cadastros » Produtos » Alíquotas de ISS) e verifique o campo** “Cód. Trib. Município”**, confirmando se o **código de tributação municipal** informado está correto.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225013448087)

 Consulte o portal da prefeitura do município** **(exemplo: Ginfes) para verificar a **lista completa de serviços** e confirmar se o **código utilizado está correto** e se **pertence ao item 12 da lista de serviços**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37697936366231)

 Após realizar os ajustes necessários, emita novamente a NFS-e.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225013451159)

 **CAUSA**

A rejeição ocorre porque **o grupo de informações de Atividade/Evento foi preenchido** para um serviço cujo **código de tributação nacional não pertence ao item 12 da lista de serviços** e também não é o código especial 99.01.01. Segundo as regras da Sefaz, este grupo de informações **somente pode ser preenchido** quando o serviço estiver classificado no item 12 da lista de serviços ou quando for utilizado o código 99.01.01.