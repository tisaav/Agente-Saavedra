# Cálculo de ICMS acontecendo com CST 50 em nota de devolução - Como Resolver

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35517743755543-C%C3%A1lculo-de-ICMS-acontecendo-com-CST-50-em-nota-de-devolu%C3%A7%C3%A3o-Como-Resolver](https://ajuda.sankhya.com.br/hc/pt-br/articles/35517743755543-C%C3%A1lculo-de-ICMS-acontecendo-com-CST-50-em-nota-de-devolu%C3%A7%C3%A3o-Como-Resolver)  
> **ID:** `35517743755543` | **Última Atualização:** 2026-07-22T14:25:03Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36018883043479)

 **SITUAÇÃO:**

Durante o lançamento de notas fiscais de devolução ou de operações com **"CST 50 – Suspensão"**, a alíquota aparece zerada, porém o sistema continua preenchendo e calculando os campos **"Base ICMS (BASEICMS)"**, **"Alíquota ICMS (ALIQICMS)"** e **"Valor ICMS (VLRICMS)"**. 

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36018883045143)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36018903423255)

 Acesse o cadastro de **''Alíquotas de ICMS''** (Comercial» Arquivo» Cadastros» Alíquotas) : 

- 

Marque o campo **"Zerar valores"** na alíquota utilizada na operação para que o sistema anule os cálculos de base e valor do ICMS quando aplicável. 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36018883047959)

 Salve a alteração no cadastro da alíquota e, se houver, atualize o item da nota afetada para que a nova configuração passe a vigorar.

![image (29).png](https://ajuda.sankhya.com.br/hc/article_attachments/36018919227415)

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36018903429015)

 **CAUSA:** 

Isso ocorre quando o parâmetro de alíquota responsável por zerar os valores não está marcado, mantendo internamente  `infoAliq.zerar = false`  e permitindo o cálculo.