# Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial. (NT2011/005)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625114-Valor-do-Produto-difere-do-produto-Valor-Unit%C3%A1rio-de-Comercializa%C3%A7%C3%A3o-e-Quantidade-Comercial-NT2011-005](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625114-Valor-do-Produto-difere-do-produto-Valor-Unit%C3%A1rio-de-Comercializa%C3%A7%C3%A3o-e-Quantidade-Comercial-NT2011-005)  
> **ID:** `360042625114` | **Última Atualização:** 2026-07-22T16:08:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510257743767)

 MENSAGEM:**

[629 - Rejeição]: Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510257752727)

 SOLUÇÃO:**
Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510234634519)

 Acesse: *Configurações » Cadastros » Produtos » Produtos*
Aba: **"Venda"**
Campo **"Digitação na nota":** 'Quant. e Valor Unitário'

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510257761431)

 Acesse: *Comercial » Rotinas » Central de Vendas*
Veja os itens da Nota e verifique qual produto está com a diferença entre** 'Quantidade' x 'Valor** **Unitário**'. Se atentar caso haja acréscimo/desconto.

Exemplo:

![56.png](https://ajuda.sankhya.com.br/hc/article_attachments/360060880673)

No exemplo acima nota-se o '**Vlr. Unitário'**  igual à R$ 9,99 (<vUnCom>9.9900</vUnCom>), com **quantidade**  igual à 2 (<qCom>2.0000</qCom>) e o **Vlr. Total** foi calculado em R$ 20,00 (<vProd>20.00</vProd>).
Contudo, o valor esperado dessa multiplicação seria **R$ 19,98** (9.9900 * 2.0000).

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510234643607)

 Acesse: *Configurações » Avançado » Preferências* e ligue o parâmetro "**DIVTOTQTDNFE- Divide VLRTOT do item pela QTDNEG no XML da NFE"**

A funcionalidade do parâmetro é dividir a tag <vProd> pela tag <qCom> até a quantidade de casas decimais cuja diferença fique dentro do limite aceitável pela SEFAZ. Isso vai evitar que a tag <vUnCom> tenha sempre 10 casas decimais fixas.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510257769879)

 Após os ajustes redigite Empresa/Parceiro da Nota e gere lote novamente. Caso seja necessário inutilize a nota e fature novamente. Certifique os ajustes anteriormente feitos e gere lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510234649367)

 CAUSA:**

A mensagem de erro é apresentada quando a Sefaz verifica as informações quanto a Valor Unitário X Quantidade X Valor total do item.
Ocorre em casos que tenha produtos/serviços com grandes quantidades e valores muito pequenos e/ou conversão de unidades.

O **SankhyaOM/JivaEVO **por padrão multiplica a Quant. pelo VlrLiqUnitario para ter o total do item, e o Sefaz faz o contrario em sua validação, divide o total do item que foi informado na tag <vProd> pela quantidade informada na tag <qCom>.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510234651031)

 OBSERVAÇÃO:**

([NT2011/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=41lDzlbw3co=)) - Nota técnica