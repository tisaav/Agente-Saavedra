# Tabelas para cálculo de frete

> **Módulo:** Comercial e Vendas | **Subseção:** Comercial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599534-Tabelas-para-c%C3%A1lculo-de-frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599534-Tabelas-para-c%C3%A1lculo-de-frete)  
> **ID:** `360044599534` | **Última Atualização:** 2026-07-29T14:22:14Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311806363543)

 Módulo:** Comercial > Arquivo > Cadastros              
```

Esta tela é destinada ao cadastro de tabelas de preços das transportadoras, que têm a intenção de sugerir e aplicar o cálculo de frete para um pedido ou nota fiscal em análise. 

Para facilitar sua navegação, acesse os links abaixo:

[Aba Região p/ tabela de Frete](#abaregi%C3%A3op/tabeladefrete)                                                   [Aba Rotas](#abarotas)   

[Aba Transportadora](#abatransportadora)

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409291730967)

Para realizar o cadastro de uma nova tabela, preencha o campo **"Cód. Cálculo de Frete"**, que pode ser realizado de forma automática ou manual, sendo que esta definição será efetuada por meio da opção **"Numeração"** localizada no botão **"Configuração da Tela"**. 

Informe, em seguida, a **"Descrição" **da tabela que está sendo cadastrada. Esta é uma informação obrigatória e tem a função de identificar a tabela, facilitando sua futura localização. 

O campo **"Observação"** é destinado à inclusão de alguma informação específica da tabela, que a caracterize perante as demais que vieram a ser cadastradas.

No campo **"Serviço Correios"** informe qual tipo de serviço de entrega prestado pelos Correios que atenderá a necessidade da empresa em seu frete, como por exemplo, o serviço Sedex 10, PAC, entre outros. Sendo que, estes serviços deverão estar previamente cadastrados na tela de [Serviço Correios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594734-Servi%C3%A7o-Correios).

Por meio do campo **"Rateio frete"** você pode definir a forma de distribuição do frete na formulação da ordem de despacho, de acordo com as opções abaixo:

- Valor da nota;

- Metro cúbico;

- Peso. 

[[voltar ao topo]](#top)

### 
Aba Região p/ tabela de Frete

Esta aba é dividida em duas grades, sendo a primeira destinada ao cadastro das Regiões e a segunda às Cidades referentes a cada Região cadastrada.

No campo** "Cód. Região"** é apresentado o código da região.

Informe a** "Região"** com sua descrição.

Preencha no campo** "Cód. Cidade"** a cidade relacionada à Região anteriormente informada. 

[[voltar ao topo]](#top)

### 
Aba Rotas

Nesta aba defina a Origem e o Destino da Rota, traçando-a por Cidade, Parceiro, Estado e Região.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409291890967)

Informe os campos** "Cidade Origem"**, **"Parceiro Origem"**, **"Estado Origem"**, **"Região Origem"**, **"Cidade Destino"**, **"Parceiro Destino"**, **"Estado Destino" **e **"Região Destino" **da Rota.

No campo** "Evento"** informe o evento relacionado à rota cadastrada; para o preenchimento deste campo, é necessário a realização de um cadastro prévio dos eventos na tela [Eventos para Cálculo de Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603334-Eventos-para-C%C3%A1lculo-de-Frete).

O Evento acima informado se tornará obrigatório nos cálculos de frete na [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973), se a marcação **"Obrigatório?"** estiver assinalada.

**Importante:** para efetuar a rotina de [Simulação de frete com escolha de transportadora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#simulaodefretecomescolhadetransportadora), por meio do botão [Outras opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top) da tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), a marcação Obrigatório? deve estar acionada.

Preencha a **"Distância"** para o correto cálculo da **"Origem"** e do **"Destino"**.

O campo** "Valor"** é destinado ao preenchimento do valor do frete.

Também preencha o** "Vlr Mínimo de Frete"**.

Defina a** "Unidade de Tempo"** a ser gasta para a rota em questão; que podem ser:

- Minutos;

- Horas;

- Dias.

No campo** "Tempo"** informe o tempo destinado à execução da Rota, de acordo com a Unidade de Tempo.

Preencha o** "Percentual"** a ser utilizado nos cálculos de frete.

Selecione a **"Via"**, pela qual a rota será executada, conforme as opções abaixo:

- 
Marítima;

- Aérea;

- Rodoviária;

- Ferroviária.

O campo** "Fórmula"** é destinado à montagem da fórmula de acordo com as variáveis disponíveis, que serão apresentadas no pop-up **"Fórmulas disponíveis" **ao clicar no botão 

![botão-Fx-construtor.FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/16678043177751)

** "f(x) Construtor"**. São elas:

- Valor;

- Percentual;

- Valor Mínimo;

- Unid. Tempo;

- Tempo;

- Distância;

- Valor da Nota;

- Peso Bruto da Nota;

- Metro Cúbico da Nota;

- Valor de Outro Evento.

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409308848407)

[[voltar ao topo]](#top)

### 
Aba Transportadora

Nesta aba informe o Parceiro Transportadora responsável pela prestação do serviço.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4409291921303)

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Serviço Correios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594734-Servi%C3%A7o-Correios)
- [Eventos para Cálculo de Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603334-Eventos-para-C%C3%A1lculo-de-Frete)
- [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973)
- [Simulação de frete com escolha de transportadora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#simulaodefretecomescolhadetransportadora)
- [Outras opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)