# Valor do campo Nro Único [XXXX] maior que o número permitido: 99

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000050962-Valor-do-campo-Nro-%C3%9Anico-XXXX-maior-que-o-n%C3%BAmero-permitido-99](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000050962-Valor-do-campo-Nro-%C3%9Anico-XXXX-maior-que-o-n%C3%BAmero-permitido-99)  
> **ID:** `1500000050962` | **Última Atualização:** 2026-07-22T15:26:27Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273129563031)

 MENSAGEM**:

Valor do campo Nro Único [XXXX] maior que o número permitido: 99

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273129566615)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273108968983)

 Acesse o cadastro de **Contas** - *Configurações » Cadastros » Bancários » Contas*
Aba: **"Intercâmbio Eletrônico de Dados (EDI)"**
Campo "**Convênio"**: Código que identifica o posto da cooperativa. Verifique com o gerente/banco Sicredi.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273129574295)

 Após o ajuste, gere novamente o documento.

 

**Nota:** O sistema possui uma regra interna onde informando no campo "Convênio" o valor zero, automaticamente é feito a substituição para o valor 7, caso essa regra não atenda a necessidade da empresa a configuração para geração de nosso número deverá ser realizada na aba Boleto(s)/Duplicatas >> quadrante Geração do Nosso Número seguindo as orientações do manual do banco.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16273108972055)

 CAUSA:**

Para o banco SICREDI, o convênio da Conta Bancaria leva o valor do Posto Cedente, que é de apenas 2 dígitos, caso esteja com um valor diferente, ocorre o erro.