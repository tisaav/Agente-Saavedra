# Fórmula p/ Ajuste Tamanho de Lote

> **Módulo:** Produção | **Subseção:** Produção/W  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360046841754-F%C3%B3rmula-p-Ajuste-Tamanho-de-Lote](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046841754-F%C3%B3rmula-p-Ajuste-Tamanho-de-Lote)  
> **ID:** `360046841754` | **Última Atualização:** 2026-07-29T14:56:17Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312801037207)

 **Módulo:** Produção > Cadastros
```

Através desta tela você poderá criar fórmulas que serão utilizadas para ajustar o tamanho do lote no lançamento de uma ordem de produção. Bem como, cadastrar variáveis em cada umas das fórmulas. Estas variáveis são representadas por nomes, podendo ter valores numéricos ou expressões.

![formulalote01.png](https://ajuda.sankhya.com.br/hc/article_attachments/8988484489495)

As variáveis deverão ser criadas na mesma ordem em que serão processadas, ou seja, se uma variável for criada após outra que a utilizar, ocorrerá um erro na avaliação da fórmula. Além disso, a estrutura das mesmas deverá estar em letra maiúscula, ou não serão identificadas.

**Nota:** é possível utilizar algumas variáveis do lançamento de OP na construção das expressões. Sendo elas:

- CODPRODPA;

- CONTROLEPA;

- IDPROC;

- TAMLOTE.

Dentro de uma função PDES é obrigatório que as variáveis sejam inseridas após o símbolo $F e entre {} (chaves), para que o avaliador de fórmula as reconheça. Vejamos um exemplo:

![ksnip_20220919-153651.png](https://ajuda.sankhya.com.br/hc/article_attachments/8988678778519)

**Nota:** uma variável poderá utilizar outra variável em sua expressão, mas para isto é necessário que estejam em ordem. Vejamos um exemplo:

- Temos a variável 1;

- Depois, a variável 2 com a expressão contendo a variável 1;

- Logo após, a variável 3 contendo na expressão a variável 1 e 2.

[[Voltar ao topo]](#top)