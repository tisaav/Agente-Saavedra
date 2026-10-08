# Não foram encontradas transações (TGFTEF) para o NSU XXX

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33279809613207-N%C3%A3o-foram-encontradas-transa%C3%A7%C3%B5es-TGFTEF-para-o-NSU-XXX](https://ajuda.sankhya.com.br/hc/pt-br/articles/33279809613207-N%C3%A3o-foram-encontradas-transa%C3%A7%C3%B5es-TGFTEF-para-o-NSU-XXX)  
> **ID:** `33279809613207` | **Última Atualização:** 2026-07-22T14:29:10Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279809610903)

 **MENSAGEM:**Não foram encontradas transações (TGFTEF) para o NSU XXX.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279809611159)

 SOLUÇÃO:**Para que os lançamentos sejam processados corretamente pela rotina de **Conciliação de Cartão**, é necessário que eles já existam previamente na tabela ''**TGFTEF''**. A partir da versão **4.32**, é possível verificar essa existência por meio da tela **"Monitoria TEF"**.  

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279797761175)

 Acesse a tela **"Monitoria TEF" (**Consulta > Monitoria TEF)**;**
 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279809611671)

 Verifique se o Número Único **(NSU)** que apresentou erro está listado na tela; 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279797761687)

 Faça uma validação extra pelo DbExplorer, acessando a tela **"DbExplorer"** (Configurações» Avançado» DBExplorer); 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279809611927)

 Execute a seguinte consulta, substituindo NSU pelo número que deseja validar:

SELECT * FROM TGFTEF WHERE NSU LIKE '%NSU%'Certifique-se de substituir NSU pelo valor real que apresentou erro durante o processamento.  

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33331492480151)

 **Observação: **caso após a realização dessas validações, o erro persista, sugerimos que entre em contato com a equipe de suporte técnico para uma análise mais aprofundada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33279797762071)

 CAUSA:**

O erro ocorre durante o processamento de um arquivo de conciliação de cartão quando o Número Único (NSU) informado não está registrado na tabela TGFTEF.