# E0532 Rejeição: O campo que informa sobre a tributação do ISSQN deve ser "4 - Não Incidência", quando o serviço prestado for 99.01.01 - Serviços sem a incidência de ISSQN e ICMS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226043330199-E0532-Rejei%C3%A7%C3%A3o-O-campo-que-informa-sobre-a-tributa%C3%A7%C3%A3o-do-ISSQN-deve-ser-4-N%C3%A3o-Incid%C3%AAncia-quando-o-servi%C3%A7o-prestado-for-99-01-01-Servi%C3%A7os-sem-a-incid%C3%AAncia-de-ISSQN-e-ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226043330199-E0532-Rejei%C3%A7%C3%A3o-O-campo-que-informa-sobre-a-tributa%C3%A7%C3%A3o-do-ISSQN-deve-ser-4-N%C3%A3o-Incid%C3%AAncia-quando-o-servi%C3%A7o-prestado-for-99-01-01-Servi%C3%A7os-sem-a-incid%C3%AAncia-de-ISSQN-e-ICMS)  
> **ID:** `37226043330199` | **Última Atualização:** 2026-07-22T14:15:23Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043292951)

 MENSAGEM**

E0532 Rejeição: O campo que informa sobre a tributação do ISSQN deve ser "4 - Não Incidência", quando o serviço prestado for 99.01.01 - Serviços sem a incidência de ISSQN e ICMS.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043293847)

 SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviço Eletrônica) para um serviço classificado com o código **99.01.01 - Serviços sem a incidência de ISSQN e ICMS**, a nota é rejeitada pela Sefaz com a mensagem de erro E0532, indicando que o **código de tributação do ISSQN** não está configurado corretamente como **"4 - Não Incidência"**.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043296919)

 SOLUÇÃO**

Para corrigir a rejeição, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043300759)

 Acesse a tela **"Serviços"** (Configurações » Cadastros » Serviços) e localize o serviço que está sendo utilizado na nota fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226026952599)

 Na aba **''Alíquotas de ISS''**, verifique o campo **''Cód. Tributação ISS''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043304983)

 Certifique-se de que o campo **"Cód. Tributação ISS"** esteja preenchido com a opção **"07 - Não Tributado"**, pois este código corresponde à situação de **não incidência do ISSQN** para o serviço 99.01.01.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043306263)

 Verifique também se o campo **"Tipo de Serviço"** está vinculado ao código correto do tipo de serviço cadastrado na rotina de **"Cadastros de Lista de Serviços"**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043307671)

 Confirme que o campo **"Cód. Trib. Município NFS-e"** esteja preenchido com o código de tributação do município correspondente ao serviço 99.01.01. Este código deve ser solicitado na prefeitura do município emissor.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043308695)

 Salve as alterações realizadas no cadastro do serviço.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226026957847)

 Retorne à nota fiscal rejeitada, exclua o serviço da nota e lance-o novamente para que as novas configurações sejam aplicadas.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043314327)

 Transmita novamente a NFS-e para a Sefaz. 
 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226043317399)

 CAUSA**

A rejeição ocorre porque o **código de tributação do ISSQN** não está configurado corretamente no cadastro do serviço. Para serviços classificados como **99.01.01 - Serviços sem a incidência de ISSQN e ICMS**, é obrigatório que o campo **"Cód. Tributação ISS"** esteja preenchido com **"07 - Não Tributado"**, indicando a **não incidência do imposto**. Quando este campo está vazio ou preenchido com um código diferente, a Sefaz rejeita a nota com a mensagem E0532.