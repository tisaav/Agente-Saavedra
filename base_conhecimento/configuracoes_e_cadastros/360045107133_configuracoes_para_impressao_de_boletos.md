# Configurações para Impressão de Boletos

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107133-Configura%C3%A7%C3%B5es-para-Impress%C3%A3o-de-Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107133-Configura%C3%A7%C3%B5es-para-Impress%C3%A3o-de-Boletos)  
> **ID:** `360045107133` | **Última Atualização:** 2026-07-29T13:54:12Z

---

Abaixo serão descritas as configurações necessárias para realizar a impressão de boletos:

Primeiramente, o modelo de Relatório Formatado no iReport deve ser cadastrado na tela [Modelos de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607134-Modelos-de-Boleto-s-). 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16117154856727)

 O Sankhya-Om não suporta impressão de boletos em formato **"****txt."**

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500008094421)

Depois, vincule o modelo cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-) por meio do campo **"Número do relatório modelo"**.

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500008095161)

Em seguida, no [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), habilite a marcação **"Emite"** e preencha os campos **"Modelo"** e **"Impressora"**.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500007907602)

Realizados os procedimentos acima, na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), configure o campo **"Imprimir Pix/Boleto/Duplicata?"**, de forma a permitir a impressão de boletos.

![Screenshot_18.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/6987984888727)

Por fim, no Cadastro de [Tipo de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), selecione no campo **"Imprimir Pix/Boleto/Duplicata"** a opção **"Manual"** ou **"Na confirmação"** da nota.

![Screenshot_19.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/6988028182039)

**Nota:** deve haver harmonia entre essas configurações, pois elas estão interligadas. Por exemplo, se um usuário tentar emitir um boleto com uma TOP que não foi configurada para a emissão de boletos, ele não obterá sucesso, ou se utilizar um Tipo de Negociação que não permita emissão de boletos, ele também não obterá sucesso.

![essencial FINAL (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/17549864134295)

 Ao selecionar um Tipo de Título na Central de Notas, e este título estiver com a marcação **"Proibir impressão boleto?" **da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) realizada, não será impresso como boleto e também não possuirá taxa de boleto. Portanto, ao confirmar a nota na [Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), poderá ser observado que no rodapé da nota em que o tipo de título selecionado está com essa marcação efetuada, as linhas [Cód. Barras Receb.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap) e **"Linha Dig. Receb."** não estarão preenchidas.


---

### 🔗 Links e Referências Internas:

- [Modelos de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607134-Modelos-de-Boleto-s-)
- [Modelos de Nota Fiscal/Duplicatas/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-)
- [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)
- [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas)
- [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)
- [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas)
- [Tipo de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)
- [Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas)
- [Cód. Barras Receb.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap)