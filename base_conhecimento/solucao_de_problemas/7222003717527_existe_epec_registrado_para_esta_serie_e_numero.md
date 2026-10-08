# Existe EPEC registrado para esta Série e Numero

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7222003717527-Existe-EPEC-registrado-para-esta-S%C3%A9rie-e-Numero](https://ajuda.sankhya.com.br/hc/pt-br/articles/7222003717527-Existe-EPEC-registrado-para-esta-S%C3%A9rie-e-Numero)  
> **ID:** `7222003717527` | **Última Atualização:** 2026-09-17T15:17:04Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16504601719959)

**Mensagem**

[692] Rejeição: Existe EPEC registrado para esta Série e Número

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/43563364492311)

**Situação**

Esta rejeição ocorre ao tentar transmitir uma NF-e à SEFAZ após a emissão em **"Contingência EPEC"**. O erro indica que já existe um registro de EPEC para a mesma série e número da nota fiscal que está sendo transmitida, porém com dados divergentes entre o EPEC registrado e a NF-e que está sendo enviada.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16504615394327)

**Solução**

Ao enviar uma NF-e em EPEC, antes que a Sefaz devolva o retorno do documento, pode ocorrer o reenvio da mesma NF-e, mas com o cNF (Código Numérico) diferente do primeiro envio. Como o cNF faz parte da Chave de Acesso, a divergência gera a rejeição.

Para resolver esta rejeição, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43563401681175)

 Verifique se houve **"alteração nos dados da nota"** após o envio do EPEC. Compare as informações da NF-e com os dados registrados no EPEC junto à SEFAZ.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43563401681687)

 Caso tenha ocorrido alteração nos dados, será necessário **"anular o EPEC"** diretamente no portal da SEFAZ do seu estado.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43563364494231)

 Após anular o EPEC, **"exclua a nota fiscal"** no sistema Sankhya (esta exclusão deve ser realizada pela equipe de tecnologia via banco de dados, devido ao vínculo com o EPEC).
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43563401684503)

**"Gere novamente a nota fiscal"** com os dados corretos e transmita-a à SEFAZ.
 

Caso o problema persista, entre em contato com a equipe do Service Desk para análise técnica.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16504615396759)

Atenção**

Evite utilizar a mesma numeração para emissão normal e para contingência, pois isso causa conflitos e EPECs pendentes de Conciliação. Para mais informações, consulte: [Ambiente de Contingência EPEC bloqueado para o Emitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102893-Status-de-retorno-142-motivo-Ambiente-de-Contingencia-EPEC-bloqueado-para-o-Emitente-Como-resolver-).

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16504615404055)

**Causa**

A rejeição ocorre quando, para uma NF-e (modelo 55) em contingência, já existe na SEFAZ um EPEC registrado com o mesmo número, série, modelo, CNPJ e UF.

- 

Divergência de dados (valores, produtos, impostos) após envio do EPEC.

- 

Reutilização de numeração.

- 

Falhas de sincronização sistema/SEFAZ.
 

**Regra de Validação da Sefaz:**

![Regra de Validação](https://www.oobj.com.br/bc/assets/Articles/830/RV692.PNG)


---

### 🔗 Links e Referências Internas:

- [Ambiente de Contingência EPEC bloqueado para o Emitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102893-Status-de-retorno-142-motivo-Ambiente-de-Contingencia-EPEC-bloqueado-para-o-Emitente-Como-resolver-)