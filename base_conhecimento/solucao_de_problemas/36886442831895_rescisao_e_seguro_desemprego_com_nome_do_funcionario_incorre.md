# Rescisão e Seguro-Desemprego com nome do funcionário incorreto

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36886442831895-Rescis%C3%A3o-e-Seguro-Desemprego-com-nome-do-funcion%C3%A1rio-incorreto](https://ajuda.sankhya.com.br/hc/pt-br/articles/36886442831895-Rescis%C3%A3o-e-Seguro-Desemprego-com-nome-do-funcion%C3%A1rio-incorreto)  
> **ID:** `36886442831895` | **Última Atualização:** 2026-07-29T13:22:03Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41054984684183)

 SITUAÇÃO

Ao emitir o Recibo de Rescisão e gerar o arquivo do Seguro-Desemprego, o nome do colaborador pode ser apresentado de forma incorreta, utilizando o **Nome Social** em vez do **Nome Civil** cadastrado.
 

**Exemplo:**

**Termo de rescisão com nome incompleto**

![image (87) (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909974717719)

**Arquivo Seguro Desemprego**

![image (88).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909975960471)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/36886442810391)

 MENSAGEM

O arquivo do Seguro-Desemprego é gerado por meio da tela **Gerenciador de Folhas** (**Pessoal+ > Rotinas Folha > Gerenciador de Folhas**).

Para realizar a geração:

1. Selecione a rescisão desejada;

1. Clique no botão **"Gerar arquivo para Seguro-Desemprego"**.

Após a execução da rotina, o sistema gerará automaticamente um arquivo no formato **TXT**, contendo as informações necessárias para importação e processamento do requerimento do Seguro-Desemprego.
 

![image (89).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909975965463)

![image (88).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909975960471)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41054991871511)

 SOLUÇÃO

Para corrigir a exibição do nome incompleto nos documentos, siga os passos abaixo:
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41054991872151)

 Acesse a tela **Configuração Funcionários** (**Pessoal+ > Cadastros > Configuração Funcionários**) e localize o colaborador desejado.

Analise qual nome está sendo apresentado nos documentos e compare com os campos **Nome** e **Nome Social** cadastrados no sistema.

![image (90).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909974726807)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41055553476247)

 

Caso o funcionário possua **Nome Social** cadastrado na Receita Federal (RFB), a opção **"Travesti ou Transexual?"** deverá estar marcada e o campo **"Nome Social"** deverá ser preenchido exatamente conforme registrado na RFB.

*Quando essa configuração estiver habilitada, o sistema passará a utilizar o nome social na emissão dos relatórios de **Rescisão** e **Seguro-Desemprego**.*
 

![image (91).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909975967895)

 

**Se o funcionário não possua Nome Social registrado na Receita Federal ou o campo tenha sido preenchido indevidamente:**

- O campo **"Nome Social"** não deve estar preenchido;

- A opção **"Travesti ou Transexual?"** deve ser desmarcada.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41054991872791)

 Ao desmarcar o campo **"Travesti ou Transexual"**, o sistema desabilita o campo **"Nome Social"** e os relatórios passarão a ser emitidos conforme o campo **"Nome"** civil no cadastro do funcionário.

![image (90).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909974726807)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41054984689687)

 Salve as alterações e gere novamente o documento para validação.
 

**Exemplo pós-correção:**
 

**Termo de Rescisão**

![image (93).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909975972759)

 

**Arquivo Seguro Desemprego**

![image (94).png](https://ajuda.sankhya.com.br/hc/article_attachments/36909974736279)