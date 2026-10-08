# Devolução de IPI ao Fornecedor Industrial

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108273-Devolu%C3%A7%C3%A3o-de-IPI-ao-Fornecedor-Industrial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108273-Devolu%C3%A7%C3%A3o-de-IPI-ao-Fornecedor-Industrial)  
> **ID:** `360045108273` | **Última Atualização:** 2026-07-29T13:54:50Z

---

Corriqueiramente, ocorrem situações em que uma empresa comercial, adquire produtos de um fornecedor que é uma indústria e portanto trabalha com IPI; ao realizar uma operação de devolução de compra, deve-se também devolver o IPI a este fornecedor.

No Sankhya Om podemos realizar este procedimento de devolução de compra, considerando os seguintes comportamentos:

- 
Será considerado o IPI na devolução de empresas comerciais, enviando o valor do IPI no XML através da tag **<vOutro>**, do item e do total;

- 
As tag's **<vIPIDevol>** e **<pDevol>** continuarão sendo enviadas;

- 
No XML da devolução não será enviado o valor do IPI através da tag **<vIPI>**;

- 
Na devolução da nota de compra, o único campo que irá conter valor para o IPI é o **"Vlr. IPI"**; os campos **"Base do IPI"** e **"Alíq. IPI"** estarão zerados.;

- No XML da devolução não irá conter o grupo de IPI.

Teremos as seguintes regras para que seja calculado somente o **"Vlr. IPI"** na devolução da compra para empresas que não trabalham com IPI:

- 
Na tela Preferências da Empresa, aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), o campo **"Trabalha com IPI?"** deve estar desmarcado;

- 
O [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) a ser utilizado, deve ser do tipo de movimento **"E-Devolução de Compra"**. Além disso, na TOP, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), o campo **"Cálculo de ICMS, IPI e ISS"** deve ser definido com a opção **"Não Calcula e digita"**.

A devolução parcial deve ser feita apenas pelo [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953), seguindo os seguintes passos:

Primeiramente, selecione a nota de compra a ser devolvida e acione o botão **"Dev./Est."**;

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4418003202455)

Logo, será aberto o pop-up, para **"Selecionar Itens" **que serão devolvidos;

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4418003243927)

Em seguida, o pop-up **"Seleção de itens para devolução"** é exibido. Informe na coluna **"Qtd. Faturada"**, a quantidade a ser devolvida de cada produto. Após clicar no botão 

![botão Concluir.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16242532460311)

 **"Concluir"**, a nota de devolução será gerada com a quantidade de itens informados e com o IPI proporcional à quantidade de itens.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4417995462935)

**Importante: **com a TOP de devolução configurada da forma acima citada, se a quantidade de itens da nota de devolução for alterada na Central de Compras, o IPI não será recalculado.


---

### 🔗 Links e Referências Internas:

- [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades)
- [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)
- [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953)