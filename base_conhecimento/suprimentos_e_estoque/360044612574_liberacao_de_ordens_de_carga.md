# Liberação de Ordens de Carga

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612574-Libera%C3%A7%C3%A3o-de-Ordens-de-Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612574-Libera%C3%A7%C3%A3o-de-Ordens-de-Carga)  
> **ID:** `360044612574` | **Última Atualização:** 2026-07-29T14:13:38Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311552621463)

 Módulo: **WMS > Rotinas
```

Esta tela permite fazer a liberação das ordens de carga, para que seja possível efetuar as separações correspondentes à mesma. Assim, o gerente do WMS determinará quais ordens de carga serão liberadas para separação. Esse procedimento acontecerá depois do envio da O.C para o WMS, e nenhuma tarefa de separação será executada até que a O.C esteja liberada.

Neste artigo, trataremos dos seguintes tópicos:

[Painel de Filtros](#paineldefiltros)                                             [Botão Liberar Separações](#bot%C3%A3oliberarsepara%C3%A7%C3%B5es)

[Validações da tela](#valida%C3%A7%C3%B5esdatela)                                           

![LOC01.png](https://ajuda.sankhya.com.br/hc/article_attachments/360086460013)

## Painel de Filtros

Insira a **"Empresa"** utilizada na O.C.

Em **"Ordem de Carga"**, informe o número da ordem de carga.

No campo **"****Período ordem de carga"**, insira o período com base na Data Inicial da Ordem de Carga.

A **"Área de Separação"** irá filtrar as O.C que tenha no mínimo uma separação, que pertença à área de separação informada.

O campo **"****Situação"**, apresenta as seguintes opções:

- 
**Todas****:** serão filtradas todas as O.C

- 
**Não Liberadas****:** Trará todas as O.C, de todas as separações não estão liberadas.

- 
**Parcialmente Liberadas****:** Trará todas as O.C que possua alguma separação liberada, mais para as quais ainda exista liberação pendente.

- 
**Totalmente Liberadas****:** Trará todas as O.C de todas as separações que estejam liberadas.

[[voltar ao topo]](#top)

## Botão Liberar Separações

Na parte superior direita da tela, o botão Liberar Separações, quando pressionado exibirá um pop-up com um resumo das separações por Área de separação, para as O.C que estejam selecionadas na grade principal.

![image__77_.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085278974)

A saber:

**Liberada****:** Virá por padrão marcado, e define se as Ordens de Carga dessa área de separação serão liberadas ou não.

**Área de Separação****:** Área de separação para a Ordem de Carga selecionada.

**Sep. Liberadas****:** Quantidade de separações liberadas.

**Sep. N Liberadas****:** Quantidade de separações não liberadas.

**Peso Total****:** Peso total das separações.

As alterações feitas no pop-up de Liberação de O.C. serão efetivadas pelo botão **"Confirmar" **no rodapé.

[[voltar ao topo]](#top)

## Validações da tela

![LCO04.png](https://ajuda.sankhya.com.br/hc/article_attachments/360085279294)

Ao realizar algumas operações nesta tela, é necessário se atentar para as seguintes validações:

- 
Caso você tente liberar uma Área de Separação, que possui uma Ordem de Carga cuja doca é indefinida, o sistema emitirá uma mensagem, não permitindo essa operação.

- 
Caso você libere uma Área de Separação e depois desmarque a mesma para não ser liberada, se existir alguma tarefa em andamento para esta Área de Separação o sistema não permitirá a operação.

- 
Você só poderá utilizar\alterar a doca da Ordem de Carga, para uma doca de saída e que esteja liberada.

- 
Caso você tente alterar a doca de uma Ordem de Carga, que já tenha tarefa de separação em andamento, o sistema não permitirá a operação.

[[voltar ao topo]](#top)