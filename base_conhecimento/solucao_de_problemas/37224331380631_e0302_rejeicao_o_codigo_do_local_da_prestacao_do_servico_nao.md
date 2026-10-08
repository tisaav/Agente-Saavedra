# E0302 Rejeição: O código do local da prestação do serviço não existe conforme a tabela de municípios IBGE disponibilizada no ANEXO_A-MUNICIPIO_IBGE-PAISES_ISO2-SNNFSe.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224331380631-E0302-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-local-da-presta%C3%A7%C3%A3o-do-servi%C3%A7o-n%C3%A3o-existe-conforme-a-tabela-de-munic%C3%ADpios-IBGE-disponibilizada-no-ANEXO-A-MUNICIPIO-IBGE-PAISES-ISO2-SNNFSe](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224331380631-E0302-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-local-da-presta%C3%A7%C3%A3o-do-servi%C3%A7o-n%C3%A3o-existe-conforme-a-tabela-de-munic%C3%ADpios-IBGE-disponibilizada-no-ANEXO-A-MUNICIPIO-IBGE-PAISES-ISO2-SNNFSe)  
> **ID:** `37224331380631` | **Última Atualização:** 2026-07-22T14:16:44Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224315752983)

 **MENSAGEM**

E0302 Rejeição: O código do local da prestação do serviço não existe conforme a tabela de municípios IBGE disponibilizada no ANEXO_A-MUNICIPIO_IBGE-PAISES_ISO2-SNNFSe.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224331358999)

 **SITUAÇÃO**

Esta rejeição ocorre durante a **emissão de NFS-e** quando o sistema tenta transmitir a nota fiscal de serviço eletrônica para a prefeitura, mas o **código do município informado como local da prestação do serviço** não está de acordo com a tabela oficial de municípios do IBGE ou está preenchido incorretamente no cadastro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224315754647)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224331362199)

 Acesse a tela ****["Empresas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas) (Configurações » Cadastros » Empresas).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37779689175191)

 Localize a empresa emissora da NFS-e.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224315759127)

 Na aba **"Endereço"**, verifique qual **cidade** está cadastrada para a empresa.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224315760791)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224331371031)

 Localize a cidade identificada no passo anterior.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224315764631)

 Na aba **"Geral"**, verifique o conteúdo do campo **"Mun. domicílio fiscal"**.

- 

Este campo deve conter o **código oficial do município conforme a tabela do IBGE**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224331371031)

 Acesse o site oficial do ****[''IBGE''](https://cidades.ibge.gov.br/).

- 

No campo **"Pesquisar"**, digite o nome da cidade.

- 

Ao abrir o conteúdo referente ao município, localize a informação **"Código do Município"**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224315764631)

 Retorne à tela "Cidades" (Configurações » Cadastros » Endereços » Cidades) e corrija o campo **"Mun. domicílio fiscal"** com o código localizado no site do IBGE.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224331372567)

 Caso a nota já tenha sido gerada, realize o **cancelamento da NFS-e** rejeitada.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224315767191)

 Gere novamente a NFS-e com as informações corrigidas.
 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37779699913111)

 OBSERVAÇÃO:** Caso não consiga localizar o código do município no site do IBGE, solicite esta informação ao seu contador.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224315768215)

 **CAUSA**

Esta rejeição ocorre quando o **código do município informado no campo "Mun. domicílio fiscal"** do cadastro de cidades está **ausente, incorreto ou divergente** da tabela oficial de municípios do IBGE. A prefeitura valida este código durante a transmissão da NFS-e e, caso não esteja conforme o padrão estabelecido no ANEXO_A-MUNICIPIO_IBGE-PAISES_ISO2-SNNFSe, a nota é rejeitada.


---

### 🔗 Links e Referências Internas:

- ["Empresas"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas)
- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)