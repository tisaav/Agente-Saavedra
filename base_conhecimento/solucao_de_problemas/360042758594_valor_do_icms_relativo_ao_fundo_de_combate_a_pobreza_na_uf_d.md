# Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042758594-Valor-do-ICMS-relativo-ao-Fundo-de-Combate-%C3%A0-Pobreza-na-UF-de-destino-difere-do-calculado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042758594-Valor-do-ICMS-relativo-ao-Fundo-de-Combate-%C3%A0-Pobreza-na-UF-de-destino-difere-do-calculado)  
> **ID:** `360042758594` | **Última Atualização:** 2026-07-22T16:06:03Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086868993431)

 MENSAGEM:**

793- Rejeição: Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086868996759)

 SOLUÇÃO:**

Normalmente estas divergências estão relacionadas a arredondamentos e ou conversões de casas decimais. Vamos utilizar o caso de Uso abaixo para compreender de forma mais clara:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086869002391)

 Através da Central de Vendas, na linha referente a cada item, botão [...] **"Outras Opções"** >> **Consultar/Alterar dados dos impostos do Item**, busque pela linha referente ao Imposto ICMS:

 

![ICMS_3.png](https://ajuda.sankhya.com.br/hc/article_attachments/12154077596311)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086869005335)

 Anote os valores destacados abaixo:

- Perc.para Fundo Comb. Pobreza

- Vlr. para Fundo Comb. Pobreza

- Base para Fundo Comb. Pobreza 

![fundo_de_pobreza.png](https://ajuda.sankhya.com.br/hc/article_attachments/12154111386135)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086869007767)

 Realize o cálculo:

**Base para Fundo X Perc.para fundo = Vlr. para Fundo**

Teremos nesse caso:

**100 x 2% = 2**

Contudo, o 'Vlr para fundo com. pobreza' que consta no sistema é =** 1,96**

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086839779095)

 Para o caso acima, ajuste o 'Vlr para fundo com. pobreza' para **2,00**.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086869011991)

 Feito o ajuste, gere um novo lote da respectiva nf-e.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16086869023127)

CAUSA:**

Quando for emitida uma NF-e e o Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de Destino (<vFCPUFDest>) informado no produto for diferente da multiplicação entre a Base de Cálculo da UF de Destino (<vBCFCPUFDest>) e o Percentual do Fundo de Combate a Pobreza na UF de Destino (<pFCPUFDest>), será retornada a rejeição.