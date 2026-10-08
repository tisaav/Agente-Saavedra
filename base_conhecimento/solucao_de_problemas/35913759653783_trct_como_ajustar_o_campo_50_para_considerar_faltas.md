# TRCT: Como Ajustar o Campo 50 para Considerar Faltas

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35913759653783-TRCT-Como-Ajustar-o-Campo-50-para-Considerar-Faltas](https://ajuda.sankhya.com.br/hc/pt-br/articles/35913759653783-TRCT-Como-Ajustar-o-Campo-50-para-Considerar-Faltas)  
> **ID:** `35913759653783` | **Última Atualização:** 2026-08-18T19:53:38Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35913917464215)

** SITUAÇÃO:**

Ao gerar a TRCT de um colaborador desligado, o campo 50 (“Saldo de DIASTRAB/Dias Salário”) não está deduzindo corretamente as faltas registradas.

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35913887135383)

** SOLUÇÃO:**

Para corrigir o comportamento apresentado, ajuste a ''**Regra de Cálculo''** (Pessoal+» Cadastros):** **

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36183211116695)

 Inclua os eventos de faltas no TRCT:**

- 

Abra a Regra de Cálculo, na aba ''**TRCT''**, e subaba ''**Eventos''; **

- 

Localize o código ''**50 - Saldo de DIASTRAB/dias Salário (líquido de FALTASDIA/faltas e DSR)''; **

- 

Inclua os eventos de ''**faltas''** e ''**DSR sobre faltas''** na configuração.

![regra de calculo.gif](https://ajuda.sankhya.com.br/hc/article_attachments/35913917467799)

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36183226760855)

 **Configure os eventos de desconto e faltas na TRCT:**

- 

Lista de eventos de faltas; 

- 

Lista de eventos de desconto DSR; 

![image (53).png](https://ajuda.sankhya.com.br/hc/article_attachments/36183226761623)

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35913917470743)

** CAUSA:**

O comportamento ocorre devido à ausência de configuração dos eventos de faltas e DSR na Regra de Cálculo da TRCT. Sem esses eventos configurados, o sistema não realiza a dedução correta das faltas no cálculo do saldo de dias trabalhados.