# Erro ao emitir NFC-e de SC: é necessário usar o PDV Web identificado

> **Módulo:** Solucao de Problemas | **Subseção:** Varejo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43548949980439-Erro-ao-emitir-NFC-e-de-SC-%C3%A9-necess%C3%A1rio-usar-o-PDV-Web-identificado](https://ajuda.sankhya.com.br/hc/pt-br/articles/43548949980439-Erro-ao-emitir-NFC-e-de-SC-%C3%A9-necess%C3%A1rio-usar-o-PDV-Web-identificado)  
> **ID:** `43548949980439` | **Última Atualização:** 2026-09-24T13:18:12Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/43548946157719)

** Mensagem**

Para emissão de NFC-e de SC é necessário usar o PDV Web identificado!

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43548949958423)

 **SITUAÇÃO**

Ao tentar emitir uma NFC-e para o estado de Santa Catarina (SC), o sistema apresenta a mensagem de erro informando que é necessário utilizar o PDV Web identificado para realizar a emissão.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43713555690519)

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/43548946157975)

** Solução**

Para solucionar o erro e permitir a emissão da NFC-e de SC, siga o passo a passo abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43548946158359)

 Acesse **Preferências (Configurações >> Avançado)** e localize o parâmetro **VALAPRRECPDV, m**antenha o parâmetro 'Desligado'

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43548946159511)

 Acesse **Usuários (Configurações > Controle de Acesso > Usuários)** e localize o usuário que será utilizado no **PDV Identificado**. Na aba **Identificação**, verifique se a marcação **“Caixa”** está desabilitada.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43548949959063)

 Acesse **Cadastro de PDV (****Comercial » Arquivo » Cadastro de PDV****)** e crie o cadastro do PDV, realizando as seguintes configurações:

- Informe a **Empresa** e mantenha o PDV como **Ativo**.

- Na aba **Geral**, informe a **Conta PDV** e a **Conta Tesouraria**, utilizando as mesmas contas configuradas para o usuário Caixa.

- Na aba **Usuários**, vincule o usuário que será utilizado como Caixa. 

- 

Por fim, clique em **“Vincular o PDV à estação física de trabalho”** para realizar o vínculo do PDV com a estação utilizada.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43728366118935)

Importante:** o usuário vinculado ao PDV não pode possuir a marcação **“Caixa”** em seu cadastro.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/43713555694487)

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/43548946174231)

** Causa**

A causa do erro está relacionada à obrigatoriedade, no estado de SC, a emissão de **NFC-e (modelo 65)** exige a identificação do hardware utilizado. Por isso, a emissão deve ser realizada pelo **PDV Web Identificado**, com as configurações e o layout devidamente parametrizados.