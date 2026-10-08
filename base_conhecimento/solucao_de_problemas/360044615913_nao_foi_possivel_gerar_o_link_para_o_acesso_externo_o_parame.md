# Não foi possível gerar o link para o acesso externo: o parâmetro 'Endereço para acesso externo ao WGE' não foi cadastrado no sistema

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615913-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-link-para-o-acesso-externo-o-par%C3%A2metro-Endere%C3%A7o-para-acesso-externo-ao-WGE-n%C3%A3o-foi-cadastrado-no-sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615913-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-link-para-o-acesso-externo-o-par%C3%A2metro-Endere%C3%A7o-para-acesso-externo-ao-WGE-n%C3%A3o-foi-cadastrado-no-sistema)  
> **ID:** `360044615913` | **Última Atualização:** 2026-07-22T15:54:37Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589648706455)

 MENSAGEM:**

[CORE_E03066]: Não foi possível gerar o link para o acesso externo: o parâmetro 'Endereço para acesso externo ao WGE' não foi cadastrado no sistema.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589634268695)

 CAUSA:**

Ao tentar executar rotinas no sistema que necessitam da URL de acesso e o parâmetro ENDACESSEXTWGE não estiver configurado, será apresentada a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589634257687)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589634261783)

 Configure o parâmetro **"****ENDACESSEXTWGE"**.

Acesse a tela **"Preferências"** *(Caminho de acesso: Configurações » Avançado)*, busque pela chave **ENDACESSEXTWGE** e no campo **"Texto"**, informe o link (domínio) de acesso ao sistema.

- O parâmetro **"Endereço para acesso externo ao WGE", ENDACESSEXTWGE"**, é utilizado para determinar a URL externa de acesso ao sistema. A empresa deverá ter um link (domínio) que será apontado para o servidor do sistema, para que o sistema possa ser acessado pela internet.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15298481916951)

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589634263319)

 **Realizada essa configuração, teste uma nova execução do procedimento que estava sendo realizado.