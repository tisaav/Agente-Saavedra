# Ajuste do Sistema para Notas Denegadas conforme a NT 2024.001

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35307289249559-Ajuste-do-Sistema-para-Notas-Denegadas-conforme-a-NT-2024-001](https://ajuda.sankhya.com.br/hc/pt-br/articles/35307289249559-Ajuste-do-Sistema-para-Notas-Denegadas-conforme-a-NT-2024-001)  
> **ID:** `35307289249559` | **Última Atualização:** 2026-08-04T17:44:05Z

---

Recentemente a SEFAZ alterou o tratamento de notas denegadas. Com essa mudança, **o sistema não deverá mais gerar NF-e com status de denegadas **nessas situações, pois esse retorno passou a ser subistituido pela **Rejeição 307 - Emitente bloqueado pela UF de destino**, que não cria nota nem consome numeração.

Este help orienta como remover configurações antigas relacionadas ao tratamento de notas denegadas, atualizar a base para a Nota Técnica e corrigir registros que ainda tenham sido marcado como denegados.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331317271)

 SOLUÇÃO:**

#### **Tipo de Operação - TOP**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331318679)

 Para desfazer a configuração acesse a tela ****[''Tipo de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331319831)

 Na aba **''NF-e/NFC-e/CF-e''**, localize as TOPs configuradas como **''Denegada''.**

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331320727)

 **Remova as notas para os tipos de emissão:** Própria, Venda, Compra e Devolução**.

 

![image (61).png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331321751)

 

#### **Preferências**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331318679)

 Acesse a tela ****[''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331319831)

 No campo **''Chave ou descrição''** pesquise por **''Denegada'' **e/ou** ''**`**TOPNFEDENEG**`**''**. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331320727)

 Verifique o campo **''Chave''** e certifique-se de que o campo esteja vazio, sem TOP cadastrada. 

 

![Imagem](/attachments/token/keji2mhshpkMdd77HuXXvw0I1/?name=image.png)

 

#### **Atualização da Nota Técnica (NT)**

Para evitar que o sistema continue rejeitando notas como denegadas, é necessário atualizar para a **NT 2024.001 **ou **versões mais recentes disponibilizadas em 2025**.

**Benefícios da atualização:**

- 

Substitui o tratamento de notas denegadas pela **Rejeição 307 – Emitente bloqueado pela UF de destino**.

- 

Corrige exceções da regra N12-20.

- 

Inclui o CFOP 5910 na NFCe (RV 108-150).

Após a atualização, situações que anteriormente resultavam em nota denegada passarão a gerar a **Rejeição 307, **sem criação de nota e sem consumo de numeração. Isso elimina a necessidade de manter notas marcadas como denegadas em sistema.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331318679)

 Acesse a tela **''Empresa'' **(Comercial » Preferências » Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331319831)

 Em **''Configuração''** (ícone da engranagem), no ícone de **''+''**, crie uma nova aba com o nome de **''Documentos Fiscais Eletrônicos''.**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331320727)

 Inclua nesta aba os campos relacionados aos documentos fiscais.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331322519)

 Em, seguida ative a ''**NT 2024.001''** e demais NTs essenciais para garantir que o sistema acompanhe as últimas regras da SEFAZ.

 

![image (62).png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331323671)

 

![image (63).png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331324695)

 

![image (64).png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331325591)

 

#### **Correção de notas já denegadas**

##### Notas que já foram registradas como denegadas antes da atualização precisam ser ajustadas diretamente no banco de dados, pois o novo tratamento de SEFAZ não utiliza mais esse status.

 

**Procedimento:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331318679)

 Altere o status da nota para **“Aguardando Correção”**, permitindo que ela volte ao fluxo normal de tratamento.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331319831)

 Verifique no sistema a situação atual da nota, garantindo que ela tenha retornado ao status adequado.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36639331320727)

 Em seguida, ajuste os campos necessários no banco de dados, observando:

- 

`NUNOTA` → número da nota que será corrigida

- 

`CODEMP` → código da empresa

- 

`STATUSNFE` → novo status da nota

A alteração desses campos deve ser realizado **exclusivamente por um DBA**, garantindo a integridade da base e aplicando os ajustes apenas para a nota e empresa desejadas.

 

#### **Resumo**

1. 

Remova as TOPs denegadas configuradas nas TOPs de emissão.

1. 

Limpe o campo ''`TOPNFEDENEG`'' nas ''Preferências''.

1. 

Atualize o sistema para a **NT 2024.001** ou versão superior.

1. 

Crie a aba de ''Documentos Fiscais Eletrônicos'' e ative as NTs necessárias.

1. 

Corrija notas já denegadas diretamente no banco de dados (somente por DBA).

1. 

Após a mudança, notas que antes ficariam denegadas passarão a apresentar a **Rejeição 307**.


---

### 🔗 Links e Referências Internas:

- [''Tipo de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)