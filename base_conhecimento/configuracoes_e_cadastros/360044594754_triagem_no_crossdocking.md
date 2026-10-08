# Triagem no Crossdocking

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594754-Triagem-no-Crossdocking](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594754-Triagem-no-Crossdocking)  
> **ID:** `360044594754` | **Última Atualização:** 2026-07-29T13:44:22Z

---

Esta rotina permite que você realize triagens quando existir um [Empenho do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos) para o Recebimento.

**Observação:** este processo só dará suporte à produtos que utilizarem o código de barras concatenado.

Primeiramente, para utilização correta desta rotina, deve-se atribuir a tarefa de Triagem Crossdocking ao executante, através da tela [Configurações por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354).

Após isto, é necessário efetuar a marcação **"Utiliza triagem no Crossdocking"** localizada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), conforme demonstrado abaixo:

![TC01.png](https://ajuda.sankhya.com.br/hc/article_attachments/9535088359831)

Assim, efetuadas as configurações acima, para que a rotina seja executada corretamente, deverá existir algum produto da Nota de Compra que contenha pelo menos um empenho realizado, ou seja, deve-se empenhar os itens de uma Nota de Compra em um Pedido de Venda para o Crossdocking; caso contrário, ao utilizar a função de Triagem Crossdocking no Coletor de Dados e informar a doca de recebimento, será exibida a seguinte mensagem:

***"Nenhuma triagem pendente encontrada para o endereço informado".***

**Observações:**

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16812010173591)

A mensagem acima também será exibida quando o Recebimento estiver com a situação **"Aguardando Conferência"**.

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16812010173591)

Apenas será autorizado o início da triagem quando a situação do Recebimento for **"Aguardando Armazenagem"**.

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16812010173591)

Quando um ou mais produtos forem triados e possuírem produtos não triados na grade, caso seja acionado o botão **"Tudo Crossdocking"** do Coletor de Dados, o sistema encaminhará para o Endereço de Crossdocking todo o estoque referente àquela triagem que existe na Doca de Entrada.

![Marcador 3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16812010173591)

A rotina de Triagem de Crossdocking não aceita quantidade de Empenho menor que a quantidade total, apenas maior.

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Empenho do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos)
- [Configurações por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa)
- [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms)