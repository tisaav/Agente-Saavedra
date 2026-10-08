# O modelo para o ajuste de estoque COM TERCEIROS não foi configurado. Verifique o cadastro da empresa

> **Módulo:** Solucao de Problemas | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/19278971255575-O-modelo-para-o-ajuste-de-estoque-COM-TERCEIROS-n%C3%A3o-foi-configurado-Verifique-o-cadastro-da-empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/19278971255575-O-modelo-para-o-ajuste-de-estoque-COM-TERCEIROS-n%C3%A3o-foi-configurado-Verifique-o-cadastro-da-empresa)  
> **ID:** `19278971255575` | **Última Atualização:** 2026-07-22T14:51:46Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19278961632279)

 **MENSAGEM:**

O modelo para o ajuste de estoque COM TERCEIROS não foi configurado. Verifique o cadastro da empresa.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19278984241559)

CAUSA:**

Ao efetuar uma cópia/contagem de estoque considerando determinado(s) produto(s) com 'Parceiro' diferente de 0 (zero) será exigido o modelo de ajuste de terceiros vinculado nas preferências da empresa para que o ajuste de estoque seja realizado.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19278984220439)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296023478423)

 Verifique na rotina **Tipos de Operação - TOP** *(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)*, se existe uma TOP criada para Ajuste de Estoque de Entrada Com Terceiros e outra para Ajuste de Estoque de Saída Com Terceiros .

Caso não tenha efetue a criação das TOP's da seguinte forma:

 

TOP Ajuste de Estoque de Entrada Com Terceiros

Aba Estoque

Campos

Atualização do Estoque -- Nenhuma

Atualiza estoque MP -- Nenhuma

 

Aba Estoque de Terceiros

Campo

Estoque com/de Terceiros -- Soma do estoque próprio em poder de Terceiros

 

![top ajuste de estoque 24-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19295993247767)

 

TOP Ajuste de Estoque de Saída Com Terceiros

Aba Estoque

Campos

Atualização do Estoque -- Nenhuma

Atualiza estoque MP -- Nenhuma

 

Aba Estoque de Terceiros

Campo

Estoque com/de Terceiros -- Subtrair do estoque próprio em poder de Terceiros

 

![ajuste de estoque saida 24-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19295993254935)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19295993260311)

 Crie um modelo para as Top's de ajuste de saída e ajuste de entrada com terceiros na rotina **Modelo de notas e pedidos**(Caminho de acesso à tela: Comercial » Consulta » Modelo de Notas e Pedidos). Caso esse modelo já exista, informe o código dele nas preferências da empresa.

 

Preencha os seguintes campos

Tipo de operação

Empresa

Tipo de Negociação

Dt. de Alteração

Parceiro: **Se atentar, pois, precisa ser diferente de zero, ou seja, nesse caso, tem que ser o parceiro que está em posse do estoque.**

 

![modelo de notas e pedidos 24-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296023511959)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296023521431)

 Realizado os passos 1 e 2, informe os números únicos dos modelos nas preferências da **Empresa** (Caminho de acesso à tela: Comercial » Preferências » Empresa) na aba Estoque/preço nos campos Modelo Ajuste de Entrada de Estoque com Terceiros e Modelo Ajuste de Saída de Estoque com Terceiros

 

![Empresa 24-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19296023529239)

 

**Observação:** Caso não deseje que produtos de terceiros sejam ajustados/inventariados, é possível criar um filtro ao executar o ajuste de estoque para que esses sejam desconsiderados. Dessa forma, as configurações acima não serão exigidas, sendo considerados apenas produtos próprios em poder da empresa.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/19278956230167)