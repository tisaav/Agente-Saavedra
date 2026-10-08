# Valor do ICMS Interestadual para UF de Destino difere do calculado [nItem:999] (Valor Informado: XXX, Valor Calculado:XXX) (NT2015/003)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050513-Valor-do-ICMS-Interestadual-para-UF-de-Destino-difere-do-calculado-nItem-999-Valor-Informado-XXX-Valor-Calculado-XXX-NT2015-003](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050513-Valor-do-ICMS-Interestadual-para-UF-de-Destino-difere-do-calculado-nItem-999-Valor-Informado-XXX-Valor-Calculado-XXX-NT2015-003)  
> **ID:** `360043050513` | **Última Atualização:** 2026-07-22T16:09:47Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475259258391)

 MENSAGEM:**

[815 - Rejeição]: Valor do ICMS Interestadual para UF de Destino difere do calculado [nItem:999] (Valor Informado: XXX, Valor Calculado:XXX).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475302030487)

 SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475259265687)

 Verifique o cálculo do DIFAL, se está devidamente configurado.

- 

  - Configurações » Cadastros » Partilhas DIFAL

  - Comercial » Arquivo » Cadastros » Tipos de Operação - TOP 

  - Aba "**Impostos"** - campo "**Calcular DIFAL Partilhado**"

  - Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS » campo **"Aliq. Interna Destino"**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475259267479)

 Alíquota Interna Destino

- Insira o percentual da alíquota interna de destino estipulada pela CONFAZ¹.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475259270295)

 Acesse a nota novamente após os ajustes e redigite o item.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475259274519)

 CAUSA:**

Quando for emitida uma NF-e com o Valor do ICMS Interestadual para a UF de Destino (vICMSUFDest) diferente do Calculado pela Sefaz, será retornado a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475302049815)

 OBSERVAÇÕES:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458172823703)

 Como as alíquotas variam de estado para estado e a legislação sempre avança, recomendamos que você faça uma consulta rápida no [portal do Conselho Nacional de Política Fazendária](https://www.confaz.fazenda.gov.br/legislacao/aliquotas-icms-estaduais) (Confaz) para sempre validar esta informação. Lá, é possível revisar o ICMS de cada tipo de mercadoria.

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458172823703)

 (**NT2015/003**) - Nota Técnica: 

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=)