# Conheça quais folhas estão no S-1210 e no S-1200

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10089175545751-Conhe%C3%A7a-quais-folhas-est%C3%A3o-no-S-1210-e-no-S-1200](https://ajuda.sankhya.com.br/hc/pt-br/articles/10089175545751-Conhe%C3%A7a-quais-folhas-est%C3%A3o-no-S-1210-e-no-S-1200)  
> **ID:** `10089175545751` | **Última Atualização:** 2026-07-29T13:16:10Z

---

#### **Veja abaixo exemplos que vão deixar claro como avaliar:**

 

**Para avaliar o S-1210 Pagamentos:**

![XML 10-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18970532423959)

 

**No XML do S-1210 acima demonstra a:**

**Folha Normal Mensal **do período de referência 06/2022 que foi paga no dia 02/07/2022.

**Folha de Adiantamento **do período de referência 07/2022 que foi paga dia 20/07/2022.

O XML do S-1210 de **perApur 07/2022**, quer dizer que o S-1210 está sendo gerado na referência 07/2022 e nele é montando os pagamentos que estiveram **dentro do período de 01/07 a 31/07/2022.**

Usando o SELECT abaixo, conseguirá visualizar mais fácil as folhas pagas dentro do período. Ele deverá ser executado na tela **DBExplorer** *(Caminho de acesso à tela: Configurações » Avançado » DBExplorer)*.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/10088933369751)

 

**Veja no portal do eSocial onde consultar S-1210:**

![ESOCIAL 1  10-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18970545542807)

Caso precise gerar exclusão do S-1210, conforme exemplo citado acima:

***** **Bloqueie a liberaçã**o da folha de pagamento **Mensal **da referência 06/2022 e folha de **adiantamento **da referência 07/2022.

***** Feito isso o S1210 será gerado como exclusão na Ref 07/2022.

**Para avaliar o S-1200 Remuneração:**

O XML do S-1200 de **perApur 06/2022**, quer dizer que o S-1200 está sendo gerado na referência 06/2022 e nele é montando as remunerações (folha) que estiveram dentro da referência, ou seja de 01/06 a 30/06/2022.

![XML 2  10-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18970545547031)

Para verificar se o S-1200 da folha normal foi enviado corretamente vá ate a referência 06/2022 e verifique a remuneração enviada (S-1200).

Caso precise verificar o adiantamento, vá até a referência 07/2022 e verifique a remuneração enviada no (S-1200).

**Veja no portal do eSocial onde consultar S-1200:**

![ESOCIAL 2  10-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18970532435991)

Caso precise gerar exclusão do S-1200, conforme exemplo citado acima:

*** Bloqueie a liberação **da folha de pagamento Mensal da referência 06/2022.

***** Feito isso o S1200 será gerado como exclusão na Ref 06/2022.

[[Voltar ao topo]](#top)