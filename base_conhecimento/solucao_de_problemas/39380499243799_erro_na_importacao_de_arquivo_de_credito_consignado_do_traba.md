# Erro na importação de arquivo de crédito consignado do trabalhador

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39380499243799-Erro-na-importa%C3%A7%C3%A3o-de-arquivo-de-cr%C3%A9dito-consignado-do-trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/39380499243799-Erro-na-importa%C3%A7%C3%A3o-de-arquivo-de-cr%C3%A9dito-consignado-do-trabalhador)  
> **ID:** `39380499243799` | **Última Atualização:** 2026-08-19T14:30:15Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39380485640983)

 **MENSAGEM**

Durante a importação do arquivo de crédito consignado do trabalhador, podem ocorrer diferentes mensagens de erro:

- 

**java.lang.StackOverflowError**

- 

É necessário o envio com sucesso do evento **"S-2206"** do cadastro ativo deste funcionário para realizar o lançamento

- 

Não há funcionário cadastrado com o CPF, matrícula e data admissão informados

- 

O **"Número do Contrato"** relacionado ao crédito do trabalhador não está informado, impedindo o cálculo

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641239)

 **SITUAÇÃO**

Os erros ocorrem ao tentar importar o arquivo de crédito consignado do trabalhador na tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento), na aba **"Funcionários"**. O problema pode afetar um ou mais funcionários, mesmo aqueles que tiveram importações bem-sucedidas em meses anteriores.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641367)

 **SOLUÇÃO**

A solução varia conforme o tipo de erro apresentado:

**Para erro java.lang.StackOverflowError ou problemas com datas de transferência:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39380499242519)

 Acesse o cadastro do funcionário e verifique as **"Datas de Transferência"** entre empresas.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641623)

 Identifique se há duplicidade de datas, onde a data de transferência de origem e destino estão iguais.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641751)

 Mantenha a data de transferência do funcionário na empresa de destino.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39380499242775)

 Na empresa de origem, ajuste a data para um dia anterior à admissão na nova empresa.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39380499243031)

 Realize novamente a importação do arquivo.
 

**Para erro relacionado ao evento S-2206:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39380499242519)

 Verifique se existe envio do evento **"S-2206"** no sistema para o funcionário em questão. Em caso de transferência essa informação já é preenchida no momento dessa transferência. 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641623)

 Caso não exista, realize o envio dos eventos **"S-2205"** e/ou **"S-2206"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641751)

 Importe novamente a planilha de crédito consignado.
 

**Para erro de divergência de dados cadastrais (CPF, matrícula ou data de admissão):**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39380499242519)

 Abra a planilha de importação e verifique os dados do funcionário que apresentou erro.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641623)

 Compare o **"CPF"**, **"Matrícula"** e **"Data de Admissão"** da planilha com os dados cadastrados no sistema.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641751)

 Acesse o portal do eSocial para confirmar qual informação está correta.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39380499242775)

 Corrija manualmente na planilha os dados divergentes, especialmente a **"Data de Admissão"**.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39380499243031)

 Realize novamente a importação.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39380499243415)

 Se a divergência estiver no sistema Emprega Brasil, abra um chamado com eles para correção das informações.
 

**Para erro relacionado ao número do contrato:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39380499242519)

 Acesse a tela **"Lançamento de Movimento"** (PPessoal+ » Rotinas Folha » Lançamento de Movimento).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641623)

 Localize os funcionários com crédito consignado e verifique se o **"Número do Contrato"** está preenchido corretamente.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641751)

 Realize o reprocessamento na tela conforme orientações da Central de Ajuda.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40921258941079)

 

**Para erro relacionado à planilha incorreta:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39380499242519)

 Verifique se a planilha utilizada é a correta e está atualizada.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641623)

 Baixe novamente o arquivo do portal Emprega Brasil ou eConsignado.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39380485641751)

 Realize a importação com o arquivo correto.
 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39380485645847)

 **CAUSA**

Os erros na importação do arquivo de crédito consignado podem ocorrer por diferentes motivos:

- 

**Datas de transferência duplicadas ou incorretas** no cadastro do funcionário, causando conflito no processamento.

- 

**Ausência de eventos S-2206 finalizados** no sistema, especialmente para funcionários transferidos entre empresas.

- 

**Divergência de dados cadastrais** entre a planilha de importação e o cadastro do sistema (CPF, matrícula ou data de admissão).

- 

**Número do contrato não informado** no lançamento de movimento do funcionário.

- 

**Utilização de planilha incorreta ou desatualizada** para importação.