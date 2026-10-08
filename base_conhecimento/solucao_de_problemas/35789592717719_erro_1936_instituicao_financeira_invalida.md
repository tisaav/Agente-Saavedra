# Erro 1936: Instituição financeira inválida

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35789592717719-Erro-1936-Institui%C3%A7%C3%A3o-financeira-inv%C3%A1lida](https://ajuda.sankhya.com.br/hc/pt-br/articles/35789592717719-Erro-1936-Institui%C3%A7%C3%A3o-financeira-inv%C3%A1lida)  
> **ID:** `35789592717719` | **Última Atualização:** 2026-07-29T13:21:09Z

---

**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309933268503)

********

| Módulo: Pessoal+ » Rotinas Folha » Central do eSocial |
| --- |

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35789637487383)

 **MENSAGEM**

[1936] Instituição financeira inválida.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35789592696599)

 **SITUAÇÃO**

O erro ocorre ao enviar os eventos **"S-1200"**, **"S-2299"** ou **"S-2399"** para o eSocial, quando o código da **"Instituição Financeira"** informado no evento de **"Empréstimo Crédito do Trabalhador"** não está presente na **"Tabela 37 – Instituições Financeiras para Empréstimo Consignado do eSocial"**. Geralmente, isso acontece porque foi utilizado um código incorreto, diferente do disponibilizado no arquivo oficial gerado no Portal Emprega Brasil.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35789592700183)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35789592702999)

  Corrija o lançamento da **"Instituição Financeira"** do **"Empréstimo Crédito do Trabalhador"**:

- 

Acesse **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento).

- 

Busque o funcionário e o lançamento do **"Desconto Crédito Trabalhador"**.

- 

Clique em **"Editar evento"** (ícone do lápis).

- 

Selecione o código correto da **"Instituição Financeira"** e salve as alterações.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35789637496599)

  Gere e envie o evento de remuneração: 

- 

Na **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial), gere o evento de remuneração e realize o envio para o eSocial.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35789637500439)

  **Importante:** Utilize sempre o código constante no arquivo oficial de empréstimos disponibilizado pelo Portal Emprega Brasil, garantindo a validação correta no eSocial.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35789637501719)

  Caso precise consultar a **"Tabela 37"**, acesse o passo a passo disponível em: [Como consultar a Tabela 37 - Instituições Financeiras para Empréstimo Consignado do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/35647758894231-Como-consultar-a-Tabela-37-Institui%C3%A7%C3%B5es-Financeiras-para-Empr%C3%A9stimo-Consignado-do-eSocial).

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35789637503639)

 **CAUSA**

O erro é causado pela utilização de um código de **"Instituição Financeira"** que não consta na **"Tabela 37 – Instituições Financeiras para Empréstimo Consignado do eSocial"**, geralmente por ter sido informado um código diferente do disponibilizado no arquivo oficial do Portal Emprega Brasil.


---

### 🔗 Links e Referências Internas:

- [Como consultar a Tabela 37 - Instituições Financeiras para Empréstimo Consignado do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/35647758894231-Como-consultar-a-Tabela-37-Institui%C3%A7%C3%B5es-Financeiras-para-Empr%C3%A9stimo-Consignado-do-eSocial)