# E0583 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que seja MEI na data de competência informada na DPS

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226477339159-E0583-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-para-o-prestador-do-servi%C3%A7o-que-seja-MEI-na-data-de-compet%C3%AAncia-informada-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226477339159-E0583-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-para-o-prestador-do-servi%C3%A7o-que-seja-MEI-na-data-de-compet%C3%AAncia-informada-na-DPS)  
> **ID:** `37226477339159` | **Última Atualização:** 2026-07-22T14:14:54Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226477326871)

 **MENSAGEM**

E0583 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que seja MEI na data de competência informada na DPS.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226496199831)

 **SITUAÇÃO**

Ao tentar emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** com retenção de ISSQN, a nota é rejeitada pela prefeitura apresentando a mensagem de erro E0583, informando que **não é permitida a retenção do imposto** quando o prestador do serviço é **Microempreendedor Individual (MEI)**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226496200855)

 **SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226477329687)

 Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226496201879)

 Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''Geral''**, verifique se o campo **"Cód. Reg. trib. ISS (NFS-e)"** está configurado com a opção **"8 - Tributável MEI"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226496202135)

 Acesse a tela** "Parceiro"** (Configurações » Cadastros » Parceiros).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37894300674071)

 Na aba** ''Fiscal''**, marque o campo **''Retém ISS''** garatindo que não haverá retenção do imposto nas operações com este parceiro.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37894287408535)

 Caso a retenção esteja sendo configurada na TOP, acesse a tela ****["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37894287409943)

 Na aba **"NFS-e"**, verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"** e certifique-se de que a **natureza da operação não está configurada para reter ISSQN**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37894287410967)

 Após realizar os ajustes necessários, **gere novamente a NFS-e** e verifique se a rejeição foi solucionada. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226496205079)

 **CAUSA**

A rejeição ocorre porque a **legislação tributária não permite que empresas optantes pelo regime MEI** (Microempreendedor Individual) tenham **retenção de ISSQN** em suas operações. Quando o sistema identifica que o prestador é MEI e a nota está configurada com retenção do imposto, a prefeitura rejeita automaticamente o documento fiscal, gerando a mensagem de erro E0583.


---

### 🔗 Links e Referências Internas:

- ["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)