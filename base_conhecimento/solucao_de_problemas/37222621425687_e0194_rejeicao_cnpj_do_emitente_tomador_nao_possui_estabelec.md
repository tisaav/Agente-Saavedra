# E0194 Rejeição: CNPJ do emitente tomador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222621425687-E0194-Rejei%C3%A7%C3%A3o-CNPJ-do-emitente-tomador-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CNPJ-e-CNC-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222621425687-E0194-Rejei%C3%A7%C3%A3o-CNPJ-do-emitente-tomador-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CNPJ-e-CNC-NFS-e)  
> **ID:** `37222621425687` | **Última Atualização:** 2026-07-22T14:17:38Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222621398807)

 **MENSAGEM**

E0194 Rejeição: CNPJ do emitente tomador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222621399447)

 **SITUAÇÃO**

Ao tentar emitir uma NFS-e para um tomador de serviços com retenção de ISSQN, o sistema apresenta a mensagem de rejeição informando que **o CNPJ do tomador não possui estabelecimento ou domicílio fiscal no município emissor** da nota fiscal, conforme os cadastros oficiais (CNPJ e CNC NFS-e) na data de competência informada.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222606714391)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222621406231)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do tomador do serviço envolvido na NFS-e rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222606716951)

 Na aba **''Identificação''**, verifique se os campos **''CNPJ / CPF''** e **''Cad. Mun. Contribuintes'' **do tomador estão preenchidos corretamente e se correspondem aos dados cadastrados na Receita Federal e na Prefeitura do município emissor.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222621407895)

 Caso o tomador **não possua estabelecimento ou domicílio fiscal no município emissor**, altere a configuração de retenção de ISSQN:

- 

Na aba **"Fiscal''**, localize o campo **''Retém ISS''**;

- 

Desmarque o campo ''Retém ISS''.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222621411223)

 Acesse a tela **"Cidades"** (Configurações » Cadastros » Endereços » Cidades) e localize o município do tomador.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222606721687)

 Na aba **"Geral"**, verifique se o campo **"Mun. domicílio fiscal"** está preenchido corretamente com o código do município conforme cadastro do IBGE. Para consultar o código correto:

- 

Acesse o site do ****[''IBGE''](https://cidades.ibge.gov.br/)**;**

- 

Pesquise pelo nome da cidade;

- 

Localize a informação **"Código do Município"** e insira no campo "Mun. domicílio fiscal".

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222621414679)

 Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222621417239)

 Na aba **"NFS-e"**, verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"** e certifique-se de que está configurado corretamente conforme a natureza da operação.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222606725527)

 Após realizar os ajustes necessários, emita novamente a NFS-e. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222621419671)

 **CAUSA**

A rejeição ocorre quando o **tomador do serviço não possui estabelecimento ou domicílio fiscal cadastrado no município emissor** da NFS-e, conforme validação realizada pela prefeitura nos cadastros oficiais (CNPJ e CNC NFS-e). A prefeitura **não permite que empresas sem inscrição no município efetuem retenção de ISSQN**, pois o tomador precisa estar regularmente cadastrado no município para que a retenção seja válida. Quando o sistema tenta emitir a nota com retenção de ISSQN para um tomador não cadastrado no município, a validação falha e a nota é rejeitada.