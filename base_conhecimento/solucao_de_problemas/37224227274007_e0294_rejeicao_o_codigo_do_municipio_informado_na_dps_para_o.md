# E0294 Rejeição: O código do município informado na DPS para o endereço do intermediário do serviço não existe conforme tabela de município do IBGE.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224227274007-E0294-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-intermedi%C3%A1rio-do-servi%C3%A7o-n%C3%A3o-existe-conforme-tabela-de-munic%C3%ADpio-do-IBGE](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224227274007-E0294-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-intermedi%C3%A1rio-do-servi%C3%A7o-n%C3%A3o-existe-conforme-tabela-de-munic%C3%ADpio-do-IBGE)  
> **ID:** `37224227274007` | **Última Atualização:** 2026-07-22T14:16:47Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260221463)

 **MENSAGEM**

E0294 Rejeição: O código do município informado na DPS para o endereço do intermediário do serviço não existe conforme tabela de município do IBGE.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260222103)

 **SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)** com intermediário do serviço informado, a nota é rejeitada durante a **validação dos dados relacionados ao endereço do intermediário**, especificamente no município informado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260222743)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260223639)

 Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260225815)

 Localize o parceiro intermediário vinculado á DPS rejeitada.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224227259031)

 Na aba **"Endereços"**, identifique o **"Cód.Cidade"** cadastrado para o intermediário.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260228247)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224227260055)

 Localize a cidade identificada no passo anterior.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260229143)

 Verifique o conteúdo do campo **"Mun. domicílio fiscal"** e valide se o código está correto.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37782708189719)

 Acesse o site oficial do ****[''IBGE''](https://cidades.ibge.gov.br/):

- 

No campo **"Pesquisar"**, digite o nome da cidade do intermediário

- 

Ao abrir as informações da cidade, localize o **"Código do Município"** oficial

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260229783)

 Retorne à tela "Cidades" (Configurações » Cadastros » Endereços » Cidades) e corrija o campo "Mun. domicílio fiscal" com o código obtido no site do IBGE.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260230551)

 Acesse novamente a tela "Parceiro" (Configurações » Cadastros » Parceiros) e redigite os dados do endereço para que o sistema atualize as informações.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260229783)

 Retorne à **DPS rejeitada**, redigite os dados do cabeçalho e gere um novo lote para transmissão.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260230551)

 Caso a rejeição persista, inutilize ou exclua a DPS e refaça o lançamento.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37782735985815)

 OBSERVAÇÃO:** Caso não consiga localizar o código do município no site do IBGE, solicite auxílio ao seu contador.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224260232855)

 **CAUSA**

A rejeição ocorre quando o **código do município (cMun)** do endereço do intermediário do serviço, informado na DPS, está **em branco, incorreto ou não corresponde** a um código válido na tabela oficial de municípios do IBGE. Isso impede que a Secretaria da Fazenda valide corretamente as informações fiscais do documento, resultando na rejeição E0294.


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)