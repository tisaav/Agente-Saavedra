# O Tipo de Operação (TOP) não permite ou usuário está com o campo "Altera Nota Fiscal Confirmada" desmarcado ou o parâmetro EXCLUIRNOTACONF está desligado

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043696513-O-Tipo-de-Opera%C3%A7%C3%A3o-TOP-n%C3%A3o-permite-ou-usu%C3%A1rio-est%C3%A1-com-o-campo-Altera-Nota-Fiscal-Confirmada-desmarcado-ou-o-par%C3%A2metro-EXCLUIRNOTACONF-est%C3%A1-desligado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043696513-O-Tipo-de-Opera%C3%A7%C3%A3o-TOP-n%C3%A3o-permite-ou-usu%C3%A1rio-est%C3%A1-com-o-campo-Altera-Nota-Fiscal-Confirmada-desmarcado-ou-o-par%C3%A2metro-EXCLUIRNOTACONF-est%C3%A1-desligado)  
> **ID:** `360043696513` | **Última Atualização:** 2026-09-03T12:42:22Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163886573207)

 MENSAGEM:**

[CORE_E00891] O Tipo de Operação (TOP) não permite ou usuário está com o campo "Altera Nota Fiscal Confirmada" desmarcado ou o parâmetro EXCLUIRNOTACONF (Permite exclusão de notas confirmadas?) está desligado.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163917203607)

 SITUAÇÃO:**

Ao tentar realizar exclusão/alterações de nota fiscal confirmada é apresentada a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163917207575)

 SOLUÇÃO:**

Para liberação de exclusão de notas confirmadas em sua base, temos as restrições abaixo que precisam ser analisadas conforme sua necessidade:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163886580375)

 Liberação de forma Geral:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163886581783)

 Acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)" ***(Configurações » Avançado)* e ligue o parâmetro **"EXCLUIRNOTACONF"**.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/14711754751639)

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163917212951)

 **Liberação por Tipo de Operação - TOP:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163886581783)

 Acesse a tela de cadastros da TOP *(Caminho de acesso: Comercial » Arquivos » Cadastro » Tipos de Operação).*

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163886581783)

 Na aba **"Geral"**, a opção **"Permitir alteração após confirmar"** deve estar marcada.

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14711785327511)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163917213847)

 Liberação por Usuário:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163886581783)

 Acesse a tela de **"[Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)"** *(Caminho de acesso: Configurações » Controle de Acesso)*, na aba Segurança, a opção **"Altera registros confirmados"** deve estar marcada.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163886581783)

Se a marcação **"Altera registros confirmados" **estiver realizada, mesmo que a TOP não permita alterar nota depois de confirmada, será possível realizar a alteração. Se a TOP permitir alteração, o sistema não usa esta marcação do cadastro de usuários e permite que todos os usuários alterem notas confirmadas.

 

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14711770744983)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16163917215511)

 CAUSA**:

Ocorre quando a TOP do lançamento  e/ou o Usuário não possui permissões para alterar nota/pedido já confirmado.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)