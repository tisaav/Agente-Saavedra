# O valor do campo pICMSInter informado é inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26491106233879-O-valor-do-campo-pICMSInter-informado-%C3%A9-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/26491106233879-O-valor-do-campo-pICMSInter-informado-%C3%A9-inv%C3%A1lido)  
> **ID:** `26491106233879` | **Última Atualização:** 2026-07-22T14:41:54Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26491106218647)

 **MENSAGEM:**

[CORE_04895] O valor do campo pICMSInter (Aliquota interestadual das UF envolvidas - 4% aliquota interestadual para produtos importados, -7% para os Estados de origem do Sul e Sudeste (exceto ES) destinado para os Estados do Norte e Nordeste ou ES, -12% para os demais casos) informado não é válido.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26491106222231)

SOLUÇÃO:**

Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos), selecione o produto em questão e nele desmarque os campos **"Cacular DIFAL? **e **"Calcular ICMS"**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26491106225815)

CAUSA:**

Normalmente ocorre quando um produto bonificado está configurado para calcular ICMS e DIFAL. Sendo assim, o mesmo é levado para a nota fiscal com um CFOP de produto bonificado e alíquota de DIFAL 100. Com isso, ao tentar aprovar a nota, o sistema cria no XML a TAG 'pICMSInter' com o valor de alíquota do DIFAL, para o produto bonificado.
Com essa configuração, ao tentar enviar a nota, a SEFAZ rejeita a mesma com o seguinte erro.

***"O valor do campo pICMSInter (Alíquota interestadual das UF envolvidas: - 4% alíquota interestadual para produtos importados; - 7% para os Estados de origem do Sul e Sudeste (exceto ES), destinado para os Estados do Norte e Nordeste ou ES; - 12% para os demais casos.) informado não é valido."***