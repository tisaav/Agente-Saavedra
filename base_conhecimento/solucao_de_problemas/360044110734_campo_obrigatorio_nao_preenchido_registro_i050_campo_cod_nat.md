# Campo obrigatório não preenchido - Registro I050 - Campo COD NAT

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110734-Campo-obrigat%C3%B3rio-n%C3%A3o-preenchido-Registro-I050-Campo-COD-NAT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110734-Campo-obrigat%C3%B3rio-n%C3%A3o-preenchido-Registro-I050-Campo-COD-NAT)  
> **ID:** `360044110734` | **Última Atualização:** 2026-07-22T15:53:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16979737733271)

 MENSAGEM:**

Campo obrigatório não preenchido - Registro I050 - Campo COD NAT.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16979767503127)

 SITUAÇÃO:**

Ao validar o arquivo ECD o seguinte erro é apresentado do validador.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16979767506071)

SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16979737739543)

 Acesse: Contabilidade » Cadastros » Plano de Contas

Selecione as contas analíticas, conforme foi criticado na descrição do erro:

Exemplo: |**I050**|01012015| |A|7|**1.1.02.04.03.02.00001**|1.1.02.04.03.02|**(-) Amort Acum Licença Softwares/Sistema**

- Aba: **"Geral"**

- Campo **"Grupo de Conta"**: selecione conforme orientação do seu Contador

- Faça o ajuste para todas as contas, que apresentaram erro no relatório do PVA.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16979737740695)

 Acesse: Contabilidade » Conexão » ECD » Geração de Arquivo - ECD:

- Gere o arquivo novamente e faça uma nova validação.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16979767511575)

CAUSA:**

Ocorre quando as contas declaradas no arquivo ECD estão sem a informação do tipo de Conta, no cadastro de Plano de Contas.