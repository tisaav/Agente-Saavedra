# 874 Rejeição: Percentual de FCP inválido [nItem: xxxxx]

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/17643265977111-874-Rejei%C3%A7%C3%A3o-Percentual-de-FCP-inv%C3%A1lido-nItem-xxxxx](https://ajuda.sankhya.com.br/hc/pt-br/articles/17643265977111-874-Rejei%C3%A7%C3%A3o-Percentual-de-FCP-inv%C3%A1lido-nItem-xxxxx)  
> **ID:** `17643265977111` | **Última Atualização:** 2026-07-22T14:53:10Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17643213023511)

 **MENSAGEM:**

 [874 - Rejeição: Percentual de FCP inválido [nItem: xxxxx]]

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/17623554531095)

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17643265966359)

SOLUÇÃO:**

Regra de Validação da Sefaz

![](https://www.oobj.com.br/bc/assets/Articles/783/RV874_1.60.PNG)

Para emissão de NF-e com FCP (Fundo de Combate à Pobreza)

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17643260138263)

 Acesse: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS*

Pesquise pela regra de ICMS que incidiu nos itens da nota e  ajuste o campo "**% ICMS FCP**", de acordo com as orientações do contador, que por sua vez irá alimentar as TAG's <pFCP> e <vFCP>.

 

Para facilitar a busca pela exceção de ICMS utilizada em cada item/lançamento verifique o conteúdo: [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043874154-Como-identificar-qual-a-al%C3%ADquota-exce%C3%A7%C3%A3o-de-ICMS-utilizada-no-lan%C3%A7amento-)

 

![PERCENTUAL DE FCP NO ICMS.gif](https://ajuda.sankhya.com.br/hc/article_attachments/17643586355863)

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17677151744535)

 OBSERVAÇÃO:**

Para essa Regra de Validação não há exceções. Sempre que preenchido o campo pFCP, a alíquota informada deve ser o percentual igual permitido para o estado emissor, conforme tabela divulgada pela [Sefaz](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Iy/5Qol1YbE=).

 

Segue a baixo como identificar o percentual correto para a UF da empresa emitente, conforme site da SEFAZ, [clique aqui](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=).

 

![PERCENTUAL FCP.gif](https://ajuda.sankhya.com.br/hc/article_attachments/17643213028375)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17643228418583)

 Após os ajustes, inutilize a numeração da NF-e atual e refaça o faturamento.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17643213032599)

CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e no campo referente ao percentual de FCP campo "**% ICMS FCP**", for informado um valor divergente ao percentual correspondente ao permitido no estado emissor, haverá a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17677151744535)

 OBSERVAÇÃO:**

****[(NT2016.002)](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=) - Nota Técnica - v 1.60


---

### 🔗 Links e Referências Internas:

- [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043874154-Como-identificar-qual-a-al%C3%ADquota-exce%C3%A7%C3%A3o-de-ICMS-utilizada-no-lan%C3%A7amento-)