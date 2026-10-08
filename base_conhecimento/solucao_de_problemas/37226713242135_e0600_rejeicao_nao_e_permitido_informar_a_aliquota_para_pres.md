# E0600 Rejeição: Não é permitido informar a alíquota para prestador de serviço optante do simples nacional do tipo MEI.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226713242135-E0600-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-a-al%C3%ADquota-para-prestador-de-servi%C3%A7o-optante-do-simples-nacional-do-tipo-MEI](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226713242135-E0600-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-a-al%C3%ADquota-para-prestador-de-servi%C3%A7o-optante-do-simples-nacional-do-tipo-MEI)  
> **ID:** `37226713242135` | **Última Atualização:** 2026-07-22T14:14:42Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226713220503)

 **MENSAGEM**

E0600 Rejeição: Não é permitido informar a alíquota para prestador de serviço optante do simples nacional do tipo MEI.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226713224087)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviço Eletrônica)** para uma empresa prestadora de serviços que é **optante pelo Simples Nacional** e enquadrada como **MEI (Microempreendedor Individual)**, o sistema rejeitou o documento fiscal com a mensagem de erro E0600.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226698491287)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226713228055)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize a empresa prestadora do serviço.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37622002656791)

 Na aba **"Naturezas"** verifique:

- 

Se a marcação **"Optante pelo SIMPLES"** está habilitada

- 

Se o campo **"Cód. Regime Tribut."** está configurado como **"Simples Nacional"** ou **"Simples Nacional - Sublimite"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37621993066647)

 Confirme se o campo **"Regime Especial trib. ISS (NFS-e)"** está preenchido com o código **"5 - Microempresário Individual (MEI)"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226713230103)

 Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa) e verifique na aba **"SIMPLES Nacional"** qual cadastro de **"Partilha/Anexo do Simples Nacional"** está vinculado à empresa.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226713230743)

 Acesse a tela **"Partilha/Anexo do Simples Nacional"** (Comercial » Arquivo » Cadastros » Alíquotas » Partilha/Anexo do Simples Nacional) e verifique se o cadastro da partilha está correto, com o **percentual de ISS** devidamente informado.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226698506007)

 Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço), na aba **''Impostos''**, verifique se o campo **"Tipo de Partilha/anexo"** está preenchido.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226713232919)

 Acesse a tela **"Alíquota de ISS"** (Contratos e Serviços » Arquivos » Cadastros » Alíquotas de ISS), certifique-se de que **não há alíquota de ISS informada manualmente**.

- 

Para empresas optantes pelo Simples Nacional do tipo MEI, o sistema deve desconsiderar essas configurações e utilizar apenas as informações da partilha.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226698507799)

 Após realizar as verificações e ajustes necessários, emita novamente a **NFS-e**. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226698509079)

 **CAUSA**

A rejeição ocorre porque **empresas optantes pelo Simples Nacional enquadradas como MEI** não devem ter alíquotas de ISS informadas diretamente no cadastro de serviços ou na tela de alíquotas. Para este regime tributário, o sistema deve buscar automaticamente as informações de tributação a partir do cadastro de **"Partilha/Anexo do Simples Nacional"** vinculado à empresa nas **"Preferências da Empresa"**. Quando uma alíquota é informada manualmente, o sistema identifica uma inconsistência com as regras fiscais aplicáveis ao MEI e rejeita o documento com a mensagem E0600.