# Como desbloquear o Sankhya ID e resolver o erro "GTW3500" "Erro na comunicação com o SankhyaId"?

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32260131739287-Como-desbloquear-o-Sankhya-ID-e-resolver-o-erro-GTW3500-Erro-na-comunica%C3%A7%C3%A3o-com-o-SankhyaId](https://ajuda.sankhya.com.br/hc/pt-br/articles/32260131739287-Como-desbloquear-o-Sankhya-ID-e-resolver-o-erro-GTW3500-Erro-na-comunica%C3%A7%C3%A3o-com-o-SankhyaId)  
> **ID:** `32260131739287` | **Última Atualização:** 2026-07-22T14:31:46Z

---

Este artigo tem como objetivo auxiliar na resolução do erro **“GTW3500 - Erro na comunicação com o SankhyaID”**, apresentado no endpoint **/login** do Gateway, cuja causa está relacionada ao bloqueio do Sankhya ID. Além disso, será demonstrado como realizar o desbloqueio

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349278696855)

**** ****MENSAGEM: **

```text
''error'': {
''codigo'': ''GTW3500'', 
''descricao'': ''Erro na comunicação com o SankhyaId.'' 
}
```

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32260148282903)

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349317765015)

 **SITUAÇÃO: **

O erro é exibido ao tentar realizar login na API do Gateway.

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349812184599)

 **Observação:** O login é realizado por meio de credenciais de e-mail vinculado ao Sankhya ID.

![mceclip300.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349781329431)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32260131732887)

**** ****SOLUÇÃO:**

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349812187543)

 **Acesse o **Sankhya Om** utilizando o Sankhya ID que se encontra bloqueado.

![mceclip4 (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/33349781332759)

 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349812190615)

 Esse acesso irá gerar automaticamente um e-mail com as instruções para o desbloqueio da conta.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32260148284695)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349781335063)

 Verifique sua caixa de entrada e siga as orientações enviadas no e-mail para realizar o desbloqueio da conta.

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349781335959)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349812196247)

 Após concluir o desbloqueio, realize uma nova tentativa de login na integração.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/40324042858263)

 

Após realizar os passos anteriores, a comunicação com o Gateway será restabelecida com sucesso. Em seguida, realize uma nova tentativa de login e o erro não deverá mais ocorrer.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33349781339287)

 **CAUSA: **

O erro ocorre quando o Sankhya ID utilizado na integração é bloqueado devido ao excesso de tentativas de login com senha incorreta. Após 3 tentativas inválidas, o Sankhya ID é bloqueado automaticamente, impedindo a geração do token necessário para autenticação no Gateway e ocasionando o erro apresentado.