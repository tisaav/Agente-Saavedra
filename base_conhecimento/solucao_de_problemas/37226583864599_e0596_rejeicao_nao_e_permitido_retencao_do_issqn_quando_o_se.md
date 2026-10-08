# E0596 Rejeição: Não é permitido retenção do ISSQN quando o serviço prestado corresponder ao subitem 220101 - Serviço de exploração de rodovia da lista de serviços do Sistema Nacional NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226583864599-E0596-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-quando-o-servi%C3%A7o-prestado-corresponder-ao-subitem-220101-Servi%C3%A7o-de-explora%C3%A7%C3%A3o-de-rodovia-da-lista-de-servi%C3%A7os-do-Sistema-Nacional-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226583864599-E0596-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-quando-o-servi%C3%A7o-prestado-corresponder-ao-subitem-220101-Servi%C3%A7o-de-explora%C3%A7%C3%A3o-de-rodovia-da-lista-de-servi%C3%A7os-do-Sistema-Nacional-NFS-e)  
> **ID:** `37226583864599` | **Última Atualização:** 2026-07-22T14:14:51Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226567582487)

 MENSAGEM**

E0596 Rejeição: Não é permitido retenção do ISSQN quando o serviço prestado corresponder ao subitem 220101 - Serviço de exploração de rodovia da lista de serviços do Sistema Nacional NFS-e.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226583854487)

 SITUAÇÃO**

Ao emitir uma Nota Fiscal de Serviço Eletrônica (NFS-e) para o serviço de exploração de rodovia (código 220101 da lista de serviços), o sistema apresenta a mensagem de rejeição informando que **não é permitida a retenção do ISSQN** para este tipo específico de serviço.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226567583383)

 SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226567585559)

 Acesse a tela **"Parceiro"** (Configurações » Cadastros » Parceiros) que está configurado como tomador do serviço na nota fiscal.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226583855895)

 Localize a configuração relacionada à **retenção de ISSQN** no cadastro do parceiro.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226567588119)

 Na aba **''Fiscal''**, desmarque o campo **''Retém ISS''**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226583857815)

 Acesse o cadastro do ****["Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) utilizado na emissão da nota fiscal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226567588631)

  Na aba **"NFS-e"**, verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"** e certifique-se de que está configurado adequadamente para operações sem retenção de ISSQN.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226583859095)

 Salve as alterações.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226567589399)

 Emita novamente a NFS-e para o serviço de exploração de rodovia, garantindo que **não haja retenção de ISSQN** configurada na operação.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226567591191)

 CAUSA**

A rejeição ocorre porque o **Sistema Nacional NFS-e não permite a retenção do ISSQN** para serviços classificados com o código **220101 - Serviço de exploração de rodovia**. Esta é uma regra específica estabelecida pela legislação tributária municipal, que determina que este tipo de serviço possui tratamento diferenciado quanto à retenção do imposto. Quando o sistema identifica que há configuração de retenção de ISSQN para este serviço específico, seja no cadastro do parceiro ou na operação fiscal, a nota é rejeitada automaticamente pela prefeitura.


---

### 🔗 Links e Referências Internas:

- ["Tipo de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)