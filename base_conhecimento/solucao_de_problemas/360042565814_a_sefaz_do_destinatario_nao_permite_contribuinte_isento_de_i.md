# A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual (NT2015/003)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042565814-A-SEFAZ-do-destinat%C3%A1rio-n%C3%A3o-permite-Contribuinte-Isento-de-Inscri%C3%A7%C3%A3o-Estadual-NT2015-003](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042565814-A-SEFAZ-do-destinat%C3%A1rio-n%C3%A3o-permite-Contribuinte-Isento-de-Inscri%C3%A7%C3%A3o-Estadual-NT2015-003)  
> **ID:** `360042565814` | **Última Atualização:** 2026-09-08T13:14:23Z

---

** 

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475589136535)

 MENSAGEM:**

[805 - Rejeição]: A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual (NT2015/003)

 

** 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475589141015)

SOLUÇÃO:**

Para correção, siga os passos abaixo.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475589142039)

  Verifique no site [Sintegra](http://www.sintegra.gov.br/)se o parceiro destinatário da nota possui Inscrição Estadual cadastrada.

- Caso o parceiro tenha I.E., a mesma deve ser devidamente preenchida em seu cadastro, aba **"Identificação"**, campo **"I.E./RG"**.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475542607383)

 Acesse "****[Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)(Caminho de acesso:* Configurações » Cadastros*)

Aba: "**Fiscal"** » Campo: "**Classificação de ICMS"**

Ajuste conforme detalhes a seguir:

- "1 - Consumidor Final Contribuinte"/ Produtor Rural **OU**

- "9 - Consumidor Final Não Contribuinte".

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475589153687)

 Para tal, sintonize com seu parceiro e/ou contador, a classificação fiscal correta e realize os devidos ajustes.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475542615703)

 IMPORTANTE:**

Nessas duas identificações, o destinatário pode possuir IE cadastrada, mas apenas em identificação como 'Consumidor Final Contribuinte' deve ser informado a IE, obrigatoriamente. 

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475589142039)

 Em **"Tipos de Operação - TOP"*** (Comercial » Arquivo » Cadastros) * » Aba: **"Impostos"**

Campo **"Classificação ICMS":** 'Usar do Parceiro'

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475542607383)

 Após os ajustes, redigite o parceiro no cabeçalho da nota e posteriormente gere o Lote.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475589153687)

 Informe no parâmetro "**UFNFECOMIEHOM**" a UF da empresa emitente. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475589162519)

 CAUSA:**

Este erro ocorre por causa da identificação da IE (Campo: dest / indIEDest - ID: E16a) como "2 - Contribuinte Isento de Inscrição Estadual" em Estado (UF) que não permite essa identificação da IE.

Os Estados que não permitem que os destinatário tenham indicação como Contribuinte Isento são: **AM, BA, CE, GO, MG, MS, MT, PA, PE, RN e SP**.

 

***

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458213864599)

 Exemplo:***

Foi emitida uma NF-e para Destinatário localizado no CE (Ceará) com identificação para sua IE como Contribuinte Isento (indIEDest = 2). Como a Sefaz CE não permite Destinatário como Contribuinte Isento, a NF-e será rejeitada pelo motivo 805.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16475589169047)

OBSERVAÇÕES:**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458213864599)

 Caso a operação seja em base de **Homologação**, verifique o parâmetro "**UFNFECOMIEHOM (UFs que exigem Insc. Estad. em homologação)" ** Caberá a SEFAZ Estadual validar ou não a I.E., caso seja validada, valide conforme orientações citadas nesse artigo. 

**Obs.:** Caso a SEFAZ do estado em questão exija a Inscrição Estadual, mesmo sendo em base de homologação, configure o nome da UF no parâmetro citado acima. Exemplo: 

![A_SEFAZ_do_destinat_rio_n_o_permite_Contribuinte_Isento_de_Inscri__o_Estadual.png](https://ajuda.sankhya.com.br/hc/article_attachments/14506802888599)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458213864599)

 (**NT2015/003**) Nota Técnica:

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=)


---

### 🔗 Links e Referências Internas:

- [Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)