# E0101 - Elemento obrigatório vazio ao enviar S-2205

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39351489748119-E0101-Elemento-obrigat%C3%B3rio-vazio-ao-enviar-S-2205](https://ajuda.sankhya.com.br/hc/pt-br/articles/39351489748119-E0101-Elemento-obrigat%C3%B3rio-vazio-ao-enviar-S-2205)  
> **ID:** `39351489748119` | **Última Atualização:** 2026-09-26T00:42:54Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39351467032983)

 **Mensagem**

E0101 - Elemento obrigatório vazio. Reveja o manual ou a documentação do sistema [eSocial/evtAltCadastral/alteracao/dadosTrabalhador/trablmig/condIng]

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39351489738519)

 **Situação**

Ao tentar enviar o evento **"S-2205"** (Alteração de Dados Cadastrais) para o eSocial, o sistema retorna a mensagem de erro informando que um elemento obrigatório está vazio. Esta situação ocorre especificamente quando o funcionário é estrangeiro e há informações cadastrais incompletas relacionadas ao trabalhador imigrante.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39351467034007)

 **Solução**

Para corrigir o erro e enviar o evento com sucesso, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39351467034391)

 Acesse o **"Cadastro do Funcionário"** (Pessoal+ » Cadastros » Configuração Funcionários) e localize o colaborador estrangeiro que apresenta o erro.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39351489739927)

 Localize a seção de **"Dados do Trabalhador Imigrante"** no cadastro do funcionário.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41397659291159)

 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39351489740311)

 Preencha obrigatoriamente os seguintes campos:

• **"Tempo de Residência do Trabalhador Imigrante"**
• **"Condição de Ingresso do Trabalhador Imigrante"**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41397637101335)

 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39351467036311)

 Salve as alterações realizadas no cadastro do funcionário.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39351489744151)

 Acesse novamente a tela **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e gere novamente o **"S-2205"** para o funcionário.
 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39351489744791)

 Envie o evento ao eSocial. Com as informações corrigidas, o envio será processado com sucesso, sem apresentação de erros.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39351489745687)

 **Causa**

O erro ocorre porque o eSocial exige informações específicas para trabalhadores estrangeiros. Quando o funcionário possui nacionalidade diferente da brasileira, os campos **"Tempo de Residência do Trabalhador Imigrante"** e **"Condição de Ingresso do Trabalhador Imigrante"** tornam-se obrigatórios para o envio do **"S-2205"**. A ausência dessas informações no cadastro impede a validação do evento pelo sistema do eSocial, resultando na mensagem de erro E0101.