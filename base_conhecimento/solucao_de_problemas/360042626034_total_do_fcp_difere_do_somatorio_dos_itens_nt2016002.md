# Total do FCP difere do somatório dos itens (NT2016/002)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626034-Total-do-FCP-difere-do-somat%C3%B3rio-dos-itens-NT2016-002](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626034-Total-do-FCP-difere-do-somat%C3%B3rio-dos-itens-NT2016-002)  
> **ID:** `360042626034` | **Última Atualização:** 2026-07-22T16:08:20Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085443226007)

 MENSAGEM:**

861-Rejeição: Total do FCP difere do somatório dos itens.(NT2016/002).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085443236759)

 SOLUÇÃO:**

Geralmente estas divergências estão relacionadas a arredondamentos e/ou conversões de casas decimais. Abaixo, trecho do Manual do Contribuinte onde considera uma tolerância de R$ 0,01 para mais ou para menos:

*O valor resultante da multiplicação deve ser arredondado para um valor numérico com duas casas decimais. Considerar uma tolerância de R$ 0,01 para mais ou para menos na validação.*

Porém, há situações em que algumas **Secretarias Estaduais** não permitem o arredondamento.  

Considere o cálculo da seguinte forma: [Exemplo do cálculo considerado pela Sefaz]

- vFCP [Total] **=** vFCP [item 1] **+** vFCP [item 2]

- vFCP [Total] **=** 3.99 + 3.99

- vFCP [Total] **=** 7.98

- No sistema considere analisar o XML de Conferência (Portal de Vendas>>Botão NF-e>>Gerar XML de NF-e em arquivo para Conferência).

- Analise em cada item o valor do campo **vFCP, **no qual a soma do valor desse campo seja o total no campo **vFCP** do grupo de Totais.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085431033879)

 Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

- Aba: **"Geral"**

- Campo **"% ICMS FCP":** Verifique o percentual de acordo com a [Tabela de Alíquotas de FCP por UF](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=TKvyZLZP3cA=) da SEFAZ;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085443248023)

 Feito as conferências e ajustes, gere o lote novamente.

Caso o problema persista e os valores no XML estejam corretos, entre em contato com nosso suporte.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085443254295)

 CAUSA:**

Quando for emitida uma NF-e (modelo 55) e o total do FCP, calculado no grupo de totais da NF-e, for diferente do somatório do FCP dos itens que fazem parte do cálculo, haverá a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16085443263383)

 OBSERVAÇÃO:**

1- (**NT2016/002**)

Nota Técnica:

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uvfnqOj%20spg=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uvfnqOj%20spg=)