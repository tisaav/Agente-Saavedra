# Configuração do Layout da Nota - DACTE

> **Módulo:** Fiscal e Contábil | **Subseção:** CT-e e CT-e OS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599454-Configura%C3%A7%C3%A3o-do-Layout-da-Nota-DACTE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599454-Configura%C3%A7%C3%A3o-do-Layout-da-Nota-DACTE)  
> **ID:** `360044599454` | **Última Atualização:** 2026-09-15T16:58:53Z

---

Para realizar a configuração de um layout padrão de emissão do CT-e, inicialmente, acesse a tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota). Ao iniciar a inserção de um novo layout, através do botão 

![Botão Novo FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16516358369815)

, será aberta uma pequena tela para escolha do layout.

![layout.gif](https://ajuda.sankhya.com.br/hc/article_attachments/1500007371501)

Escolhendo a opção **"Criar um layout usando um modelo"**, será feito o direcionamento para a tela seguinte, para que você escolha o modelo **"Conhecimento de Transporte (CT-e)"**.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500007372821)

Clicando em **"Próximo"**, na tela seguinte informe a **"Descrição"** do layout, seu correspondente **"Tipo movimento"** e, através da marcação **"Usar como padrão para este tipo de movimento?"**, defina se o modelo de layout será utilizado como padrão para o tipo de movimento escolhido.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500007215722)

Clicando em **"Concluir"**, você finaliza o cadastro do layout, onde o modelo criado possui todas as configurações padrão de campos, informações e ordem para lançamento do CT-e.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/1500007372961)

Caso você queira personalizar o layout sugerido pelo modelo, poderá fazê-lo nessa tela, definindo os campos e ordenações desejados.

**Observação:** o sistema conta com o campo **"Cód. Ident. Operação Transporte"**, de forma abreviada **"CIOT"**; ele se encontra disponível para ser inserido em todos os tipos de layout de nota também por meio da tela Configurador de Layout da Nota. Ao gerar o lote do CT-e, essa informação será apresentada na tag** <CIOT>** que está contida na tag **<rodo>**. O DACTE impresso também contará com o valor informado no CIOT.

**Configuração do SanNFe**

No caso do CT-e, as configurações do SanNFe são equivalentes às definições realizadas para emissão da NF-e, sendo a principal dela, a inserção do certificado digital da empresa. Além disso, os parâmetros **"IP do Servidor de Nota Fiscal Eletrônica - IPSERVNFE"** e **"Pasta de instalação do SanNFe - SANNFEINSTDIR"** também devem ter sua configuração analisada ao configurar-se o SanNFe.


---

### 🔗 Links e Referências Internas:

- [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota)