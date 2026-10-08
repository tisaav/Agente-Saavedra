# Erro evento S-1210 pensão alimentícia ("Erro 8 - Grupo 'Informação dos beneficiários da pensão alimentícia' deve ser preenchido.")

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43546495645207-Erro-evento-S-1210-pens%C3%A3o-aliment%C3%ADcia-Erro-8-Grupo-Informa%C3%A7%C3%A3o-dos-benefici%C3%A1rios-da-pens%C3%A3o-aliment%C3%ADcia-deve-ser-preenchido](https://ajuda.sankhya.com.br/hc/pt-br/articles/43546495645207-Erro-evento-S-1210-pens%C3%A3o-aliment%C3%ADcia-Erro-8-Grupo-Informa%C3%A7%C3%A3o-dos-benefici%C3%A1rios-da-pens%C3%A3o-aliment%C3%ADcia-deve-ser-preenchido)  
> **ID:** `43546495645207` | **Última Atualização:** 2026-09-17T13:29:43Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/43546504172311)

 **MENSAGEM**

"Erro 8" - Grupo 'Informação dos beneficiários da pensão alimentícia' deve ser preenchido.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/43546504172439)

 **SITUAÇÃO**

O erro ocorre ao tentar enviar o evento **"S-1210"** ao eSocial, quando há desconto de pensão alimentícia para um ou mais dependentes, mas as informações obrigatórias desses beneficiários não estão devidamente cadastradas ou vinculadas no sistema. Isso pode acontecer tanto em folhas normais quanto em folhas de décimo terceiro salário.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/43546495620503)

 **SOLUÇÃO**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/43546495621399)

 Acesse a tela **"Configuração Funcionários"** Pessoal+ » Cadastros » Configuração Funcionários e selecione o colaborador que possui desconto de pensão alimentícia.

 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/43546495622295)

 Na aba **"Dependentes"**, localize o dependente que recebe a pensão e clique para editar.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/43546504177047)

 Na sub-aba **"Dados da Pensão"**, preencha obrigatoriamente:

- 

Marque o dependente como **"Pensionista"**;
 

1. 

Informe o **"Parceiro responsável pelo recebimento da pensão"**;
 

1. 

Cadastre o(s) evento(s) de desconto de pensão utilizados na folha;
 

1. 

Se houver mais de um dependente pensionista, cadastre os eventos individualmente para cada um.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/43546495622807)

 Salve o cadastro do dependente.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/43546504178327)

 Acesse a tela **"Lançamento de Movimento"** (Pessoal+ Rotinas Folha Lançamento de Movimento) e confira se o evento de desconto de pensão está lançado corretamente para o dependente na referência desejada.
 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/43546495624855)

 Bloqueie e libere novamente a folha no **"Gerenciador de Folhas"** (Pessoal+ Rotinas Folha Gerenciador de Folhas).
 

![7](https://ajuda.sankhya.com.br/hc/article_attachments/43546495629719)

 Reenvie o evento **"S-1210"** pela **"Central do eSocial"** (Pessoal+ Rotinas Folha Central do eSocial).
 

 
 

Artigo relacionado: 

https://ajuda.sankhya.com.br/hc/pt-br/articles/33792842489623-Cadastro-de-Dependente-para-Pens%C3%A3o-Aliment%C3%ADcia
 

**Dicas importantes:**

- 

Sempre utilize a tela **"Configuração Funcionários"** para cadastrar e vincular informações de pensão, evitando lançamentos manuais apenas pela tela **"Lançamento de Movimento"**.
 

1. 

O preenchimento do **"Parceiro responsável pelo recebimento da pensão"** é obrigatório para o correto envio ao eSocial.
 

1. 

Certifique-se de que a sequência do dependente está correta no cadastro, lançamento e cálculo da folha.
 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/43546504185239)

 **CAUSA**

O erro ocorre porque o sistema identificou desconto de pensão alimentícia na folha, mas não encontrou todas as informações obrigatórias do grupo **"penAlim"** para o dependente: falta marcar o dependente como pensionista, informar o parceiro responsável, cadastrar o evento de desconto ou garantir que o dependente está corretamente vinculado e enviado ao eSocial. Sem esses dados, o evento **"S-1210"** não consegue montar o grupo de informações dos beneficiários da pensão alimentícia, gerando o erro 8.