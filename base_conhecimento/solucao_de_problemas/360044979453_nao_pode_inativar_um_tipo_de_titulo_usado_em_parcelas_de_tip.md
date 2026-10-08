# Não pode inativar um tipo de título usado em parcelas de tipo de negociação

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044979453-N%C3%A3o-pode-inativar-um-tipo-de-t%C3%ADtulo-usado-em-parcelas-de-tipo-de-negocia%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044979453-N%C3%A3o-pode-inativar-um-tipo-de-t%C3%ADtulo-usado-em-parcelas-de-tipo-de-negocia%C3%A7%C3%A3o)  
> **ID:** `360044979453` | **Última Atualização:** 2026-07-22T15:51:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311204288791)

 MENSAGEM:**

[ORA-20101]: Não pode inativar um tipo de título usado em Parcelas de TIPO DE NEGOCIAÇÃO. 
[ORA-06512]: em "SANKHYA.TRG_INC_UPD_TGFTIT", line 43 
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPD_TGFTIT'

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311178073367)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311178075543)

 Para que o tipo de título possa ser inativado, acesse a tela **"[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)"** *(Caminho de acesso: Comercial » Arquivo » Cadastros)* e identifique os tipos de negociação que possuem o respectivo tipo de título vinculado na aba **"[Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)"**, conforme exemplo abaixo:

 

![Tipo_de_negocia__o.png](https://ajuda.sankhya.com.br/hc/article_attachments/14399898606487)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311178076439)

 Desvincule o tipo de título a ser inativado para todas as parcelas onde o mesmo encontra-se vinculado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311178079255)

 Feito isso, tente inativá-lo. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16311178080407)

 **CAUSA:**

Mensagem apresentada ao tentar inativar um tipo de título que está sendo utilizado na aba Parcelas de determinado tipo de negociação.


---

### 🔗 Links e Referências Internas:

- [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)
- [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)