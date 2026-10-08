# Código de situação tributaria (CST) para PIS está incorreto no cadastro da alíquota de PIS: CST = 0

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008692661-C%C3%B3digo-de-situa%C3%A7%C3%A3o-tributaria-CST-para-PIS-est%C3%A1-incorreto-no-cadastro-da-al%C3%ADquota-de-PIS-CST-0](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008692661-C%C3%B3digo-de-situa%C3%A7%C3%A3o-tributaria-CST-para-PIS-est%C3%A1-incorreto-no-cadastro-da-al%C3%ADquota-de-PIS-CST-0)  
> **ID:** `1500008692661` | **Última Atualização:** 2026-07-28T22:00:09Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16336194937495)

 MENSAGEM**:

[CORE_E01571] Código de situação tributaria (CST) para PIS está incorreto no cadastro da alíquota de PIS: CST = 0

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16336179033879)

 SOLUÇÃO:**

Primeiramente verifique com o setor fiscal qual é o CST correto a ser gerado no  lançamento para PIS e COFINS, uma vez que hoje está sendo gerada a CST = 0. 
Em seguida procure entender se o imposto foi digitado, se sim:
 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16336166648599)

 Ou digita-se TODAS as informações de PIS e COFINS, incluindo CST;

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16336190057879)

 Ou então, configura-se a Alíquota devidamente, porém vale ressaltar que só será informado PIS e COFINS na confirmação.
 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16336194947095)

 CAUSA:**

O erro acontece quando não é informado o número do [CST(Código de situação tributária)](https://pt.wikipedia.org/wiki/C%C3%B3digo_de_situa%C3%A7%C3%A3o_tribut%C3%A1ria) no campo de preenchimento do PIS/COFINS. 

 

**Artigo de referência: **

**[Nota não possui informações sobre PIS e esta informação é obrigatória para NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042870014--CORE-E01568-Nota-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-PIS-e-esta-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-NFe-Como-resolver-)**


---

### 🔗 Links e Referências Internas:

- [Nota não possui informações sobre PIS e esta informação é obrigatória para NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042870014--CORE-E01568-Nota-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-PIS-e-esta-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-NFe-Como-resolver-)