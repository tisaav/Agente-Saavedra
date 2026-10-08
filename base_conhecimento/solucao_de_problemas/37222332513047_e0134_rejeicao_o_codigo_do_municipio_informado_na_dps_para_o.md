# E0134 Rejeição: O código do município informado na DPS para o endereço do prestador do serviço, identificado pelo CPF, não corresponde ao município registrado em seus cadastros na data de competência informada na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222332513047-E0134-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-prestador-do-servi%C3%A7o-identificado-pelo-CPF-n%C3%A3o-corresponde-ao-munic%C3%ADpio-registrado-em-seus-cadastros-na-data-de-compet%C3%AAncia-informada-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222332513047-E0134-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-prestador-do-servi%C3%A7o-identificado-pelo-CPF-n%C3%A3o-corresponde-ao-munic%C3%ADpio-registrado-em-seus-cadastros-na-data-de-compet%C3%AAncia-informada-na-DPS)  
> **ID:** `37222332513047` | **Última Atualização:** 2026-07-22T14:17:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222332503319)

 **MENSAGEM**

E0134 Rejeição: O código do município informado na DPS para o endereço do prestador do serviço, identificado pelo CPF, não corresponde ao município registrado em seus cadastros na data de competência informada na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222334824471)

 **SITUAÇÃO**

Ao tentar emitir uma **Declaração de Prestação de Serviços (DPS)**, o sistema apresenta a mensagem de rejeição informando que o **código do município do prestador** não corresponde ao município cadastrado na base de dados da Sefaz para a data de competência informada no documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222332505111)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222334825623)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize a **empresa prestadora do serviço** identificada na DPS rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222332507159)

 Na aba **"Endereço"**, verifique o **código da cidade** cadastrado para o endereço do prestador.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222332507543)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e localize a cidade identificada no passo anterior.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222334828823)

 Verifique o conteúdo do campo **"Mun. domicílio fiscal"** e certifique-se de que está preenchido corretamente com o **código do município conforme tabela do IBGE**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222332508951)

 Consulte o código correto do município no site oficial do ****[''IBGE''](https://cidades.ibge.gov.br/):

- 

No campo **"Pesquisar"**, digite o nome da cidade do prestador

- 

Localize a informação **"Código do Município"** na página da cidade

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222334829591)

 Retorne à tela "Cidades" (Configurações » Cadastros » Endereços » Cidades) e corrija o campo "Mun. domicílio fiscal" com o código obtido no site do IBGE.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37826936140055)

 Verifique também se o cadastro do prestador na **Sefaz** está atualizado com o mesmo município. Caso necessário, solicite ao contador a **atualização cadastral junto à Receita Federal**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222334830871)

 Após realizar os ajustes necessários, acesse a tela ****[''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas), e redigite os dados do cabeçalho da DPS e gere um novo lote de envio.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222332511639)

 Caso a rejeição persista, **inutilize ou exclua a DPS rejeitada** e **refaça o lançamento**, garantindo que todos os dados estejam corretamente informados.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222334832023)

 **CAUSA**

Esta rejeição ocorre quando o **código do município informado no cadastro do prestador** no sistema está **divergente do código do município** que consta nos cadastros da Sefaz para o mesmo prestador na data de competência da DPS. A divergência pode ocorrer por:

- 

Código do município cadastrado incorretamente no campo **"Mun. domicílio fiscal"** da tela de Cidades

- 

Código do município não preenchido no cadastro

- 

Desatualização cadastral do prestador junto à Receita Federal

- 

Mudança de endereço do prestador não atualizada nos sistemas oficiais


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)
- [''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)