# Nota (s) com frete incluso.<br>Não é possível vincular o CT-e com esta(s) nota(s)

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16612708990743-Nota-s-com-frete-incluso-br-N%C3%A3o-%C3%A9-poss%C3%ADvel-vincular-o-CT-e-com-esta-s-nota-s](https://ajuda.sankhya.com.br/hc/pt-br/articles/16612708990743-Nota-s-com-frete-incluso-br-N%C3%A3o-%C3%A9-poss%C3%ADvel-vincular-o-CT-e-com-esta-s-nota-s)  
> **ID:** `16612708990743` | **Última Atualização:** 2026-09-18T14:22:37Z

---

**  

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612708975127)

  MENSAGEM:**

Nota (s) com frete incluso.<br>Não é possível vincular o CT-e com esta(s) nota(s).

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612699884567)

 CAUSA:**

O erro ocorre pois a nota referenciada já se encontra aprovada no sistema e com o campo tipo frete definido como incluso.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612693011607)

 SOLUÇÃO:**

Segue abaixo alguns parâmetros que influenciam na rotina: 

 

**

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612699880343)

 **O parâmetro **"Recalcular Custos ao final de calc.de frete - RECALCCUSTOFRET"** ao ser habilitado, calculará o custo de entrada da nota e o custo médio.
 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618524469399)

 Caso o parâmetro **"Permite Frete Extra Nota em nota com Frete Incluso? - RATEXTNOTAFRINC"** se encontre ligado, o sistema permitirá o rateio do frete mesmo quando as notas já possuam o frete incluso.
 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16618486417559)

 Caso o parâmetro **"Aquisição de serviço de frete com frete incluso - AQSERVFRETINC"** esteja ativado, o cálculo de frete para melhor transportadora (de forma automática ou manual), desde que seja Incluso, será registrado no campo **"Vlr. frete calc."**.