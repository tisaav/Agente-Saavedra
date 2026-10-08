# Conta: não pode ser alterado. Pois a carteira já se encontra homologada

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/38435339448215-Conta-n%C3%A3o-pode-ser-alterado-Pois-a-carteira-j%C3%A1-se-encontra-homologada](https://ajuda.sankhya.com.br/hc/pt-br/articles/38435339448215-Conta-n%C3%A3o-pode-ser-alterado-Pois-a-carteira-j%C3%A1-se-encontra-homologada)  
> **ID:** `38435339448215` | **Última Atualização:** 2026-07-22T14:01:34Z

---

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38435339438231)

**Mensagem**

Conta: não pode ser alterado. Pois a carteira já se encontra homologada.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39627875338391)

**Situação**

Ao tentar realizar o **"Credenciamento"** ou **"Recredenciamento"** de uma conta bancária na tela **"Contas"** (Financeiro >> Cadastros >> Contas), utilizando a funcionalidade **"Habilitar Boleto Rápido via API"**, o sistema apresenta a mensagem de erro informando que o identificador da carteira/convênio não pode ser atualizado enquanto a carteira estiver ativa ou homologada.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38435346809367)

**Solução**

Para resolver este erro, siga os passos abaixo:
**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38479698170391)

 **Revise cuidadosamente todos os dados informados na jornada de credenciamento, validando principalmente:

- Conta bancária;

- Agência;

- Convênio;

- Carteira/Variação.

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38479713023639)

 **Confirme as informações diretamente com o banco, garantindo que:

- Nenhum número esteja incorreto;

- O convênio esteja vinculado à conta correta;

- O beneficiário esteja exatamente como cadastrado na instituição bancária.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38479713024791)

 Caso seja realmente necessário alterar a conta ou qualquer dado estrutural da carteira, realize contato com o suporte para análise do cenário e orientações quanto aos procedimentos necessários.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/38435339440407)

**Causa**

O erro é apresentado quando a **carteira bancária já se encontra homologada junto à instituição bancária** e, em nova tentativa de credenciamento ou recredenciamento, há alteração de dado estrutural que não permite modificação após a homologação.

De forma geral, o erro acontece quando:

- 

É iniciada uma nova jornada de credenciamento;

- 

Há tentativa de alteração de informação já validada e homologada pela instituição bancária;

- 

O dado informado diverge do cadastro previamente homologado.

Como a carteira já passou pelo processo de validação junto à instituição bancária, o sistema não permite alterações em informações estruturais, tais como:

- 

Conta bancária;

- 

Agência;

- 

Convênio;

- 

Carteira/Variação.

Qualquer divergência em relação aos dados homologados resulta em rejeição automática da operação.