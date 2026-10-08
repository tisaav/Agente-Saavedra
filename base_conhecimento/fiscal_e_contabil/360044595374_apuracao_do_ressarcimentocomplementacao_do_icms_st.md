# Apuração do Ressarcimento/Complementação do ICMS-ST

> **Módulo:** Fiscal e Contábil | **Subseção:** Ressarcimento e complementação  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595374-Apura%C3%A7%C3%A3o-do-Ressarcimento-Complementa%C3%A7%C3%A3o-do-ICMS-ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595374-Apura%C3%A7%C3%A3o-do-Ressarcimento-Complementa%C3%A7%C3%A3o-do-ICMS-ST)  
> **ID:** `360044595374` | **Última Atualização:** 2026-09-15T17:22:18Z

---

```text

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312900644759)

 **Módulo:** Livros Fiscais > Arquivos
```

Essa tela possibilita que você realize a apuração mensal de seus documentos e, assim, possa verificar se possui direito ao ressarcimento, ou se deve efetuar a complementação dos valores referentes às vendas para o consumidor final.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416165716631)

Dessa forma, você pode acessar os links a seguir para saber mais sobre as funcionalidades dessa tela:

[Painel Principal](#painelprincipal)[Aba Filtros](#abafiltros)

[Botões no topo da tela](#botesnotopodatela)[Aba Itens Apurados](#abaitensapurados)

|  |  |  |
| --- | --- | --- |
|  |  |  |

## 
Painel Principal

Inicialmente, informe a **"Empresa"** e a **"Dt. Referência"** para que o sistema possa verificar os documentos e realize a apuração dos mesmos.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416175877655)

O campo **"Alíquota Interna"** exibirá a alíquota interna para a UF da Empresa selecionada.

Em relação ao campo **"Vlr. Total de Ressarcimento"**, tem-se que este mostrará a soma dos itens apurados, considerando as sequências que tiveram direito ao ressarcimento.

No campo **"Vlr. Total de Complementação"** teremos a soma dos itens apurados, considerando as sequências que deverão ser complementadas.

Será exibido no campo **"Vlr. Total da Diferença da Operação"**, a diferença entre o total do ressarcimento e o total da complementação. Considere ainda que, esse campo sempre terá seu valor positivo.

Mostra-se no campo **"Vlr. Total da Apuração"** o valor total do ressarcimento ou da complementação para a Empresa e Referência selecionadas, já aplicando a alíquota interna.

O campo **"Apuração Final"** será preenchido informando se a empresa tem direito ao ressarcimento na referência ou se a mesma deverá realizar a complementação dos valores.

[[voltar ao topo]](#top)

## Aba Filtros

Nessa aba, é possível definir quais os documentos que deverão ser analisados, ou seja, no campo "Filtro Personalizado" você poderá inserir algum tipo de restrição para buscar produtos, itens e/ou notas específicos para a apuração.

```text
**    

![dica FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312900648599)

 Dica:** Para saber como realizar a inserção de informações nesse campo de forma correta, 
     basta acionar o botão 

![ajuda.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312900649239)

 **"Ajuda"** localizado ao lado do campo.
```

Se a marcação **"Desconsiderar produto usado como brinde e consumo"  **for habilitada, os itens dos documentos não serão considerados no processamento.

[[voltar ao topo]](#top)

## Aba Itens Apurados

Nessa aba, você pode realizar a apuração de todos os itens com ICMS-ST, para verificar os casos de restituição ou complementação. Dessa forma, o sistema efetuará o levantamento de vendas para o consumidor final, cruzando as vendas com as compras que possuem ICMS-ST.

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416178716055)

Será possível selecionar uma nota/item tanto da venda quanto da compra através do campo **"Nro. Único"**.

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16254421485591)

 **Informações adicionais:**

A regra de busca dos documentos no pop-up **"Seleção da Nota"**, sendo ele aberto ao buscar a nota pelo campo acima informado, ocorrerá da seguinte forma:

- Primeiramente, o produto deverá possuir rastreamento de estoque;

- O documento deverá ser uma venda aprovada e estar ligada a uma compra pelo rastreamento;

- 
O Parceiro da Nota deve ser um consumidor final, contribuinte ou não contribuinte;

- 
A tributação do item de venda deve ser igual a **"60-ICMS cobrado anteriormente por substituição"**;

- O item de venda deverá possuir quantidade informada maior que zero;

- 
A tributação do item da compra de origem também deverá ser igual a 60-ICMS cobrado anteriormente por substituição ou apresentar valor informado no campo **"Base Substituição"**, ou seja, a tributação será para um item com cálculo do ST;

- O item de compra também precisará possuir quantidade informada maior que zero;

- E, por fim, a diferença entre o valor de compra e o valor de venda deverá ser diferente de zero.

Deve-se realizar o seguinte cálculo para definir se determinado item tem direito ou não ao ressarcimento:

```text
 

![Calculadora.FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312900649751)

  *(VALOR DA COMPRA - VALOR DA VENDA)*
```

Caso o valor seja positivo, possui direito ao ressarcimento. Por outro lado, sendo negativo, o valor deverá ser complementado.

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16254421498519)

 Para conhecer os detalhes das opções do campo Tributação, acesse o artigo Alíquotas de ICMS, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#tributa%C3%A7%C3%A3o).

