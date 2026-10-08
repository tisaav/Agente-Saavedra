# RNTRC situação inválida.(NT2015/001)

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043105353-RNTRC-situa%C3%A7%C3%A3o-inv%C3%A1lida-NT2015-001](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043105353-RNTRC-situa%C3%A7%C3%A3o-inv%C3%A1lida-NT2015-001)  
> **ID:** `360043105353` | **Última Atualização:** 2026-07-22T16:07:59Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443925735831)

 MENSAGEM:**

[682-Rejeição]: RNTRC situação inválida.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443925737495)

 SOLUÇÃO:**

Para correção siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443925741463)

 A Sefaz passou a validar as informações dos dados do RNTRC, caso seja enviado tal informação.

Para essa Regra de Validação não há exceções. Em caso de rejeição por esta regra, o emitente deverá buscar informações diretamente com a ANTT através do canal da ouvidoria (telefone 166). A situação poderá ser consultada na página do RNTRC na internet ([http://rntrc.antt.gov.br](http://rntrc.antt.gov.br)).

 

![mceclip0__1_.png](https://ajuda.sankhya.com.br/hc/article_attachments/360060881133)

 

Diante, disso, é preciso identificar se o veículo utilizado no transporte está com as informações sobre RNTRC corretos. 

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443925742487)

 Para consultar o RNTRC acesse o Portal da ANTT:

[https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/](https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/)

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458171143319)

 Se for veículo da empresa (frota própria), acesse:

- Configurações » Cadastros » Empresas

- Aba: "**Naturezas"**

- Campo: "**RNTRC**" [Informe o RNTRC correto da Empresa]

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458171143319)

 Se for veículo de terceiro, acesse:

- Configurações » Cadastros » Veículos

- Aba: "**Propriedades"**

- Campo: "**RNTRC"  **[Informe o RNTRC correto do veiculo]

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443925744663)

 Caso a RNTRC, esteja inválida ou não possua o respectivo cadastro, desligue o parâmetro  ***RNTRCFROTAPROP-Enviar RNTRC da empresa para frota própria? ***e gere novamente a MDF-e. Assim, as informações do RNTRC não serão encaminhadas no XML, validando a aprovação da MDF-e. A SEFAZ trata esta informação como opcional.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458171143319)

 Este parâmetro está disponível **a partir** das versões:

- 3.26b85 [Release]

- 3.25b255 [Release]

- 3.24b366 [Release]

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443925745815)

 **CAUSA:**

Quando for emitido um MDF-e (modelo 58) e o RNTRC (Registro Nacional de Transportadores Rodoviários de Carga), informado no grupo de tags <infANTT> ou <prod>, estiver com a situação inválida na base da ANTT (Agência Nacional de Transportes Terrestres), haverá a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16443925746711)

 OBSERVAÇÃO:**

**1-** (**NT2015/001**) Nota Técnica:

[https://mdfe-portal.sefaz.rs.gov.br/Site/DownloadArquivoNovo/?tipoArquivo=3&nomeArquivo=MDFe_Nota_Tecnica_2015_001.pdf](https://mdfe-portal.sefaz.rs.gov.br/Site/DownloadArquivoNovo/?tipoArquivo=3&nomeArquivo=MDFe_Nota_Tecnica_2015_001.pdf)