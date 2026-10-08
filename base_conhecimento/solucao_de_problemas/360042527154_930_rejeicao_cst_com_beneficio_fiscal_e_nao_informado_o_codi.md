# 930 Rejeição: CST com benefício fiscal e não informado o código de benefício fiscal [nItem: nnn]

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042527154-930-Rejei%C3%A7%C3%A3o-CST-com-benef%C3%ADcio-fiscal-e-n%C3%A3o-informado-o-c%C3%B3digo-de-benef%C3%ADcio-fiscal-nItem-nnn](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042527154-930-Rejei%C3%A7%C3%A3o-CST-com-benef%C3%ADcio-fiscal-e-n%C3%A3o-informado-o-c%C3%B3digo-de-benef%C3%ADcio-fiscal-nItem-nnn)  
> **ID:** `360042527154` | **Última Atualização:** 2026-09-22T13:23:21Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457540457367)

 MENSAGEM:**

930 Rejeição: CST com benefício fiscal e não informado o código de benefício fiscal.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457491358999)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:
Quando trabalharmos com Desoneração do ICMS, tag <motDesICMS>, será obrigatória a informação do 'Cód. de Benefício Fiscal na UF', para isso:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457540461335)

 Acesse a tela "****[Produtos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113): (Caminho de acesso:* Configurações » Cadastros » Produtos » Produtos*)

- Aba "**Impostos"**

- Campo "**Cód. de Benefício Fiscal na UF"**: informe o respectivo Código, o mesmo deverá ser disponibilizado pela Contabilidade.

![Captura_de_tela_2023-05-08_153158.png](https://ajuda.sankhya.com.br/hc/article_attachments/14448334486807)

 

Se o código for preenchido após o lançamento do produto na Nota, exclua o item na nota e faça novamente o lançamento, para puxar o código.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457491365271)

 Acesse a tela "****[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)": (Caminho de acesso:* Comercial » Preferências » Empresa*)

- Aba: "**NFe/ NFC-e"**

- Campos: "**Considere Benefícios ao incluir/alterar item da nota"=** [Marcado], "**Atualização Cód. Beneficio no Faturamento pelo Produto**"=Sempre Atualizar

![Captura_de_tela_2023-05-08_153457.png](https://ajuda.sankhya.com.br/hc/article_attachments/14448431436439)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457540466583)

 Após os ajustes, gerar o Lote novamente.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457540468887)

 **CAUSA:**

Quando realizada operação com CST (Tributação):

20 - Com redução de base de cálculo
30 - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
40 - Isenta
41 - Não tributada
50 - Suspensão
51 - Diferimento
60 - ICMS cobrado anteriormente por substituição tributária
70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
90 - Outras

E a tag** <cBenef>** não for preenchida.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457491373975)

 OBSERVAÇÃO:**

([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota Técnica.


---

### 🔗 Links e Referências Internas:

- [Produtos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)
- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)