# Erro em Reclassificação de produtos para Movimentações Próprias

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34184825143063-Erro-em-Reclassifica%C3%A7%C3%A3o-de-produtos-para-Movimenta%C3%A7%C3%B5es-Pr%C3%B3prias](https://ajuda.sankhya.com.br/hc/pt-br/articles/34184825143063-Erro-em-Reclassifica%C3%A7%C3%A3o-de-produtos-para-Movimenta%C3%A7%C3%B5es-Pr%C3%B3prias)  
> **ID:** `34184825143063` | **Última Atualização:** 2026-07-22T14:27:25Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34184870132503)

 **MENSAGEM:**

"O modelo para o ajuste de Saída de estoque não foi configurado.
Verifique o cadastro da empresa."

![22.png](https://ajuda.sankhya.com.br/hc/article_attachments/35010264046359)

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35010276926359)

 **SITUAÇÃO:**

Ao realizar a cópia de estoque, quando há produtos com movimentações de terceiros e a Top utilizada é para movimentações próprias, com o campo **"Atualização de Estoque"** diferente de **"Nenhum"** na aba **"Estoque"**, o sistema apresenta esta mensagem de erro.

 

Para validar as movimentações dos produtos, consulte a tabela **TGFCTE** filtrando pelo código do produto. No campo **CODPARC**:

- 

**0** → movimentações próprias

- 

**diferente de 0** → movimentações de terceiros

`SELECT *`
`FROM TGFCTE`
`WHERE CODPROD = (Código do Produto); `

![23.png](https://ajuda.sankhya.com.br/hc/article_attachments/35010264049175)

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34184825137943)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35010264050839)

  Acesse a tela **"Cópia de Estoque"** (Inventário > Arquivo >Cópia de Estoque); 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35010276930711)

  Crie um filtro utilizando **CODPARC = 0** para considerar apenas movimentações próprias; 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35010276931735)

  Execute a cópia de estoque novamente. A validação é feita pela primeira linha retornada na consulta (última contagem); 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35010276933399)

  Se a cópia já foi refeita com **CODPARC = 0**, não é necessário refazê-la, a menos que o erro volte a ocorrer.
 

**Ajuda oficial:******[AQUI](https://ajuda.sankhya.com.br/hc/pt-br/articles/6024489775895-Reclassifica%C3%A7%C3%A3o-do-Produto)
**Movimentação com terceiros:** ****[AQUI](https://ajuda.sankhya.com.br/hc/pt-br/articles/10117649858583-O-modelo-para-o-ajuste-de-Sa%C3%ADda-de-estoque-COM-TERCEIROS-n%C3%A3o-foi-configurado-Verifique-o-cadastro-da-empresa)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34184825135895)

 **CAUSA: **

O erro ocorre porque, ao tentar copiar o estoque de produtos com movimentações de terceiros utilizando uma Top configurada para movimentações próprias, o sistema não encontra o modelo de ajuste adequado, devido ao campo **"Atualização de Estoque"** estar diferente de **"Nenhum"** na aba **"Estoque"**.


---

### 🔗 Links e Referências Internas:

- [AQUI](https://ajuda.sankhya.com.br/hc/pt-br/articles/6024489775895-Reclassifica%C3%A7%C3%A3o-do-Produto)
- [AQUI](https://ajuda.sankhya.com.br/hc/pt-br/articles/10117649858583-O-modelo-para-o-ajuste-de-Sa%C3%ADda-de-estoque-COM-TERCEIROS-n%C3%A3o-foi-configurado-Verifique-o-cadastro-da-empresa)