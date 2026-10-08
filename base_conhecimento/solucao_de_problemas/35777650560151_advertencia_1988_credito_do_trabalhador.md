# Advertência 1988 - Crédito do Trabalhador

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35777650560151-Advert%C3%AAncia-1988-Cr%C3%A9dito-do-Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/35777650560151-Advert%C3%AAncia-1988-Cr%C3%A9dito-do-Trabalhador)  
> **ID:** `35777650560151` | **Última Atualização:** 2026-07-29T13:21:01Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777650546839)

**MENSAGEM**

O trabalhador **"<cpfTrab>"**, matrícula **"<matricula>"** possui parcela(s) de empréstimo consignado do Programa Crédito do Trabalhador prevista para desconto na competência **"<MM/AAAA>"**. No entanto, o empregador informou os dados incorretos ou não informou rubrica de desconto do empréstimo neste evento.
Verifique a informação correta no arquivo disponibilizado no Portal Emprega Brasil e retifique este evento.
Foram localizados os seguintes contratos de empréstimo consignado com previsão de pagamento de parcela nesta competência: Instituição Financeira: **"<instFinanc>"** — Contrato **"<nrDoc>"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777650547351)

**SITUAÇÃO**

Durante o envio dos eventos **"S-1200"**, **"S-2299"** ou **"S-2399"**, o sistema identificou divergência entre os dados informados da Instituição Financeira e/ou o Número do Contrato de empréstimo consignado e as informações oficiais do Portal Emprega Brasil.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777658804247)

**SOLUÇÃO**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777650548631)

  Acesse a tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento).

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777658805015)

  Filtre a empresa e a referência (mês/ano), e selecione o funcionário indicado na mensagem.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777658805527)

  Localize a rubrica **"Empréstimo eConsignado"** (natureza **"9253"**) e clique em editar (ícone de lápis).

 

![advertencia-1988 - Carine Barreto Araujo.gif](https://ajuda.sankhya.com.br/hc/article_attachments/35777658806167)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777658806807)

  Ajuste os campos **"Instituição Financeira"** e/ou **"Contrato eConsignado"**, conforme a mensagem ou consulta no Portal Emprega Brasil. Salve as alterações.
No ícone de detalhes, confira os dados atualizados.

 

![advertencia-1988-corrigida - Carine Barreto Araujo.gif](https://ajuda.sankhya.com.br/hc/article_attachments/35777658807319)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40923400003607)

  Verifique se a **"Folha Mensal"** foi liberada para envio ao e-Social. Caso não tenha sido liberada, o evento do empréstimo consignado pode não ser processado corretamente.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777650552215)

  Acesse a **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial), gere e envie novamente o evento **"S-1200"**, **"S-2299"** ou **"S-2399"**.
Após o ajuste, o evento será recepcionado corretamente, sem a advertência.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35777658808727)

**CAUSA**

A advertência 1988 pode ocorrer por:

- 

**Divergência de dados:** Os dados da **"Instituição Financeira"** e/ou **"Número do Contrato"** informados no sistema não coincidem com as informações oficiais do Portal Emprega Brasil.
 

1. 

**Folha não liberada:** A folha mensal não foi liberada para envio ao e-Social, impedindo o processamento do evento.
 

1. 

**Falta de saldo ou erro de rubrica:** O empréstimo não foi descontado ou a rubrica de desconto não foi devidamente informada no sistema.