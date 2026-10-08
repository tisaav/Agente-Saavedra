# A soma dos valores dos fatos contábeis deve ser igual ao saldo final do código de aglutinação menos o saldo inicial do código de aglutinação

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617333-A-soma-dos-valores-dos-fatos-cont%C3%A1beis-deve-ser-igual-ao-saldo-final-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-menos-o-saldo-inicial-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617333-A-soma-dos-valores-dos-fatos-cont%C3%A1beis-deve-ser-igual-ao-saldo-final-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-menos-o-saldo-inicial-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o)  
> **ID:** `360044617333` | **Última Atualização:** 2026-07-22T15:53:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595394803095)

 MENSAGEM:**

A soma dos valores dos fatos contábeis (somatório do campo 04 dos registros J215 filhos) deve ser igual ao saldo final do código de aglutinação (campo 07 do registro J210) menos o saldo inicial do código de aglutinação (campo 05 do registro J210).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595394805143)

SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

*

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595405962519)

 *Acesse: *Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD, *aba: **"Fatos DMPL / DLPA".**

Para cada registro de Fato contábil, registro um histórico na grade inferior.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15184999901207)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16595405964823)

CAUSA **

Todos os históricos utilizados nos lançamentos que fazem parte da DMPL (geralmente lançamentos de transferências para as contas de lucros/prejuízos) devem ter seu histórico devidamente informado, se houver lançamento sem histórico ou que o histórico por ventura não esteja configurado nesta aba, este erro será apresentado.