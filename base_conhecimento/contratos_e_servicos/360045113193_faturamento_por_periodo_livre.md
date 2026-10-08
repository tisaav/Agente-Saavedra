# Faturamento por Período Livre

> **Módulo:** Contratos e Serviços | **Subseção:** Contratos e Serviços  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113193-Faturamento-por-Per%C3%ADodo-Livre](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113193-Faturamento-por-Per%C3%ADodo-Livre)  
> **ID:** `360045113193` | **Última Atualização:** 2026-07-29T14:05:22Z

---

```text
**

![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311248354967)

 Módulo: **Contratos e Serviços > Rotinas  
```

![Tela_Faturamento_por_Per_odo_Livre.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/9004412132759)

Existe apenas uma diferença entre a tela Faturamento de Contratos e esta tela, o campo **"Mês para referência"**, foi alterado para **"****Data para Referência"**.

**Observação:** ao realizar um faturamento de forma agrupada, os campos Número da nota, Número do contrato e Data de Referência serão registrados na tabela TGFRCA.

Será possível gerar notas para Parceiros diferentes quando a marcação **"Agrupar contratos"** (localizada no Filtro **"Parâmetros Obrigatórios"**) estiver selecionada, ou seja, o sistema agrupará os contratos dos mesmos Parceiros e gerará uma única nota para cada Parceiro que encontrar-se na grade.

A tela para faturamento por período livre irá apresentar somente os [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abapropriedades) que tenham o campo **"Periodicidade do Faturamento" **marcado como **"****Livre"**, além disso, para aparecerem na tela os contratos devem ter a 'Referência Próximo Faturamento' menor ou igual a **"****Data para Referência" **e a **"****Data de Término"** do contrato;

![Tela_Contratos_campo_Periodicidade_do_Faturamento_marcado_como_Livre.png](https://ajuda.sankhya.com.br/hc/article_attachments/9004404946839)

As demais opções são as mesmas da tela de [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025391873-Faturamento-de-Contratos).

O período de faturamento será definido entre a “Data de Término” do contrato e a **"Referência próximo Faturamento"**.

Na tela de **"****Faturamento por Período Livre"** existe a grade dos **"****Contratos"**, na coluna ‘Referência’ aparece o mesmo texto que sairá na observação da nota gerada pelo faturamento que pode ser, por exemplo, Referente ao período de 07/05/2011 a27/05/2011. As datas são a **"Referência Próximo Faturamento"** e a **"Data de Término"** de cada contrato no momento do faturamento.

Ao faturar um contrato, a data de vencimento da fatura será a Referência Próximo Faturamento, somada à quantidade de dias do campo **"Prazo de vencimento"** e a Referência Próximo Faturamento é alterada para um dia posterior a data de término do contrato, ou seja, **"Data de Término"** + 1.

**Nota:** na tela de Contratos, se o contrato estiver marcado para usar a Periodicidade do Faturamento Livre, o campo **"Tipo de Pagamento"** deve estar marcado como **"Mês corrente"**, a Data de Término do contrato e a “Referência próximo Faturamento” devem estar preenchidos, senão o sistema irá mostrar uma mensagem informando que esses campos devem ser preenchidos.

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abapropriedades)
- [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025391873-Faturamento-de-Contratos)