# Como configurar a desoneração da folha?

> **Módulo:** Pessoas+ | **Subseção:** Tributação da folha  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14355845772311-Como-configurar-a-desonera%C3%A7%C3%A3o-da-folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/14355845772311-Como-configurar-a-desonera%C3%A7%C3%A3o-da-folha)  
> **ID:** `14355845772311` | **Última Atualização:** 2026-09-27T14:22:11Z

---

****

| Através da Lei 12.546/2011 foi instituída a denominada "Desoneração da Folha de Pagamento", que substitui parte das contribuições previdenciárias da folha de salários pela receita bruta ajustada. A partir de 01/12/2015, por força da Lei 13.161/2015, a aplicação da desoneração é facultativa, ou seja, o contribuinte pode escolher qual forma de tributar a folha é mais interessante, se pela forma tradicional (contribuição sobre a folha de pagamento) ou se pela forma desonerada (contribuição sobre a receita). |
| --- |

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450632966295)

 Para tal, seguem as principais configurações:

 

### **

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315105280919)

 Avançado » Registro Fiscal:**

Ao acessar a tela do **"Registro Fiscal"** tem-se os dados referentes aos requisitos para atender a Lei de no 12.546/2011, especificamente no grupo “Desoneração da folha”.

 

![1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16859869846551)

 

#### **1.1. Grupo ‘Normal’:**

O Grupo ‘Normal’ apresenta os campos **"Percentual da Receita Bruta para INSS"** que retornará com o percentual reduzido, facilitando a conferência com as Bases do Resumo da Folha.

O processo de 'Desoneração da Folha' não tem ligação direta com o campo 'Percentual de INSS', o cálculo para os valores relacionados ao 'Percentual da Receita Bruta para INSS' atua com um determinado cálculo e o campo 'Percentual de INSS' opera com outro conforme a seguir:

- ****

| ((20 * (100 - x)) / 100) , sendo X o valor do percentual da desoneração |
| --- |

 

**Exemplo Prático:**

- 

| 20 * (100 - 18) / 100 = 16,4 (valor levado para o campo "Percentual de INSS") |
| --- |

 

Valor do INSS da Receita Bruta: deverá ser alimentado manualmente, pelos usuários, com um valor correspondente ao percentual que lhe couber sobre o valor da Receita Bruta, oriunda das atividades que se enquadram nas regras da Lei 12.546/2011.

 

#### **1.2. Grupo '13º Salário’:**

No Grupo "13º Salário" temos o campo Percentual da Receita Bruta para INSS utilizado para que o usuário insira o percentual da ‘Receita Bruta’ manualmente. O valor informado será utilizado para deduzir o percentual de 20% informado no campo **"Percentual de INSS"**.

Percentual de INSS: será alimentado automaticamente, com o valor de 20% reduzido, conforme o valor inserido no campo ‘Percentual da Receita Bruta para INSS’. Essa redução será conforme é realizado na’ Folha Normal’.

O usuário precisa, primeiramente, apurar o quanto a ‘Receita Desonerada’ representa sobre a ‘Receita Total’. O que será inserido no campo 'Percentual Receita Bruta para INSS' é a diferença entre o ‘Percentual total’ e o ‘Percentual extraído’ da razão citada. Uma vez inserido, ele irá reduzir o percentual aplicado sobre o valor original, informado no campo 'Percentual de INSS'.

 

#### **1.3. Indicativo de substituição da Contribuição Previdenciária Patronal:**

Nesse campo deve-se informar se a empresa é:

- 

1-Totalmente substituída ou

- 

2-Parcialmente substituída

O indicativo e o percentual da contribuição patronal a serem aplicados sobre as remunerações pagas, devidas ou creditadas, para os contribuintes enquadrados nos artigos 7º a 9º da Lei no 12.546/2011, conforme classificação tributária indicada no evento de Informações Cadastrais do empregador/contribuinte, serão enviados para o eSocial, através do evento ‘S-1280 Informações Complementares aos Eventos Periódicos’.

 

### **

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315094899095)

 Tela Arquivos » Empresas:**

Na tela da** "Empresa"**, do Pessoal, na aba **"Informações Fiscais"**, tem-se o campo **“Indicativo de Desoneração da Folha”** que determina o tipo de desoneração de folha para ser enviado ao E-Social.

 

### **

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315094899863)

 Emissão do Resumo da folha:**

Ao emitir o resumo da folha, o campo **"Parte da Empresa"** deverá estar igual ao do Registro Fiscal, no campo “Valor do INSS Receita Bruta”.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14392880852631)

 

Repare que foi considerado o percentual parte empresa de 16,4% sobre a Base de INSS no valor de R$15473,49.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14392924938647)

 

### **

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42315105282711)

 Geração arquivo DARF e GPS:**

O ‘DARF DA RECEITA BRUTA’ e ‘GPS’ juntas serão a soma do valor da **Guia **emitida no DARF da Dctfweb, as referidas guias serão impressas acessando o caminho Relatórios » Gerador Documento/Guias - Gráfico » Guia de INSS.

Para gerar o arquivo da DARF acesse a tela Guia de INSS, em seguida, clique sobre o layout da ‘DARF Receita Bruta’.

Selecione, nas abas **"Guia"** e **"Empresas"**, os dados para geração. Em seguida, acione o botão de visualização. Para integrar os valores para pagamento, utilize a aba **"Financeiro"** para fazer a integração.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14392886935447)

 

Por último é possível imprimir e integrar com o financeiro a GPS da folha de pagamento.

Selecione, nas abas Guia e Empresas os dados para geração. Depois, acione o botão de visualização.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14392939731735)

 

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14392965238679)

**

 

**

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16859869859479)

 Conclusão:**

Vimos neste artigo como realizar as configurações no MGE Pessoal para que a desoneração da folha seja considerada na totalidade dos impostos da empresa. Assim, a desoneração da folha de pagamento é a possibilidade da retirada da Contribuição Previdenciária Patronal e substituição dela pela CPRB, o imposto que incide sobre a receita bruta do empreendimento.

A Contribuição Previdenciária sobre a Receita Bruta é calculada sobre o montante do negócio, a partir de um percentual que varia de acordo com o ramo. A empresa pode optar anualmente pelo regime que for mais conveniente, sendo sempre o pagamento da CPRB mensal.

Lembrando que as áreas Contábil e Fiscal da empresa poderão apoiar para o preenchimento correto do percentual a ser considerado para a desoneração da folha de pagamento.