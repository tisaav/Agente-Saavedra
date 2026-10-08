# E0254 Rejeição: CNPJ do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223045903127-E0254-Rejei%C3%A7%C3%A3o-CNPJ-do-emitente-intermedi%C3%A1rio-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CNPJ-e-CNC-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223045903127-E0254-Rejei%C3%A7%C3%A3o-CNPJ-do-emitente-intermedi%C3%A1rio-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CNPJ-e-CNC-NFS-e)  
> **ID:** `37223045903127` | **Última Atualização:** 2026-07-22T14:17:05Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223061048727)

 **MENSAGEM**

E0254 Rejeição: CNPJ do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223061049239)

 **SITUAÇÃO**

Esta rejeição ocorre ao emitir uma **Declaração de Prestação de Serviços (DPS)** informando um **emitente intermediário** cujo CNPJ não possui estabelecimento ou domicílio fiscal cadastrado no mesmo município do emitente principal da DPS, considerando a data de competência informada no documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223045898519)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223045900055)

 Consulte o cadastro do **CNPJ do emitente intermediário** no site oficial da Receita Federal e verifique:

- 

A situação cadastral do CNPJ.

- 

O município de domicílio fiscal informado.

- 

A existência de filiais e os respectivos municípios de cada estabelecimento.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223061050391)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223061050647)

 Localize o cadastro do **emitente intermediário** utilizado na DPS.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223045900823)

 Na aba **“Geral”**, no campo **“CNPJ/CPF”**, confirme se o CNPJ informado está correto e corresponde a um estabelecimento situado **no mesmo município do emitente principal da NFS-e**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223045901335)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37798397588119)

 Verifique o cadastro do município vinculado ao endereço do emitente intermediário:

- 

Confirme se a cidade selecionada está correta.

- 

Verifique o campo **“Mun. Domicílio Fiscal”** e valide se o código do município está conforme a tabela oficial do IBGE.

- 

Caso necessário, consulte o código correto no site do **IBGE** e realize o ajuste.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38495644670999)

 Caso o emitente intermediário **não possua estabelecimento no mesmo município** do emitente principal:

- 

Utilize o **CNPJ de uma filial** localizada no município correto.

- 

Remova a informação do emitente intermediário da DPS, caso essa informação não seja obrigatória para a operação.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38495658086551)

 Após realizar os ajustes necessários, **redigite o cabeçalho da DPS**, gere um novo lote e realize novamente a transmissão do documento fiscal. 

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223061051927)

 **CAUSA**

A rejeição ocorre quando o **CNPJ do emitente intermediário** informado na DPS não possui estabelecimento ou domicílio fiscal cadastrado no mesmo município do emitente principal do documento, conforme validação realizada pela SEFAZ nos cadastros oficiais (CNPJ e CNC NFS-e), considerando a **data de competência** informada na declaração.


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)