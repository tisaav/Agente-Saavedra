# Ressuprimento Automático de Filiais

> **Módulo:** Comercial e Vendas | **Subseção:** Comercial  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/6194716592663-Ressuprimento-Autom%C3%A1tico-de-Filiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/6194716592663-Ressuprimento-Autom%C3%A1tico-de-Filiais)  
> **ID:** `6194716592663` | **Última Atualização:** 2026-09-09T18:31:17Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312200594455)

 Módulo: **Comercial > Avançado > Agendadores           

![Versão - 32x32 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42312200596631)

 **Versão disponível:** A partir da 4.12 
```

Através dessa tela você poderá configurar a periodicidade e preferências para geração de movimentações de ressuprimento provenientes de outras unidades ou Centro de Distribuição.

Para saber mais sobre os campos e funcionalidades dessa tela, clique nos link's abaixo:

[Preenchimentos Iniciais](#preenchimentosiniciais)[Aba Horários](#abahor%C3%A1rios)

[Aba Frequência Agendamento](#abafrequ%C3%AAnciaagendamento)[Aba Configurações Gerais](#abaconfigura%C3%A7%C3%B5esgerais)

[Aba Origem](#abaorigem)[Aba Destino](#abadestino)

[Aba Sazonalidade](#abasazonalidade)[Aba Histórico](#abahist%C3%B3rico)

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |

![ressup_filiais.png](https://ajuda.sankhya.com.br/hc/article_attachments/6195393752343)

## 
Preenchimentos Iniciais

O campo **"Nro. Agendamento"** é preenchido automaticamente pelo sistema e é desabilitado para edição.

Informe no campo **"Descrição agendamento"** um nome para identificar o agendamento que está sendo cadastrado. Esse campo é de preenchimento obrigatório.

O campo **"Status Última Execução"** é atualizado automaticamente com o status da última execução do agendamento.

A marcação **"Ativo"** define se o agendador está ou não disponível.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16837427833495)

 É necessário que você informe a "**Empresa Origem"** e um **"Modelo Mov. Origem"** na aba [Origem](#abaorigem) antes de salvar o agendamento cadastrado.

[[voltar ao topo]](#top)

## 
Aba Horários

![ressup_filiais2.png](https://ajuda.sankhya.com.br/hc/article_attachments/6198400261143)

No campo **"Próxima execução em"** você agenda a data e hora da próxima execução, podendo ser inclusive para forçar uma execução imediata.

Na **"Data Final de execução"** informe uma data e hora limite para execução do agendamento.

[[voltar ao topo]](#top)

## 
Aba Frequência Agendamento

Nessa aba você define quando será a **"1ª execução"** e a frequência em que o agendador será executado, sendo **"Diário"**, **"Semanal"** ou **"Mensal"**.

**Importante:** deve ser definido ao menos um horário de execução.

![ressup_filiais9.png](https://ajuda.sankhya.com.br/hc/article_attachments/6198698098839)

[[voltar ao topo]](#top)

## 
Aba Configurações Gerais

![ressup_filiais4.png](https://ajuda.sankhya.com.br/hc/article_attachments/6198767477783)

Nessa aba temos as seguintes informações:

**Seção Opções**

Informe se o **"Tipo Ressuprimento"** será:

- 

**Estoque Mínimo**: com essa opção selecionada, o sistema irá calcular se o estoque atual do produto é menor do que o estoque mínimo definido para a empresa e identificar a quantidade necessária de ressuprimento para gerar os pedidos de compra e venda.

A sequência utilizada pelo sistema para buscar o Estoque Mínimo é:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27324925254807)

 Campo Estoque Mínimo da aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaestoque) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos);

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27324925257751)

 Campo Estoque Mínimo da aba [Impostos/ Informações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa), sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#SubabaGeral) do Cadastro de Produtos;

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/27324925259799)

 Campo Estoque Minímo da aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestoque) do Cadastro de Produtos.

Assim, o primeiro campo da sequência acima que houver valor preenchido, será utilizado no cálculo.

- 

**Estoque Máximo**: selecionando essa opção, o sistema calculará se o estoque atual do produto é menor do que o estoque máximo definido para a empresa e identificar a quantidade necessária de ressuprimento para gerar os pedidos de compra e venda.

Defina o **"Estoque disponível menor que necessidade"** segundo as opções abaixo:

- 

**Gerar conforme prioridade:** com essa opção selecionada, as empresas de destino são atendidas integralmente, uma a uma, na ordem definida pelo campo **"Prioridade"** da aba [Destino](#abadestino), até que a disponibilidade na origem se esgote — as empresas seguintes na ordem podem ficar sem atendimento.

- 

**Proporcionalizar:** Essa opção faz com que as empresas de destino sejam parcialmente atendidas, na mesma proporção de sua necessidade.

- 

**Não gerar:** selecionando essa opção, os produtos com necessidade total maior do que a disponibilidade, não serão enviados a nenhuma das unidades de destino.

Para decidir entre atender por prioridade ou proporcionalizar, o sistema soma a necessidade calculada de todas as Empresas de Destino e compara com a quantidade disponível na Empresa Origem. Se a disponibilidade for suficiente, cada destino recebe o que precisa normalmente; se não for e a opção **Proporcionalizar** estiver selecionada, o sistema distribui os produtos entre os destinos conforme o cálculo:

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16837427833495)

 *Qtde para a filial = (necessidade da filial ÷ necessidade total das filiais) × quantidade disponível na origem*

Quando a Empresa Origem tiver o produto em mais de um local de estoque, a quantidade proporcional de cada filial é distribuída entre esses locais até ser totalmente atendida.

E, por fim, insira qual será a **"Qtd. dias Manut. Histórico"**. Esse campo tem o valor padrão de 30 e sempre deverá ser maior do que 0 (zero).

 

**Seção Filtros**

Nessa seção você pode filtrar por:

- 

**Produtos: **Seleciona todos os produtos com USOPROD < > S, ou seja, se não for definido nenhum filtro, apenas os Serviços serão desprezados pelo agendador.

- 

**Estoque Disponível (Origem): **Será somado todo o estoque da Empresa de Origem para o Produto.

- 

**Estoque Necessário (Destino): **Será somado todo o estoque da Empresa de Destino para o Produto.

[[voltar ao topo]](#top)

## 
Aba Origem

![ressup_filiais5.png](https://ajuda.sankhya.com.br/hc/article_attachments/6198735355671)

No campo **"Empresa Origem"** você deve informar uma Empresa de Origem que esteja ativa na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) e possuir o campo **"Cód. Parceiro"** informado em seu [Cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas).

**Observação:** uma vez cadastrada como Empresa de Destino, a mesma não poderá ser configurada como Empresa de Origem, simultaneamente.

Defina se o **"Local Origem"** será:

- 

**A partir da maior disponibilidade: **Com essa opção, quando a soma das necessidades de todas as empresas for inferior ou igual à disponibilidade existente na Empresa de Origem, o sistema priorizará o consumo de saldo dos produtos no local com maior disponibilidade para atender as necessidades das Empresas de Destino.

- 

**A partir da menor disponibilidade: **Selecionando essa opção, quando a soma da necessidade de todas as empresas for inferior ou igual à disponibilidade existente na Empresa de Origem, o sistema irá priorizar o consumo de saldo dos produtos do local com menor disponibilidade para atender as necessidades das Empresas de Destino.

- 

**Fixo: **Aqui, quando a soma da necessidade de todas as empresas for inferior ou igual à disponibilidade existente na Empresa de Origem, o sistema consumirá o saldo do produto no local indicado para atender as necessidades das Empresas de Destino.

**Nota:** quando essa última opção for escolhida, será habilitado o campo **"Local"** logo abaixo do campo Local Origem.

Quando a marcação **"Considera Reservas?"** estiver realizada, o estoque reservado na Empresa Origem é descontado do Estoque Real — o agendamento passa a considerar apenas o Estoque Disponível para avaliar a disponibilidade na origem. Por exemplo, se a Empresa Origem tiver 100 unidades em estoque e 30 estiverem reservadas, a disponibilidade considerada será de 70 unidades. Se a marcação estiver desabilitada, o estoque reservado é ignorado e apenas o Estoque Real será observado.

No campo **"Modelo Mov. Origem"** podem ser utilizados os [modelos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos) que possuam TOP do Tipo de Movimento** "Pedido de Venda"** e que tenham um **"Tipo de Negociação"** informado. Aqui serão exibidos apenas os modelos cadastrados para a Empresa Origem preenchida e, caso não seja informada nenhuma, o campo de modelo ficará desabilitado para edição.

[[voltar ao topo]](#top)

## 
Aba Destino

![ressup_filiais6.png](https://ajuda.sankhya.com.br/hc/article_attachments/6198771229207)

No campo **"Empresa Destino"** você deve informar uma Empresa de Destino que esteja ativa na tela Preferências da Empresa e possuir o campo **"Cód. Parceiro"** informado em seu Cadastro.

**Observação:** não é possível que uma Empresa Origem seja cadastrada no campo Empresa Destino.

O campo **"Prioridade"** não é editável. Você conseguirá mudar a prioridade através do botão** "Ordenar Prioridade"**.

O campo **"Local Destino"** será habilitado quando o parâmetro **"Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL"** estiver ligado.

Ainda em relação ao Local Destino, o sistema seguirá a seguinte ordem para buscar o local:

**1°-** O local especificado nesta aba;

**2°-** O campo **"Local padrão"** definido na aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa) da tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113);

**3°-** Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo), no campo **"Local Padrão"**;

**4°-** No Cadastro de Produtos, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageral), no campo **"Local Padrão"**;

**5°-** Por último, o local informado no parâmetro** "Local Padrão para Pedidos e Notas - LOCALPADRAO"**.

Com a marcação** "Considera Reservas?"** realizada, o estoque reservado na Empresa Destino é tratado como indisponível para venda — o agendamento passa a considerar o Estoque Disponível, o que aumenta a necessidade calculada. Por exemplo, se a Empresa Destino tiver 80 unidades em estoque e 30 estiverem reservadas, a necessidade será calculada como se houvesse apenas 50 unidades disponíveis. Se a marcação estiver desmarcada, o estoque reservado é ignorado e apenas o Estoque Real será observado.

**Notas:**

- 

Quando a marcação acima estiver feita e o Tipo Ressuprimento for Estoque Mínimo, o sistema fará o cálculo: *Estoque do produto - Estoque reservado + Compra Pendente < Estoque Mínimo*.

- 

Quando a marcação acima estiver feita e o Tipo Ressuprimento for Estoque Máximo, o sistema fará o cálculo: *Estoque do produto - Estoque reservado + Compra Pendente < Estoque Máximo*.

No campo **"Modelo Mov. Destino"** podem ser utilizados os [modelos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos) que possuam TOP do Tipo de Movimento** "Pedido de Compra"** e que tenham um **"Tipo de Negociação"** informado.

O botão será habilitado quando a opção **"Gerar conforme prioridade"** do campo **"Estoque disponível menor que necessidade"** da aba [Configurações Gerais](#abaconfigura%C3%A7%C3%B5esgerais) estiver selecionada. Ao clicar nele, será exibido um pop-up para que você organize a prioridade conforme sua necessidade:

![ressup_filiais10.gif](https://ajuda.sankhya.com.br/hc/article_attachments/6201205470231)

[[voltar ao topo]](#top)

## 
Aba Sazonalidade

![ressup_filiais7.png](https://ajuda.sankhya.com.br/hc/article_attachments/6198805224471)

Informe a **"Dh. In. Execução"** e **"Dh. Fim Execução"**, bem como a **"Descrição"** da Sazonalidade. O campo **"% Acréscimo"** será habilitado quando a data de início estiver preenchida.

O % Acréscimo incidirá sobre a quantidade do produto, conforme configuração feita no campo **"Tipo Ressuprimento"** da aba [Configurações Gerais](#abaconfigura%C3%A7%C3%B5esgerais).

Aqui você pode cadastrar múltiplos períodos de sazonalidade porém, não será permitido que o mesmo período seja cadastrado em mais de um registro, nem haver sobreposição entre partes desses intervalos.

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16837427833495)

 Com essa aba preenchida, ao gerar os pedidos, o sistema irá acrescentar para cada produto filtrado, a quantidade referente ao cálculo *Xsazonal = X +X*Y%*, onde **"Xsazonal"** é a quantidade de ressuprimento necessário em período sazonal, **"X"** é a necessidade da empresa e** "Y%"** o acréscimo.

[[voltar ao topo]](#top)

## 
Aba Histórico

Nessa aba você visualizará o histórico e os detalhes das execuções da geração dos pedidos automáticos com as informações de **"Nro Execução"**, **"Dh. Ini. Execução"**, **"Dh. Fim Execução"**, **"Qtd. Docs. Saída"**, **"Qtd. Docs. Entrada"**, **"Qtd. Produtos Atendidos"**, **"Qtd. Produtos Não Atendidos"** e **"Erro"**.

![ressup_filiais8.png](https://ajuda.sankhya.com.br/hc/article_attachments/6198785051799)

**Observação:** quando um registro do histórico tiver ultrapassado a quantidade de dias de armazenamento, o sistema limpará esse registro do histórico e da base de dados.

O botão **"Ver Detalhes"** mostrará as informações dos **"Pedidos gerados"** e **"Produtos não atendidos"**:

![ressup_filiais11.gif](https://ajuda.sankhya.com.br/hc/article_attachments/6201424286359)

Na aba de Pedidos gerados e Produtos não atendidos serão exibidos todos os documentos gerados na execução que você selecionou, sendo possível acessar o documento nas Centrais de Compra ou Vendas (dependendo do Tipo de Movimento do documento gerado) caso você tenha acesso liberado à essas telas.

**Observação:** quando não houver estoque na Empresa de Origem, será lançada uma exceção de estoque insuficiente com os dados do primeiro produto encontrado com falta de estoque. Assim, os pedidos de compra e venda não serão concluídos e o histórico do ressuprimento, atualizado. Desse modo, a descrição será atualizada para todos os itens do pedido com as informações do motivo da impossibilidade de inclusão dos itens junto aos dados do produto retornado pela exceção.

O campo de **"Observações"** da aba Produtos não atendidos será preenchido com o motivo pelo qual o sistema não conseguiu atender o produto.

![acesse também FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/29127376357783)

 Caso a mensagem ***"Não foi possível gerar o pedido para o produto X, pois não há disponibilidade de estoque para o mesmo na empresa de origem"*** seja exibida, consulte este [artigo detalhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/29122338864151-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-pedido-para-o-produto-X-pois-n%C3%A3o-h%C3%A1-disponibilidade-de-estoque-para-o-mesmo-na-empresa-de-origem) para identificar as possíveis causas e soluções.

[[voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaestoque)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos)
- [Impostos/ Informações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#SubabaGeral)
- [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque)
- [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestoque)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas)
- [modelos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)
- [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa)
- [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageral)
- [artigo detalhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/29122338864151-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-pedido-para-o-produto-X-pois-n%C3%A3o-h%C3%A1-disponibilidade-de-estoque-para-o-mesmo-na-empresa-de-origem)