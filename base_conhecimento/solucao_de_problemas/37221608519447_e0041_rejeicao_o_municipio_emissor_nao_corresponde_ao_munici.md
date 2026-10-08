# E0041 Rejeição: O município emissor não corresponde ao município do emitente MEI no CNPJ.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221608519447-E0041-Rejei%C3%A7%C3%A3o-O-munic%C3%ADpio-emissor-n%C3%A3o-corresponde-ao-munic%C3%ADpio-do-emitente-MEI-no-CNPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221608519447-E0041-Rejei%C3%A7%C3%A3o-O-munic%C3%ADpio-emissor-n%C3%A3o-corresponde-ao-munic%C3%ADpio-do-emitente-MEI-no-CNPJ)  
> **ID:** `37221608519447` | **Última Atualização:** 2026-07-22T14:18:32Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221608505623)

 **MENSAGEM**

E0041 Rejeição: O município emissor não corresponde ao município do emitente MEI no CNPJ.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221624484503)

 **SITUAÇÃO**

Esta rejeição ocorre quando uma **empresa cadastrada como MEI** (Microempreendedor Individual) tenta emitir uma NF-e e o **código do município informado no cadastro do emitente** no sistema **não corresponde ao município cadastrado** no CNPJ junto à Receita Federal. A SEFAZ valida se o município do emitente MEI está correto conforme os dados oficiais do CNPJ.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221608506903)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221624485271)

 Consulte o **cadastro oficial do CNPJ** da empresa emitente no site da ****[''Receita Federal''](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp) e identifique qual é o **município correto** cadastrado para o MEI.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221624485783)

 Acesse o site do ****[''IBGE''](https://cidades.ibge.gov.br/)** **e realize os seguintes procedimentos: 

- 

No campo **"Pesquisar"**, digite o nome do município identificado no passo anterior;

- 

Ao abrir as informações da cidade, localize o **"Código do Município"** e anote-o.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37855140412311)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e localize o município emitente.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221624486807)

 Na aba **"Geral"**, no campo **"Mun. Domicílio Fiscal"**, corrija informando o código do município obtido no site do IBGE, conforme o passo 2.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221608509975)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o cadastro da empresa emitente.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221624487703)

 Na aba **"Endereços"**, verifique se o **"Cód. Cidade"** está correto e corresponde ao município cadastrado na Receita Federal.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221624488215)

 Caso necessário, ajuste o **"Cód. Cidade"** para o município correto.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221608511255)

 Retorne à NF-e rejeitada, **redigite qualquer informação do cabeçalho** para que o sistema recalcule os dados e **gere um novo lote** para envio à SEFAZ.
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37855140413591)

 OBSERVAÇÃO:** Caso não consiga localizar o código do município no site do IBGE ou persistam dúvidas sobre o cadastro correto, solicite auxílio ao **contador da empresa**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221608512791)

 **CAUSA**

Esta rejeição é apresentada quando o **código do município informado no cadastro do emitente MEI** no sistema **diverge do município cadastrado no CNPJ** junto à Receita Federal. A SEFAZ realiza a validação cruzada entre os dados do emitente e o cadastro oficial do CNPJ, e ao identificar a **inconsistência no município**, a nota fiscal eletrônica é rejeitada para garantir a conformidade fiscal.


---

### 🔗 Links e Referências Internas:

- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)