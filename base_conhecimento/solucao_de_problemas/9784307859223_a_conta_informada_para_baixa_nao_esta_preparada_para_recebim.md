# A conta informada para baixa não está preparada para recebimento com PIX

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9784307859223-A-conta-informada-para-baixa-n%C3%A3o-est%C3%A1-preparada-para-recebimento-com-PIX](https://ajuda.sankhya.com.br/hc/pt-br/articles/9784307859223-A-conta-informada-para-baixa-n%C3%A3o-est%C3%A1-preparada-para-recebimento-com-PIX)  
> **ID:** `9784307859223` | **Última Atualização:** 2026-07-22T15:06:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789932411671)

 MENSAGEM:**

[CORE_E06645] A conta informada para baixa não está preparada para recebimento com PIX.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789932417047)

 SITUAÇÃO:**

Ao tentar receber um título a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789925707927)

 CAUSA:**

Quando a conta não está devidamente configurada com as informações do PIX.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18789932424983)

 SOLUÇÃO:**

Para que seja possível o recebimento com PIX, verifique as configurações na **movimentação financeira** *(Financeiro » Rotinas » Movimentação Financeira)*.

O botão Receber com Pix, permitirá que você realize o recebimento de um título de receita (real/pendente) por meio da transação Pix. 

![Receber_com_pix.png](https://ajuda.sankhya.com.br/hc/article_attachments/9784252611223)

Para utilizar essa funcionalidade, acesse a tela '[Contas'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), vá até a aba '[Pix'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abapix) e preencha devidamente os campos **"Client Secret Pix"**,**"Client ID Pix" **e **"Chave Pix"**. 

Dessa forma, na tela de Baixa da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), quando o botão Receber com Pix for acionado, o sistema validará as informações do título em questão e o enviará para a API. Assim, um QR Code será gerado para que você realize a leitura deste e faça o pagamento.

Para verificar todas as configurações necessárias acesse o link abaixo:

[Movimentação Financeira - Baixa de Títulos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos#recebercompix)


---

### 🔗 Links e Referências Internas:

- [Contas'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)
- [Pix'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abapix)
- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)
- [Movimentação Financeira - Baixa de Títulos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos#recebercompix)