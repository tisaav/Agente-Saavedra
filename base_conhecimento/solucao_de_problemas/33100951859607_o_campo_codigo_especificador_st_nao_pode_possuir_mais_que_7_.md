# O campo 'Código Especificador ST' não pode possuir mais que 7 dígitos

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33100951859607-O-campo-C%C3%B3digo-Especificador-ST-n%C3%A3o-pode-possuir-mais-que-7-d%C3%ADgitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33100951859607-O-campo-C%C3%B3digo-Especificador-ST-n%C3%A3o-pode-possuir-mais-que-7-d%C3%ADgitos)  
> **ID:** `33100951859607` | **Última Atualização:** 2026-07-22T14:29:42Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33100951839383)

 **MENSAGEM:**

[CORE_E03869] Ao importar um XML no portal de importação de XML apresenta o erro 'O campo 'Código Especificador ST' não pode possuir mais que 7 dígitos. 

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33101316918423)

 SITUAÇÃO:**

Esse comportamento ocorre quando o sistema está configurado para "Exigir Liberação e Alterar o Cadastro" na tela Importação de XML Comercial > Rotinas > Outras Opções > Configuração de Liberação de Divergência.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33101349786519)

 CAUSA:**
O campo CEST no XML contém mais de 7 dígitos, e o sistema tenta inserir essa informação no cadastro do produto.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33100964371863)

SOLUÇÃO:**

Nessa situação, o XML será importado normalmente, porém o código CEST não será atualizado no cadastro do produto.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/33100951846935)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/33100951846423)