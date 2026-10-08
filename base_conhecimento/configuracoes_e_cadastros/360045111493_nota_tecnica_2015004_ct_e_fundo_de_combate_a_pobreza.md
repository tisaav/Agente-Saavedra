# Nota Técnica 2015.004 - CT-e - Fundo de Combate a Pobreza

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111493-Nota-T%C3%A9cnica-2015-004-CT-e-Fundo-de-Combate-a-Pobreza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111493-Nota-T%C3%A9cnica-2015-004-CT-e-Fundo-de-Combate-a-Pobreza)  
> **ID:** `360045111493` | **Última Atualização:** 2026-07-29T13:57:51Z

---

A Nota Técnica 2015.004 apresenta novas tratativas a serem consideradas para o CT-e. Dentre elas, há modificação no layout da NF-e para que este receba as informações da cobrança de ICMS nas operações interestaduais de vendas a consumidor final não contribuinte do imposto, de forma que, insira ainda novos campos para cálculo do Fundo de Combate à Pobreza UF Destino.  

Para se adequar às modificações, há no sistema novos campos que buscarão essas informações para enviá-las para as tag's do XML, pois são elas que serão validadas para que o CT-e seja aprovado.

Observe abaixo, os campos que receberão os valores do Fundo de Combate à Pobreza: 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

****[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)[Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral)****

|  |  | TGFICM.PERCICMSFCP: tela , aba , campo "Perc. ICMS Fundo Comb. Pobreza"; |
| --- | --- | --- |

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

****[Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)[Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234)****

|  |  | TGFDIN.PERCFCP: tela , botão , opção "Perc. para Fundo Comb. Pobreza"; |
| --- | --- | --- |

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

[Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)[Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593994-Central-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)****

|  |  | TGFDIN.VLRFCP: tela , botão , opção "Perc. para Fundo Comb. Pobreza". |
| --- | --- | --- |

 

## Validações na confirmação do CT-e

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

****[CT-e/MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abactemde)****

******

|  |  | Caso CT-e a ser confirmado possua documentos anteriores cadastrados (TGFDANT) e o campo "Tipo de Serviço CT-e" (aba ) seja definido com a opção "Normal" (TGFTOP.TIPSERVCTE = 0), a seguinte mensagem será exibida: "Não devem ser informados documentos anteriores para CT-e com o tipo de serviço normal." |
| --- | --- | --- |
|  |  |  |
|  |  |  |

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

******

|  |  | Se o CT-e a ser confirmado possuir dois serviços ou mais, e houver cálculo de DIFAL ou de Pobreza, os percentuais devem ser os mesmos (TGFDIN.ALIQINTDEST e TGFDIN.PERCFCP), caso contrário, a seguinte mensagem será exibida: "Verifique a tributação dos componentes do serviço (serviços) o CT-e! Para confirmação do CT-e é necessário que a tributação (CST), a alíquota de ICMS, percentual de redução de base, CFOP, alíquota interna de destino e fundo de combate à pobreza sejam os mesmos." |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |

 

## Cálculo do ICMS para o Fundo de Combate à Pobreza

As regras para o cálculo do Fundo de Combate à Pobreza, seguem as mesmas condições para o cálculo do DIFAL. Observe:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

[Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)************

|  |  | O  utilizado deve possuir o "Tipo de Movimento" como "V-Venda" ou "P-Pedido de venda"; |
| --- | --- | --- |

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

[Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)****

|  |  | Na mesma tela, aba , a marcação "Calcular DIFAL Partilhado" (TGFTOP.CALCDIFALPART) deve ser habilitada; |
| --- | --- | --- |

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

[Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso)********

|  |  | Além disso, na aba  o campo "Tipo de serviço CT-e" tem de ser definido com a opção "Normal"; |
| --- | --- | --- |

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)********[Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)

|  |  | O parceiro destinatário, sendo este cadastrado na tela , precisar ser configurado com a opção "Consumidor Final" do campo "Classificação ICMS", sendo este localizado na aba . |
| --- | --- | --- |

Dessa forma, o cálculo será realizado por item da seguinte forma:

