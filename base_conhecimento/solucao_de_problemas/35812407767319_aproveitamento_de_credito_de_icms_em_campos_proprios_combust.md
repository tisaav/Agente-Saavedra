# Aproveitamento de crédito de ICMS em campos próprios — combustíveis

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35812407767319-Aproveitamento-de-cr%C3%A9dito-de-ICMS-em-campos-pr%C3%B3prios-combust%C3%ADveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/35812407767319-Aproveitamento-de-cr%C3%A9dito-de-ICMS-em-campos-pr%C3%B3prios-combust%C3%ADveis)  
> **ID:** `35812407767319` | **Última Atualização:** 2026-07-22T14:24:40Z

---

Este artigo visa orientar a configuração do aproveitamento parcial (1,12%) do crédito de ICMS em campos próprios para operações de compra de combustíveis (CST 060), nos casos em que a legislação estadual autorizar esse crédito.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36021163322903)

 **SITUAÇÃO:**

Empresas que adquirem, distribuem ou consomem combustíveis precisam registrar no sistema o aproveitamento do crédito de ICMS em campos próprios quando a legislação estadual permitir. Por padrão, operações com ICMS-ST não alimentam créditos em campos próprios; para combustíveis, existe exceção parcial (1,12%) que exige configuração específica.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36021158927127)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36021163326487)

 Acesse a tela **"Empresa''** (Comercial» Preferências), na aba **"Geração ICMS IPI": **

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35812407763223)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36021158929815)

 Localize o campo **"Creditar ICMS e ICMS/ST de NFe Compra Combustível (CST 060)"** e informe os códigos das TOPs que permitirão o aproveitamento do crédito em campos próprios (incluir todas as TOPs aplicáveis às operações de compra de combustível): 

![image (33).png](https://ajuda.sankhya.com.br/hc/article_attachments/36021158930583)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36021158931607)

 Salve a configuração e regenere a nota no livro fiscal:

- 

Se a nota ainda não estiver no livro, gere a nota normalmente; 

- 

Se a nota já estiver gerada no livro, exclua a geração atual do livro e gere novamente para que os campos de ICMS próprio sejam populados.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36021158931607)

 Confirme que os campos de ICMS próprio foram preenchidos no livro; essa informação será exportada para o **EFD ICMS IPI** durante a geração do arquivo fiscal.
 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36021158932503)

 Importante: **Após alterar a configuração, exclua e regenere a nota no livro fiscal sempre que ela já tiver sido previamente gerada, garantindo o correto preenchimento dos campos de ICMS próprio.