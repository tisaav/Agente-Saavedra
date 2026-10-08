# Unidade alternativa com WMS

> **Módulo:** Melhores Praticas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4402883089687-Unidade-alternativa-com-WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/4402883089687-Unidade-alternativa-com-WMS)  
> **ID:** `4402883089687` | **Última Atualização:** 2026-07-22T15:24:13Z

---

Ao realizar o cadastro de um produto que trabalhe com Unidade alternativa, este produto deverá ser utilizado nas rotinas do módulo WMS. É valido a consideração de sempre configurar a menor unidade para este produto, sendo a unidade padrão, pois atualmente o Modulo de WMS trabalha com apenas 4 casas decimais em suas tabelas de origem. Ao configurar uma unidade alternativa dividindo, poderá causar divergência ao realizar a conversão em algum momento.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16343104537111)

 OBSERVAÇÃO:**

A marcação **"Apresentar nas tarefas do WMS"** quando acionada, influenciará apenas nas tarefas de separação.  O registro de 'validades' utilizado na tela Estoque/Endereçamento WMS sempre irá trazer a quantidade nas tabelas de data de validade, a unidade Padrão do produto.