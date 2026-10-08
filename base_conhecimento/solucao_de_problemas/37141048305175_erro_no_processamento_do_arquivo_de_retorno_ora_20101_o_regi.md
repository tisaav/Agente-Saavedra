# Erro no processamento do arquivo de retorno: ORA-20101: O registro de "Tipo de Operação" (TGFTOP) selecionado não esta cadastrado, ou não esta ativo, ou não é analítico.

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37141048305175-Erro-no-processamento-do-arquivo-de-retorno-ORA-20101-O-registro-de-Tipo-de-Opera%C3%A7%C3%A3o-TGFTOP-selecionado-n%C3%A3o-esta-cadastrado-ou-n%C3%A3o-esta-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico](https://ajuda.sankhya.com.br/hc/pt-br/articles/37141048305175-Erro-no-processamento-do-arquivo-de-retorno-ORA-20101-O-registro-de-Tipo-de-Opera%C3%A7%C3%A3o-TGFTOP-selecionado-n%C3%A3o-esta-cadastrado-ou-n%C3%A3o-esta-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico)  
> **ID:** `37141048305175` | **Última Atualização:** 2026-07-22T14:19:38Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141048301591)

 **MENSAGEM:**

ERRO NA BAIXA: NUFIN= XXX, V.TITULO= XXXX, V.RECEBIDO= XXXX. ORA-20101: O registro de "Tipo de Operação" (TGFTOP) selecionado não esta cadastrado, ou não esta ativo, ou não é analítico.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141048301719)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37276647902871)

 Acesse a tela ****[''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141049317399)

 Verifique os parâmetros responsáveis pela definição da **TOP** utilizada na baixa automática durante o processamento do arquivo de retorno bancário, e ajuste conforme o tipo de título:

**Para títulos de receita (recebimentos)**:

- 

**TOPBAIXA – TOP para baixa de recebimentos: **Informe um código de Tipo de Operação válido e ativo, que será utilizado na baixa automática de recebimentos no processamento do retorno bancário.

**Para títulos de despesa (pagamentos):**

- 

**TOPBAIXAPAG – TOP para baixa de pagamentos: **Informe um código de Tipo de Operação válido e ativo, que será utilizado na baixa automática de pagamentos no processamento do retorno bancário.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37276647903767)

 Após os ajustes, processe novamente o arquivo de retorno bancário para validar a baixa correta dos títulos.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37141049318423)

CAUSA:**

O erro ocorre durante o processamento do arquivo de retorno bancário porque o sistema utiliza a **TOP** definida nos parâmetros para realizar a baixa automática dos títulos financeiros. O problema acontece quando a TOP não está cadastrada nos parâmetros ou está inativa. Nesses casos, o sistema não consegue concluir a baixa do título e retorna a mensagem de erro.


---

### 🔗 Links e Referências Internas:

- [''Preferências''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)