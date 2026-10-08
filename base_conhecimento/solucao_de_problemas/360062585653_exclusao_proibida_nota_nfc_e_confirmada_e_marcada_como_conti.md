# Exclusão proibida. Nota NFC-e confirmada e marcada como Conting.Off-Line NFC-e

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360062585653-Exclus%C3%A3o-proibida-Nota-NFC-e-confirmada-e-marcada-como-Conting-Off-Line-NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360062585653-Exclus%C3%A3o-proibida-Nota-NFC-e-confirmada-e-marcada-como-Conting-Off-Line-NFC-e)  
> **ID:** `360062585653` | **Última Atualização:** 2026-07-22T15:25:42Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302472858647)

 MENSAGEM**:

[CORE_E02690] Exclusão proibida. Nota NFC-e confirmada e marcada como Conting.Off-Line NFC-e.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302479804183)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302479805591)

 Verifique a chave gerada na aba NF-e no rodapé da nota e consulte verificando se de fato a nota não existe na SEFAZ.

* Chave: 31191207602070000169650010000000049006671801 Não consta na SEFAZ. *

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302479806871)

 Via DBEXplore realize a consulta: **SELECT TPEMISNFE FROM TGFCAB WHERE NUNOTA = XXXX TPEMISNFE - 9 Notas com TPEMISNFE - 9** não podem ser excluídas. Então faça o ajuste do campo via banco de dados: altere o campo **TPEMISNFE** para **NULL** ou 0 (zero)

Após procedimento realize a exclusão da nota.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302479808535)

 CAUSA:**

Mensagem ocorre porque o campo TPEMISNFE foi atualizado com 9 e apenas notas com o campo TPEMISNFE igual a NULL ou zero (0) podem ser excluídas.