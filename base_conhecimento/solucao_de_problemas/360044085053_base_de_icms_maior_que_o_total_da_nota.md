# Base de ICMS maior que o total da nota

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044085053-Base-de-ICMS-maior-que-o-total-da-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044085053-Base-de-ICMS-maior-que-o-total-da-nota)  
> **ID:** `360044085053` | **Última Atualização:** 2026-07-22T16:02:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108066856087)

 MENSAGEM:**

[CORE_E00345] Base de ICMS maior que o total da nota.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108099168151)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108066863383)

 Revise os valores de impostos apresentados em seu lançamento, preferencialmente com o apoio de seu Contador. Dessa forma, conseguirá compreender se essa diferença de valor entre a 'Base de ICMS' e o 'Valor Total da Nota' é coerente. Caso seja incoerente, realize os devidos ajustes.

 

Caso seja coerente, realize a análise abaixo:

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108066864791)

 Verifique na tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** *(Configurações » Avançado) *o parâmetro **"*ACEITARVLRMEICM - Aceitar valor da nota menor que a base de ICMS":***

Se estiver **"Sim"**, permitirá que a nota tenha base de ICMS com valor maior que o total da nota.

Se estiver **"Não"**, caso o valor da base de ICMS superior ao total da nota o sistema barrará a inclusão.

 

![ACEITARVLRMEICM.png](https://ajuda.sankhya.com.br/hc/article_attachments/12300027001879)

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458155984151)

 IMPORTANTE:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108099178519)

 Manter esse parâmetro como 'Ligado' pode propiciar lançamentos indevidos, visto que esse valor a maior não é algo comum.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108099178519)

 Caso alinhe que para essa nota em específico de fato ele precise ser ajustado, retorne-o para 'Desligado' em seguida.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16108099181975)

 CAUSA**:

Ao tentar confirmar lançamentos, onde a informação 'Base de ICMS' possuir um valor maior que o Vlr.Nota será apresentada a mensagem.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)