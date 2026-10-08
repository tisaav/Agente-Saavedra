# Valor da substituição não pode ficar negativo. Produto X

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043180034-Valor-da-substitui%C3%A7%C3%A3o-n%C3%A3o-pode-ficar-negativo-Produto-X](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043180034-Valor-da-substitui%C3%A7%C3%A3o-n%C3%A3o-pode-ficar-negativo-Produto-X)  
> **ID:** `360043180034` | **Última Atualização:** 2026-07-22T16:02:28Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162604723863)

MENSAGEM:**

[CORE_E04483] Valor da substituição não pode ficar negativo. Produto X.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162604727447)

 SITUAÇÃO:**

Ao tentar confirmar uma Nota fiscal, ocorre a mensagem.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162604737815)

 CAUSA**:

Ocorre ao realizar emissão de NF-e e a regra de ICMS calculada irá gerar um valor de ST menor que zero, se a opção Zerar valor da substituição tributária quando negativo estiver desmarcada, será apresentada a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162625439383)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162625439895)

 Primeiro: busque na tela **"[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)"** *(Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas)* a regra que irá incidir sobre a nota fiscal eletrônica gerada e revise os valores configurados na aba **"Substituição Tributária"**.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162604731927)

 **Caso os valores estejam corretos e de fato é provável o cálculo de um valor ST negativo, realize a marcação **"Zerar valor da substituição tributária quando negativo"**, aba 'Substituição Tributária, tela 'Alíquotas de ICMS'.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162604733335)

 Zerar valor da substituição tributária quando negativo: Se esta opção estiver marcada e o cálculo de ST resultar em menor que zero, o sistema deixará o cálculo zerado.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162604733335)

 Caso a opção esteja desmarcada e o cálculo de ST venha a ser menor que zero, o sistema emitirá a mensagem: "Valor da substituição não pode ficar negativo. Produto: xxxx".

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16162625446679)

 **Realizada a marcação, refaça o faturamento.


---

### 🔗 Links e Referências Internas:

- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)