# E0212 Rejeição: CPF do emitente tomador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CPF e CNC NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222705182743-E0212-Rejei%C3%A7%C3%A3o-CPF-do-emitente-tomador-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CPF-e-CNC-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222705182743-E0212-Rejei%C3%A7%C3%A3o-CPF-do-emitente-tomador-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CPF-e-CNC-NFS-e)  
> **ID:** `37222705182743` | **Última Atualização:** 2026-07-22T14:17:32Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222719973527)

 **MENSAGEM**

E0212 Rejeição: CPF do emitente tomador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CPF e CNC NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222705174423)

 **SITUAÇÃO**

Ao emitir uma **NFS-e**, o sistema retorna a rejeição **E0212** informando que o **CPF do emitente tomador** não possui estabelecimento ou domicílio cadastrado no município emissor da nota fiscal. Esta validação é realizada pela **SEFAZ** no momento da transmissão do documento, confrontando os dados informados na DPS com as informações constantes nos cadastros oficiais **CPF e CNC**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222705175191)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222719975703)

 Verifique o **cadastro do tomador** nos sistemas oficiais da Receita Federal:

- 

****[''Cadastro Centralizado de Contribuinte (CCC)''](https://dfe-portal.svrs.rs.gov.br/NFE/CCC)

- 

****[''SINTEGRA''](http://www.sintegra.gov.br/.)**.**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222719977111)

 Confirme se o **CPF do tomador** possui estabelecimento ou domicílio fiscal cadastrado no município emissor da nota fiscal na data de competência informada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222719978135)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e verifique se o campo **"Mun. domicílio fiscal"** está preenchido corretamente com o código do município correspondente. 

- 

Consulte o **código do município** no site do ****[''IBGE''](https://cidades.ibge.gov.br/).

- 

Digite o nome da cidade na pesquisa e localize a informação **"Código do Município"**.

- 

Corrija o campo "Mun. domicílio fiscal" com o código identificado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222705177495)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do tomador envolvido na NFS-e rejeitada.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222705178775)

 Na aba **"Endereço"**, verifique se o **"Cód.Cidade"** do tomador está correto e corresponde ao município emissor da nota fiscal.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222719993111)

 Caso necessário, ajuste os dados cadastrais do tomador conforme as informações consultadas nos sistemas oficiais da Receita Federal.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222705179543)

 Após realizar as correções necessárias, reemita a **NFS-e** para o tomador. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222705180183)

 **CAUSA**

A rejeição **E0212** é retornada pela **SEFAZ** quando o **CPF do emitente tomador** informado na DPS não possui estabelecimento ou domicílio fiscal cadastrado no município emissor da nota fiscal, na data de competência informada. Esta validação ocorre através do cruzamento de dados com os cadastros oficiais **CPF e CNC NFS-e**, garantindo que apenas contribuintes regularmente estabelecidos no município possam emitir documentos fiscais.


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)