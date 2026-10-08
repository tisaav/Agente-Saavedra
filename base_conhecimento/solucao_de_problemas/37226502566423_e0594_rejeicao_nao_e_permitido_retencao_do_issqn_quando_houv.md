# E0594 Rejeição: Não é permitido retenção do ISSQN quando houver Benefício Municipal do tipo Isenção.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226502566423-E0594-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-quando-houver-Benef%C3%ADcio-Municipal-do-tipo-Isen%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226502566423-E0594-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-quando-houver-Benef%C3%ADcio-Municipal-do-tipo-Isen%C3%A7%C3%A3o)  
> **ID:** `37226502566423` | **Última Atualização:** 2026-07-22T14:14:52Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226517307927)

 **MENSAGEM**

E0594 Rejeição: Não é permitido retenção do ISSQN quando houver Benefício Municipal do tipo Isenção.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226502554263)

 **SITUAÇÃO**

Ao tentar emitir uma NFS-e (Nota Fiscal de Serviços eletrônica), o sistema apresenta a mensagem de rejeição informando que **não é permitida a retenção do ISSQN** quando existe um **benefício fiscal municipal do tipo isenção** configurado para a operação.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226517309847)

 **SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226517310487)

 Acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a TOP utilizada na emissão da NFS-e. 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226517310999)

 Na aba **"NFS-e"**, verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"**. Certifique-se de que o código configurado **não seja do tipo isenção** (código 3 - Isenção) quando houver retenção de ISSQN. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226517311383)

 Caso a operação possua **benefício fiscal municipal de isenção**, altere o campo **"ISSQN Retido"** para a opção **"2 - Sem retenção de ISSQN"** no cadastro do parceiro ou na própria nota fiscal. 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226502559255)

 Acesse o cadastro de **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37636769325335)

 Na aba de **''Fiscal''**, verifique se o campo **"Retém ISS"** está marcado. Caso esteja marcado e a operação possua isenção municipal, **desmarque esta opção**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226502562071)

 Valide no **manual da Prefeitura do Município** se realmente existe benefício fiscal de isenção para o serviço prestado e se a retenção de ISSQN é permitida neste cenário.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226502563095)

 Após realizar os ajustes necessários, tente emitir novamente a NFS-e. 
 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226517316119)

 **CAUSA**

A rejeição ocorre porque a **legislação municipal não permite** que haja **retenção de ISSQN** em operações que possuem **benefício fiscal do tipo isenção**. Quando a nota fiscal é configurada com retenção de ISS e simultaneamente possui um código de natureza de operação ou benefício municipal indicando isenção, há uma **incompatibilidade fiscal** que resulta na rejeição pela prefeitura. O sistema identifica essa inconsistência entre a configuração de retenção e o benefício de isenção aplicado, impedindo a autorização do documento fiscal.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)