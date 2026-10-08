# Total da nota menor que a base de ICMS

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575894-Total-da-nota-menor-que-a-base-de-ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575894-Total-da-nota-menor-que-a-base-de-ICMS)  
> **ID:** `360043575894` | **Última Atualização:** 2026-07-22T16:02:16Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092900391703)

 MENSAGEM:**

[CORE_E03081] Total da nota menor que a base de ICMS.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092854224535)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092854227479)

 Valide se os valores apresentados para a Base de ICMS estão coerentes com o esperado. Em caso negativo, revalide as configurações da exceção de ICMS desse lançamento, de acordo com o recomendado pela Contabilidade. Após ajustes, testes uma nova confirmação do lançamento.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092854233367)

 **Caso essa divergência seja válida, para permitir sua confirmação no sistema é necessário que o parâmetro abaixo seja ligado:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092854235927)

 Tela **"Preferências" ***(Configurações >> Avançado)*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092854235927)

 Chave **"ACEITARVLRMEICM - Aceitar valor da nota menor que a base de ICMS"**

 

![ACEITARVLRMEICM.png](https://ajuda.sankhya.com.br/hc/article_attachments/12290562356759)

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092854243607)

 **Após ligar o parâmetro teste a confirmação novamente.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458165016599)

 **IMPORTANTE:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092854235927)

 Manter esse parâmetro como **Ligado** pode propiciar lançamentos indevidos, visto que esse valor a maior não é algo comum.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092854235927)

 Caso alinhe que para essa nota em específico de fato ele precise ser ajustado, aconselhamos retorná-lo para **Desligado** em seguida.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16092900418711)

 CAUSA:**

Ao tentar confirmar lançamentos, onde a informação Base de ICMS possuir um valor maior que o Vlr.Nota será apresentada a mensagem.