```text
        

![Calculadora.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310973367319)

 **TGFDIN.VLRFCP = TGFDIN.BASE * Perc. ICMS para Fundo Comb. Pobreza 
                                 (TGFICMS.PERCFCP)**
```

 

![roxo_2.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310952937111)

|  | No caso de a Alíquota de ICMS ser igual a Alíquota Interna de Destino, não haverá cálculo para o DIFAL, no entanto, caso seja informado o Perc. ICMS Fundo Comb. Pobreza, será calculado o valor do ICMS para o Fundo de Combate a Pobreza, e todas as tag's pertencentes ao Grupo das vendas interestaduais para Consumidor Final não contribuinte do ICMS, serão geradas. |  |
| --- | --- | --- |

 

No exemplo abaixo, você poderá observar alguns XML's de notas aprovadas:

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

 Com DIFAL e com Fundo de Combate à Pobreza:

```text
<imp>
        <ICMS>
                <ICMS00>
                        <CST>**00**</CST>
                        <vBC>**535.00**</vBC>
                        <pICMS>**12.00**</pICMS>
                        <vICMS>**64.20**</vICMS>
                </ICMS00>
        </ICMS>
        <ICMSUFFim>
                <vBCUFFim>**535.00**</vBCUFFim>
                <pFCPUFFim>**2.00**</pFCPUFFim>
                <pICMSUFFim>**23.00**</pICMSUFFim>
                <pICMSInter>**12.00**</pICMSInter>
                <pICMSInterPart>**40.00**</pICMSInterPart>
                <vFCPUFFim>**10.70**</vFCPUFFim>
                <vICMSUFFim>**23.54**</vICMSUFFim>
                <vICMSUFIni>**35.31**</vICMSUFIni>
        </imp>
```

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

 Com DIFAL e sem Fundo de Combate à Pobreza:

```text
<imp>
        <ICMS>
                <ICMS00>
                        <CST>**00**</CST>
                        <vBC>**521.81**</vBC>
                        <pICMS>**12.00**</pICMS>
                        <vICMS>**62.62**</vICMS>
               </ICMS00>
        </ICMS>
        <ICMSUFFim>
                <vBCUFFim>**521.81**</vBCUFFim>
                <pFCPUFFim>**0.00**</pFCPUFFim>
                <pICMSUFFim>**23.00**</pICMSUFFim>
                <pICMSInter>**12.00**</pICMSInter>
                <pICMSInterPart>**40.00**</pICMSInterPart>
                <vFCPUFFim>**0.00**</vFCPUFFim>
                <vICMSUFFim>**22.96**</vICMSUFFim>
                <vICMSUFIni>**34.44**</vICMSUFIni>
         </ICMSUFFim>
  </imp>
```

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

 Sem DIFAL e com Fundo de Combate à Pobreza:

```text
<imp>
        <ICMS>   
                  <ICMS00>
                          <CST>**00**</CST>  
                          <vBC>**739.25**</vBC>
                          <pICMS>**12.00**</pICMS>
                          <vCIMS>**88.71**</vCIMS>
                   </ICMS00>
           </ICMS>
           <ICMSUFFim>
                   <vBCUFFim>**739.25**</vBCUFFim>
                   <pFCPUFFim>**2.00**</pFCPUFFim>
                   <pICMSUFFim>**0.00**</pICMSUFFim>
                   <pICMSInter>**12.00**</pICMSInter>
                   <pICMSInterPart>**40.00**</pICMSInterPart>
                   <vFCPUFFim>**14.78**</vFCPUFFim>
                   <vICMSUFFim>**0.00**</vICMSUFFim>
                   <vICMSUFIni>**0.00**</vICMSUFIni>
            </ICMSUFFim>
</imp>
```

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458109863063)

 Sem DIFAL e sem Fundo de Combate à Pobreza:

```text
      <imp>
              <ICMS>
                      <ICMS00>
                              <CST>**00**</CST>
                              <vBC>**416.32**</vBC>
                              <pICMS>**12.00**</pICMS>
                              <vICMS>**49.96**</ICMS>
                       </ICMS00>
               </ICMS>
      </imp>
```

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234)
- [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)
- [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593994-Central-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)
- [CT-e/MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abactemde)
- [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)
- [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso)
- [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)
- [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)