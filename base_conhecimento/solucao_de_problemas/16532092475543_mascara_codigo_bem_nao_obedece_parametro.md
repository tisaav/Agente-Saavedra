# Máscara código Bem - Não obedece parâmetro

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16532092475543-M%C3%A1scara-c%C3%B3digo-Bem-N%C3%A3o-obedece-par%C3%A2metro](https://ajuda.sankhya.com.br/hc/pt-br/articles/16532092475543-M%C3%A1scara-c%C3%B3digo-Bem-N%C3%A3o-obedece-par%C3%A2metro)  
> **ID:** `16532092475543` | **Última Atualização:** 2026-07-22T14:55:05Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16532092656535)

  MENSAGEM:**

Máscara código Bem - Não obedece parâmetro.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16532152750615)

 CAUSA:**

Ocorre devido a configuração do parâmetro **"Qtd dígitos máscara geração automática de BENS - QTDDIGGERBEM".**

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16532137590295)

 SOLUÇÃO:**

Esse parâmetro irá definir o tamanho da máscara numérica para geração dos bens. O default será 4, e os valores válidos serão de 1 a 10. 
Na tela de geração automática de BENS, ao informar no campo "Inicial - Sequencia", por exemplo, TESTE, o sistema automaticamente irá gerar os bens, dependendo da configuração do parâmetro.

Parâmetro igual a 1 (limite de 1-9)
Parâmetro igual a 2 (limite de 1-99)
Parâmetro igual a 3 (limite de 1-999) 
Parâmetro igual a 4 (limite de 1-9999) (padrão)
Parâmetro igual a 5 (limite de 1-99999)

**Exemplo:**

Uma nota com 10 itens e o parâmetro configurado para 2. Na tela de geração do automática dos itens, no campo "Inicial - Sequencia", é informado TESTE (sem hifen) será gerado a sequência
TESTE-01
TESTE-02
...
TESTE-10

Caso o parâmetro estiver configurado para 3. Na tela de geração do automática dos itens, no campo "Inicial - Sequencia", é informado TESTE (sem hifen) será gerado a sequência
TESTE-001
TESTE-002
...
TESTE-010

O modelo "Numeração Sequencial", também seguirá as definições do parâmetro, porém, como para este modelo é necessário mais digítos, o sistema utilizará a definição do parâmetro e mais 3 dígitos.
Parâmetro igual a 3 = 000001 
Parâmetro igual a 4 = 0000001(padrão)
Parâmetro igual a 5 = 00000001
Parâmetro igual a 6 = 000000001