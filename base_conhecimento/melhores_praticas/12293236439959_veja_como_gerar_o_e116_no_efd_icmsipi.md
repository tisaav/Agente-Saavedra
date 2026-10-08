# Veja como gerar o E116 no EFD ICMS/IPI

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/12293236439959-Veja-como-gerar-o-E116-no-EFD-ICMS-IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/12293236439959-Veja-como-gerar-o-E116-no-EFD-ICMS-IPI)  
> **ID:** `12293236439959` | **Última Atualização:** 2026-07-23T00:35:47Z

---

O somatório dos campos **"Valor da obrigação a recolher"** dos registros E116 não é igual à soma dos campos **"Valor total de ICMS a recolher"** e **"Valores recolhidos ou a recolher, extrapuração"** do registro E110. Este registro tem o objetivo de discriminar os pagamentos realizados ou a realizar, referentes à apuração do ICMS. Pode acontecer de gerar erro no validador que indicará a necessidade da geração do E116.

### 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42156856334871)

 SITUAÇÃO

O erro ocorre durante a validação do arquivo SPED no PVA, indicando divergência entre os valores de apuração de ICMS e os valores informados para recolhimento nos registros E116.

### 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42156856334999)

 CAUSA

A divergência é causada pela ausência ou incorreção das obrigações a recolher cadastradas no sistema, que não coincidem com os valores apurados no Registro de Apuração do ICMS.

### 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42156856335383)

 SOLUÇÃO

Siga os passos abaixo para realizar o ajuste das informações:

### **1. Verificar as preferências da empresa**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16426972657687)

 Acesse a tela **"Empresa"** (Comercial >> Preferências >> Empresa) e confira as configurações:

- 

Selecione a empresa e acesse a aba **"EFD-Escrituração Fiscal Digital"**.
 

1. 

No campo **"Tipo de Escrituração"**, selecione a opção EFD.
 

1. 

No painel **"Blocos e Registros"**, selecione o Bloco 'E'.
 

1. 

No painel **"Registros"**, verifique se para o registro E116 está marcada a opção **"Gerar Registro"**.
 

1. 

Na aba **"EFD"**, garanta que o registro **"C170"** esteja marcado. Adicionalmente, verifique se os registros **"C173"**  e **"C176"** devem ser ativados de acordo com as operações da sua empresa. Faça o mesmo para a opção **"Considerar ICMS e ST majorados com o FCP"**, ativando-a apenas se aplicável ao seu negócio e estado.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/42156856337431)

### **2. Cadastrar as obrigações de ICMS e ICMS ST**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16426972660759)

 Acesse a tela **"Obrigações do ICMS e ICMS ST a Recolher"** (Livros Fiscais >> Avançado >> Escrituração Fiscal Digital >> Obrigações do ICMS e ICMS ST a Recolher):

- 

Clique em **"Incluir"** e preencha os dados de recolhimento.
 

1. 

Defina o campo **"Tipo Apuração"** como **"ICMS ST"** ou **"ICMS ST FCP"**.
 

1. 

Preencha o campo **"Código UF"**.
 

1. 

Informe o campo **"Valor da Obrigação a Recolher"** líquido, já descontados os créditos.
 

1. 

Salve os registros com o aval do contador.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14626610053015)

### **3. Gerar a apuração de ICMS**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16426972667671)

 Acesse a tela **"Registro de Apuração do ICMS"** (Livros Fiscais >> Relatórios >> Registro de Apuração do ICMS):

- 

Preencha a empresa e o período.
 

1. 

Clique em **"Abrir"** para processar os lançamentos e confira os valores na guia **"Demonstrativos"**.
 

1. 

Após a validação, clique em **"Salvar"**.
 

1. Lembrando que, a cada alteração feita na tela de Obrigações do ICMS e ICMS ST a Recolher, sempre é necessário acessar a tela de Registro de Apuração do ICMS, clicar em abrir e salvar, antes de gerar o arquivo EFD-Fiscal..
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14626608086039)

### **4. Ajustes de apuração e geração do SPED**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/16427060055063)

 Se necessário, verifique a tela **"Ajuste de Apuração ICMS e ICMS ST"** (Livros Fiscais » Arquivos), garantindo que o **"Tipo Imposto"** e **"Código UF"** estejam corretos.
Por fim, acesse **"EFD - Escrituração Fiscal Digital - ICMS/IPI"** (INSERIR CAMINHO DA TELA), gere novamente o arquivo e valide no PVA.