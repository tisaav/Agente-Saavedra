# Parcela calculada pela fórmula não pode ter seu valor alterado

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044085733-Parcela-calculada-pela-f%C3%B3rmula-n%C3%A3o-pode-ter-seu-valor-alterado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044085733-Parcela-calculada-pela-f%C3%B3rmula-n%C3%A3o-pode-ter-seu-valor-alterado)  
> **ID:** `360044085733` | **Última Atualização:** 2026-09-21T20:01:30Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105902810135)

 MENSAGEM:**

[CORE_E02785] Parcela calculada pela fórmula não pode ter seu valor alterado.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105917709207)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105902816535)

 Verifique se o tipo de negociação utilizado possui fórmula vinculada:

Tela **"[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)**" *(Caminho de acesso: Comercial » Arquivo » Cadastros)*, aba **"Parcelas"**, campo **"Fórmula"**.

 

![formula_tipos_de_negocia__o.png](https://ajuda.sankhya.com.br/hc/article_attachments/14505980142615)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105902820247)

 Para a situação reportada no item 1, não serão permitidas alterações no respectivo financeiro que façam com que as parcelas não atendam aos requisitos da fórmula.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458194700055)

 Importante:**

Caso essa situação ocorra na rotina **"[Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)"** atente-se a opção **"Usar financeiro"** da aba **"Financeiro"**. Para tipo de negociação com fórmula, essa opção deverá ser igual **Usar financeiro do sistema**.

 

![usar_financeiro_do_sistema.png](https://ajuda.sankhya.com.br/hc/article_attachments/14505981259031)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16105917716759)

 CAUSA:**

Mensagem apresentada ao realizar alterações em financeiros que são gerados por fórmulas e tais alterações não atendem aos requisitos da respectiva fórmula.


---

### 🔗 Links e Referências Internas:

- [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)
- [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)