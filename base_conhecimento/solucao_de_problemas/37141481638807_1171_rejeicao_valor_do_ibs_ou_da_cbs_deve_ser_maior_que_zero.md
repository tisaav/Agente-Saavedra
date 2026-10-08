# 1171 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no ajuste de competência [nItem: 999]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141481638807-1171-Rejei%C3%A7%C3%A3o-Valor-do-IBS-ou-da-CBS-deve-ser-maior-que-zero-no-ajuste-de-compet%C3%AAncia-nItem-999](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141481638807-1171-Rejei%C3%A7%C3%A3o-Valor-do-IBS-ou-da-CBS-deve-ser-maior-que-zero-no-ajuste-de-compet%C3%AAncia-nItem-999)  
> **ID:** `37141481638807` | **Última Atualização:** 2026-07-22T14:19:14Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141472741143)

 **MENSAGEM**

1171 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no ajuste de competência [nItem: 999]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141472741655)

 **SITUAÇÃO**

Ao emitir um documento fiscal com o grupo de ajuste de competência (gAjusteCompet), os valores do IBS (Imposto sobre Bens e Serviços) ou da CBS (Contribuição sobre Bens e Serviços) foram informados com valor zero ou não foram preenchidos, gerando a rejeição pela SEFAZ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141481634967)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141481635223)

 Acesse a tela de "**Notas Fiscais**" (Gestão Fiscal » Movimentação » Notas Fiscais) e localize o documento fiscal que apresentou a rejeição.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141472743191)

 Verifique se o CST utilizado possui indicador que obriga o preenchimento do grupo de ajuste de competência (**ind_gAjusteCompet = 1**).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141472743447)

 Acesse a aba "**Itens**" da nota fiscal e selecione o item que apresentou a rejeição.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38136082092311)

 Na seção "**IBS/CBS**", localize o grupo "**Ajuste de Competência**" e verifique os valores informados.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141481637015)

 Certifique-se de que pelo menos um dos campos a seguir esteja preenchido com valor **maior que zero**: Campo "**Valor do IBS**" (gAjusteCompet/vIBS) Campo "**Valor da CBS**" (gAjusteCompet/vCBS).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141472746135)

 Após realizar as correções necessárias, salve as alterações e tente emitir o documento fiscal novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141472746391)

 **CAUSA**

Esta rejeição ocorre quando o documento fiscal possui o grupo de ajuste de competência (gAjusteCompet) informado, mas os valores do IBS (Imposto sobre Bens e Serviços) ou da CBS (Contribuição sobre Bens e Serviços) estão zerados ou não foram preenchidos. De acordo com a regra de validação UB112-30 da SEFAZ, quando o grupo de ajuste de competência é informado, pelo menos um dos valores (IBS ou CBS) deve ser maior que zero.

Esta validação faz parte das regras implementadas pela Lei Complementar 214/2025 no contexto da Reforma Tributária, que estabelece a necessidade de informar corretamente os valores dos novos tributos (IBS e CBS) nos documentos fiscais, inclusive nos casos de ajuste de competência.