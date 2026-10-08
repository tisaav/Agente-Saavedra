# Como calcular a diferença de reajuste da convenção coletiva?

> **Módulo:** Pessoas+ | **Subseção:** Reajustes Salariais e Dissídio  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/40242689587095-Como-calcular-a-diferen%C3%A7a-de-reajuste-da-conven%C3%A7%C3%A3o-coletiva](https://ajuda.sankhya.com.br/hc/pt-br/articles/40242689587095-Como-calcular-a-diferen%C3%A7a-de-reajuste-da-conven%C3%A7%C3%A3o-coletiva)  
> **ID:** `40242689587095` | **Última Atualização:** 2026-09-27T17:49:56Z

---

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:** br.com.sankhya.rh.ReajusteSalarial

 

### **Descrição e Usabilidade**

A rotina de **Reajuste Salarial** permite atualizar o salário dos colaboradores de forma individual ou coletiva, com base em diferenças definidas em:

- Convenção Coletiva (CCT);

- Acordo coletivo;

- Reajustes internos (não sindicais).

No caso de **diferença de Convenção Coletiva**, o sistema aplica automaticamente:

- Percentual ou valor definido na CCT;

- Regras de arredondamento;

- Validações do sindicato;

- Integração com o eSocial;

- Geração de diferenças para folha de dissídio.

 

### **Pré-requisitos**

Antes de realizar o reajuste, verifique:

- Cadastro do **Sindicato** com a **Convenção Coletiva** preenchida;

- Datas corretas de **data-base** e **data de assinatura**;

- Parâmetros da CCT (percentual, piso, teto);

- 

Configuração de **RRA (Rendimentos Recebidos Acumuladamente)**, quando houver pagamento retroativo.

📚 Para cenários com diferenças de anos anteriores, consulte o artigo: ****[Rendimentos Recebidos Acumuladamente (RRA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319).

 

### **Jornada de Uso**

 

![reajustesindicalcct.gif](https://ajuda.sankhya.com.br/hc/article_attachments/40249476781079)

1. Acesse a tela **Reajuste Salarial **(Pessoal+ > Rotinas Folha);

1. Clique no *card** *****Lançar reajuste** e informe:

  - 
**Empresa**;

  - 
**Mês referência** (mês em que o reajuste será aplicado);

1. Marque **Realiza reajuste sindical?** = Sim;

1. Informe o **Sindicato **correspondente;

1. Selecione a **Convenção Coletiva**;

1. 

Configure as opções conforme a CCT:

  - 
**Aplicar reajuste para demitidos entre data-base e assinatura** (quando aplicável);

  - 

**Considera projeção do aviso prévio indenizado dentro do mês data-base**.

Quando essa opção estiver marcada, colaboradores demitidos podem ser considerados no reajuste, caso tenham projeção de aviso dentro do período.

1. O **Tipo de Arredondamento** de valores para os colaboradores mensalistas e horistas/diaristas é preenchido automaticamente conforme a regra de cálculo para a empresa;

1. Preencha **Qual salário mínimo da classe?**;

1. Clique em **Selecionar funcionários;**

1. Escolha os colaboradores que receberão o reajuste clicando no cards ou marcando todos;

1. Clique em **Conferir Reajuste**;

1. Revise os valores apresentados;

1. Clique em **Efetivar**;

1. Após a aplicação, realize o **cálculo da folha de dissídio**.

********

****

****

********

| ⚠️Readequação ao piso sindical Ao selecionar Readequar o salário dos colaboradores admitidos após a data-base ao piso do sindicato?, o sistema vai filtrar apenas os colaboradores admitidos depois da data-base e ajustar automaticamente os salários que estiverem abaixo do piso definido. Se o reajuste sindical incluir a readequação do salário de colaboradores admitidos até a data-base, é preciso preencher o campo Qual salário mínimo da classe? com o valor do reajuste desejado, desde que seja maior que o salário atual do colaborador. Para que o sistema possa calcular o reajuste salarial de todos os colaboradores admitidos após a data-base, é necessário informar o campo Ref. Salario Base (na tela Sindicato > aba Convenção coletiva, Acordo coletivo ou Sentença Normativa) com o mês anterior à assinatura da convenção. Por exemplo, se a assinatura ocorrer em 05/2025, o campo Ref. Salario Base deve ser preenchido com 04/2025. |
| --- |

 

### **Pontos de Atenção**

- Reajustes retroativos podem gerar RRA.

- A sequência de reajustes deve ser respeitada.

- O campo **Ref. Salário Base** impacta diretamente o cálculo.

- Colaboradores demitidos podem entrar no cálculo (dependendo da configuração).

- O eSocial exige a data correta da alteração.

 

### **Perguntas Frequentes (FAQ)**

**1. Posso fazer reajuste sem sindicato?**

Sim, utilizando a opção **Não** em reajuste sindical.

**2. O reajuste altera folhas já calculadas?**

Não automaticamente. É necessário recalcular a folha.

**3. Colaboradores demitidos entram no reajuste?**

Depende das opções marcadas (aviso prévio e período).

**4. Quando o RRA é gerado?**

Quando há pagamento de diferenças de anos anteriores.

**5. Posso aplicar reajuste em etapas?**

Sim, desde que respeite a sequência definida pela CCT.

 

### **Artigos Relacionados**

- [Rendimentos Recebidos Acumuladamente (RRA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319)

- [Cadastro de Sindicato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953)

- Cálculo de Folha

- Gerenciador de Folhas


---

### 🔗 Links e Referências Internas:

- [Rendimentos Recebidos Acumuladamente (RRA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319)
- [Cadastro de Sindicato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953)