# E0268 Rejeição: CPF do intermediário não encontrado no cadastro CPF.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37223138553111-E0268-Rejei%C3%A7%C3%A3o-CPF-do-intermedi%C3%A1rio-n%C3%A3o-encontrado-no-cadastro-CPF](https://ajuda.sankhya.com.br/hc/pt-br/articles/37223138553111-E0268-Rejei%C3%A7%C3%A3o-CPF-do-intermedi%C3%A1rio-n%C3%A3o-encontrado-no-cadastro-CPF)  
> **ID:** `37223138553111` | **Última Atualização:** 2026-07-22T14:17:01Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223154750103)

 **MENSAGEM**

E0268 Rejeição: CPF do intermediário não encontrado no cadastro CPF.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223138543511)

 **SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** com informações de intermediador da operação, o **CPF do intermediário** informado no documento fiscal **não foi encontrado** na base de dados da Receita Federal. A rejeição ocorre no momento da transmissão do documento fiscal eletrônico.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223138544663)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223138545815)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223154755223)

 Localize o cadastro do **intermediador** da operação.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223138548119)

 Na aba **''Identificação''**, verifique se o **CPF informado** no campo **"CPF/CNPJ"** está correto e **devidamente cadastrado** na Receita Federal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223138548887)

 Caso o CPF esteja incorreto, corrija a informação no cadastro do parceiro com o **número válido** do CPF do intermediador.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223138550167)

 Se o CPF estiver correto, mas ainda assim ocorrer a rejeição, verifique se o **CPF está ativo** e regularizado junto à Receita Federal através do site oficial.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37797974699799)

 Após realizar as correções necessárias no cadastro do intermediador, **reemita a NF-e ou NFC-e** para que o documento seja transmitido corretamente. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37223154759319)

 **CAUSA**

A rejeição é retornada pela **SEFAZ** quando o **CPF do intermediário** informado no documento fiscal eletrônico **não existe** ou **está inválido** na base de dados da Receita Federal. Isso pode ocorrer devido a **erro de digitação** no cadastro do parceiro, CPF **cancelado** ou **suspenso**, ou ainda por se tratar de um **número inexistente**.