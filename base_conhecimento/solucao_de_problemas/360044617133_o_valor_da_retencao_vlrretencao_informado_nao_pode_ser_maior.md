# O valor da retenção {vlrRetencao} informado não pode ser maior que 11% da Base de cálculo da retenção da contribuição previdenciária {vlrBaseRet}

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617133-O-valor-da-reten%C3%A7%C3%A3o-vlrRetencao-informado-n%C3%A3o-pode-ser-maior-que-11-da-Base-de-c%C3%A1lculo-da-reten%C3%A7%C3%A3o-da-contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-vlrBaseRet](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617133-O-valor-da-reten%C3%A7%C3%A3o-vlrRetencao-informado-n%C3%A3o-pode-ser-maior-que-11-da-Base-de-c%C3%A1lculo-da-reten%C3%A7%C3%A3o-da-contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-vlrBaseRet)  
> **ID:** `360044617133` | **Última Atualização:** 2026-07-22T15:53:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16942820667415)

 MENSAGEM:**

[Erro MS1183]: O valor da retenção {vlrRetencao} informado não pode ser maior que 11% da Base de cálculo da retenção da contribuição previdenciária {vlrBaseRet}.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16942820672919)

 SOLUÇÃO:**

 Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16942867086743)

 Acesse a tela **"Preferências":** *Configurações » Avançado » Preferências*

Chave: **"****TIPCALCLVLRRET"**
Descrição: **"Tipo do cálculo do valor da retenção para o Reinf"**

- Considere a soma dos impostos dos movimentos;

- Considere base dos movimentos e aplique a alíquota.

Considere marcar a segunda opção: 

Pois, desta forma, em um mesmo documento não haverá diferença de centavos ocasionadas por arredondamentos nos valores de retenções, uma vez que o sistema irá somar o valor das base de cálculo dos itens e aplicar a alíquota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16942867091607)

 CAUSA:**

Na geração dos eventos R-2010 e R-2020 o sistema soma os valores de retenções dos diferentes itens de serviço. Caso este somatório seja superior ao cálculo obtido pela aplicação da alíquota sobre a base de calculo, o erro é retornado.