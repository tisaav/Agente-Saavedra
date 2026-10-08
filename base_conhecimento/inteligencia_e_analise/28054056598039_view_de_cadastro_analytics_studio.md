# VIEW de Cadastro - Analytics Studio

> **Módulo:** Inteligência e Análise | **Subseção:** Dados e conexões  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/28054056598039-VIEW-de-Cadastro-Analytics-Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/28054056598039-VIEW-de-Cadastro-Analytics-Studio)  
> **ID:** `28054056598039` | **Última Atualização:** 2026-09-23T17:04:14Z

---

Dentro dos componentes do [Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231), a **"VIEW de Cadastro"** é uma das duas maneiras no-code de definir os dados que preencherão os [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio#Componentes). Ao contrário da [VIEW de Análise de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/28045340825239), que exige a configuração manual dos dados e agrupadores, a VIEW de Cadastro já organiza tudo automaticamente a partir do cadastro selecionado. Isso facilita a criação de tabelas perfeitas para operações de CRUD (Create, Read, Update, Delete), pois todos os atributos do cadastro já são gerados como dados, prontos para visualização e edição.

### **Estrutura da VIEW de Cadastro**

A estrutura da VIEW de Cadastro é similar à VIEW de Análise de Dados, mas o diferencial é que ela se baseia em um cadastro específico para organizar os dados automaticamente.

- **Cadastro**: a primeira etapa ao configurar a VIEW de Cadastro é selecionar um cadastro (entidade). Por exemplo, se selecionar o [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), o Analytics AI organiza todos os atributos desse cadastro como colunas (dados) e define o cadastro como o agrupador.

- **Agrupador**: o cadastro selecionado (ex.: Parceiros) se torna o agrupador principal, que organiza os dados.

- **Dados**: todos os atributos do cadastro (FKs, texto, numérico, data) são automaticamente configurados como colunas da tabela.

### **Conteúdos comuns à VIEW de Análise de dados**

Os **"Dados"** na VIEW de Cadastro seguem a mesma estrutura da VIEW de Análise de Dados, podendo ser do tipo **"Atributo"** ou **"Função"**.

#### **

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309629301527)

 Atributo**

Os atributos extraídos do cadastro são automaticamente inseridos como Dados, podendo ser:

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28054618771479)

****Atributo normal**

Os atributos numéricos, textuais e de data são gerados diretamente a partir do cadastro e extraídos do banco de dados.

As principais funcionalidades incluem:

- **Função de Agregação**: escolher como o dado será agregado (soma, média, contagem).

- **Entrada de Dados**: permitir que o usuário insira ou edite valores diretamente nas células da tabela. Para mais informações, acesse a documentação **"Entrada de Dados"**.

- **Offset**: usar esta opção para comparar dados de períodos diferentes, como vendas do mês atual com as do ano anterior.

- **Filtros Adicionais**: aplicar filtros diretamente no dado. Por exemplo: para ver vendas de diferentes curvas em colunas diferentes. Como demonstrado a seguir, na primeira coluna, ver vendas da 'Curva A', na segunda coluna, 'Curva B' e na terceira coluna, 'Curva C'.

- **Formatação Condicional**: em tabelas, pode-se aplicar formatação condicional com base nos valores das células.

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28054618771479)

****Atributo FK**

Os **"Atributos FK"** também são gerados automaticamente, permitindo que visualize os relacionamentos da entidade do cadastro com outros cadastros, exibindo FKs como colunas. Por exemplo, ao selecionar o cadastro de **"Vendedores"**, pode-se trazer o **"Gerente de Vendas"** relacionado.

- **Relacionamento com Agrupador**: o atributo FK só pode ser utilizado quando relacionado a um agrupador, como descrito.

- **Entrada de Dados com FK**: é possível alterar o relacionamento diretamente na VIEW, como mudar o Gerente de Vendas de um Vendedor. Para mais informações, acesse a documentação Entrada de Dados.

Outro uso interessante do atributo FK é quando desejar utilizar a descrição ou o código do agrupador em funções específicas. Por exemplo, suponha que queira criar uma função onde todos os vendedores com ID menor que 3 sejam classificados como 2, e aqueles com ID maior que 3 sejam classificados como 1. Para isso, notará que o atributo Função não consegue acessar diretamente os valores que estão no agrupador, pois ele só trabalha com os dados da VIEW. Nesse caso, pode-se trazer o ID ou a descrição do agrupador como um Atributo FK, e assim usá-lo dentro da função para definir os critérios que desejar.

Esse critério pode ser usado, por exemplo, em um filtro de coluna ou até ser exibido diretamente ao usuário como um valor calculado dentro da tabela.

#### 
**

![Marcador 1 FINAL.png.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309629301527)

 ****Função**

A **"Função"** na VIEW de Cadastro funciona da mesma maneira que na VIEW de Análise de Dados, permitindo cálculos e manipulações diretas com os dados.

- **Expressões Matemáticas**: exemplo: A / B, onde A são as vendas e B é a quantidade de vendas.

- **Concatenação**: utilize o operador de adição (+) para concatenar valores e strings. Exemplo: A + 'é maior que' + B.

- **If Condicional**: estrutura condicional: A > 100 ? 1 : 0.

- **JavaScript**: permite manipulações avançadas, como funções de arredondamento, comparação e cálculos dinâmicos.

- **Função _old**: permite comparar o valor atual de um dado com o valor da linha anterior.

### **Agrupadores**

O **"Agrupador"** na VIEW de Cadastro é o cadastro selecionado. Pode-se definir como os dados relacionados serão exibidos:

- **Descrição **(padrão);

- **Código**;

- **Ambos **(código seguido da descrição).

### **Filtros**

A VIEW de Cadastro também permite a aplicação de filtros:

- **Filtros da Tela**: a VIEW respeita automaticamente os filtros aplicados na tela;

- **Filtros Adicionais**: adicione filtros específicos dentro da própria VIEW;

- **Filtro por Coluna**: permite filtrar valores específicos de colunas.

### **Ordenação**

A ordenação dos dados na VIEW de Cadastro pode ser definida:

- **Ordenação por Dado**: exemplo, ordenar os parceiros pela mensalidade, de forma decrescente.

- **Ordenação por Agrupador**: ordene os parceiros em ordem alfabética, ou por qualquer atributo relacionado.

### **Limite de registros**

A VIEW de Cadastro permite limitar o número de registros retornados.


---

### 🔗 Links e Referências Internas:

- [Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231)
- [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio#Componentes)
- [VIEW de Análise de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/28045340825239)
- [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)