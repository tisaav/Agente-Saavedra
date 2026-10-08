# Erro COM_E00560: Não é possível usar variáveis nos filtros na Ficha de Parceiros (Giro Negociações)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39359330507287-Erro-COM-E00560-N%C3%A3o-%C3%A9-poss%C3%ADvel-usar-vari%C3%A1veis-nos-filtros-na-Ficha-de-Parceiros-Giro-Negocia%C3%A7%C3%B5es](https://ajuda.sankhya.com.br/hc/pt-br/articles/39359330507287-Erro-COM-E00560-N%C3%A3o-%C3%A9-poss%C3%ADvel-usar-vari%C3%A1veis-nos-filtros-na-Ficha-de-Parceiros-Giro-Negocia%C3%A7%C3%B5es)  
> **ID:** `39359330507287` | **Última Atualização:** 2026-08-31T02:48:46Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39359332626967)

 **Mensagem**

**[COM_E00560] Não é possível usar variáveis nos filtros**

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39359330497303)

 **Situação**

Este erro pode ocorrer quando o usuário tenta criar um filtro dentro da ficha de parceiros (Giro de Negociações), onde está configurado para usar variáveis. 

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39359332628503)

 **Solução**

Para resolver este erro, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43114726007063)

 Acesse **Ficha de Parceiros**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43114726007319)

 No painel **Giro de Negociações**, role até o final e abra o **Filtro Personalizado**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43114709387159)

 Abra o **Assistente de Filtros** e localize o filtro marcado como ativo.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43114709387799)

 Se a expressão contiver um `?`, remova esse parâmetro:

- Substitua por um valor fixo, ou

- 
*(se aplicável)* use a opção específica de "usuário logado" do assistente, em vez de digitar o parâmetro manualmente.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39359330501527)

 Salve o filtro novamente e teste o Giro de Negociações.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39359332633367)

 **Causa**

O Filtro Personalizado do painel Giro de Negociações (Ficha de Parceiros) não aceita parâmetros dinâmicos representados pelo caractere `?` na expressão SQL. Se o filtro ativo tiver sido salvo com esse tipo de parâmetro, o sistema bloqueia a consulta e exibe esse erro.

*(pendente sua confirmação: "A única variável aceita é o usuário logado, disponível como opção própria no Assistente de Filtros, ela não é digitada manualmente como '?'.")*