[[voltar ao topo]](#top)

## Botões no topo da tela

A tela Apuração do Ressarcimento/Complementação do ICMS-ST é composta por abas, as quais descrevemos até aqui e também por botões que executam diversas funções dentro desta rotina. Abaixo, você pode saber mais sobre eles:

**

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416188955671)

 Filtros:** Este botão abre o assistente de configuração de filtros personalizados para a tela.

![modo_grade_configurar_grade.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766656052375)

 **Modo grade [F6]/Configurar grade:** Por meio deste botão, alterna-se a visualização da tela entre modo grade e modo formulário; além disso, configura-se a grade da maneira almejada, ou seja, pode-se selecionar, ordenar ou ocultar as colunas da forma mais confortável para o usuário.

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416193723927)

 **Cadastrar Apuração do Ressarcimento/Complementação do ICMS-ST [F8]: **Por meio deste botão, tem-se a inicialização do cadastro de uma Apuração.

![CP73.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766692979735)

 **Anterior e Próximo:** Neste, os botões de navegação entre os registros já cadastrados.

![CP74.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766693611415)

 **Excluir [F9]:** Ao acionar esse botão, realiza-se a exclusão do registro selecionado na tela.

![duplicar.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766662862103)

 **Duplicar:** Este botão replica o registro selecionado, criando um novo com as configurações equivalentes àquele primeiramente selecionado.

![atualizar.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766733084055)

 **Atualizar:** Por meio deste botão, recarrega-se toda a tela de Apuração do Ressarcimento/Complementação do ICMS-ST.

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416180978711)

 **Processar:** Ao acionar esse botão, uma busca dos documentos contidos dentro da **"Dt. Referência"** será realizado e em seguida calcula-se a apuração.

![informações adicionais FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16254421485591)

 **Informações adicionais:**

Caso você realize o processamento de uma apuração e seja verificado que já existem [Itens Apurados](#abaitensapurados), o processo será interrompido para que uma decisão seja tomada através do pop-up que se abrirá, e este conterá os seguintes itens:

- 
**Substituir:** Ao acionar esse botão tem-se que toda a apuração será deletada e refeita;

- 
**Incluir:** Esta opção quando selecionada fará com que apenas documentos que não foram apurados sejam incluídos;

- 
**Cancelar:** Acionando-se esta opção, tem-se que o processo será cancelado.

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416189109911)

 **Visualizar:** Este botão quando acionado, gerará um relatório com todos os documentos apurados na referência informada.

![botao-exportar-grade-para-pdf FINAL.jpg](https://ajuda.sankhya.com.br/hc/article_attachments/22891338713751)

 **Exportar grade para PDF:** Este botão apresenta opções de exportação e visualização das informações da tela. Pode-se **"Exportar para PDF"**, **"Exportar para planilha"** ou **"Exportar para cubo"**.

![anexo.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766721430295)

 **Anexo:** Por meio deste botão pode-se anexar qualquer documento que seja relevante para a rotina de Apuração do Ressarcimento/Complementação do ICMS-ST.
 

![CP60.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766723187735)

 **Outras Opções:** As funcionalidades disponibilizadas por este botão podem ser visualizadas no link [Botão Outras Opções...](#botooutrasopes...).

![configura__o_da_tela.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766776032919)

 **Configuração da Tela:** Por meio deste botão, você poderá realizar a configuração da tela e suas respectivas abas e campos de forma mais proveitosa e adequada para o usuário. Além disto, será possível determinar como ocorrerá a geração da numeração da tela, seja **"Automática"** ou **"Manual"**.

[[voltar ao topo]](#top)

## Botão Outras Opções...

O botão **"Outras Opções..."** é acionado por meio do ícone 

![CP60.png](https://ajuda.sankhya.com.br/hc/article_attachments/8766723187735)

 localizado no alto da tela, conforme mencionado acima; tem-se aqui, as seguintes funcionalidades:

![mceclip9.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416181008535)

Essas duas opções possuem vínculo com a marcação **"Apuração Confirmada?"** localizada no [Painel Principal](#painelprincipal) dessa tela; uma vez confirmada a apuração, o reprocessamento não poderá ser executado, portanto, as opções **"Marcar Apuração como Confirmada" e "Desmarcar Apuração como Confirmada"** deverão ser utilizadas para que você execute a marcação da maneira que for conveniente.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#tributa%C3%A7%C3%A3o)