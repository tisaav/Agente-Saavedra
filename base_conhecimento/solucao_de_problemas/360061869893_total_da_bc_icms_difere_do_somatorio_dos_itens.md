# Total da BC ICMS difere do somatório dos itens

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869893-Total-da-BC-ICMS-difere-do-somat%C3%B3rio-dos-itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360061869893-Total-da-BC-ICMS-difere-do-somat%C3%B3rio-dos-itens)  
> **ID:** `360061869893` | **Última Atualização:** 2026-07-22T15:25:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286182867223)

 MENSAGEM**:

[531-Rejeição]: Total da BC ICMS difere do somatório dos itens.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286196391063)

 SOLUÇÃO**:

Para correção, siga os passos abaixo:

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453262493079)

 Verifique os impostos que incidem na base de calculo de ICMS. Exemplo: IPI.
 Veja artigo: [Cálculo de ICMS: Quais as principais configurações no sistema ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044295053)

As configurações de cálculo de Impostos no sistema, geralmente configuradas em Alíquotas de ICMS, proporcionaliza de forma automática os impostos nos itens e destaca no rodapé.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453262493079)

 Caso o imposto de ICMS esteja sendo lançada de forma manual na nota, considere:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286182875287)

 Para cada item, some o valor de ICMS e destaque no rodapé da nota.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286196397975)

 Caso haja redução da base de cálculo, considere essa redução para destacar o total no rodapé da nota.

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286196401303)

 Exemplo**:

Foi emitida uma NF-e com dois itens informados, cada um com o Valor da Base de Cálculo do ICMS de R$ 199,99 reais, mas no rodapé da NF-e foi informado o valor de R$ 400,00 reais. Como o somatório correto é R$ 399,98 reais.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286182883863)

 CAUSA**:

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e, o Total da Base de Cálculo do ICMS  informado no Grupo de Totais da NF-e for diferente do somatório da Base de Cálculo dos itens que fazem parte do cálculo, será retornado a rejeição.


---

### 🔗 Links e Referências Internas:

- [Cálculo de ICMS: Quais as principais configurações no sistema ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044295053)