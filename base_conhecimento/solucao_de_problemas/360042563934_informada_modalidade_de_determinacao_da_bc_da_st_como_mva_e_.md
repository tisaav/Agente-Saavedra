# Informada modalidade de determinação da BC da ST como MVA e não informado o campo pMVAST [nItem: nnn]

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042563934-Informada-modalidade-de-determina%C3%A7%C3%A3o-da-BC-da-ST-como-MVA-e-n%C3%A3o-informado-o-campo-pMVAST-nItem-nnn](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042563934-Informada-modalidade-de-determina%C3%A7%C3%A3o-da-BC-da-ST-como-MVA-e-n%C3%A3o-informado-o-campo-pMVAST-nItem-nnn)  
> **ID:** `360042563934` | **Última Atualização:** 2026-07-22T16:09:43Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459781601175)

 MENSAGEM:**

[932 - Rejeição]: Informada modalidade de determinação da BC da ST como MVA e não informado o campo pMVAST [nItem: nnn]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459781610647)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459781616023)

 Sistema atualizado para versões abaixo:

- 3.32b37 ou superior

- 3.31b206 ou superior

- 3.30b351 ou superior

Para mais informações sobre como realizar o processo de atualização verifique os artigos: 
[Atualização do sistema SankhyaOM via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596634)

[Atualização do sistema JIVAEVO via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043012853)

Caso utilize nossos produtos **Mitra** e **MGE Comercial,** atualize também o release para a última versão disponível no Place: **4.30.0.4** . Atualize também o SanNFe para a versão mais recente (**SanNFe 2.42b5 ou superior**), disponível em nossa área de Downloads.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459781620759)

 Acesse a tela "**[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)"** (Caminho de acesso:* Comercial » Preferências*), na aba "**NF-e/NFC-e"** e preencha o campo** "Versão NT" **com a opção** Última (Nota Técnica 2021.004):**

 

![Captura_de_tela_2023-05-09_150445.png](https://ajuda.sankhya.com.br/hc/article_attachments/14473951479319)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459781624727)

 Acesse a tela "**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Caminho de acesso:* Configurações » Avançado*):

- Busque o parâmetro** "DATINIULTNTNFE"** - Data Início da última nota técnica da NF-e' e preencha com **01/09/2021**

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/11989861550615)

 

Se  o campo "**Modalidade BC ICMS ST"** for igual a "**Margem Valor Agregado (%)"**, informe o campo "**Margem Lucro (MVA)"**

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459812514071)

 Acesse: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS*

 

![Captura_de_tela_2023-05-09_150746.png](https://ajuda.sankhya.com.br/hc/article_attachments/14474066406551)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459812516503)

 Dessa forma, no XML será gerado:

 

![Captura_de_tela_2023-05-09_150845.png](https://ajuda.sankhya.com.br/hc/article_attachments/14474091144471)

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459812525719)

 Após os ajustes, gere o Lote novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459812528919)

 CAUSA:**

Quando emitida uma nota, cuja 'Modalidade BC ICMS ST', tag <modBCST> , esteja preenchida com o valor 'Margem Valor Agregado (%)' e o campo 'Margem Lucro (MVA)', tag <pMVAST>,  não for gerada.

Modalidade de determinação da BC do ICMS ST, tag <modBCST>:

0 = Preço tabelado ou máximo sugerido;
1 = Lista Negativa (valor);
2 = Lista Positiva (valor);
3 = Lista Neutra (valor);
4 = Margem Valor Agregado (%);
5 = Pauta (valor);

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16459812536727)

 OBSERVAÇÃO:**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458198802327)

** Regra de Validação opcional a critério da UF.

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458198802327)

** ([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota Técnica.


---

### 🔗 Links e Referências Internas:

- [Atualização do sistema SankhyaOM via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596634)
- [Atualização do sistema JIVAEVO via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043012853)
- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)