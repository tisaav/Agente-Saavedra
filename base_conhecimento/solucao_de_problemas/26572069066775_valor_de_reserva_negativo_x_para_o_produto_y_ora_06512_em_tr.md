# Valor de reserva negativo(-,X) para o produto: (Y) ORA-06512: em "TRG_UPD_TGFEST", line 111

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26572069066775-Valor-de-reserva-negativo-X-para-o-produto-Y-ORA-06512-em-TRG-UPD-TGFEST-line-111](https://ajuda.sankhya.com.br/hc/pt-br/articles/26572069066775-Valor-de-reserva-negativo-X-para-o-produto-Y-ORA-06512-em-TRG-UPD-TGFEST-line-111)  
> **ID:** `26572069066775` | **Última Atualização:** 2026-07-22T14:41:11Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26572069046295)

 **MENSAGEM:**

[ORA-20101] Valor de reserva negativo(-,X) para o produto: (Y) ORA-06512: em "TRG_UPD_TGFEST", line 111

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26572069047959)

SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26572084810775)

 Verifique se algum item **não **existe na tabela TGFCAB, mas existe na TGFITE. Ou seja, o lançamento possui item reservando estoque, no entanto não tem cabeçalho. Por meio da tela DBExplorer, rodando a consulta abaixo, é possível analisar se existe algum lançamento incorreto.

 

```text
SELECT *
FROM tgfite
WHERE codprod = X
AND nunota NOT IN(SELECT nunota FROM tgfcab)
```

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450196981399)

 Caso a consulta resulte algum valor, algum objeto do banco de dados não realizou a exclusão do item quando o lançamento foi excluído/cancelado, ou alguma intervenção via banco de dados pode ter excluído apenas da TGFCAB (cabeçalho). Para solução, procure o responsável pelo banco de dados da empresa, ou até mesmo a unidade responsável, a fim de entender o motivo pelo qual existe só o item e se pode ser excluído.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26572069057687)

 Se o passo acima não foi efetivo, acesse a tela **"Verificação de Saldo de Estoque"**, filtre o produto em questão e clique em **"Aplicar"**.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450196981399)

 A tela é responsável por comparar tudo que foi movimentado nos portais com o saldo de estoque atual. Caso apresente algum resultado, mostra que o cálculo do saldo realizado dos movimentos dos portais ficou diferente do saldo atual do estoque, e sugere a correção para que o saldo fique igual ao movimentado nos portais. Isso prova que houve intervenções via banco alterando o saldo do estoque e ficando diferente do que realmente foi movimentado.