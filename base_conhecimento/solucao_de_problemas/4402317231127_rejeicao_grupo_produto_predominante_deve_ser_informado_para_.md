# Rejeição: Grupo produto predominante deve ser informado para modal rodoviário

> **Módulo:** Solucao de Problemas | **Subseção:** Distribuição  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4402317231127-Rejei%C3%A7%C3%A3o-Grupo-produto-predominante-deve-ser-informado-para-modal-rodovi%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/4402317231127-Rejei%C3%A7%C3%A3o-Grupo-produto-predominante-deve-ser-informado-para-modal-rodovi%C3%A1rio)  
> **ID:** `4402317231127` | **Última Atualização:** 2026-07-22T15:24:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16341895971863)

 MENSAGEM:**

Rejeição: Grupo produto predominante deve ser informado para modal rodoviário.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16341895973911)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16341895975191)

 Na Sub-aba **"Produto predominante" **(Tela **"Viagens de Transporte"**, aba **"MDF-e"**) informe:

- 

'Tipo de carga'

- 

'Descrição do produto principal'

- 

'NCM'

- 

'CEP' de carregamento

- 

CEP do descarregamento.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16341911221527)

 OBSERVAÇÃO:**

Caso tenha mais de um endereço de descarregamento, informe o último endereço.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15079941055127)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16341911222551)

CAUSA:**

Quando for emitido um MDF-e (modelo 58) com as seguintes informações:

- 

Modal (campo: modal) igual a '1' - Rodoviário;

- 

Tipo do Emitente (campo: tpEmit) igual a '1' - Prestador de serviço de transporte ou '3' - Prestador de serviço de transporte que emitirá CT-e Globalizado;

E não for informado o Grupo de Informações do Produto Predominante da Carga (**campo: prodPred**) será apresentada a rejeição.