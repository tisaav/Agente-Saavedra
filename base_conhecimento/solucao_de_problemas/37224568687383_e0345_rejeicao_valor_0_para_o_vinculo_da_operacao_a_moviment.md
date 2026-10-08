# E0345 Rejeição: Valor 0 para o Vínculo da Operação à Movimentação Temporária de Bens não é permitido na Sefin do Sistema Nacional NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224568687383-E0345-Rejei%C3%A7%C3%A3o-Valor-0-para-o-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224568687383-E0345-Rejei%C3%A7%C3%A3o-Valor-0-para-o-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e)  
> **ID:** `37224568687383` | **Última Atualização:** 2026-07-22T14:16:30Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224568678807)

 **MENSAGEM**

E0345 Rejeição: Valor 0 para o Vínculo da Operação à Movimentação Temporária de Bens não é permitido na Sefin do Sistema Nacional NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224568681111)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** no Sistema Nacional, o usuário informou o **valor "0" (zero)** no campo relacionado ao **vínculo da operação à movimentação temporária de bens**. Este preenchimento não é aceito pela **Sefin (Secretaria de Finanças)**, resultando na rejeição do documento fiscal com a mensagem de erro E0345.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224552819735)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224552820631)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224568683031)

 Localize o **tipo de operação** utilizado na emissão da NFS-e rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224552821655)

 Verifique se a operação está corretamente configurada para **movimentação temporária de bens**. Caso a operação não envolva movimentação temporária, ajuste o **vínculo da operação** para o tipo adequado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224568683927)

 Se a operação realmente envolver **movimentação temporária de bens**, certifique-se de que o campo relacionado ao vínculo esteja preenchido com um **valor válido diferente de zero**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224552823191)

 Revise o **cadastro da NFS-e** e confirme que todos os campos obrigatórios relacionados à **movimentação temporária** estão corretamente preenchidos conforme as exigências da Sefin.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37704649342231)

 Após realizar os ajustes necessários, **reemita a NFS-e** para que o documento seja validado e aprovado pela Sefin.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224568685591)

 **CAUSA**

A rejeição ocorreu porque o **Sistema Nacional NFS-e** não permite que o campo de **vínculo da operação à movimentação temporária de bens** seja preenchido com o **valor "0" (zero)**. A Sefin exige que, quando houver movimentação temporária de bens, este campo contenha um **valor válido e diferente de zero**, garantindo a correta identificação e tributação da operação fiscal.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)