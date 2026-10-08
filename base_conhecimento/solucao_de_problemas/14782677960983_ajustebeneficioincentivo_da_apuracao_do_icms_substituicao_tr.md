# Ajuste/Benefício/Incentivo da Apuração do ICMS Substituição Tributária

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/14782677960983-Ajuste-Benef%C3%ADcio-Incentivo-da-Apura%C3%A7%C3%A3o-do-ICMS-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria](https://ajuda.sankhya.com.br/hc/pt-br/articles/14782677960983-Ajuste-Benef%C3%ADcio-Incentivo-da-Apura%C3%A7%C3%A3o-do-ICMS-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria)  
> **ID:** `14782677960983` | **Última Atualização:** 2026-07-22T14:58:05Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969395370007)

 MENSAGEM:**

[Registro E220]: Ajuste/Benefício/Incentivo da Apuração do ICMS Substituição Tributária.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969355750679)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969355753623)

 Acesse a tela **"****Ajuste da Apuração de ICMS e ICMS ST"  ***(Caminho de acesso: **Livros Fiscais » Arquivos » Ajuste da Apuração de ICMS e ICMS ST). *

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969355757335)

 O registro E220 é utilizado para informar os ajustes, benefícios ou incentivos fiscais relacionados à apuração do ICMS (Imposto sobre Circulação de Mercadorias e Serviços) na modalidade de substituição tributária. No entanto, alguns usuários têm enfrentado problemas ao preencher essas informações na tela de Ajuste da Apuração ICMS e ICMS ST, pois elas não estão sendo geradas corretamente no arquivo EFD - Escrituração Fiscal Digital.

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450644701847)

 Acesse: Empresa Comercial » Preferências » Empresa

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450644701847)

 Procure na aba **"EFD- Escrituração Fiscal Digital",**  opção de configurações relacionadas à geração do arquivo EFD;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450644701847)

 Tipo de escrituração:  EFD; 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450644701847)

 Na aba **"Blocos e Registros"**, ative a opção de geração do registro E240;

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28450644701847)

 Salve as alterações realizadas nas preferências.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969355759383)

 Após realizar esses passos, será possível gerar corretamente o registro E220 contendo as informações referentes aos ajustes, benefícios ou incentivos fiscais da apuração do ICMS na substituição tributária. Certifique-se de revisar e preencher corretamente os dados necessários na tela de Ajuste da Apuração ICMS e ICMS ST antes de gerar o arquivo EFD.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969395377431)

 Nesta tela estão lançadas as informações de apuração, preenchendo os campos e os campos com (*) de preenchimento obrigatório. Porém o **"Código UF"** deverá estar disponível para escolha somente se o tipo de imposto for ICMS ST e, caso não estiver preenchido o campo de UF, o registro E220 não será populado no arquivo de Sped fiscal.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16969355764119)

 CAUSA:**

Após uma análise detalhada, verificamos que todas as configurações relacionadas à substituição tributária foram revisadas e estão corretas. No entanto, ao examinarmos a query de geração do arquivo, percebemos que o resultado indica a necessidade de ativar a geração do registro E240 nas preferências da empresa comercial. Essa ativação é necessária para que o registro E220 possa ser gerado corretamente.