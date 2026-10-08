# Informada modalidade de determinação da BC da ST como MVA e informado o campo pMVAST [nItem: nnn] 

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043006773-Informada-modalidade-de-determina%C3%A7%C3%A3o-da-BC-da-ST-como-MVA-e-informado-o-campo-pMVAST-nItem-nnn](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043006773-Informada-modalidade-de-determina%C3%A7%C3%A3o-da-BC-da-ST-como-MVA-e-informado-o-campo-pMVAST-nItem-nnn)  
> **ID:** `360043006773` | **Última Atualização:** 2026-07-22T16:10:13Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456698494871)

 MENSAGEM:**

[933- Rejeição]: Informada modalidade de determinação da BC da ST diferente de MVA e informado o campo pMVAST [nItem: nnn]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684017175)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684022935)

 Sistema atualizado para versões abaixo:

- 3.32b37 ou superior

- 3.31b206 ou superior

- 3.30b351 ou superior

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684025751)

 Para mais informações sobre como realizar o processo de atualização verifique os artigos: 

[Atualização do sistema SankhyaOM via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596634)

[Atualização do sistema JIVAEVO via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043012853)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684027415)

 Acesse a tela "**[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)"** (Caminho de acesso: *Comercial » Preferências*), vá até a aba "**NF-e/NFC-e"** e defina o campo "**Versão NT" = Última (Nota Técnica 2021.004):**

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14445115763351)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684031383)

 Acesse a tela "**Preferências"** (Caminho de acesso: *Configurações » Avançado*):

- Parâmetro** "DATINIULTNTNFE"** - Data Início da última nota técnica da NF-e = **[01/09/2021**]

 

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/11989595199895)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456698514455)

 Acesse  a tela "****[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)": (Caminho de acesso: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS*) e observe:

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456698517655)

 O campo "**Margem Lucro (MVA)"** não deverá ter valor quando  o campo "**Modalidade BC ICMS ST"** for diferente de "**Margem Valor Agregado (%)"**.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684047383)

 Após os ajustes, gere o Lote novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684025751)

 CAUSA:**

Quando emitida uma nota, cuja 'Modalidade BC ICMS ST', tag <modBCST> esteja preenchida com valor diferente de 'Margem Valor Agregado (%)' e a tag <pMVAST> for gerada.

Modalidade de determinação da BC do ICMS ST, tag <modBCST>:

0 = Preço tabelado ou máximo sugerido; 
1 = Lista Negativa (valor); 
2 = Lista Positiva (valor); 
3 = Lista Neutra (valor); 
4 = Margem Valor Agregado (%);
5 = Pauta (valor);

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684052119)

 OBSERVAÇÕES:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684022935)

 **Regra de Validação opcional a critério da UF.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16456684027415)

 (**NT2021.004)**) - Nota Técnica: 

[http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)


---

### 🔗 Links e Referências Internas:

- [Atualização do sistema SankhyaOM via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596634)
- [Atualização do sistema JIVAEVO via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043012853)
- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)