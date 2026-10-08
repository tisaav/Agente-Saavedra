# 1089 Rejeição: Total Devolvido da CBS difere da soma dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37097856297751-1089-Rejei%C3%A7%C3%A3o-Total-Devolvido-da-CBS-difere-da-soma-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/37097856297751-1089-Rejei%C3%A7%C3%A3o-Total-Devolvido-da-CBS-difere-da-soma-dos-itens)  
> **ID:** `37097856297751` | **Última Atualização:** 2026-07-22T14:20:28Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097856277143)

 **MENSAGEM**

1089 Rejeição: Total Devolvido da CBS difere da soma dos itens

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097819751191)

 **SITUAÇÃO**

Ao emitir uma nota fiscal de devolução com valores de CBS, o sistema está calculando incorretamente o total devolvido da CBS, gerando uma divergência entre o valor total informado e a soma dos valores de CBS de cada item da nota.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097819752855)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097819754135)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097856280471)

 Localize a nota fiscal rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097819755799)

 Acesse a **grade de Itens** da nota e selecione qualquer item.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097856282519)

 Forçe o recálculo dos valores:

- 

Altere temporariamente um campo do item (por exemplo, modifique a **quantidade** de 1 para 2 e pressione Enter);

- 

Em seguida, retorne o valor ao original (de *2* para *1*);

- 

Salve o item e a nota fiscal para que o sistema recalcule automaticamente os valores.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097819760919)

 Na aba **''Reforma Tributária''**, verifique se o campo **''Valor total de devolução de tributos (CBS)''** está preenchido corretamente nos itens aplicáveis.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37997603244951)

 Após a validação dos dados, **gere um novo lote** ou **reenvie a nota fiscal** para transmissão.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37997626645143)

 O sistema irá **gerar um novo XML com os totais atualizados**, permitindo a **autorização da nota fiscal**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37097819761559)

 **CAUSA**

Esta rejeição ocorre quando o valor total devolvido da CBS informado no documento fiscal é diferente da soma dos valores de CBS de cada item da nota. Conforme as regras de validação da SEFAZ, o total do valor devolvido da CBS deve corresponder exatamente à soma dos valores de CBS de todos os itens da nota fiscal de devolução. A divergência pode ocorrer quando o sistema não está configurado para calcular proporcionalmente os valores de CBS nos itens, ou quando há arredondamentos que não estão sendo tratados corretamente no cálculo total.