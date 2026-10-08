# Transferência Orçamentária

> **Módulo:** Inteligência e Análise | **Subseção:** Estrutura e planejamento  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360048880094-Transfer%C3%AAncia-Or%C3%A7ament%C3%A1ria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048880094-Transfer%C3%AAncia-Or%C3%A7ament%C3%A1ria)  
> **ID:** `360048880094` | **Última Atualização:** 2026-09-23T18:08:47Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312671513623)

 **Módulo:** Metas e Orçamentos
```

Nesta tela, poderemos realizar transferências de saldos entre qualquer período que desejar, o que o proporcionará mais agilidade no preenchimento e planejamento orçamentário.

Quando você clicar na tela para que esta seja aberta, primeiramente teremos um pop up para seleção do planejamento a que será feita a transferência:

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360072980194)

Após a seleção do orçamento, o sistema o questionará se deseja realizar a **"Atualização do Realizado"**, caso você clicar em **"Sim"** o sistema trará todos os realizados atualizados; Se clicar em **"Não"** a tela trará os realizados, porém estes poderão estar defasados.

Na grade superior da Transferência Orçamentária serão apresentados todos os orçamentos que possuem recursos disponíveis para transferência. Você poderá transferir recursos de um ou mais orçamentos simultaneamente, basta você inserir o valor desejado na coluna **"Valor a Transferir"**: 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/360072986994)

Além desta coluna mencionada, também ainda:

- 
**Prev. + Mov. Orçamentárias:** as informações demonstradas nesta são resultados do cálculo da fórmula: *Despesa Prevista + Suplementação + Antecipação + Transferência + Transferência de Saldo - Redução*;

- 
**Saldo disponível:** aqui será exibido o saldo para realizar transferências;

- 
**Realizado: **esta coluna exibirá todas as despesas reais, sem considerar possíveis devoluções.

Ao clicar no botão 

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/360074192813)

 **"Cadastrar Meta Atual [F8]"** na grade inferior da tela, você definirá qual será o orçamento destino das transferências, assim, ao clicar neste o sistema exibirá os campos para que o cadastro seja efetuado.

Entre os campos disponibilizados, tem-se que o **"Cód. Meta"** será o único indisponível para preenchimento, pois não é permitido transferências para orçamentos de outros planejamentos. No campo "Período" você informará o período que irá receber o saldo, considere o exemplo:

Se transferirmos R$ 100,00 de janeiro para julho, então julho será o Período destino que receberá o saldo.

Após preencher este e os demais campos da grade, clique em 

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/360072991754)

 para salvar as informações.

Para confirmar a transferência clique no botão **"Confirmar"**, após a confirmação será mostrada uma mensagem de confirmação antes de efetuar a transferência.

Caso queira realizar o estorno da transferência, deve-se inserir o código da transferência ou pesquisá-la no respectivo campo localizado no painel de filtros. Se este campo estiver preenchido com um valor válido, ao clicar no botão **"Aplicar"**, todos os orçamentos envolvidos naquela transferência serão carregados na tela.  Após o sistema trazer os orçamentos na transferência, clique no botão **"Estornar"** e confirme o estorno.

Todos os estornos são integrais, ou seja, se uma transferência teve origem em mais de um orçamento, o estorno será feito para todos orçamentos.

**Botão Outras Opções...**

Neste botão temos disponível a opção Atualização do Realizado, nele você poderá executar a atualização de maneira **"Automática"** ou **"Manual"**.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/360074200853)

No pop up exibido, poderemos selecionar se a Atualização ocorrerá de maneira **"Automática"** ou **"Manual"**.

Porém, independente da configuração que será realizada, você poderá utilizar o botão 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/360074186053)

 para atualizar o realizado sempre que houver a necessidade.

**Parâmetros que influenciam essa rotina**

**Remanejamento de saldos entre naturezas - REMANSALNAT:** quando este parâmetro estiver habilitado, o sistema permitirá a transferência de saldo para naturezas que não possuam valor definido, caso ele esteja desabilitado, seguirá o comportamento atual, validando se existe algum saldo para a natureza transferida.