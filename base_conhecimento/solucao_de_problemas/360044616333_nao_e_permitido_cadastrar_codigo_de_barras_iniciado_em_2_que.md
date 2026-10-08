# Não é permitido cadastrar código de barras iniciado em 2 que case com a formatação de código de barras (parâmetro FORMABARRASQTD) juntamente com o parâmetro CODBARDECOMP2 ligado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616333-N%C3%A3o-%C3%A9-permitido-cadastrar-c%C3%B3digo-de-barras-iniciado-em-2-que-case-com-a-formata%C3%A7%C3%A3o-de-c%C3%B3digo-de-barras-par%C3%A2metro-FORMABARRASQTD-juntamente-com-o-par%C3%A2metro-CODBARDECOMP2-ligado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616333-N%C3%A3o-%C3%A9-permitido-cadastrar-c%C3%B3digo-de-barras-iniciado-em-2-que-case-com-a-formata%C3%A7%C3%A3o-de-c%C3%B3digo-de-barras-par%C3%A2metro-FORMABARRASQTD-juntamente-com-o-par%C3%A2metro-CODBARDECOMP2-ligado)  
> **ID:** `360044616333` | **Última Atualização:** 2026-08-25T14:38:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605650937111)

 MENSAGEM:**

[CORE_E03947] Não é permitido cadastrar código de barras iniciado em 2 que case com a formatação de código de barras (parâmetro FORMABARRASQTD) juntamente com o parâmetro CODBARDECOMP2 ligado.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605650948631)

 CAUSA:**

Ocorre quando o parâmetro **Formatação código de barras - FORMABARRASQTD** está configurado  e **Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2** está ligado, havendo um conflito de configuração.

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605650942871)

 SOLUÇÃO:**

Considere o Comportamento da aplicação, conforme abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605650950807)

 Configurações » Avançado » Preferências

Pesquise pelos parâmetros:

- 
**Formatação código de barras - FORMABARRASQTD** = [Caso este esteja configurado]

- 
**Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2** = [Quando ligado, o código de barras, quando iniciado com 2, vem do uso de Balança.]

- 
**Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2 **- Ligado entende que o todo código de barras começado em 2 são originado de balança, composto pela seguinte sintaxe "Cód.Prod./Preço/Qtd". Isso ocorre pois com o parâmetro ligado o sistema entende que esse produto foi pesado em balança e vendido de acordo com seu peso.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18605650953239)

Importante revisar, pois caso algum produto realmente use a pesagem, não poderá desligar o parâmetro **Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2**, então deverá ajustar as configurações de formação do parâmetro **Formatação código de barras - FORMABARRASQTD**.