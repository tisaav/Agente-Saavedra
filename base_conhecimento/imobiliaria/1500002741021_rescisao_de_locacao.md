# Rescisão de Locação

> **Módulo:** Imobiliária | **Subseção:** Imobiliária  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002741021-Rescis%C3%A3o-de-Loca%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002741021-Rescis%C3%A3o-de-Loca%C3%A7%C3%A3o)  
> **ID:** `1500002741021` | **Última Atualização:** 2026-07-29T14:06:55Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311297335703)

 **Módulo:** Imobiliária > Rotinas > Locação

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311297336983)

 **Versão disponível:** a partir da 3.31
```

Através dessa tela, você efetiva uma rescisão do [Contrato de Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o) e disponibiliza o Imóvel para um novo aluguel ou venda.

Os links abaixo facilitarão sua navegação nas funcionalidades dessa rotina:

[Painel de Filtros](#paineldefiltros)[Painel Principal](#painelprincipal)

[Aba Geral](#abageral)[Aba Detalhamentos de Rescisão](#abadetalhamentosderescis%C3%A3o)

[Botão Outras Opções...](#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)[Dedução do IRRF](#dedu%C3%A7%C3%A3odoIRRF)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500002769562)

### 
Painel de Filtros

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500002770282)

Através do Painel de Filtros, você consegue criar filtros personalizados ou filtrar os resultados que serão exibidos nessa tela de acordo com os campos **"Código"**, **"Dt. Rescisão"** e **"Contrato de Locação"**.

**Nota:** os campos **"Gerou Rescisão"** e **"Estágio do Contrato"** são de preenchimento obrigatório para que o filtro escolhido seja aplicado.

[[voltar ao topo]](#top)

### 
Painel Principal

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500002798001)

Nesse Painel, você deve preencher alguns campos. Abaixo, falamos sobre cada um deles:

O campo **"Estágio do Contrato"** é atualizado automaticamente, conforme for atualizado o Contrato de Locação.

Você pode configurar o campo **"Código"** para ser gerado de forma automática ou manual, através do botão 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500002798641)

 **"Configuração da Tela"**, opção **"Numeração"**.

Informe a **"Dt. Recisão"** e também a **"Dt. Pagamento"** da rescisão.

A marcação **"Efetivou Rescisão"** será ativada quando você **"Efetivar Rescisão"** pelo botão [Outras Opções...](#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)

No campo **"Contrato de Locação"** defina qual contrato será rescindido.

**Observação:** caso seja criada uma rescisão que possua a data anterior ao final do último período pago pelo inquilino, o sistema irá buscar o último aluguel não extinto até a data da rescisão para realizar o cálculo. Dessa forma, a data de rescisão deve ser posterior ao último aluguel pago pelo inquilino.

[[voltar ao topo]](#top)

### 
Aba Geral

O campo **"Check List da Rescisão"** é preenchido automaticamente caso a Rescisão de Locação possua um checklist vinculado a ele na tela [CheckList de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045936973-CheckList-de-Contratos).

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500002770402)

[[voltar ao topo]](#top)

### 
Aba Detalhamentos de Rescisão

Essa aba é automaticamente preenchida quando você aciona a opção **"Gerar Rescisão"** do botão [Outras Opções](#bot%C3%A3ooutrasop%C3%A7%C3%B5es...), sendo possível também inserir de forma manual, conforme alguma negociação feita extra contrato:

![rescisao.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360101658734)

[[voltar ao topo]](#top)

### 
Botão Outras Opções...

**Importante:** para utilizar as opções desse botão, ative o parâmetro **"Utilizar rescisão para finalizar contratos - TIMUTILRESFICO"**.

O botão **"Outras Opções..."**, localizado ao lado superior direito da tela, representado pelo ícone 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500002770802)

 possui as seguintes ações:

Quando a opção **"Gerar Rescisão"** for acionada, serão gerados os [Detalhamentos de Rescisão](#abadetalhamentosderescis%C3%A3o).

**Observação:** demonstramos o comportamento dessa ação na documentação da aba acima.

A opção **"Efetivar Rescisão"** confirma a rescisão do Contrato. Automaticamente, quando acionada essa opção, a marcação **"Efetivou Rescisão"** do [Painel Principal](#painelprincipal) fica habilitada:

![rescisao2.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360101658754)

A opção **"Finalizar Contrato"** faz com que o contrato seja imediatamente finalizado. Para finalizar o contrato, você deve efetivar a rescisão anteriormente. Automaticamente, o Estágio do Contrato mudará de **"Ativo"** para **"Extinto"** ou **"Extinto - No Jurídico"**, dependendo da escolha que você fizer no **"Tipo de Extinção"** do pop-up **"Finalizar Contrato de Locação"**. Observe no gif abaixo como fazemos o procedimento:

![rescisao4.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500002771582)

Você também tem a opção **"Cancelar Rescisão"**, caso não tenha sido baixada a despesa de rescisão gerada. Quando essa ação for feita, a marcação Efetivou Rescisão do Painel Principal será desabilitada:

![rescisao4.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360103882273)

Por fim, a opção **"Docs. Recisão"** permite que você gere o documento de rescisão se ele tiver sido cadastrado previamente na tela de [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

[[voltar ao topo]](#top)

### 
Dedução do IRRF

Para que o cálculo da Dedução do IRRF ocorra na rescisão, você deverá realizar as seguintes configurações:

- Preencha o parâmetro **"% e base para clculo de IR na Resciso-TIMPERCIRDTLRES" **com o percentual a ser deduzido do IRRF na multa de quebra de contrato;

- Informe o parâmetro **"Tipo dtl. deduo de I.R.R.F de resciso- TIMIRRFDTLREC"**, com o detalhamento para gerar o IRRF de rescisão;

- Na tela [Contrato de Administração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117173), acesse a aba [Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117173-Contrato-de-Administra%C3%A7%C3%A3o#abaloca%C3%A7%C3%A3o) e preencha o campo  **"Perc. Multa Repasse Proprietário (%)"**;

- Informe o **“Inquilino”** na tela [Contrato de Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213), aba [Inquilino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abainquilino), sendo que o **“Tipo de pessoa”** indicada deverá ser **“Jurídica”**. Nesta mesma tela, aba [Locadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abalocadores), o proprietário locador tem que ser pessoa **“Física”**. Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abageral), os campos **"Meses Para Isenção"** e **"Meses de Multa"** devem estar configurados conforme o contrato, para que seja gerada a multa por quebra de contrato.

**Nota:** para que não ocorra o cálculo do IRRF duas vezes, é necessário que o detalhamento de multa por rescisão definido no parâmetro TIMIRRFDTLREC, não possua a marcação de incidência de IRRF.

**Observação:** conforme o percentual informado no parâmetro TIMPERCIRDTLRES, será efetuada a soma no cálculo do IRRF da rotina de forma automática, assim, se for para cobrar apenas a dedução do TIMPERCIRDTLRES, o detalhamento de multa deve estar com a opção de incidência no IRRF desmarcada.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Contrato de Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o)
- [CheckList de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045936973-CheckList-de-Contratos)
- [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados)
- [Contrato de Administração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117173)
- [Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117173-Contrato-de-Administra%C3%A7%C3%A3o#abaloca%C3%A7%C3%A3o)
- [Contrato de Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213)
- [Inquilino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abainquilino)
- [Locadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abalocadores)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abageral)