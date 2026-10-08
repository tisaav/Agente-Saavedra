# The value '0.00' of element 'pICMSInter' is not valid

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042637734-The-value-0-00-of-element-pICMSInter-is-not-valid](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042637734-The-value-0-00-of-element-pICMSInter-is-not-valid)  
> **ID:** `360042637734` | **Última Atualização:** 2026-07-22T16:07:49Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510625339927)

 MENSAGEM:**

[CORE_E04895]  cvc-enumeration-valid: value '0.00' is not facet-valid with respect to enumeration '[4.00, 7.00, 12.00]'. it must be a value from the enumeration. cvc-type.3.1.3: the value '0.00' of element 'picmsinter' is not valid.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510649167511)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510649169815)

 Acesse: *Configurações » Avançado » Preferências*

Parâmetro: **"UFDESTNFEBENFIS - UFs destino NF-e com benefício fiscal para DIFAL"**

- No parâmetro** "UFDESTNFEBENFIS"** que por padrão é vazio, informe a sigla de cada UF da SEFAZ de destino (separada por vírgula); caso a SEFAZ de origem/destino estejam amparadas por benefícios fiscais, ou seja, a alíquota interestadual é igual a zero.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510649174423)

 Acesse: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS*

Aba: **"Geral"**

- Campo "**Aliq. Interna Destino": **Alíquota interestadual deve ser igual a zero

- Campo "**Tributação**": CST's deverão estar configurados igual a 40, 41, 50, 51, ou 60.

Desta forma, o valor do DIFAL e do Fundo de Combate à Pobreza, não serão calculados quando o produto estiver com a alíquota interestadual igual a zero, e o "**Cód.Tributação(CST)**" for igual a 40, 41, 50, 51 ou 60, e a UF destino esteja no parâmetro **"UFDESTNFEBENFIS"**.

Não existindo o cálculo do DIFAL, o grupo <ICMSUFDest> não será gerado.

A geração do grupo <ICMSUFDest> no XML não foi alterada e sua premissa continua sendo a existência de valor em algum dos campos referentes ao DIFAL ou ao Fundo de Combate à Pobreza.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510649178391)

 Após os ajustes, exclua a nota e fature ou crie uma nova nota, e posteriormente gere lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16510649187863)

 CAUSA:**

SEFAZ que não exigir o DIFAL (grupo <ICMSUFDest>), devido às UF's origem/destino participarem de Protocolos ou Convênios que definem os benefícios fiscais tais como Isenção, por exemplo.