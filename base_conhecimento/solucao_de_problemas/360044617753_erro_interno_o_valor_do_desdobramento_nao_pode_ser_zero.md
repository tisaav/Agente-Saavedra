# Erro interno: O valor do desdobramento não pode ser zero

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617753-Erro-interno-O-valor-do-desdobramento-n%C3%A3o-pode-ser-zero](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617753-Erro-interno-O-valor-do-desdobramento-n%C3%A3o-pode-ser-zero)  
> **ID:** `360044617753` | **Última Atualização:** 2026-07-22T15:52:33Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617025801239)

 MENSAGEM:**

[CORE_E02398]: Erro interno: O valor do desdobramento não pode ser zero.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617025804055)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617063156375)

 Certifique-se que o valor de baixa = 0 corresponde ao esperado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617025809815)

 Caso a baixa com valor desdobramento zerado seja necessária, ajuste o parâmetro **"VLRBAIXAZERO"** para ligado:

- Tela **"****Preferências"** *(Caminho de acesso: Configurações » Avançado) *

- Chave **'VLRBAIXAZERO': ligado. **Se estiver "Sim" permite que o usuário efetue baixa com valor zero. Se estiver "Não", só serão aceitas baixas com valores maiores que zero.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14919162365591)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617063160087)

 Ajustado o parâmetro, proceda com a baixa. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16617063163415)

 CAUSA:**

Mensagem apresentada ao tentar realizar o procedimento de baixa, quando o valor do desdobramento for igual a zero, e o parâmetro Aceita valor de baixa igual a zero estiver desligado.