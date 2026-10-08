# Conta Bancária não existe ou está inativo ou não pode ser usado aqui

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34278687617815-Conta-Banc%C3%A1ria-n%C3%A3o-existe-ou-est%C3%A1-inativo-ou-n%C3%A3o-pode-ser-usado-aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/34278687617815-Conta-Banc%C3%A1ria-n%C3%A3o-existe-ou-est%C3%A1-inativo-ou-n%C3%A3o-pode-ser-usado-aqui)  
> **ID:** `34278687617815` | **Última Atualização:** 2026-07-22T14:27:22Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34278687605911)

 **MENSAGEM**

[CORE_E01315] Conta bancária não existe ou está inativa ou não pode ser usada aqui.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34278722141079)

 **SOLUÇÃO**

Antes de utilizar uma conta bancária, é necessário realizar algumas validações importantes para garantir que a conta esteja ativa, disponível para uso e corretamente configurada no sistema.:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34278687608343)

  Acesse a tela **"Contas"** (Configurações » Cadastros » Bancários » Contas).

    **O que verificar:**

- 

Campo **"Ativa"**: certifique-se de que a conta está marcada como ativa.

- 

Campo **"Exclusiva da Empresa"**: verifique se está marcada como exclusiva e, se necessário, ajuste conforme o contexto de uso.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34278722141463)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34278722141975)

  Acesse a tela **"Central de Certificações"** (Comercial » Avançado » Certificações » Central de Certificações).

    **O que verificar:**

- 

Se existe alguma **limitação de uso** da conta.

- 

Caso haja limitação, verifique se a regra está **vinculada ao usuário** que está tentando utilizar a conta.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34278687609495)

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34278687610263)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34430586325271)

  Durante o processo de baixa, observe a **sequência prioritária** para sugestão de conta bancária pelo sistema:
 

- 

**Conta informada na aba "Contas p/ Baixa"** no cadastro do usuário.

- 

**Conta definida no parâmetro** **CONTAPADRAO** ("Número da conta padrão na baixa").

- 

**Conta bancária informada no título** na movimentação financeira.

- 

**Conta marcada como "Exclusiva da Empresa"** no cadastro de contas bancárias.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34278687611287)

 **CAUSA**

A mensagem ocorre quando a conta bancária utilizada está inativa, não cadastrada ou possui restrições que impedem seu uso no processo.