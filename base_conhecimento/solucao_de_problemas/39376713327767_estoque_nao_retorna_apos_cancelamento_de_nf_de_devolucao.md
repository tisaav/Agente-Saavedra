# Estoque não retorna após cancelamento de NF de Devolução

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39376713327767-Estoque-n%C3%A3o-retorna-ap%C3%B3s-cancelamento-de-NF-de-Devolu%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/39376713327767-Estoque-n%C3%A3o-retorna-ap%C3%B3s-cancelamento-de-NF-de-Devolu%C3%A7%C3%A3o)  
> **ID:** `39376713327767` | **Última Atualização:** 2026-08-01T02:53:00Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39376713326103)

 **Mensagem**

Após o cancelamento de uma Nota Fiscal de Devolução, o estoque do produto não retorna ao sistema, impedindo a emissão de uma nova nota de devolução correta.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39376713326231)

 **Situação**

Após o cancelamento de uma Nota Fiscal de Devolução, o estoque do produto não retorna ao sistema, impedindo a emissão de uma nova nota de devolução correta.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39376683203735)

 **Solução**

Para resolver esta situação, avalie as seguintes alternativas:

**Opção 1: Concluir o cancelamento extemporâneo no Sankhya**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39376713326359)

 Consulte a Contabilidade sobre a possibilidade de solicitar o Cancelamento Extemporâneo junto à Sefaz.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39376713326487)

 Com a aprovação da Sefaz em mãos, informe o número e a data do protocolo de cancelamento na tela específica do Sankhya para cancelamentos fora do prazo.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39376713326615)

 Ao concluir esse passo, o sistema reverte automaticamente o estoque da nota cancelada.

 

**Opção 2: Ajuste de Estoque de Entrada (se o cancelamento não puder ser concluído no sistema)**

Caso não seja possível realizar o cancelamento extemporâneo, siga as orientações abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39376713326359)

 Acesse a tela **"Ajuste de Estoque"**.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39376713326487)

 Registre um Ajuste de Estoque de Entrada com os mesmos produtos, quantidades e local de estoque da nota cancelada.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39376713326743)

 **Causa**

O cancelamento de uma nota fiscal no Sankhya sempre estorna o estoque automaticamente, pois o processo exclui o registro da nota do sistema. Isso vale tanto para o cancelamento dentro do prazo quanto para o extemporâneo.

O estoque só deixa de retornar quando o cancelamento não é concluído de fato no Sankhya. Isso costuma acontecer quando:

- A nota está fora do prazo de cancelamento (regular + tolerância, parametrizados na empresa) e o usuário obteve aprovação diretamente com a Sefaz, mas **não informou o protocolo do cancelamento extemporâneo na tela do Sankhya,** sem esse passo, o sistema não reconhece a nota como cancelada.

- Houve falha de comunicação com a Sefaz e a nota ficou em status pendente.