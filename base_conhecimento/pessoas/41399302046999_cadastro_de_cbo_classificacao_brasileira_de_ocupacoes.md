# Cadastro de CBO (Classificação Brasileira de Ocupações)

> **Módulo:** Pessoas+ | **Subseção:** Estrutura da Empresa  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es](https://ajuda.sankhya.com.br/hc/pt-br/articles/41399302046999-Cadastro-de-CBO-Classifica%C3%A7%C3%A3o-Brasileira-de-Ocupa%C3%A7%C3%B5es)  
> **ID:** `41399302046999` | **Última Atualização:** 2026-07-29T16:04:36Z

---

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.CBO

### **Sumário**

[Descrição e Usabilidade](#h_01KVQVT9ZNJ8E8Q2CYE0DGT19B)

[1. Descrição da Funcionalidade](#h_01KVQVM8D5F02XZD3KWP60ATVX)
[2. Pré-requisitos](#h_01KVQVM8D6MTDRM8B35TTS335F)
[3. Jornada de Uso](#h_01KVQVM8D87STEDHAF7RYMDAZH)
[4. Ponto de Atenção](#h_01KVQVM8DJGHQ82H7K3CPSM1CG)
[5. Dicas de Usabilidade](#h_01KVQVM8DK3FG7E2CPN4B1VP5W)

[Perguntas Frequentes (FAQ)](#h_01KVQVM8DQ3M2S15E7PWD0RAPC)
[Artigos Relacionados](#h_01KVQVM8DVTFQ5NJ7VG0NRGNCG)

 

## **Descrição e Usabilidade**

A **Classificação Brasileira de Ocupações (CBO)** é o instrumento oficial utilizado pelo Governo Federal para identificar e padronizar as ocupações exercidas pelos trabalhadores no mercado de trabalho brasileiro.

No Pessoal+, o cadastro de CBO é utilizado para classificar corretamente os cargos e funções existentes na empresa, garantindo consistência nas informações trabalhistas, previdenciárias e nas obrigações enviadas ao eSocial.

Esse cadastro auxilia na organização da estrutura de cargos da empresa e contribui para a conformidade das informações prestadas aos órgãos fiscalizadores.

 

### **1. Descrição da Funcionalidade**

A rotina de Cadastro de CBO permite registrar os códigos oficiais da Classificação Brasileira de Ocupações utilizados pela empresa.

Cada CBO possui um código e uma descrição que identificam uma ocupação específica conforme a tabela oficial disponibilizada pelo Ministério do Trabalho.

Após o cadastro, a CBO poderá ser vinculada aos cargos ou diretamente aos colaboradores, conforme a configuração adotada pela empresa.

Além disso, o cadastro permite definir o tipo de horário noturno aplicável à ocupação, informação utilizada em cálculos relacionados ao adicional noturno.

 

### **2. Pré-requisitos**

Antes de realizar o cadastro, verifique:

- Acesso liberado à rotina **CBO** (Pessoal+ > Cadastros. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

- Código da ocupação disponível na [Tabela Oficial da Classificação Brasileira de Ocupações](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/cbo);

- Definição prévia da estrutura de cargos utilizada pela empresa.

 

### **3. Jornada de Uso**

 

![CBO.png](https://ajuda.sankhya.com.br/hc/article_attachments/41400748699927)

#### 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315091891095)

 **Cadastrar uma CBO**

1. Acesse a tela **CBO** (Pessoal+ > Cadastros);

1. Clique em **Cadastrar CBO** (Código Brasileiro de Ocupação);

1. Preencha os campos:

  - 

**Código**

Informe o código da ocupação conforme a tabela oficial da CBO.

O campo aceita até seis dígitos.

  - 

**Descrição**

Informe a descrição correspondente à ocupação cadastrada.

****

| ℹ️ Nota Recomenda-se utilizar a nomenclatura oficial da Classificação Brasileira de Ocupações para facilitar integrações e conferências futuras. |
| --- |

#### 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315091892119)

 **Configurar o Tipo do Horário Noturno**

1. 

Na aba **Geral**, o campo **Tipo do Horário Noturno **determina qual regra será utilizada para cálculo do adicional noturno dos trabalhadores vinculados à ocupação.

As opções disponíveis são:

- 
**Urbano**: utilizado para trabalhadores urbanos;

- 
**Rural (Lavoura)**: utilizado para trabalhadores rurais que atuam em atividades agrícolas;

- 

**Rural (Pecuária)**: utilizado para trabalhadores rurais que atuam em atividades pecuárias.

****

| 🚨 Risco operacional A escolha incorreta pode impactar o cálculo do adicional noturno realizado pelo sistema. |
| --- |

#### 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315102477591)

 **Salvar o Cadastro**

1. 

Após preencher todas as informações necessárias, clique em **Salvar [F7]**.

O cadastro ficará disponível para utilização nos demais processos do sistema.

Por padrão, a CBO costuma ser vinculada ao cadastro de **Cargos**, que funciona como agrupador das funções da empresa.

Caso seja necessário alterar esse comportamento, utilize o parâmetro **Onde Utiliza o CBO? - FPUTILIZACBO. **Esse parâmetro permite definir em qual cadastro a informação da CBO será utilizada dentro do sistema.

********

| ⚠️ Atenção Alterações nesse parâmetro podem impactar a forma de manutenção das informações funcionais dos colaboradores. |
| --- |

 

### **4. Pontos de Atenção**

- A CBO deve corresponder à ocupação efetivamente exercida pelo trabalhador.

- O código informado deve existir na tabela oficial da Classificação Brasileira de Ocupações.

- O tipo de horário noturno influencia diretamente os cálculos relacionados ao adicional noturno.

- Alterações na CBO podem impactar integrações trabalhistas e informações enviadas ao eSocial.

 

### **5. Dicas de Usabilidade**

- Mantenha os códigos de CBO atualizados conforme a tabela oficial vigente.

- Utilize a descrição oficial da ocupação para facilitar consultas e auditorias.

- Revise periodicamente os cargos vinculados às CBOs cadastradas.

- Valide o tipo de horário noturno antes da utilização em cálculos de folha.

 

## **Perguntas Frequentes (FAQ)**

**1. O cadastro de CBO é obrigatório?**

Sim. A informação da CBO é utilizada em diversas obrigações trabalhistas e previdenciárias, incluindo eventos enviados ao eSocial.

**2. Onde encontro o código correto da CBO?**

O código deve ser consultado na tabela oficial da Classificação Brasileira de Ocupações disponibilizada pelos órgãos governamentais.

**3. Posso criar um código de CBO que não existe na tabela oficial?**

Não é recomendado. O cadastro deve seguir os códigos oficiais para evitar inconsistências em obrigações legais e integrações.

**4. Qual a relação entre CBO e Cargo?**

Normalmente a CBO é vinculada ao Cargo, permitindo que todos os colaboradores daquele cargo utilizem a mesma classificação ocupacional.

**5. Quando devo utilizar Horário Noturno Rural?**

Quando a ocupação estiver relacionada a atividades rurais de lavoura ou pecuária e estiver sujeita às regras específicas de adicional noturno previstas na legislação.

**6. Alterar a CBO afeta cálculos já realizados?**

A alteração impactará os processos futuros. Caso existam obrigações já enviadas ou cálculos já processados, recomenda-se avaliar a necessidade de recálculo ou retificação.

 

## **Artigos Relacionados**

- [Cadastro de Cargos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41423883668119)

- [Cadastro de Funções](https://ajuda.sankhya.com.br/hc/pt-br/articles/41401796198679)

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)


---

### 🔗 Links e Referências Internas:

- [Cadastro de Cargos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41423883668119)
- [Cadastro de Funções](https://ajuda.sankhya.com.br/hc/pt-br/articles/41401796198679)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)