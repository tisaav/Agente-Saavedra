# Não está destacando os impostos federais como PIS / COFINS / CSLL no XML da NFS-e

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865434-N%C3%A3o-est%C3%A1-destacando-os-impostos-federais-como-PIS-COFINS-CSLL-no-XML-da-NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865434-N%C3%A3o-est%C3%A1-destacando-os-impostos-federais-como-PIS-COFINS-CSLL-no-XML-da-NFS-e)  
> **ID:** `360042865434` | **Última Atualização:** 2026-07-22T16:05:49Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214643351)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214646167)

 Acesse Configurações » Cadastros » **"[Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)"**

Campo **"Tipo Impostos"**, selecione o Imposto correspondente e configure o Tipo de Imposto como Retido.

 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/12092734646167)

 

O sistema na geração do XML, busca primeiramente os impostos calculados via outros impostos como retidos (TGFIMN), desde que o Tipo Imposto no cadastro do imposto esteja devidamente configurado com imposto correspondente (TGFIMC.TIPOIMPOSTO), como PIS/COFINS/CSLL.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214649367)

 Caso não tenha configuração via Outros Impostos, sistema passa para Etapa 2.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214653847)

 Acesse Alíquotas de PIS / COFINS / CSLL

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214649367)

 Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214649367)

 Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214649367)

 Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de CSLL

Campo **"Retém no Financeiro" **marcado.

 

Na ausência de impostos calculados via outros impostos, o sistema verifica na tabela de impostos, se existem os impostos PIS, COFINS e CSLL, calculados como retidos -  marcação 'Retém no financeiro' do cadastro de alíquotas de PIS, COFINS e CSLL (TGFIFE.RETEMFIN).

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214649367)

 Caso o cálculo dos impostos federais seja não retido, mas precisa destacar no xml, sistema passa para a Etapa 3.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214656919)

 Caso não exista o cálculo dos impostos como **retidos,  **mas os mesmos estejam calculados em um dos pontos mencionados acima como inclusos, para destacar os impostos federais no XML, ligue o parâmetro **"DESTIMPNRETIDO - Destacar impostos federais na NFS-e mesmo quando não retidos"**.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16114214663959)

 CAUSA:**

Ocorre quando em casos que o imposto não seja do tipo retido via outros impostos ou via Alíquotas de Impostos e mesmo assim precisa destacar na nota, porém o parâmetro DESTIMPNRETIDO está desligado.


---

### 🔗 Links e Referências Internas:

- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)