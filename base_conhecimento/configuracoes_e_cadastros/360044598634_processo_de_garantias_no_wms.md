# Processo de Garantias no WMS

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598634-Processo-de-Garantias-no-WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598634-Processo-de-Garantias-no-WMS)  
> **ID:** `360044598634` | **Última Atualização:** 2026-07-29T13:47:51Z

---

Este processo deve ser utilizado para produtos avariados que podem ser trocados pelo fornecedor da mercadoria.

Neste artigo trataremos sobre os seguintes tópicos:

![Processo_de_Garantias_no_WMS.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411511018775)

#### **Configurações Iniciais**

Inicialmente, no Sankhya Om na tela [Endereços de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento) crie um endereço chamado** "Garantia"**, o mesmo deve estar abaixo do nível identificado como endereços especiais. Este endereço deve ter as seguintes configurações:

- 
O campo **"Situação do Estoque"** deve ser configurado com a opção **"Bloqueado"**;

- 
As opções **"Multi Produto"**, **"Permite Expedição"** e **"Permite Fragmentar Estoque"** devem estar marcadas.

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411468650903)

Em seguida, nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), informe o endereço criado anteriormente no campo **"Endereço especial de garantia"**.

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411468987159)

No [Cadastro de Docas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612974-Docas), configure pelo menos uma doca com a marcação **"Balcão"** acionada.

![mceclip10.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411466316823)

Por fim, acesse o [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e em uma TOP de Devolução de Compra, configure na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abawms) as opções **"Envio em Garantia?"** e **"Separação em Balcão"**.

![envio_e_separa_ao.gif](https://ajuda.sankhya.com.br/hc/article_attachments/4411466244887)

[[voltar ao topo]](#top)

#### **Movimentação**

Ao identificar um produto avariado, registre a avaria por meio do coletor, na função Avaria:

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411465143831)

 

![mceclip4.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411459821463)

Uma vez informado, é necessário executar a tarefa de transferência, que consiste em retirar a mercadoria fisicamente do endereço e colocá-la no endereço de avaria.

Após efetuar a análise de recuperação da mercadoria, verifique se esta mercadoria poderá ser trocada pelo fornecedor. Então, movimente esta mercadoria para o endereço de garantia, por meio da tela **"Rotinas/Movimentação de Mercadorias entre Endereço"**, que irá gerar uma tarefa de transferência a ser executada.

Quando esta mercadoria for devolvida, gere uma nota de Devolução de Compra com a TOP configurada anteriormente e informe a quantidade a ser devolvida.

A nota deve ser confirmada e em seguida enviada para a Separação no WMS, escolhendo a doca configurada para saída de balcão. Logo após, execute o processo de separação da mercadoria, lembrando que agora a opção a ser escolhida será a **"Separação por Balcão"**.

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411459761431)

Depois de efetuada a separação, será necessário fazer a conferência, assim como em um processo comum de separação, e em seguida liberar a doca.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42310681074071)

|  | Nesse processo não poderá ser realizado o corte por falta de estoque na conferência, pois é explícita a quantidade que será enviada para a garantia, sendo que, via sistema, não existe nenhuma restrição para que seja informado um corte na separação ou conferência. |
| --- | --- |

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Endereços de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa)
- [Cadastro de Docas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612974-Docas)
- [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abawms)