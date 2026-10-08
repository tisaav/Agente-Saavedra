# Tipo de Operação não existe ou está inativo ou não pode ser usado aqui.

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39357340584087-Tipo-de-Opera%C3%A7%C3%A3o-n%C3%A3o-existe-ou-est%C3%A1-inativo-ou-n%C3%A3o-pode-ser-usado-aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/39357340584087-Tipo-de-Opera%C3%A7%C3%A3o-n%C3%A3o-existe-ou-est%C3%A1-inativo-ou-n%C3%A3o-pode-ser-usado-aqui)  
> **ID:** `39357340584087` | **Última Atualização:** 2026-08-11T01:54:19Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39357340580247)

 MENSAGEM**

Tipo de Operação não existe ou está inativo ou não pode ser usado aqui. CORE_E01315

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42624523528855)

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39357381032471)

 SITUAÇÃO**

Esta mensagem aparece ao tentar **"Faturar um pedido"** no sistema, especialmente quando o usuário está realizando um **"Faturamento de pedido para pedido"**, ou ao tentar processar uma operação com um **Tipo de Operação **que não está configurado adequadamente para o fluxo desejado.

 

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39357381032599)

 SOLUÇÃO**

Para resolver este erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39357381033751)

 Acesse a tela **"Tipos de Operação"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) e localize o **"TOP"** de origem que está sendo utilizado no faturamento.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39357340582423)

 Clique na aba **"Restrições e Exceções"** dentro do cadastro do **"TOP"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39357381034135)

 Configure uma Restrição informando que esta **"TOP"** pode ser usado com o **"TOP"** de destino desejado.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39357340582807)

 Verifique se o **"Tipo de movimento"** da **"TOP"** está configurado corretamente para o fluxo que está sendo executado (exemplo: Pedido para Pedido, Pedido para Nota, etc.).

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39357340582935)

 Salve as alterações e tente realizar o faturamento novamente.
 

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39357340583063)

 CAUSA**

O erro ocorre porque o fluxo padrão do sistema é de pedido para nota. Quando o usuário tenta realizar um faturamento diferente deste fluxo padrão, como pedido para pedido, é necessário criar uma exceção na configuração do **"TOP"**, informando explicitamente que aquele tipo de operação pode ser usado com o **"TOP"** de destino específico.

Além disso, o erro pode estar relacionado a:

- 

**"TOP"** inativo ou não cadastrado no sistema.

- 

**"Tipo de movimento"** incompatível com a operação que está sendo realizada.

- 

Falta de configuração nas restrições e exceções do **"TOP"**.

- 

Problemas de cache no navegador que impedem o carregamento correto dos controladores do sistema.