# Não é permitido renegociação com títulos de competências (Mês/Ano) diferentes

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615233-N%C3%A3o-%C3%A9-permitido-renegocia%C3%A7%C3%A3o-com-t%C3%ADtulos-de-compet%C3%AAncias-M%C3%AAs-Ano-diferentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615233-N%C3%A3o-%C3%A9-permitido-renegocia%C3%A7%C3%A3o-com-t%C3%ADtulos-de-compet%C3%AAncias-M%C3%AAs-Ano-diferentes)  
> **ID:** `360044615233` | **Última Atualização:** 2026-07-22T15:55:17Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426948170775)

 MENSAGEM:**

Não é permitido renegociação com títulos de competências (Mês/Ano) diferentes.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426948176919)

 SOLUÇÃO:**

- Essa situação ocorre devido a criação do parâmetro **"MANTEMDTENTSAI", **que determina a geração de títulos de renegociação com 'Data Entrada e Saída' igual à dos títulos renegociados.

- Quando selecionado mais de um título na renegociação o sistema vai assumir a maior 'Data Entrada e Saída' dentre eles.

- Com esse parâmetro ligado, o sistema **não permitirá** renegociação de títulos com 'Data Entrada e Saída' de competência(Mês) diferentes.

Dessa forma, caso não deseje trabalhar com esse comportamento, desligue o parâmetro:

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426919941527)

 **Acesse a tela **"Preferências"** (Caminho de acesso: *Configurações » Avançado » Preferências*).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426919944087)

 Busque pela chave MANTEMDTENTSAI**.**

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426919947159)

 **Provavelmente ele estará **"Ligado"**, classifique-o como **"Desligado"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426948198167)

 Após a realização do procedimento acima, refaça a Renegociação.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16426919955479)

 CAUSA**

Ocorre ao tentar renegociar títulos com 'Data Entrada e Saída' de competência(Mês) diferentes.