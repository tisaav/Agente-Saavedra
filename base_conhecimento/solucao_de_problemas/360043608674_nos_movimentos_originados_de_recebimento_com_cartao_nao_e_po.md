# Nos movimentos originados de recebimento com cartão não é possível alterar os campos

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043608674-Nos-movimentos-originados-de-recebimento-com-cart%C3%A3o-n%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-os-campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043608674-Nos-movimentos-originados-de-recebimento-com-cart%C3%A3o-n%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-os-campos)  
> **ID:** `360043608674` | **Última Atualização:** 2026-07-22T16:01:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192557141015)

 MENSAGEM**:

[CORE_E03463] Nos movimentos originados de recebimento com cartão não é possível alterar os campos:
Taxa Administradora, Vlr Desconto, Vlr Multa, Vlr Juros, Despesas c/ Cartório, Vlr INSS, Vlr ISS, Vlr IRF,
Valor do Desdobramento, TOP, Tipo de Título, Datas de Entrada e Saída, Data de Vencimento, Data de Negociação, Receita/Despesa, Parceiro, Empresa, Provisão, Cód. e Valor da Moeda.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192557142679)

 SOLUÇÃO**:

A validação existe para manter a integridade das informações de títulos originados de cartões.

Para consultar que o título é oriundo de um recebimento de cartão, acesse a **"[Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)" **(Caminho de acesso: Financeiro » Rotinas » Movimentação Financeira) e consulte os campos indicados a seguir.

- Campos "**NSU"** e "**Autorização"**: Quando esses 2 campos estão preenchidos, significa que é um título de transação via Cartão via TEF/POS ] - O título não poderá ser alterado em hipótese alguma.

 

![mov_financeira3.png](https://ajuda.sankhya.com.br/hc/article_attachments/14607209229463)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16192543206167)

 CAUSA**:

Mensagem ocorre quando um título autorizado por transação TEF/POS está sendo alterado pelo sistema, por restrições de integridade esse título não poderá sofrer nenhuma alteração via sistema.


---

### 🔗 Links e Referências Internas:

- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)