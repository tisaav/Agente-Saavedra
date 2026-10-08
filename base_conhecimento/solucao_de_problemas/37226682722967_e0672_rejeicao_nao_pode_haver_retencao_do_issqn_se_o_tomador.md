# E0672 Rejeição: Não pode haver retenção do ISSQN se o tomador for o emitente da DPS e estiver estabelecido em município diferente do município de incidência do ISSQN.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226682722967-E0672-Rejei%C3%A7%C3%A3o-N%C3%A3o-pode-haver-reten%C3%A7%C3%A3o-do-ISSQN-se-o-tomador-for-o-emitente-da-DPS-e-estiver-estabelecido-em-munic%C3%ADpio-diferente-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226682722967-E0672-Rejei%C3%A7%C3%A3o-N%C3%A3o-pode-haver-reten%C3%A7%C3%A3o-do-ISSQN-se-o-tomador-for-o-emitente-da-DPS-e-estiver-estabelecido-em-munic%C3%ADpio-diferente-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN)  
> **ID:** `37226682722967` | **Última Atualização:** 2026-07-22T14:14:46Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226682711191)

 **MENSAGEM**

E0672 Rejeição: Não pode haver retenção do ISSQN se o tomador for o emitente da DPS e estiver estabelecido em município diferente do município de incidência do ISSQN.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226682712215)

 **SITUAÇÃO**

Ao tentar emitir uma NFS-e para um tomador de serviço localizado em município diferente do município onde ocorreu a prestação do serviço, com **retenção de ISSQN configurada**, a nota é rejeitada pela prefeitura apresentando a mensagem de erro E0672.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226682713623)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226682714007)

 Acesse o cadastro do **"Parceiro"** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37891369738135)

 Verifique o campo **“Retém ISS”** no cadastro da operação. Caso esteja configurado como **“Sim”**, altere para **“Não”**, uma vez que o tomador do serviço não possui inscrição no município de incidência do ISSQN.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226682715799)

 Confirme se o **CNPJ** e a **Inscrição Municipal** do tomador estão corretos no cadastro.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226666504343)

 Acesse a tela ****[''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas), na aba **''Cabeçalho''**, verifique se o campo **''Cidade de Prestação de Serviço''** está preenchido corretamente com o município onde o serviço foi efetivamente prestado.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226666505495)

 Acesse o cadastro do ****["Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226666505879)

 Na aba **“NFS-e”**, no campo **“Cód. Natureza Oper. ISS (NFS-e)”**, selecione a natureza de operação adequada à prestação do serviço, garantindo que a configuração esteja compatível com **operações sem retenção de ISS**, quando o tomador estiver localizado em município diferente do município de incidência do imposto.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226682719255)

 Gere novamente o lote da NFS-e e exporte o arquivo XML no Portal de Vendas (NFS-e » Gerar XML do RPS para NFS-e).

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226682719383)

 Verifique no XML se a tag **<ISSRetido>** está preenchida com **"2"** (Sem retenção de ISSQN). Se estiver com valor diferente, revise as configurações anteriores. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226682719895)

 **CAUSA**

A rejeição ocorre porque o sistema está configurado para **reter o ISSQN**, porém o **tomador do serviço não está inscrito no município de incidência do imposto**. Segundo as regras da legislação tributária municipal, **apenas empresas inscritas no município podem efetuar a retenção de ISSQN**. Quando o tomador está estabelecido em município diferente do município onde ocorreu a prestação do serviço, a retenção não é permitida, devendo o ISSQN ser recolhido pelo prestador no município de incidência.


---

### 🔗 Links e Referências Internas:

- [''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- ["Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)