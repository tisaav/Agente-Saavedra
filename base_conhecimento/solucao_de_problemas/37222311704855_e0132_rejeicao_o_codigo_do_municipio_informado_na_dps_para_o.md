# E0132 Rejeição: O código do município informado na DPS para o endereço do prestador do serviço, identificado pelo CNPJ, não corresponde ao município registrado em seus cadastros na data de competência informada na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222311704855-E0132-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-prestador-do-servi%C3%A7o-identificado-pelo-CNPJ-n%C3%A3o-corresponde-ao-munic%C3%ADpio-registrado-em-seus-cadastros-na-data-de-compet%C3%AAncia-informada-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222311704855-E0132-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-prestador-do-servi%C3%A7o-identificado-pelo-CNPJ-n%C3%A3o-corresponde-ao-munic%C3%ADpio-registrado-em-seus-cadastros-na-data-de-compet%C3%AAncia-informada-na-DPS)  
> **ID:** `37222311704855` | **Última Atualização:** 2026-07-22T14:17:55Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222344469783)

 **MENSAGEM**

E0132 Rejeição: O código do município informado na DPS para o endereço do prestador do serviço, identificado pelo CNPJ, não corresponde ao município registrado em seus cadastros na data de competência informada na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222311689495)

 **SITUAÇÃO**

Ao tentar emitir uma **Declaração de Prestação de Serviços (DPS)**, o sistema apresenta a rejeição E0132, indicando que o **código do município do prestador** informado no documento **não corresponde ao município cadastrado** na base de dados da Sefaz para o CNPJ do prestador na data de competência da DPS.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222344471191)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222311691671)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize a empresa prestadora do serviço que está emitindo a DPS.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222311692439)

 Na aba **"Endereço"**, verifique o campo **"Cód. Cidade"** vinculado ao endereço principal da empresa.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222311692567)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e localize a cidade identificada no passo anterior.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222344478999)

 Verifique se o campo **"Mun. domicílio fiscal"** está preenchido corretamente com o código ****[''IBGE''](https://cidades.ibge.gov.br/) do município:

- 

Digite o nome da cidade na pesquisa;

- 

Localize a informação **"Código do Município"** na página da cidade.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222344479639)

 Caso o código esteja incorreto, retorne o passo 3 e 4 e corrija o campo "Mun. domicílio fiscal"** **com o código obtido no site do IBGE.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222311694103)

 Consulte o cadastro da empresa junto à Sefaz para confirmar qual município consta registrado oficialmente para o CNPJ do prestador na data de competência da DPS.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222344481559)

 Caso necessário, atualize o cadastro da empresa junto à Sefaz para que o município corresponda ao endereço correto do prestador.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222344482583)

 Após realizar os ajustes necessários, retorne à DPS e gere um novo lote de envio.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222344483351)

 **CAUSA**

Esta rejeição ocorre quando existe **divergência entre o código do município** informado no cadastro da empresa prestadora no sistema e o **município registrado na base de dados da Sefaz** para o CNPJ do prestador. A validação considera a data de competência informada na DPS, garantindo que o endereço do prestador esteja atualizado e corresponda aos registros oficiais no momento da prestação do serviço.


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)