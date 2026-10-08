# REJEIÇÃO E0204: CNPJ ou CPF do tomador não foi informado, mas existe uma indicação para retenção do ISSQN na DPS no campo de tipo "Retenção do ISSQN"

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222627581207-REJEI%C3%87%C3%83O-E0204-CNPJ-ou-CPF-do-tomador-n%C3%A3o-foi-informado-mas-existe-uma-indica%C3%A7%C3%A3o-para-reten%C3%A7%C3%A3o-do-ISSQN-na-DPS-no-campo-de-tipo-Reten%C3%A7%C3%A3o-do-ISSQN](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222627581207-REJEI%C3%87%C3%83O-E0204-CNPJ-ou-CPF-do-tomador-n%C3%A3o-foi-informado-mas-existe-uma-indica%C3%A7%C3%A3o-para-reten%C3%A7%C3%A3o-do-ISSQN-na-DPS-no-campo-de-tipo-Reten%C3%A7%C3%A3o-do-ISSQN)  
> **ID:** `37222627581207` | **Última Atualização:** 2026-07-22T14:17:36Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222627569431)

 **MENSAGEM**

E0204 Rejeição: CNPJ ou CPF do tomador não foi informado, mas existe uma indicação para retenção do ISSQN na DPS no campo de tipo "Retenção do ISSQN".

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222627570711)

 **SITUAÇÃO**

Ao tentar emitir uma NFS-e (Nota Fiscal de Serviços Eletrônica) com **retenção de ISSQN**, a nota é rejeitada pela prefeitura apresentando a mensagem de erro E0204. Isso ocorre quando o sistema identifica que foi configurada a **retenção do imposto**, porém o **CNPJ ou CPF do tomador do serviço** não foi informado corretamente no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222627571223)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222663130775)

 Acesse o cadastro do **"Parceiro"** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço para o qual está emitindo a NFS-e.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222627572247)

 Na aba **''Identificação''**, verifique se o campo **''CNPJ / CPF''** está preenchido corretamente.

- 

Caso esteja vazio ou incorreto, corrija a informação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222663132055)

 Caso o tomador possua **Inscrição Municipal**, verifique se este campo também está preenchido corretamente no cadastro do parceiro.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222663132695)

 Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222627574167)

 Na grade **''Rodapé''**, verifique na aba **''Impostos'' **o campo** ''Tipo de Retenção do ISS''**. Certifique-se de que está configurado corretamente:

- 

**''Não Retido'':** quando não há retenção de ISS;

- 

**''Retido pelo Tomador'':** quando o tomador é responsável pela retenção;

- 

**''Retido pelo Intermediário'':** quando há intermediário responsável pela retenção.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222663134487)

 Se o tomador **não deve reter o ISS**, acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222663134999)

 Na aba **''Fiscal''**, desmarque o campo **"Retém ISS"**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38326079211031)

 Em seguida, no documento fiscal, altere o campo "Tipo de Retenção do ISS" para "Não retido".

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38328955616151)

 Após realizar as correções, gere novamente o lote da NFS-e e tente transmitir o documento fiscal.

![10 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38328964317847)

 Se o erro persistir, retorne ao **passo 4**, clique em **''NFS-e''** e selecione a opção **''Gerar XML do RPS para NFS-e''**. No XML gerado, verifique se as tags relacionadas ao tomador estão preenchidas corretamente, especialmente as informações de **CNPJ/CPF** e **ISSRetido**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222663135511)

 **CAUSA**

A rejeição E0204 ocorre porque o sistema identificou que existe uma **indicação de retenção de ISSQN** configurada no documento fiscal (campo "Tipo de Retenção do ISSQN"), porém o **CNPJ ou CPF do tomador do serviço não foi informado** ou está incorreto. A prefeitura exige que, quando houver retenção de ISS, os dados cadastrais completos do tomador sejam enviados no XML da NFS-e, incluindo obrigatoriamente o documento de identificação (CNPJ ou CPF). Sem essa informação, não é possível identificar o responsável pela retenção do imposto, resultando na rejeição do documento fiscal.