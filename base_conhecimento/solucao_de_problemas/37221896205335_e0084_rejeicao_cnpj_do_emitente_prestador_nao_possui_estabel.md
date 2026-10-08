# E0084 Rejeição: CNPJ do emitente prestador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37221896205335-E0084-Rejei%C3%A7%C3%A3o-CNPJ-do-emitente-prestador-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CNPJ-e-CNC-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/37221896205335-E0084-Rejei%C3%A7%C3%A3o-CNPJ-do-emitente-prestador-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CNPJ-e-CNC-NFS-e)  
> **ID:** `37221896205335` | **Última Atualização:** 2026-07-22T14:18:15Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221896189847)

 **MENSAGEM**

E0084 Rejeição: CNPJ do emitente prestador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221896192023)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)**, o sistema rejeitou o documento informando que o **CNPJ do emitente prestador** não possui estabelecimento ou domicílio fiscal cadastrado no município que está sendo informado como **município emissor** na DPS (Declaração de Prestação de Serviços). Esta divergência é identificada pela SEFAZ ao confrontar os dados do **cadastro CNPJ** e do **CNC NFS-e (Cadastro Nacional de Contribuintes de NFS-e)** com as informações declaradas no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221943699095)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221943699607)

 Consulte o **cadastro oficial do CNPJ** da empresa emitente no site da **Receita Federal** ou no **SINTEGRA** para verificar qual é o **município de domicílio fiscal** cadastrado oficialmente para o estabelecimento.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221896194711)

 Acesse o site do ****[''IBGE''](https://cidades.ibge.gov.br/) e pesquise o **Código do Município** correspondente ao município identificado no cadastro oficial:

- 

Digite o nome da cidade no campo de pesquisa;

- 

Localize a informação **"Código do Município"** na página de detalhes da cidade.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37835263899799)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o cadastro da **empresa emitente**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221943703063)

 Na aba **"Endereço"**, verifique o campo **"Cód. Cidade"** e certifique-se de que está preenchido corretamente com o código do município onde a empresa possui domicílio fiscal.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221896199319)

 Acesse a tela **"Cidades"** (Configurações » Cadastros » Endereços » Cidades) e localize a cidade vinculada ao cadastro da empresa.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221896199703)

 Na aba **“Geral”**, verifique o campo **“Mun. Domicílio Fiscal”** e, se necessário, atualize-o com o **código do município** obtido no site do **IBGE**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221943707543)

 Confira também se o campo **“Cód. UF”** está corretamente preenchido e corresponde ao **estado do município informado**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221943707927)

 Após realizar os ajustes, **redigite os dados do cabeçalho da NFS-e** para carregar as informações atualizadas e **gere um novo lote para transmissão**.

![9 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221896201239)

 Caso a rejeição persista, **inutilize ou exclua a NFS-e rejeitada** e **refaça o lançamento do documento fiscal** com os dados corrigidos.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37835268526743)

 OBSERVAÇÃO:**

Além das validações cadastrais, verifique se o prestador de serviços possui **liberação ativa junto à prefeitura do município ou no Portal Nacional da NFS-e** para emissão de notas fiscais.

Em alguns casos, mesmo com os dados de município e domicílio fiscal corretamente configurados, a emissão da NFS-e pode ser bloqueada por **ausência de autorização/liberação do prestador**, sendo necessária uma **solicitação formal de liberação junto à prefeitura responsável**.

Caso não seja possível confirmar as informações corretas nos cadastros oficiais ou no site do IBGE, **solicite auxílio ao contador da empresa** para realizar as devidas verificações junto à SEFAZ e à Receita Federal.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37221896201751)

 **CAUSA**

A rejeição ocorre quando o **Código do Município (cMun)** informado como **município emissor** na DPS não corresponde ao município onde o **CNPJ do emitente prestador** possui estabelecimento ou domicílio fiscal cadastrado oficialmente.

A SEFAZ realiza a validação cruzando as informações da **data de competência** informada na DPS com os dados constantes no **cadastro CNPJ da Receita Federal** e no **CNC NFS-e**. Quando há divergência entre o município declarado no documento fiscal e o município cadastrado oficialmente para o estabelecimento, o sistema rejeita a NFS-e para garantir a conformidade fiscal e a correta arrecadação tributária municipal.