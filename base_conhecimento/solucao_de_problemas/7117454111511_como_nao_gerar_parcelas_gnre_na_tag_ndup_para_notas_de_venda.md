# Como não gerar parcelas GNRE na tag ndup para Notas de Vendas

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7117454111511-Como-n%C3%A3o-gerar-parcelas-GNRE-na-tag-ndup-para-Notas-de-Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/7117454111511-Como-n%C3%A3o-gerar-parcelas-GNRE-na-tag-ndup-para-Notas-de-Vendas)  
> **ID:** `7117454111511` | **Última Atualização:** 2026-07-22T15:14:58Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361291819543)

 MENSAGEM:**

 O valor da parcela do ICMS ST está sendo gerado no XML e não deveria.

<cobr>
<fat>
<nFat>0</nFat>
<vOrig>23.40</vOrig>
<vDesc>0.00</vDesc>
<vLiq>23.40</vLiq>
</fat>
<dup>
<nDup>001</nDup>
<dVenc>2022-06-29</dVenc>
<vDup>23.40</vDup>
</dup>
<dup>
<nDup>002</nDup>
<dVenc>2022-07-11</dVenc>
<vDup>3.40</vDup>
</dup>
</cobr>

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361328194711)

SOLUÇÃO:**

Realize a configuração no tipo de negociação conforme print abaixo, no campo **"Tipo de Financeiro"**, coloque **"Usar da natureza padrão".**

E no campo **"Natureza Padrão"**, insira uma natureza do tipo Receita 

 

![Imagem](/attachments/token/RUns6sYmCnSFKaNb0Q4Zfx9l8/?name=image.png)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16361291819799)

CAUSA:**

Acontece quando não está parametrizado na preferência **"NATTITNAONOT"** as naturezas de títulos que serão não apresentados na nota.

Caso deseja colocar mais de uma natureza, estas devem ser separadas por virgulas conforme abaixo

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/7118941424407)