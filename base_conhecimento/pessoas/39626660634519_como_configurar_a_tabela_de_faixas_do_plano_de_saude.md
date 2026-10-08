# Como configurar a tabela de faixas do plano de saúde?

> **Módulo:** Pessoas+ | **Subseção:** Plano de Saúde  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519-Como-configurar-a-tabela-de-faixas-do-plano-de-sa%C3%BAde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519-Como-configurar-a-tabela-de-faixas-do-plano-de-sa%C3%BAde)  
> **ID:** `39626660634519` | **Última Atualização:** 2026-09-27T18:36:10Z

---

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.TabelaDeFaixa

 

## **Descrição e Usabilidade**

Utilize a **Tabela de Faixas** quando o valor do [plano de saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527-Cadastro-e-V%C3%ADnculo-de-Plano-de-Sa%C3%BAde#h_01KMJR7YQ3R89C7A962WQHRT5R) variar conforme critérios definidos pela operadora ou pela política interna da empresa, como:

- idade;

- faixa salarial;

- categoria do colaborador;

- percentual por dependente.

Essa configuração permite que o valor seja calculado automaticamente no vínculo do plano de saúde do titular e dos dependentes, garantindo mais precisão no desconto em folha.

**⚠️** **Quando usar este artigo:** sempre que o plano não possuir valor fixo.

 

### **1. Pré-requisitos**

Antes de configurar, confirme:

- Acesso liberado à tela **Tabela de Faixas**, concedido pelo usuário administrador do sistema por meio da rotina **Acessos** (Configurações > Controle de Acessos);

- 
[Plano de saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527-Cadastro-e-V%C3%ADnculo-de-Plano-de-Sa%C3%BAde#h_01KMJR7YQ3R89C7A962WQHRT5R) já cadastrado;

- Evento de Plano de Saúde cadastrado;

- Regra comercial da operadora definida;

- Valores por faixa em mãos;

- Tipo de tabela definido para uso do benefício.

 

### **2. Jornada de Uso**

 

#### 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315038344471)

 **Criar a tabela**

![CADASTRO-TABELA-PLANOSAUDE.gif](https://ajuda.sankhya.com.br/hc/article_attachments/39627420999191)

1. 

Acesse a tela **Tabelas de Faixas (Pessoal+ > Cadastros)**.

1. 

Clique em **Adicionar Tabela**.

1. 

Preencha:

  - 

**Descrição da faixa:** ex. *Unimed Empresarial 2026;*

  - 

**Referência:** mês inicial da vigência;

  - 

**Tipo de Tabela:** código da regra usada no plano.

1. 

Clique em Confirmar.

#### 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315038345623)

 **Montar as faixas**

![CADASTROlinha-TABELA-PLANOSAUDE.gif](https://ajuda.sankhya.com.br/hc/article_attachments/39627943466519)

Agora, cadastre as linhas da tabela.

1. 

Para cada faixa, informe:

  - 

**Limite da Faixa**;

  - 

**Valor 1.**

1. 

Clique em **Adicionar nova faixa** para inserir novas linhas. 

1. 

Após preencher cada linha, clique em **Finalizar Edição** para salvar.

**Exemplo por idade**

| Limite da Faixa | Valor |
| --- | --- |
| 18 | 120,00 |
| 23 | 150,00 |
| 28 | 185,00 |
| 33 | 230,00 |
| 38 | 290,00 |

**Exemplo por salário**

| Limite da Faixa | Valor |
| --- | --- |
| 2.000,00 | 80,00 |
| 4.000,00 | 120,00 |
| 6.000,00 | 180,00 |

####  

#### 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315065547159)

 **Replicar para próximas competências**

![deplicarref-TABELA-PLANOSAUDE.gif](https://ajuda.sankhya.com.br/hc/article_attachments/39628174914583)

Se a operadora mantiver o mesmo valor por vários meses:

1. Abra a tabela;

1. Clique em **Replicar para outras referências**;

1. Informe o **período inicial** e **final**;

1. Clique em **Duplicar valores**.

Esse processo evita retrabalho mensal e garante continuidade da regra nas próximas competências.

 

#### 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315038346519)

 **Vincular a Tabela ao cadastro do colaborador ou dependente**

Depois da tabela criada, retorne ao vínculo do plano de saúde do colaborador ou dependente e preencha o campo **Tabela de Faixa** com o código cadastrado.

![tabelafaixa-planosaudefunc.png](https://ajuda.sankhya.com.br/hc/article_attachments/39651754818839)

 

#### 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315065549847)

 **Configurar Fórmula no Evento correspondente ao Plano de Saúde**

Configure uma **fórmula **que considere a **tabela de faixas** cadastrada e vincule essa fórmula ao** evento** correspondente ao plano de saúde.

Essa etapa é fundamental para que o sistema busque o valor correto durante o cálculo da folha.

![formulaeventotabeladefaixa-planode saude.png](https://ajuda.sankhya.com.br/hc/article_attachments/39651707159191)

 

#### **

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315038350231)

 Lançar evento de Plano de Saúde no Movimento do colaborador/dependente**

Na tela **Lançamento de Movimento** (Pessoal+ > Rotinas Folha), realize o [lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319) do **Evento** correspondente ao ao plano de saúde na referência desejada para o colaborador ou dependente.

![lançmovplanodesaude.png](https://ajuda.sankhya.com.br/hc/article_attachments/39651707159319)

 

#### 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315038351767)

 **Calcular a folha do colaborador**

Após concluir as configurações:

1. calcule a folha do colaborador;

1. valide o valor do desconto do plano de saúde;

1. confira se a faixa aplicada corresponde ao valor esperado.

![calculoplanosaudecomtabelafaixa.gif](https://ajuda.sankhya.com.br/hc/article_attachments/39652341403671)

 

### **4. Pontos de Atenção**

- A referência deve acompanhar a competência da folha.

- Alterações impactam somente referências futuras.

- Mudança com folha calculada exige recálculo.

- Faixa salarial incorreta gera desconto incorreto.

- Use nomes claros para facilitar manutenção.

 

## **Perguntas Frequentes (FAQ)**

**1. Posso usar a mesma tabela para titular e dependente?**

Sim. Desde que a regra comercial seja a mesma.

**2. Preciso criar uma tabela nova todo mês?**

Somente se houver alteração de valores.

Se permanecer igual, utilize  a funcionalidade de **Replicar para outras referências**. 

**3. O valor não carregou no vínculo. O que pode ser?**

Valide:

- referência da tabela;

- código da faixa;

- faixa salarial;

- tipo da tabela;

- vigência do plano.

## **Artigos Relacionados**

- [Cadastro e Vínculo de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)

- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)

- [Reprocessamento de Plano de Saúde para Funcionários e Dependentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079)

- [Valores de Plano de Saúde na DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/28555465280663)

- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)


---

### 🔗 Links e Referências Internas:

- [plano de saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527-Cadastro-e-V%C3%ADnculo-de-Plano-de-Sa%C3%BAde#h_01KMJR7YQ3R89C7A962WQHRT5R)
- [lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319)
- [Cadastro e Vínculo de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Reprocessamento de Plano de Saúde para Funcionários e Dependentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079)
- [Valores de Plano de Saúde na DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/28555465280663)
- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)