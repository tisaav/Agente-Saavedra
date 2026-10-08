# Sugestão de Local por Empresa

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111993-Sugest%C3%A3o-de-Local-por-Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111993-Sugest%C3%A3o-de-Local-por-Empresa)  
> **ID:** `360045111993` | **Última Atualização:** 2026-07-29T13:58:37Z

---

Na inclusão de itens em uma nota, o sistema pode sugerir o local padrão para cada empresa, dessa forma, o processo de inserção nas notas pode ser agilizado e menos erros referente às informações de locais nas notas podem ser evitados.

Além das configurações básicas de controle de local, efetue os seguintes ajustes:

1. Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), realize a habilitação da marcação **"Sugerir local padrão do parceiro?"**;

1. Depois, nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo) preencha o campo** "Local Padrão" **com o local que você deseja que seja sugerido no lançamento do item na nota.

1. Por fim, informe um local padrão para os produtos, através do campo **"Local padrão para produtos"**, da aba [Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao), na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros).

Assim, ao inserir um produto no item da nota nas Centrais, o sistema irá sugerir o local conforme configurado. Neste caso, as seguintes validações serão realizadas:

- O sistema irá verificar se nas Preferências da Empresa existe um local padrão informado. Caso haja, irá sugeri-lo, sendo que, você poderá mudá-lo se quiser.

- Se  não existir local padrão definido, ou seja, estiver informado zero, o sistema irá fazer as demais validações já existentes no sistema que sugerem o local na inclusão do item.

É importante ressaltarmos que a configuração nas Preferências da Empresa é soberana em relação às outras existentes, dessa forma, caso exista um local diferente de zero informado nela, o sistema sempre irá sugerir aquele local na inclusão do item, mesmo que o primeiro e segundo itens sejam o segundo item e o item anterior tenha sido confirmado com um local diferente e o parâmetro **"Repete último local digitado? - REPETELOCALANT" **esteja ligado.

**Regras utilizadas para sugerir o local ao incluir o item**

Se o Local de Origem for igual a zero e a marcação **"Sugerir local padrão do parceiro?"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)) não estiver habilitada, então o sistema irá buscar pelo campo **"Local Padrão"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893). 

Caso a marcação Sugerir local padrão do parceiro? esteja habilitada, o sistema terá o seguinte comportamento:

- Se a nota for de Venda:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458079782807)

 Caso você informe no campo **"Parceiro Remetente"** um valor maior que zero, o sistema irá buscar o local padrão configurado para este parceiro (campo **"Local padrão para produtos"**, aba [Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abainformaes),** **tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)).
 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458079782807)

 Se você informar zero no campo Parceiro remetente do cabeçalho da nota, ou seja, não utilizá-lo, então o sistema fará a validação normal para o local informado nas Preferências da Empresa.

**Observação:** as movimentações internas terão as mesmas validações do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654).

**Nota:**  a marcação Sugerir local padrão do parceiro? do cadastro da TOP não é soberana em relação as outras configurações. Para a obtenção do local na inserção de itens na venda, o sistema seguirá a ordem hierárquica abaixo, sendo que, caso exista um local indicado em uma determinada tela e o mesmo for diferente de zero, este local será utilizado. Observe:

1. Será verificado inicialmente, se o campo **"Local Padrão"**, da aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa), do [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) foi preenchido para a empresa do cabeçalho.

1. Não obtendo a informação na tela acima, o sistema irá procurar o local preenchido no campo **"Local Padrão"**, da aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo) nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

1. Em seguida, caso o parâmetro **"Repete último local digitado?- REPETELOCALANT"** esteja habilitado, o sistema irá verificar o local do item lançado anteriormente.

1. Após isso, caso a opção **"Sugerir local padrão do parceiro?"**, da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) do [Cadastro do Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizada no lançamento, esteja marcada e exista informação no campo **"Parceiro Remetente"** do lançamento, o sistema irá procurar o local do parceiro remetente.

1. Caso não exista local definido na tela acima, o sistema buscará no [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113).

1. Não existindo, será verificado se possui local determinado no parâmetro **"Local Padrão para Pedidos e Notas- LOCALPADRAO"**, lembrando que esse parâmetro é por usuário.

1. Por fim, se o parâmetro **"Informa menor local de armazenagem com estoque- INFMINLOC"** estiver ligado o sistema buscará na tabela de estoque (TGFEST) o menor local com estoque para esse produto, obedecendo às restrições para local da TOP e a informação do parâmetro **"Filtro de empresas/local de estoque- FILEMPLOCALEST"**.

- Se a nota for de Compra:

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28458079782807)

 Caso você informe no local padrão do parceiro (campo Local padrão para produtos, aba Informações,** **tela Cadastro de Parceiros), um valor maior que zero, o sistema irá buscar o local padrão configurado para este parceiro. Se estiver igual a zero, o sistema irá buscar o local informado nas Preferências da Empresa.

Temos ainda, as seguintes validações com os parâmetros referentes ao Local que o sistema já faz e que podem interferir nesta funcionalidade:

1. Se o **"Local Origem"** for igual a zero (isso pode acontecer, por exemplo, quando se utiliza uma empresa que não tem local padrão informado e nenhuma das demais regras do sistema para uso de local seja válida para este produto, o que faz com que o mesmo fique sem local de origem), e o parâmetro **"Repete último local digitado?- REPETELOCALANT"** estiver ligado, o sistema irá pegar o Local de origem digitado no item anterior (válido a partir do segundo item lançado).

1. Caso o Local Origem for igual a zero, o sistema irá buscar o Local padrão cadastrado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral), campo **"Local Padrão"** do [Cadastro de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113). Se este campo também for zero, o sistema buscará o local informado no parâmetro **"Local Padrão para Pedidos e Notas por usuário- LOCALPADRAO"**.

1. Se o Local de origem for igual a zero e o parâmetro **"Informa menor local de armazenagem com estoque-INFMINLOC"** estiver ligado, o sistema buscará o menor local com estoque.

1. Caso a empresa do item ou do cabeçalho da nota seja alterado, apenas a seguinte validação será analisada: Se o local de origem for igual a zero e o campo **"Sugerir local padrão do parceiro?"**, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) estiver desmarcado, o sistema irá buscar o campo **"Local padrão"** das Preferências da Empresa.

1. O parâmetro **"Utiliza a coluna Local para controlar o estoque-UTILIZALOCAL"** também pode influenciar nesta rotina.

[[Voltar ao topo]](#top)


---

### 🔗 Links e Referências Internas:

- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)
- [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo)
- [Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao)
- [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)
- [Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abainformaes)
- [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)
- [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa)
- [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos)
- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Cadastro do Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)
- [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral)