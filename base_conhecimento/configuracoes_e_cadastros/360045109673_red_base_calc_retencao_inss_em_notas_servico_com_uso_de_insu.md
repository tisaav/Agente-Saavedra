# Red. base cálc. retenção INSS em notas serviço com uso de insumos

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109673-Red-base-c%C3%A1lc-reten%C3%A7%C3%A3o-INSS-em-notas-servi%C3%A7o-com-uso-de-insumos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109673-Red-base-c%C3%A1lc-reten%C3%A7%C3%A3o-INSS-em-notas-servi%C3%A7o-com-uso-de-insumos)  
> **ID:** `360045109673` | **Última Atualização:** 2026-07-29T13:55:50Z

---

Neste artigo trataremos das configurações que prevem a redução da base de cálculo da retenção de INSS em notas de serviços com utilização de insumos.

Para utilização desta funcionalidade é necessário que o serviço tenha o cálculo de INSS e a TOP esteja configurada com o % mínimo para redução de INSS. 

Para configurar este cálculo, acesse a tela [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos) e informe os seguintes campos: 

- 
**Tem INSS****:** marque esta opção se incidir INSS sobre o serviço quando este for de terceiros.

- 
**% INSS:** preencha o percentual de incidência de INSS sobre o serviço.

- 
**% Red Base INSS:** preencha o percentual de redução na base do INSS se houver redução.

![Tela_Servi_o_aba_Impostos.png](https://ajuda.sankhya.com.br/hc/article_attachments/11178661274647)

Feito isso, acesse a tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), e acione a marcação **"Calcula FUNRURAL/INSS****"**, pois ele sempre será retido nesta situação.

![Tela_Cadastro_de_Parceiros_aba_fiscal.png](https://ajuda.sankhya.com.br/hc/article_attachments/11178662135447)

```text

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310909306263)

****
```

| O INSS só é calculado para pessoa jurídica. |
| --- |

Agora, acesse a tela [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), e preencha o campo **"****% Mín. da Base de INSS sobre o Total da Nota****"** com o percentual de redução base do INSS sobre o total da nota.

![Tela_Tipos_de_opera__o_top_aba_impostos.png](https://ajuda.sankhya.com.br/hc/article_attachments/11178662138775)

```text

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310909306263)

****
********

```

| Esta opção ficará habilitada somente se a TOP estiver com a opção "Tem INSS" ou "Tem Funrural\INSS" habilitada. |
| --- |

#### **Cenário 1**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16745344678935)

 A TOP não possui % informado

Neste caso, o percentual de redução será o que for informado no serviço.

Serviço: 189 - Tem INSS marcado, Aliq. INSS: 10% %Red.INSS: 0

Serviço: 190 - Tem INSS marcado, Aliq. INSS: 15% %Red.INSS: 30%

Serviço: 191 - Tem INSS desmarcado, Aliq. INSS: 0% %Red.INSS: 0

Na nota de venda exemplo, segue:

![RDINSS04.png](https://ajuda.sankhya.com.br/hc/article_attachments/9524813400855)

Serviço: 189 - VlrTotal: 1000,00   BaseINSS: 1000,00   VlrINSS: 100,00

Serviço: 190 - VlrTotal: 1200,00   BaseINSS: 840,00     VlrINSS: 126,00

Serviço: 191 - não tem o cálculo de INSS

Base INSS: 1000,00 +840,00 = 1840,00

   Vlr INSS:   100,00+126,00 = 226,00

#### **Cenário 02**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16745344678935)

 A TOP possui % informado e o % é menor que o percentual de redução dos serviços.

Serviço: 189 - Tem INSS marcado, Aliq. INSS: 10%   %Red.INSS: 0

Serviço: 190 - Tem INSS marcado, Aliq. INSS: 15%    %Red.INSS: 100%

Serviço: 191 - Tem INSS desmarcado, Aliq. INSS: 0% %Red.INSS: 0

% da Top: 80%

Nota de Venda:

![RDINSS05.png](https://ajuda.sankhya.com.br/hc/article_attachments/9524786042135)

Serviço: 189:

Vlr. Total Item: 70,00

Base INSS: 70 * (1-(20/100)) = 56,00

Vlr. INSS: 56,00*10% = 5,60

Serviço: 190 

Vlr. Total Item: 1200,00

Base INSS: 1200 * (1-(20/100)) = 960,00

Vlr. INSS: 960,00*15% = 144,00

Serviço: 191 - não tem o cálculo de INSS

Base INSS: 56,00 + 960,00 = 1016,00 

   Vlr INSS: 5,60 + 144,00 = 149,60

**Cenário 03**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16745344678935)

A TOP possui % informado e o % é maior que o % de redução dos serviços.

Serviço: 189 - Tem INSS marcado, Aliq. INSS: 10%   %Red.INSS: 0

Serviço: 190 - Tem INSS marcado, Aliq. INSS: 15%   %Red.INSS:50%

Serviço: 191 - Tem INSS desmarcado, Aliq. INSS: 0%   %Red.INSS: 0

#### % da Top: 20%

Redução Máxima: 100-20 = 80%

Nota de Venda:

![RDINSS06.png](https://ajuda.sankhya.com.br/hc/article_attachments/9524871339415)

Serviço: 189

Vlr. Total Item: 70,00

Base INSS: 70,00

Vlr. INSS: 70*10% =7,00

Serviço: 190 

Vlr. Total Item: 1200,00

Base INSS: 1200* (1-50/100) =600,00

Vlr. INSS: 600*15% = 90,00

Serviço: 191 - não tem o cálculo de INSS

Base INSS:  70,00+600,00  = 670,00        

    Vlr INSS: 7+90,00  = 97,00 

**Parâmetros que influenciam este cálculo**

**Valor Líquido p/Retenção de INSS-VLRCALCINSS****:** Este parâmetro serve para definir o valor mínimo a ser retido. Considere o seguinte exemplo:

Uma empresa precisa que o cálculo do INSS seja feito somente quando o valor do imposto for maior ou igual a R$ 29,00.

**1)** Caso a configuração do percentual de redução não esteja configurado na TOP a base de redução utilizada será do item.

**2)** Se o percentual de redução da TOP estiver entre 0 e 100, exemplo:

- PERCREDTOP = 30;

- PERCREDTOP = 100 – 30 = 70 (70 é o percentual máximo de redução da top);

Se o valor total base de redução do itens (VLRTOTALREDITENS) for menor que o valor total dos itens sem redução (VLRTOTALITENS), então o percentual de redução da nota (PERCREDNOTA) será (1 – (VLRTOTALREDITENS / VLRTOTALITENS) * 100)

Caso o percentual de redução da nota (PERCREDNOTA) seja maior que o da TOP (PERCREDTOP), então o novo percentual de redução será o da TOP (NOVPERCRED = PERCREDTOP). Caso contrário o novo percentual será igual a zero (NOVPERCRED = 0);

Se NOVPERCRED = 0 a rotina seguirá o fluxo do item 1, utilizando a base de redução do item.

Se NOVPERCRED > 0 então, a base de redução será o (valor_base_sem_redução_item * (1 – (NOVPERCRED / 100))

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos)
- [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)
- [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)
- [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)