# 1105 Rejeição: Valor total do Item (vItem) difere do somatório dos valores que o compõem

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097372395671-1105-Rejei%C3%A7%C3%A3o-Valor-total-do-Item-vItem-difere-do-somat%C3%B3rio-dos-valores-que-o-comp%C3%B5em](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097372395671-1105-Rejei%C3%A7%C3%A3o-Valor-total-do-Item-vItem-difere-do-somat%C3%B3rio-dos-valores-que-o-comp%C3%B5em)  
> **ID:** `37097372395671` | **Última Atualização:** 2026-07-30T20:57:19Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097341373975)

 **MENSAGEM**

1105 Rejeição: Valor total do Item (vItem) difere do somatório dos valores que o compõem

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097372384151)

 **SITUAÇÃO**

Ao emitir uma nota fiscal eletrônica, o valor total do item informado na NF-e (modelo 55) ou NFC-e (modelo 65) não correspondeu ao resultado da soma dos valores que compõem o item no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097341375255)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097341376023)

 Acesse a **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas) e localize o documento que foi rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097341378199)

 Verifique os valores dos itens da nota fiscal e certifique-se de que o valor total de cada item (vItem) corresponde corretamente à soma dos seguintes componentes:

```text
Valor unitário do produto × quantidade Descontos (se houver) Frete (se houver) Seguro (se houver) Despesas acessórias (se houver).
```

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097372390807)

 Caso identifique divergências, corrija os valores manualmente para que o valor total do item seja exatamente igual à soma dos componentes que o formam.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097341380247)

 Se estiver utilizando arredondamentos, verifique se eles estão sendo aplicados corretamente. Considere que a SEFAZ permite uma **tolerância de ± R$ 0,10** para mais ou para menos.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097341381143)

 Após realizar as correções necessárias, tente emitir a nota fiscal novamente.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097341382039)

 **CAUSA**

A rejeição 1105 ocorre quando o valor total do item (vItem) informado no documento fiscal é diferente do resultado da soma dos componentes que formam este valor. Esta validação é realizada pela SEFAZ para garantir a consistência matemática dos valores declarados nos documentos fiscais. O valor total do item deve ser igual à soma dos seguintes componentes:

```text
vItem = (vProd - vDesc + vOutro + vFrete + vSeg) - vTotTrib
```

 

Onde:

- 

vProd = Valor bruto do produto (valor unitário × quantidade);

- 

vDesc = Valor do desconto vOutro = Valor de outras despesas acessórias;

- 

vFrete = Valor do frete;

- 

vSeg = Valor do seguro;

- 

vTotTrib = Valor dos tributos incidentes sobre o item.

Esta validação é aplicada tanto para NF-e (modelo 55) quanto para NFC-e (modelo 65), e não há exceções para esta regra. A SEFAZ permite apenas uma pequena tolerância de ± R$ 0,10 para mais ou para menos, para acomodar possíveis diferenças de arredondamento.