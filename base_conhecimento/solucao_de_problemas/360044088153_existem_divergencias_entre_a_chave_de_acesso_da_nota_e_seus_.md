# Existem divergências entre a chave de acesso da nota e seus dados

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088153-Existem-diverg%C3%AAncias-entre-a-chave-de-acesso-da-nota-e-seus-dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088153-Existem-diverg%C3%AAncias-entre-a-chave-de-acesso-da-nota-e-seus-dados)  
> **ID:** `360044088153` | **Última Atualização:** 2026-09-03T19:07:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363221160471)

 MENSAGEM:**

[CORE_E02961] Existem divergências entre a chave de acesso da nota e seus dados: (...)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363226832791)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363221166103)

 Identifique na mensagem de validação apresentada quais são as informações causadoras da divergência.

**Exemplo:**

Existem divergências entre a chave de acesso da nota e seus dados:

- AAMM (Chave) = 1902

- Dt. Neg. (Sistema) = 1903

Para o caso acima, a data de negociação no sistema consta como 19/03 e na chave enviada pelo parceiro como 19/02. Dessa forma, a opção seria **ajustar esse campo data no sistema**, para que a confirmação seja permitida.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363226838295)

 Caso a divergência de fato deva existir, ajuste o parâmetro abaixo para "**Não Valida"** ou "**Valida e avisa"**:

- 
*Configurações » Avançado » Preferências*: Chave **"VALCHAVETERC"**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363226839959)

 **CAUSA:**

Ao realizar o lançamento/importação de nota de "**Terceiros"**, quando existir divergências entre as informações apresentadas no sistema e as informações do XML, se o parâmetro VALCHAVETERC encontrar-se configurado como Valida, será apresentada a mensagem.