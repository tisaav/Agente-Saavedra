# Cadastro de Alíquotas IBS/CBS - Registro Duplicado Após Atualização de Base

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39372610835223-Cadastro-de-Al%C3%ADquotas-IBS-CBS-Registro-Duplicado-Ap%C3%B3s-Atualiza%C3%A7%C3%A3o-de-Base](https://ajuda.sankhya.com.br/hc/pt-br/articles/39372610835223-Cadastro-de-Al%C3%ADquotas-IBS-CBS-Registro-Duplicado-Ap%C3%B3s-Atualiza%C3%A7%C3%A3o-de-Base)  
> **ID:** `39372610835223` | **Última Atualização:** 2026-08-13T17:46:44Z

---

Este artigo aborda a situação em que, após uma atualização de base de dados, o sistema pode apresentar **registros duplicados** no cadastro de alíquotas de **IBS** (Imposto sobre Bens e Serviços) e **CBS** (Contribuição sobre Bens e Serviços), impedindo a criação ou edição de novas alíquotas.

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39372610822551)

 **Causa**

Durante o processo de atualização de base ou migração de dados, podem ocorrer inconsistências que resultam em:

- 

Duplicação de registros de alíquotas com os mesmos parâmetros.
 

1. 

Mensagens de erro ao tentar cadastrar novas alíquotas.
 

1. 

Impedimento de edição de cadastros existentes.
 

1. 

Conflitos de chave única no banco de dados.
 

### **Identificação de Registros Duplicados**

Para identificar se há registros duplicados:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39372655888023)

 Acesse a tela **"Alíquotas de IBS"** (Livros Fiscais>Cadastros>Alíquotas de IBS) ou **"Alíquotas de CBS"** (Livros Fiscais>Cadastros>Alíquotas de CBS).
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39372610829591)

 Verifique se existem múltiplos registros com a mesma combinação de parâmetros: NCM ou NBS, Regime Tributário, CNAE, UF Destino, Município de Destino, Finalidade da Operação e Tipo de Operação.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39372655888407)

 Ao tentar cadastrar uma nova alíquota, observe se o sistema exibe a mensagem: **"****Já existe uma alíquota cadastrada com o ID xxx que possui as mesmas informações fornecidas**.**"**.
 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39372610830103)

 **Solução**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39372655888023)

 Identifique os IDs dos registros duplicados nas telas de cadastro de alíquotas.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39372610829591)

 Compare os registros duplicados e identifique qual deve ser mantido, preferencialmente o mais recente ou o que possui dados mais completos.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39372655888407)

 Exclua os registros duplicados, mantendo apenas um registro válido para cada combinação de parâmetros.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39372610830359)

 Após a exclusão, tente cadastrar ou editar novamente a alíquota desejada.
 

### **Campos Obrigatórios no Cadastro**

Na guia **"Tributação"**, quando a combinação de **"CST"** e **"Classificação Tributária"** tiver o indicador de tributação regular ativo, o grupo **"Tributação Regular"** deve ser preenchido com:

- 

**"CST"**
 

1. 

**"Classificação Tributária"**
 

1. 

**"Alíquota UF"**
 

1. 

**"Alíquota Município"**
 

Para **"Alíquotas de CBS"**, o grupo deve conter: **"CST"**, **"Classificação Tributária"** e **"Alíquota"**.

A duplicidade de registros pode afetar o cálculo automático dos tributos. Certifique-se de que apenas um registro válido exista para cada combinação de parâmetros, garantindo a correta aplicação das alíquotas nos documentos fiscais.