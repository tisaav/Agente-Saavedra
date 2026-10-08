# IE do destinatário não informada

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042525874-IE-do-destinat%C3%A1rio-n%C3%A3o-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042525874-IE-do-destinat%C3%A1rio-n%C3%A3o-informada)  
> **ID:** `360042525874` | **Última Atualização:** 2026-09-21T18:51:00Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457260373143)

 MENSAGEM:**

[232 - Rejeição]: IE do destinatário não informada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457260377239)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457211476119)

 Consulte o CNPJ do destinatário no SINTEGRA para verificar qual a Inscrição Estadual está vinculada ao seu CNPJ.

[http://www.sintegra.gov.br/](http://www.sintegra.gov.br/)

No site do Sintegra, selecione o Estado do respectivo parceiro destinatário e realize a consulta de seu CNPJ. 

É possível também usar o [Portal de Consulta do Cadastro Centralizado de Contribuinte (CCC)](https://dfe-portal.svrs.rs.gov.br/NFE/CCC)

 

**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457260387735)

 **Identificado a Inscrição Estadual correta do destinatário, altere essa informação no cadastro do parceiro:

- Tela "****[Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) (Caminho de acesso:* Configurações » Cadastros*)

- Aba: "**Identificação"**

 

![Captura_de_tela_2023-05-08_144720.png](https://ajuda.sankhya.com.br/hc/article_attachments/14446951831703)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457260390935)

 Certifique-se de que a 'Classificação de ICMS' vinculada em seu cadastro, encontra-se correta, em caso negativo realize os devidos ajustes:

- Tela Parceiros : (Caminho de acesso:* Configurações » Cadastros) *

- Aba:  "**Fiscal"**

- Campo:** "Classificação de ICMS"**

 

![Captura_de_tela_2023-05-08_144330.png](https://ajuda.sankhya.com.br/hc/article_attachments/14446862609687)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457260394007)

 Realizado os ajustes acima, redigite o cabeçalho da nota e gere um novo lote.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457211489431)

 IMPORTANTE:**

Para destinatários do '**Distrito Federal**', ao realizar a consulta no Sintegra, verifique se existem informações para o campo '**CF/DF' (Cadastro Fiscal do Distrito Federal). **Caso exista, essa informação deverá ser preenchida no campo "**Inscrição Estadual"**.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457260399639)

 CAUSA:**

Quando for emitida uma NF-e para destinatário, identificado como Isento (indIEDest = 2) ou Não Contribuinte (indIEDest = 9), que possui Inscrição Estadual (IE) ativa no seu Estado (UF) e essa não for informada em seus dados, será retornado a rejeição.


---

### 🔗 Links e Referências Internas:

- [Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)