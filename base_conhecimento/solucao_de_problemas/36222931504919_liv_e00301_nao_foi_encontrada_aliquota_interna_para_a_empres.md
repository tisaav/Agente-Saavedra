# LIV_E00301 - Não foi encontrada alíquota interna para a empresa selecionada. Verifique o Cadastro de Alíquota de ICMS

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36222931504919-LIV-E00301-N%C3%A3o-foi-encontrada-al%C3%ADquota-interna-para-a-empresa-selecionada-Verifique-o-Cadastro-de-Al%C3%ADquota-de-ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/36222931504919-LIV-E00301-N%C3%A3o-foi-encontrada-al%C3%ADquota-interna-para-a-empresa-selecionada-Verifique-o-Cadastro-de-Al%C3%ADquota-de-ICMS)  
> **ID:** `36222931504919` | **Última Atualização:** 2026-07-22T14:23:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36222931502871)

 MENSAGEM:**

[LIV_E00301] Não foi encontrada alíquota interna para a empresa selecionada. Verifique o Cadastro de Alíquota de ICMS.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36222931503255)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36419783096727)

 Acesse a tela ****[''Alíquota de ICMS''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS) (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36419797662103)

 Localize o **estado (UF) **correspondente ao cadastro da empresa, e em seguida, **cadastre uma alíquota interna** para essa UF, garantindo que:

- 

Não exista **exceção** configurada;

- 

A alíquota seja cadastrada como **interna**;

- 

O campo **“Alíquota”** possua um valor **maior que zero**.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36222931503767)

 CAUSA:**

A rotina exige uma **alíquota interna de ICMS sem exceções** para realizar o processamento.

Quando essa alíquota não está configurada, o sistema não encontra um valor válido para aplicar, gerando a mensagem de erro.


---

### 🔗 Links e Referências Internas:

- [''Alíquota de ICMS''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)