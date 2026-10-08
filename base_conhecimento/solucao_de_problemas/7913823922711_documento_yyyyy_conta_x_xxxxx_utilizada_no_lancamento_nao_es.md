# Documento YYYYY: Conta X - XXXXX utilizada no lançamento, não está configurada para emissao de boletos

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7913823922711-Documento-YYYYY-Conta-X-XXXXX-utilizada-no-lan%C3%A7amento-n%C3%A3o-est%C3%A1-configurada-para-emissao-de-boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/7913823922711-Documento-YYYYY-Conta-X-XXXXX-utilizada-no-lan%C3%A7amento-n%C3%A3o-est%C3%A1-configurada-para-emissao-de-boletos)  
> **ID:** `7913823922711` | **Última Atualização:** 2026-07-22T15:12:47Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361408917527)

 MENSAGEM:**

Documento YYYYY: Conta X - XXXXX utilizada no lançamento, não está configurada para emissão de boletos. VERIFIQUE (Configurações Cadastros Bancários Contas » ABA: boletos/duplicatas: campo: EMITE). =IP.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14680102800023)

 

**Porém, existe um caso frequente quando a configuração foi feita conforme print acima, mas não é um boleto.***
*Quando o financeiro da nota possui mais de uma forma de pagamento, sendo uma delas o boleto propriamente dito e outro cadastrado como boleto, mas que não é efetivamente um, o sistema apresenta a mensagem para que seja configurada a opção de emissão na conta bancária.*
*

**Exemplo:** Cliente realiza venda que será paga de duas formas:
1 - Boleto bancário;
2 - Saldo de crédito do cliente na loja.

No registro da forma de pagamento 2 (conta bancária) foi selecionada a opção 'boleto', porém por não ser um de fato foi desmarcada a opção Emite. No entanto, como a outra forma de pagamento é boleto e precisará ser impresso, ao mandar imprimir o sistema retornará o erro pela inconsistência. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361408918807)

SOLUÇÃO:**
Verifique o Tipo de Título vinculado àquela movimentação financeira que não é verdadeiramente um boleto. 
Abra a tela **"Tipos de Título"** e verifique na aba **"Geral"** se a opção **"Proibir impressão de boleto?"** está marcada. Caso não esteja, marque a opção, salve as configurações e emita novamente os boletos pela Central.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361416379671)

 IMPORTANTE:**

Verifique também se o campo **"Tipo de pgto para NFC-e/NF-e/CF-e"** representa de fato o tipo de operação do título.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14680164179479)

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361416381975)

CAUSA:**

Apresenta esta mensagem sempre que uma 'Conta Bancária' for configurada como boleto e ao tentar emitir o boleto, a opção **"Emite"** da tela **"Contas", **aba **"Boleto(s)/Duplicatas"**, campo **"Boleto Avançado/Duplicatas"** está desmarcada.