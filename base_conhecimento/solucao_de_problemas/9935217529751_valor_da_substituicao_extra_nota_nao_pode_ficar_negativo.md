# Valor da substituição extra nota não pode ficar negativo

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9935217529751-Valor-da-substitui%C3%A7%C3%A3o-extra-nota-n%C3%A3o-pode-ficar-negativo](https://ajuda.sankhya.com.br/hc/pt-br/articles/9935217529751-Valor-da-substitui%C3%A7%C3%A3o-extra-nota-n%C3%A3o-pode-ficar-negativo)  
> **ID:** `9935217529751` | **Última Atualização:** 2026-07-22T15:05:14Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17318040931351)

 **MENSAGEM:**

[CORE E04477] Valor da substituição extra nota não pode ficar negativo

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17266512069911)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17266512072343)

 Primeiro busque na tela **"Alíquotas de ICMS"** *(Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas)* a regra que irá incidir sobre a nota fiscal eletrônica gerada e revise os valores configurados na aba **"Substituição Tributária"**.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17266512074647)

 Caso os valores estejam corretos e de fato é provável o cálculo de um valor ST negativo, realize a marcação "**Zerar valor da substituição tributária quando negativo**" (Aba Substituição Tributária/ Tela Alíquotas de ICMS).

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/12292716718103)

 

- Zerar valor da substituição tributária quando negativo: se esta opção estiver marcada e o cálculo de ST resultar em menor que zero, o sistema deixará o cálculo zerado.

- Caso a opção esteja desmarcada e o cálculo de ST venha a ser menor que zero, o sistema emitirá a mensagem: "Valor da substituição não pode ficar negativo. Produto: xxxx".

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17266512077079)

 Realizada a marcação, refaça o faturamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17266512077719)

CAUSA:**

Ocorre ao realizar emissão de NF-e e a regra de ICMS calculada irá gerar um valor de ST menor que zero, se a opção Zerar valor da substituição tributária quando negativo estiver desmarcada, será apresentada a mensagem.