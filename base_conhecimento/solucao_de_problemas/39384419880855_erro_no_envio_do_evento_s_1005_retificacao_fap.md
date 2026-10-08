# Erro no envio do evento S-1005 - Retificação FAP

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39384419880855-Erro-no-envio-do-evento-S-1005-Retifica%C3%A7%C3%A3o-FAP](https://ajuda.sankhya.com.br/hc/pt-br/articles/39384419880855-Erro-no-envio-do-evento-S-1005-Retifica%C3%A7%C3%A3o-FAP)  
> **ID:** `39384419880855` | **Última Atualização:** 2026-07-29T13:23:34Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39384428480407)

 **Mensagem**

[1737] Campo Fap não pode ser preenchido

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39384428482327)

 **Situação**

Esta mensagem ocorre ao tentar enviar ou retificar o **"evento S-1005"** do eSocial para atualizar o **"Fator Acidentário de Prevenção (FAP)"** de estabelecimentos da empresa. O erro impede o processamento do evento, mesmo quando o usuário está tentando alterar o valor do **"FAP"** (por exemplo, de 0,5 para 1,0 ou de 1,31 para 1,06) ou realizar qualquer retificação relacionada ao **"FAP"** no eSocial.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39384428482839)

 **Solução**

Para corrigir o erro e enviar o **"evento S-1005"** com sucesso, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39384419876887)

 Acesse a tela **"Empresas"** (Configurações » Cadastros » Pessoal » Empresas). E selecione o estabelecimento (matriz ou filial) para o qual deseja enviar o **"evento S-1005"**.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39384419877143)

 Desmarque a opção **"Estabelecimento com FAP não publicada no eSocial" **e deixe o campo **"****Alíquota FAP"** vazio. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40797193321495)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39384428483863)

 Retorne à **"Central do eSocial"** (Pessoal+ >> Rotinas Folha >> Central do eSocial) e gere novamente o **"evento S-1005"**.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39384419878679)

 Antes de enviar o S-1005, verifique se a opção **"Utilizar Data Padrão do Sistema"** está desmarcada e informe a data de início de validade correta (por exemplo, 01/2026). 
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40797187026967)

 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39384428483991)

 Acesse a tela **"Registro Fiscal"** (Pessoal+ >> Cadastros >> Registro Fiscal) e verifique se a alíquota do **"FAP"** está corretamente cadastrada, pois é a partir dessa informação que o sistema vai gerar o Resumo de Folha. 

 

**Observações importantes:**

- 

A opção “Estabelecimento com FAP não publicada no eSocial” deve ser marcada quando a empresa ainda não possuir a informação da FAP disponibilizada no eSocial ou nos órgãos oficiais para o período vigente.

 

- O “Fator Acidentário de Prevenção (FAP)” somente poderá ser enviado pelo sistema quando a informação ainda não tiver sido disponibilizada no eSocial ou quando houver processo administrativo/judicial que justifique esse envio.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39384428484631)

 **Causa**

O erro ocorre porque a opção “Estabelecimento com FAP não publicada no eSocial” está habilitada no cadastro da empresa, porém a empresa já possui a informação da FAP disponibilizada no eSocial ou nos órgãos oficiais para o período vigente. Com isso, o envio do evento não é recepcionado pelo eSocial.