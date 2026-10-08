# E0037 Rejeição: O código do município emissor informado na DPS é inexistente no cadastro de convênio municipal do sistema nacional.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221555865495-E0037-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-emissor-informado-na-DPS-%C3%A9-inexistente-no-cadastro-de-conv%C3%AAnio-municipal-do-sistema-nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221555865495-E0037-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-emissor-informado-na-DPS-%C3%A9-inexistente-no-cadastro-de-conv%C3%AAnio-municipal-do-sistema-nacional)  
> **ID:** `37221555865495` | **Última Atualização:** 2026-07-22T14:18:34Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221570777239)

 **MENSAGEM**

E0037 Rejeição: O código do município emissor informado na DPS é inexistente no cadastro de convênio municipal do sistema nacional.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221570777751)

 **SITUAÇÃO**

Esta rejeição ocorre ao tentar **emitir uma NFS-e** (Nota Fiscal de Serviços Eletrônica) quando o **código do município emissor** informado no documento não está cadastrado ou não possui convênio ativo no Sistema Nacional de Notas Fiscais de Serviços Eletrônicas.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221570779415)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221570779927)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize a **empresa emissora** da NFS-e.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37856574572439)

 Na aba **''Endereço''** no campo **''Cód. Cidade''**, verifique o código cadastrado para a empresa e confirme se o códio do município está correto.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221555851927)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e localize o município da empresa emissora.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221570781463)

 Na aba **''Geral''**, verifique se o campo **''Mun. domícilio fiscal''** está preenchido com o código correto do município conforme a Tabela do IBGE. 

- 

Para consultar o código correto, acesse o site do ****[''IBGE''](https://cidades.ibge.gov.br/)**.**

- 

Digite o nome da cidade na pesquisa e localize a informação **"Código do Município"**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221555853463)

 Caso o código esteja incorreto, retorne o passo 3 e 4 e corrija o campo "Mun. domicílio fiscal" com a informação obtida no IBGE.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221555854103)

 Verifique se o **município possui convênio ativo** com o Sistema Nacional de NFS-e.

- 

Caso o município não esteja conveniado, a emissão deverá ser realizada pelo sistema próprio da prefeitura.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221570783383)

 Após realizar as correções necessárias, retorne à **NFS-e rejeitada** e tente realizar a **transmissão novamente**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221555857815)

 Se a rejeição persistir, **cancele ou inutilize** a NFS-e rejeitada e refaça o lançamento com os dados corretos. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221555858455)

 **CAUSA**

Esta rejeição ocorre quando o **código do município emissor** informado na DPS (Declaração de Prestação de Serviços) está **incorreto, desatualizado ou não consta** no cadastro de convênios municipais do Sistema Nacional. Isso pode acontecer quando:

- 

O código do município cadastrado na empresa ou na cidade está **divergente do código oficial do IBGE**

- 

O município **não possui convênio ativo** com o Sistema Nacional de NFS-e

- 

Houve **erro de digitação** no cadastro do código do município

- 

O cadastro da cidade está **desatualizado** no sistema


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)