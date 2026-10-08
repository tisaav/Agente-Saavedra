# Controle de Qualidade dos Materiais

> **Módulo:** Produção | **Subseção:** Produção/W  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596374-Controle-de-Qualidade-dos-Materiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596374-Controle-de-Qualidade-dos-Materiais)  
> **ID:** `360044596374` | **Última Atualização:** 2026-07-29T14:51:07Z

---

Este processo representa a execução do Controle de Qualidade dos Materiais (Matérias-Primas) que tiveram entrada no estoque da empresa antes de serem consumidos pela produção.

Neste artigo iremos tratar dos seguintes tópicos:

![Icones__43_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312674979351)

[#configura%C3%A7%C3%B5es](#configura%C3%A7%C3%B5es)

![Icones__42_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312662268439)

[#opera%C3%A7%C3%B5es](#opera%C3%A7%C3%B5es)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |

```text

```

| Clique nos tópicos e saiba mais sobre cada um deles. |
| --- |

#### 
**Configurações**

Para o funcionamento deste processo primeiramente, efetue a ativação dos parâmetros **"Controle de Laudo de Amostras? - CONTRLAUDOAMOST"** e **"Utiliza Status do Lote? - UTILSTATUSLOTE"**.

Em seguida, defina um modelo de requisição no parâmetro **"Nro Requisição Modelo p/ Baixa Est.MP.Amostragem - MODREQAMOSTRAS"**. Assim, sempre que uma amostra for aprovada ou reprovada, uma requisição de estoque representando o consumo do produto/lote para se formar a amostra será gerada.

Feito isso, cadastre um Tipo de Amostra para ser utilizado pelo produto (material) ao qual se deseja executar o Controle de Qualidade. Este cadastro deverá ser realizado a partir da tela [Tipos de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119013-Tipos-de-Amostra).

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416856718743)

Além disso, na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) você deverá realizar as seguintes configurações:

- 

Na aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional), no campo **"Controlar por"** selecione a opção **"Número de lote"**:

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416872608279)

- 

Em seguida, efetue a marcação **"Usa Status de Lote"**, aba Medidas e estoque, sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaestoque):

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416856681879)

- 

Informe também o **"Tipo de Amostra"** que será utilizado para o produto em questão, na aba [Tipos de Amostra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119013-Tipos-de-Amostra):

![mceclip3.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416864448791)

Agora, defina na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque), se os movimentos gerados a partir dela, devem gerar amostra do produto de forma automática; esta marcação é opcional e, portanto, caso não seja marcada, será necessário lançar a amostra manualmente na tela [Registro de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611334-Registro-de-Amostras).

![mceclip5.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416864562455)

Cadastre também na tela [Padrões de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o) um Padrão de Classificação para o produto em questão. Este padrão é a representação sistêmica do ensaio (análise) ao qual o produto deve ser submetido durante o processo de Controle de Qualidade. Nele, são relacionadas as características analisáveis que devem ser consideradas no ensaio, bem como o intervalo de aceitação de cada uma delas para o produto. 

![mceclip6.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416872928791)

