# Não existem produtos/quantidades disponíveis para essa operação

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043363333-N%C3%A3o-existem-produtos-quantidades-dispon%C3%ADveis-para-essa-opera%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043363333-N%C3%A3o-existem-produtos-quantidades-dispon%C3%ADveis-para-essa-opera%C3%A7%C3%A3o)  
> **ID:** `360043363333` | **Última Atualização:** 2026-08-20T14:55:59Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160583447)

 MENSAGEM:**

[CORE_E04678] Não existem produtos/quantidades disponíveis para essa operação.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115176057367)

 SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160593047)

 Verifique se existe estoque suficiente para os itens a serem faturados/devolvidos:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 No processo padrão de uma devolução de compra, que em sua maioria atualiza estoque como entrada, para que sua devolução de compra ocorra é necessário que a atualização de estoque ocorra como saída;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Dessa forma, se está, por exemplo, tentando devolver 4 UN do produto X, é necessário ter em estoque essas 4 UN;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Se esse estoque não existe, seu controle de estoque precisa ser revisto, para que seja compreendido internamente motivos pelos quais não existe estoque de um produto que será devolvido ao fornecedor;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Após ajuste desse estoque, tente novamente realizar a devolução.

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160598039)

 Verifique se já existe uma nota de destino vinculada à essa nota:**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

Selecione a nota a ser faturada/devolvida no portal, dê um duplo clique e abra a mesma na Central de Notas;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Com a nota aberta, selecione um item e no botão **"Outras Opções (...)" **» "**Documentos Relacionados" **marque a opção **"Todos os Itens"**;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Verifique se em **"Documento de Destino"** existe algum documento vinculado.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Dê um duplo clique nesse documento, o mesmo será aberto;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Verifique se trata-se de uma nota com os itens/quantidades que você está tentando devolver/faturar;

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Em caso positivo, não será possível devolver/faturar duas vezes os mesmos itens.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115160595095)

 Será necessário entender o processo e verificar se a nota localizada é a que você necessita, não sendo necessário refazê-la.

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115176067735)

 Outra análise a ser considerada é se foi realizado 'Corte' que impeça esse faturamento.**

No exemplo abaixo para um pedido com Qtde= 510 já havia sido feito o Corte de 510, não permitindo assim o faturamento. Nesse caso, entenda o processo e, se necessário, **Limpar o Corte:**

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/14599386670743)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115176070039)

 CAUSA:**

Ocorre quando ao tentar realizar o faturamento/devolução de uma nota que não exista quantidade suficiente em estoque dos itens ou não existir quantidade pendente suficiente para esse processo.