# E0272 Rejeição: CPF do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CPF e CNC NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223192434199-E0272-Rejei%C3%A7%C3%A3o-CPF-do-emitente-intermedi%C3%A1rio-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CPF-e-CNC-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223192434199-E0272-Rejei%C3%A7%C3%A3o-CPF-do-emitente-intermedi%C3%A1rio-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CPF-e-CNC-NFS-e)  
> **ID:** `37223192434199` | **Última Atualização:** 2026-07-22T14:16:59Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223176010775)

 **MENSAGEM**

E0272 Rejeição: CPF do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CPF e CNC NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223192409751)

 **SITUAÇÃO**

Durante a emissão de uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** com intermediário, o documento fiscal é rejeitado na transmissão quando as informações do intermediário indicam que ele não possui estabelecimento ou domicílio fiscal no mesmo município do emissor, considerando a data de competência informada na DPS.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223192410135)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223176012055)

 Consulte o **cadastro do CPF do intermediário** nos sistemas oficiais da Receita Federal para verificar qual é o **município de domicílio fiscal** registrado na data de competência da nota.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223192411415)

 Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223176014231)

 Localize o cadastro do intermediário envolvido na emissão da NFS-e.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223176016663)

 Na aba **“Endereço”**, verifique o campo **“Cód. Cidade”** do cadastro do intermediário e confirme se ele está vinculado corretamente ao município de domicílio fiscal validado no passo 1.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223176017687)

 Acesse a tela ****[''Cidades''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223176019479)

 Localize a cidade identificada no cadastro do intermediário.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223192420119)

 Na aba **"Geral"**, verifique o campo **"Mun. Domicílio Fiscal"** e confirme se o código está correto.

- 

Se necessário, consulte o código oficial do município no site do ****[''IBGE''](https://cidades.ibge.gov.br/)**.**

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223176021655)

 Corrija o campo **"Mun. Domicílio Fiscal"** com o código correto do município, caso esteja divergente.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37785244597783)

 Certifique-se de que o **município do intermediário** corresponde ao **município emissor da NFS-e**, conforme exigido pela validação da SEFAZ.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38495579187735)

 Após realizar os ajustes necessários, reemita a **NFS-e** para o destinatário.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223176023831)

 **CAUSA**

A rejeição é retornada pela **SEFAZ** quando o **CPF do emitente intermediário** informado na NFS-e não possui estabelecimento ou domicílio fiscal cadastrado no mesmo município do emissor da nota, na data de competência informada na DPS. Essa validação é realizada com base nos **cadastros CPF e CNC (Cadastro Nacional de Contribuintes)** da NFS-e, garantindo a conformidade fiscal e a correta identificação do intermediário no processo de prestação de serviços.


---

### 🔗 Links e Referências Internas:

- [''Cidades''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)