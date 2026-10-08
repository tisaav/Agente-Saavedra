# E0439 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN, quando o benefício municipal informado na DPS for do tipo "Isenção".

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225302557719-E0439-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-dos-campos-do-grupo-de-informa%C3%A7%C3%B5es-relativas-%C3%A0-Dedu%C3%A7%C3%A3o-Redu%C3%A7%C3%A3o-do-ISSQN-quando-o-benef%C3%ADcio-municipal-informado-na-DPS-for-do-tipo-Isen%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225302557719-E0439-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-dos-campos-do-grupo-de-informa%C3%A7%C3%B5es-relativas-%C3%A0-Dedu%C3%A7%C3%A3o-Redu%C3%A7%C3%A3o-do-ISSQN-quando-o-benef%C3%ADcio-municipal-informado-na-DPS-for-do-tipo-Isen%C3%A7%C3%A3o)  
> **ID:** `37225302557719` | **Última Atualização:** 2026-07-22T14:16:03Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225302532375)

 **MENSAGEM**

E0439 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN, quando o benefício municipal informado na DPS for do tipo "Isenção".

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225286724631)

 **SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviço Eletrônica), o usuário configurou na DPS (Declaração de Prestação de Serviços) um **benefício municipal do tipo "Isenção"** e, simultaneamente, preencheu campos relacionados ao **grupo de Dedução/Redução do ISSQN**. Essa combinação viola as regras de validação da Sefaz, resultando na rejeição da nota fiscal com a mensagem E0439.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225286727191)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225302538135)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225286730775)

 Localize o tipo de operação utilizado no documento fiscal rejeitado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225286734231)

 Navegue até a aba **"NFS-e"** e verifique as configurações relacionadas ao ISSQN.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225302545943)

 No campo **“Cód. Natureza Oper. ISS (NFS-e)”**, verifique se está configurado com a opção **“3 – Isenção”**.

- 

Essa configuração indica que o **benefício municipal aplicado é do tipo isenção**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225302547223)

 Verifique se há preenchimento nos campos relacionados a **deduções ou reduções do ISSQN**, tais como:

- 

**"Valor de Dedução"**

- 

**"Indicador de Dedução"**

- 

**"Valor Deduções"**

- 

**"Desconto Condicionado para NFS-e"**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225302548375)

 Caso existam valores preenchidos nos campos de **dedução ou redução do ISSQN** e o benefício municipal esteja configurado como **“3 – Isenção”**, realize uma das seguintes ações:

- 

**Remova os valores** dos campos de dedução/redução do ISSQN, mantendo apenas a configuração de **isenção**

- 

**Altere o tipo de benefício municipal** no campo **“Cód. Natureza Oper. ISS (NFS-e)”** para uma opção diferente de **“3 – Isenção”**, caso a operação realmente envolva **deduções ou reduções**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225302550039)

 Salve as alterações.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37676139361047)

 Retorne ao documento fiscal rejeitado e realize uma nova tentativa de emissão da NFS-e.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225302551447)

 **CAUSA**

A rejeição ocorre porque a **Sefaz não permite** que sejam informados simultaneamente um **benefício municipal do tipo "Isenção"** e valores no **grupo de Dedução/Redução do ISSQN**. Quando uma operação é classificada como isenta, não há base de cálculo sobre a qual aplicar deduções ou reduções, tornando o preenchimento desses campos incompatível com a natureza da operação. A validação visa garantir a **consistência das informações fiscais** enviadas no XML da NFS-e, evitando contradições entre o tipo de benefício declarado e os valores tributários informados.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)