[[voltar ao topo]](#top)

#### 
**Operações**

Este processo envolve três operações, a seguir trataremos sobre cada uma delas. Para facilitar sua navegação clique nos links abaixo:

![Icones__48_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312674981015)

[#entradademateriais](#entradademateriais)

![Icones__49_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312662270487)

[#amostragem](#amostragem)

![Icones__50_.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312674981527)

[#an%C3%A1lise](#an%C3%A1lise)

|  |  |  |
| --- | --- | --- |

**Entrada de Materiais**

Depois de realizadas as configurações apresentadas acima, quando um movimento de entrada ([Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras)/[Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)) for gerado para o produto em questão, será possível definir o status de seu lote por meio do campo **"Status do Lote"** no item em questão.

```text

```

| O valor padrão deste campo é "Quarentena", porém, poderá ser modificado para            "Aguardando Aprovação". |
| --- |

![mceclip11.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416858687895)

As notas que movimentarem o estoque do produto para a saída ou reserva, deverão considerar também este status (configurado no campo **"Status para Baixa no estoque"** do Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)).

[[voltar ao subtítulo]](#opera%C3%A7%C3%B5es) 

**Amostragem**

Com o produto em estoque, será possível retirar uma amostra do mesmo. Sistematicamente, este procedimento é realizado na tela [Registro de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611334-Registro-de-Amostras); nela são comandadas as ações sobre a amostra.

![mceclip7.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416873849367)

Com o Registro de Amostra gerado, temos a possibilidade de realizar algumas ações:

- 

**Apontar amostragem:** através do preenchimento do campo **"Dh. Amostragem"**; Amostragem é a coleta do produto para se formar uma amostra.

- 

**Apontar verificação:** será realizada, através do preenchimento do campo **"Dh. Verificação"**. A Verificação é um processo de validação da amostra após sua coleta, de forma a definir se ela pode ou não ser utilizada no ensaio (teste); ela vem seguida da aprovação/reprovação pelos botões no topo da tela.

- 

**Desmembrar amostra:** através do botão **"Desmembrar"** localizado no alto da tela. Apenas amostras aprovadas e cujo o tipo de amostra que permita o desmembramento, terão este botão habilitado.

- 

**Apontar análise:** realizando o preenchimento do campo **"Dh. Análise"**. Apenas as amostras aprovadas permitirão tal apontamento, sendo que, o apontamento de amostra representa o início da análise que terá sua continuidade através do lançamento de um laudo.

Para realização das ações de **"Desmembrar"**, **"Aprovar"** ou **"Reprovar"** uma amostra, é necessário realizar a liberação de um acesso especial através da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) no Módulo Produção no menu **"Rotinas > Registro de Amostras > Permite Aprovar/Reprovar/Desmembrar"**.

Além disso, uma amostra só poderá ser aprovada ou reprovada se:

1. 

O usuário possuir acesso especial para esta ação (tela Acessos);

1. 

Lidar com um registro de amostra já coletado e conferido (verificado) onde o status estará igual a **"Coletando"**.

[[voltar ao subtítulo]](#opera%C3%A7%C3%B5es) 

**Análise**

A execução do ensaio (teste) é representando pela inserção de um laudo na tela [Controle de Laudo de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114-Controle-de-Laudo-de-Amostras).

O funcionamento desta tela é simples; com a aplicação do filtro, serão apresentadas as amostras na grade superior **"Amostras"**, a qual será executado o ensaio.

Com a amostra desejada selecionada, clique sobre o botão de inserir novo laudo. Um pop-up para seleção do **"Padrão de Classificação"** será apresentado de forma a especificar-se qual teste está sendo executado. Os Padrões de Classificação carregados no pop-up são aqueles ligados ao produto da amostra ou grupo de produto do mesmo, conforme sua configuração realizada na tela [Padrão de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o).

![mceclip8.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416858021911)

Com o Padrão de Classificação selecionado e o laudo salvo, você poderá apontar o resultado das características analisáveis (tela Controle de Laudo de Amostras, aba [Item de laudo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114-Controle-de-Laudo-de-Amostras#abaitemdelaudo)). A medida que forem apontadas as características, será sinalizado com as cores **azul**** **e **vermelho** se o resultado está dentro ou fora do aceitável.

![mceclip10.png](https://ajuda.sankhya.com.br/hc/article_attachments/4416879650327)

O espaço **"Observação"** é carregado automaticamente com um valor definido no cadastro da característica ou então no vínculo **"Produto x Padrão de Classificação"**, com o objetivo de instruir o analista no momento do teste. Este espaço também poderá ser utilizado após a execução de testes, para a especificação de uma justificativa da não aprovação da característica, por exemplo.

Com o resultado de cada característica apontado no sistema, será possível concluir o ensaio por meio do botão **"Concluir Laudo"**. Este botão será habilitado apenas para os usuários que possuírem acesso especial para tal ação na tela Acessos no Módulo Produção no menu **"Rotinas > Controle de Laudo de Amostras > Concluir Laudo"**.

No momento de conclusão do laudo, serão consideradas todas as amostras com laudos **"Aguardando Aprovação"** para o **"Produto/lote"**, além de sempre considerar o último laudo de cada amostra.

Sendo assim, quando desejar realizar ensaios diferentes sobre o mesmo Produto/lote, será necessário lançar uma amostra para cada ensaio. Outra característica, é o fato de sempre ser considerado o último laudo da amostra; com isto, uma forma de corrigir uma análise anterior incorreta, é lançar um segundo laudo para a mesma amostra.

Para geração do resultado final para o Produto/lote, será criado um elemento denominado de **"Laudo Pai"**. Logo, o efeito deste Laudo Pai será o resultado final de todos os últimos laudos pendentes para aquele Produto/lote.

 Quando um Laudo Pai é reprovado por consequência de algum dos laudos das amostras do Produto/lote ter sido reprovado, é possível aprovar este Produto/lote, desde que o usuário possua acesso especial para fazê-lo na tela Acessos no Módulo Produção no menu **"Rotinas > Controle de Laudo de Amostras > Concluir laudo fora do padrão"** e, o [Padrão de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o) permita tal ação (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o#abageral), marcação **"Permite confirmar quando laudo for rejeitado"**.

Considerando esta situação, o sistema exibirá um pop-up com o seguinte questionamento:

***"O Produto XX lote Y possui um ou mais laudos reprovados. Deseja continuar?"***

Você pode optar por:

- 

**Reprovando Laudo Pai:** a reprovação do laudo pai gera consequentemente a reprovação do Produto/Lote. Deste modo, o STATUSLOTE deste produto no estoque e na nota de entrada será alterado para **"R-Reprovado"**.

- 

**Aprovando Laudo Pai:** a aprovação do laudo pai gera consequentemente a aprovação do Produto/Lote. Sendo assim, o STATUSLOTE deste produto no estoque e na nota de entrada será alterado para **"P-Aprovado"**.

 

ℹ️**Nota sobre o Status do Lote:** É importante observar que o sistema não permite múltiplos status para um mesmo lote de produto. O status do lote é sempre atualizado conforme o laudo mais recente emitido. Este comportamento se deve ao fato de o estoque ser tratado de forma agrupada pelo lote, e não individualizado por nota fiscal de entrada.

 

 

[[voltar ao subtítulo]](#opera%C3%A7%C3%B5es) [[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Tipos de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119013-Tipos-de-Amostra)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-)
- [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque)
- [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional)
- [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaestoque)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)
- [Registro de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611334-Registro-de-Amostras)
- [Padrões de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o)
- [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras)
- [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)
- [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos)
- [Controle de Laudo de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114-Controle-de-Laudo-de-Amostras)
- [Item de laudo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114-Controle-de-Laudo-de-Amostras#abaitemdelaudo)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o#abageral)