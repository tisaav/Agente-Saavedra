# E0238 Rejeição: O código do município informado na DPS para o endereço do tomador do serviço não existe conforme tabela de município do IBGE.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222952999319-E0238-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-tomador-do-servi%C3%A7o-n%C3%A3o-existe-conforme-tabela-de-munic%C3%ADpio-do-IBGE](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222952999319-E0238-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-tomador-do-servi%C3%A7o-n%C3%A3o-existe-conforme-tabela-de-munic%C3%ADpio-do-IBGE)  
> **ID:** `37222952999319` | **Última Atualização:** 2026-07-22T14:17:13Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222952976151)

 **MENSAGEM**

E0238 Rejeição: O código do município informado na DPS para o endereço do tomador do serviço não existe conforme tabela de município do IBGE.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222937050519)

 **SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** ou **Declaração de Prestação de Serviços (DPS)**, o documento foi **rejeitado pela SEFAZ** com a mensagem informando que o **código do município do tomador do serviço** não corresponde a um código válido na **tabela oficial do IBGE**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222952977303)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222937053975)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **tomador do serviço** vinculado à nota rejeitada.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222937054359)

 Na aba **"Endereço"**, identifique o campo **"Cód.Cidade"** configurado para o parceiro.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222952981911)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e localize a cidade identificada no passo anterior.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222952982551)

 Na aba **"Geral"**, verifique o conteúdo do campo **"Mun. domicílio fiscal"**. Este campo deve conter o **código IBGE oficial do município**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222952984471)

 Acesse o site oficial do ****[''IBGE''](https://cidades.ibge.gov.br/):

- 

No campo **"Pesquisar"**, digite o nome da cidade do tomador;

- 

Ao abrir o conteúdo referente à cidade, localize a informação **"Código do Município"**;

- 

Copie o código correto fornecido pelo IBGE.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222937062935)

 Retorne à tela "Cidades" (Configurações » Cadastros » Endereços » Cidades) e corrija o campo **"Mun. domicílio fiscal"** com o **código IBGE correto** obtido no passo anterior.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222952988439)

 Acesse a ****["Central de Vendas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas), localize a nota rejeitada e **redigite os dados do cabeçalho** para atualizar as informações do parceiro.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222952989463)

 Gere um **novo lote** e reenvie o documento fiscal.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222952992279)

 Caso a rejeição persista, **inutilize ou exclua** a NFS-e rejeitada e refaça o lançamento do documento.
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37800675778967)

 OBSERVAÇÃO:** Caso não consiga localizar o código do município no site do IBGE, solicite essa informação ao seu **contador** ou ao **responsável fiscal** da empresa.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222937067159)

 **CAUSA**

A rejeição ocorre quando o **código do município do tomador do serviço** informado no cadastro está **em branco, incorreto ou divergente** em relação à **tabela oficial de municípios do IBGE**. O sistema utiliza o código configurado no campo **"Mun. domicílio fiscal"** do cadastro de cidades para preencher a tag **<cMun>** no XML da DPS. Se este código não for válido conforme o IBGE, a SEFAZ rejeita o documento com a mensagem E0238.


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)
- ["Central de Vendas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)