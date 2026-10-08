# Não está sendo apresentado os valores no totalizadores do IRRF no esocial

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4405933292695-N%C3%A3o-est%C3%A1-sendo-apresentado-os-valores-no-totalizadores-do-IRRF-no-esocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405933292695-N%C3%A3o-est%C3%A1-sendo-apresentado-os-valores-no-totalizadores-do-IRRF-no-esocial)  
> **ID:** `4405933292695` | **Última Atualização:** 2026-07-29T13:23:46Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370293590039)

 MENSAGEM:**

Ao tentar se consultar no portal, na aba totalizadores, não aparece o total de imposto de renda retido da empresa, como era esperado. 

S-5012 - Informações do IRRF consolidadas por contribuinte

 

**Menu: Folha de Pagamentos ➔ Totalizadores ➔ Empregador ➔ Imposto de Renda**

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4405933235351)

 

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4405933254039)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16370293593111)

 CAUSA:**

O que ocorre é que o evento S-5012 - Informações do IRRF consolidadas por contribuinte foi excluído da versão S-1.0 do eSocial simplificado, por esse motivo ele não será mais processado. 

Então só é possível consultar e conferir agora o evento totalizador S-5002 – que trata do evento de retorno do evento S-1210 por empregado. O eSocial, diferentemente do que faz em relação à contribuição previdenciária, não efetua cálculo do valor devido e apenas consolida o valor informado pelo declarante como efetivamente retido a título de Imposto de Renda. 

Então a partir da implantação da versão S-1.0 (19/07/2021), quando o evento S-1299 for enviado na versão 2.5 (período de convivência) o respectivo totalizador S-5012 será retornado “vazio”, isso porque, o evento S-5012 não existe na versão S-1.0 e não está sendo utilizado para apuração do IRRF no eSocial. Esta apuração é feita pela RFB, por meio da DCTF (PGD) e pela DIRF.