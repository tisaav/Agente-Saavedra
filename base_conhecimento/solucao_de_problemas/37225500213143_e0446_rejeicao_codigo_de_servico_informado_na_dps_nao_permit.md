# E0446 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por valor monetário.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225500213143-E0446-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-servi%C3%A7o-informado-na-DPS-n%C3%A3o-permite-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-na-base-de-c%C3%A1lculo-do-ISSQN-por-valor-monet%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225500213143-E0446-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-servi%C3%A7o-informado-na-DPS-n%C3%A3o-permite-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-na-base-de-c%C3%A1lculo-do-ISSQN-por-valor-monet%C3%A1rio)  
> **ID:** `37225500213143` | **Última Atualização:** 2026-07-22T14:15:55Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225516789271)

 **MENSAGEM**

E0446 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por valor monetário.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225516789527)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviço Eletrônica)**, o usuário configurou no sistema um **percentual de dedução ou redução na base de cálculo do ISSQN** por valor monetário. Porém, o **código de serviço** informado na DPS (Declaração de Prestação de Serviços) **não permite** esse tipo de dedução conforme as regras estabelecidas pela legislação municipal. Ao tentar transmitir a nota, a Sefaz rejeitou o documento com a mensagem de erro acima.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225516790423)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225500203671)

 Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225516791447)

 Localize o **serviço** que está sendo utilizado na NFS-e rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225516791831)

 Na aba **''Impostos''** no campo **"Cód. Trib. Município NFS-e"**, verifique o **''Código de Tributação do Município''** vinculado ao serviço.

- 

Confirme junto á prefeitura municipal se este código permite dedução ou redução na base de cálculo do ISSQN por valor monetário.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225516792983)

 Caso o código de serviço **não permita dedução**, remova o percentual informado no campo **"Perc. de dedução na base do ISS"** no cadastro do serviço, deixando-o zerado ou em branco.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225500205463)

  Ajuste também o campo **"Tipo de dedução de base do ISS"**, selecionando a opção adequada conforme a legislação municipal, como:

- 

**07 - Não Tributado**

- 

**06 - Isento**

- 

**00 - Tributado**

- 

**Ou outra opção que não envolva dedução por valor monetário**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225500206871)

 Salve as alterações realizadas no **cadastro do serviço**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225500207383)

 Retorne à **NFS-e rejeitada** e refaça a emissão do documento, garantindo que **nenhum valor de dedução** seja aplicado na base de cálculo do ISSQN.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225500207383)

 Transmita novamente a **NFS-e** para a Sefaz.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225516802199)

 **CAUSA**

A rejeição ocorre porque o **código de serviço** informado na DPS **não está habilitado** pela legislação municipal para permitir **dedução ou redução na base de cálculo do ISSQN por valor monetário**. Cada município possui **regras específicas** sobre quais serviços podem ter deduções aplicadas, e quando o sistema tenta transmitir uma nota com dedução para um código de serviço que não a permite, a **Sefaz rejeita** o documento com o erro E0446.