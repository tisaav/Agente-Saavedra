# Reclassificação do Produto 

> **Módulo:** Fiscal e Contábil | **Subseção:** Cadastros e Configurações Fiscais  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/6024489775895-Reclassifica%C3%A7%C3%A3o-do-Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/6024489775895-Reclassifica%C3%A7%C3%A3o-do-Produto)  
> **ID:** `6024489775895` | **Última Atualização:** 2026-09-15T14:11:36Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313148278295)

 **Módulo:** Livros Fiscais > Arquivos          

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42313125135127)

 **Versão:** A partir da 4.12
```

Nessa tela, você poderá efetuar a reclassificação de produtos, ou seja, realizar a transferência de saldo entre os produtos, para que assim, o registro K220 possa ser gerado.

![reclacifica__o.png](https://ajuda.sankhya.com.br/hc/article_attachments/6023107194647)

No campo **"Produto Origem"**, insira o código do produto a ser reclassificado e em seguida, no campo **"Produto Destino"**, o produto novo junto à **"Quantidade"** que será alocada na troca.

A referida Quantidade, conforme a unidade a ser utilizada no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), sendo assim, enviada ao Registro 0200.

Considere ainda que, para que as notas de Entrada e Saída de reclassificação sejam geradas, crie seus modelos na tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos) informando o Tipo de Negociação em pelo menos uma dessas notas. Em seguida, informe o código desses modelos nos parâmetros **"Nota Modelo Ajuste Estoque Reclassificacao (Entrada) - MODENTRECLAS"** e **"Nota Modelo Ajuste Estoque Reclassificacao (Saida) - MODSAIRECLAS"**.

Após a geração das notas, você não poderá realizar alterações na tela, dessa forma, caso uma alteração ou exclusão se faça necessária, deve-se excluir as notas. Além disso, não é possível gerar mais de uma nota no mesmo processamento.

![obs.png](https://ajuda.sankhya.com.br/hc/article_attachments/6024860631575)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)
- [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)