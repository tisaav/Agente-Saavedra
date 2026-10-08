# E0138 Rejeição: O CEP informado para o endereço nacional do prestador do serviço não existente ou não pertence ao município informado na DPS. Informe um CEP existente e que pertença ao município informado para o endereço do prestador do serviço na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222384457239-E0138-Rejei%C3%A7%C3%A3o-O-CEP-informado-para-o-endere%C3%A7o-nacional-do-prestador-do-servi%C3%A7o-n%C3%A3o-existente-ou-n%C3%A3o-pertence-ao-munic%C3%ADpio-informado-na-DPS-Informe-um-CEP-existente-e-que-perten%C3%A7a-ao-munic%C3%ADpio-informado-para-o-endere%C3%A7o-do-prestador-do-servi%C3%A7o-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222384457239-E0138-Rejei%C3%A7%C3%A3o-O-CEP-informado-para-o-endere%C3%A7o-nacional-do-prestador-do-servi%C3%A7o-n%C3%A3o-existente-ou-n%C3%A3o-pertence-ao-munic%C3%ADpio-informado-na-DPS-Informe-um-CEP-existente-e-que-perten%C3%A7a-ao-munic%C3%ADpio-informado-para-o-endere%C3%A7o-do-prestador-do-servi%C3%A7o-na-DPS)  
> **ID:** `37222384457239` | **Última Atualização:** 2026-07-22T14:17:52Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222384430871)

 **MENSAGEM**

E0138 Rejeição: O CEP informado para o endereço nacional do prestador do serviço não existente ou não pertence ao município informado na DPS. Informe um CEP existente e que pertença ao município informado para o endereço do prestador do serviço na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222384432151)

 **SITUAÇÃO**

Ao gerar o lote de uma **NFS-e**, o sistema apresenta a mensagem de rejeição informando que o **CEP cadastrado para o prestador do serviço** não existe ou não pertence ao município informado no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222384437783)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222368247191)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222368248343)

 Localize a **empresa prestadora do serviço** que emitiu a NFS-e rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222384442903)

 Na aba **"Endereços"**, verifique o **CEP** cadastrado para a empresa.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222368252055)

 Acesse o site dos ****[''Correios''](https://buscacepinter.correios.com.br/) e valide se o **CEP informado** está correto e corresponde ao **município cadastrado**:

- 

**Se o CEP estiver incorreto**, corrija-o no cadastro da empresa, informando o CEP válido conforme os Correios;

- 

**Se o CEP estiver correto, mas o município estiver divergente**, acesse a tela **“Cidades”** (Configurações » Cadastros » Endereços » Cidades) e verifique se o campo **“Mun. domicílio fiscal”** está preenchido corretamente com o **código IBGE** correspondente ao município.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222368252567)

 Para validar o **código IBGE do município**, acesse o site do ********[''IBGE''](https://cidades.ibge.gov.br/) e siga os passos abaixo:

- 

Digite o **nome da cidade** no campo de pesquisa;

- 

Localize a informação **“Código do Município”** na página da cidade;

- 

Retorne à tela **“Cidades”** e corrija o campo **“Mun. domicílio fiscal”** com o código obtido no site do IBGE.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222384447383)

 Após realizar as correções, retorne à **NFS-e rejeitada** e gere um novo lote de envio.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222368254487)

 Caso a rejeição persista, inutilize ou exclua a NFS-e e refaça o lançamento.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222368255511)

 **CAUSA**

A rejeição ocorre quando o **CEP informado no cadastro da empresa prestadora** não existe na base dos Correios ou quando o CEP não corresponde ao **município informado no documento fiscal**. Isso pode acontecer devido a:

- 

**CEP digitado incorretamente** no cadastro da empresa;

- 

**Código IBGE do município** cadastrado de forma divergente na tela **"Cidades"**;

- 

**Desatualização cadastral** do endereço da empresa no sistema.