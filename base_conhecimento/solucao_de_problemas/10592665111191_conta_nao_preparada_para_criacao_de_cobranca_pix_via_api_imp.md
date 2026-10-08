# Conta não preparada para Criação de Cobrança PIX via API. Impressão cancelada

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10592665111191-Conta-n%C3%A3o-preparada-para-Cria%C3%A7%C3%A3o-de-Cobran%C3%A7a-PIX-via-API-Impress%C3%A3o-cancelada](https://ajuda.sankhya.com.br/hc/pt-br/articles/10592665111191-Conta-n%C3%A3o-preparada-para-Cria%C3%A7%C3%A3o-de-Cobran%C3%A7a-PIX-via-API-Impress%C3%A3o-cancelada)  
> **ID:** `10592665111191` | **Última Atualização:** 2026-07-22T15:03:19Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18972372943895)

 MENSAGEM:**

[CORE_E06638] Conta não preparada para Criação de Cobrança PIX via API. Impressão cancelada.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18972356470295)

 SITUAÇÃO:**

Ao realizar o recebimento na movimentação financeira a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18972356475031)

 CAUSA: **

Ocorre quando os dados não estão preenchidos corretamente no cadastro da conta bancária.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18972356480791)

 SOLUÇÃO:**

Para gerar uma cobrança avulsa como meio de pagamento via PIX, acesse a tela 'Contas', vá até a aba 'Boleto(s)/Duplicatas' e configure a conta bancária para emitir cobranças através da marcação 'Cobranças Pix Api. 

Em seguida, na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), realize a geração de um lançamento financeiro de receita por meio do botão 

![cadastrar_financeiro.png](https://ajuda.sankhya.com.br/hc/article_attachments/18972373105431)

 **"Cadastrar Financeiro [F8]"**e preencha os campos obrigatórios da tela.

Por fim, utilize a opção **"Imprimir Pix", **no botão Outras Opções, para que assim o documento de cobrança seja gerado. Na geração deste, os dados do QR Code e o ID da Transação ficarão gravados nos campos **"PIX Copia e Cola", **da aba [Cobrança,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abacobran%C3%A7a) e no **"TXID Pix" **da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abageral), respectivamente.

Caso já exista um título de receita real e pendente, e possua os dados do QR Code e ID da Transação gravados nos seus respectivos campos, ao acionar a opção Imprimir Pix a reimpressão do documento de cobrança será realizada.

 

**Importante:** Se a conta bancária não estiver preparada para a geração de Cobrança Pix no momento da impressão, ou seja, se os dados não estiverem preenchidos corretamente, você será informado por meio da mensagem:

 

***"Não foi possível imprimir pix. Conta não preparada para Criação de Cobrança Pix via API. Impressão cancelada."***

Para mais informações sobre as configurações necessárias, acesse o manual abaixo:

[Pix – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/4413021641495-Pix#Pixrecebimento)


---

### 🔗 Links e Referências Internas:

- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)
- [Cobrança,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abacobran%C3%A7a)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abageral)
- [Pix – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/4413021641495-Pix#Pixrecebimento)