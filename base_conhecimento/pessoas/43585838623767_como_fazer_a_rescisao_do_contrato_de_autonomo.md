# Como fazer a rescisão do contrato de autônomo?

> **Módulo:** Pessoas+ | **Subseção:** Contrato Autônomo  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43585838623767-Como-fazer-a-rescis%C3%A3o-do-contrato-de-aut%C3%B4nomo](https://ajuda.sankhya.com.br/hc/pt-br/articles/43585838623767-Como-fazer-a-rescis%C3%A3o-do-contrato-de-aut%C3%B4nomo)  
> **ID:** `43585838623767` | **Última Atualização:** 2026-09-27T14:39:50Z

---

**Módulo: **Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela: **br.com.sankhya.rh.CalculoIndFolha

## **Descrição e Usabilidade**

### **1. Descrição da Funcionalidade**

A rotina de **Rescisão** permite calcular o encerramento do contrato de prestação de serviço de um **autônomo (vínculo 90)** e realizar os procedimentos relacionados ao envio das informações ao eSocial.

Embora o autônomo não possua vínculo empregatício, o encerramento do contrato de prestação de serviço continuado pode ser calculado no **Pessoas+** por meio da rotina de **Rescisão**, observando as particularidades aplicáveis a esse tipo de vínculo.

### **2. Pré-requisitos**

Antes de realizar o cálculo, verifique se:

- O autônomo está cadastrado com o vínculo **90 - Autônomo**.

- O vínculo **90 - Autônomo **está incluído no parâmetro **Vínculos sem direito a férias - FPSEMFERIAS** (tela **Preferências** (Configurações > Avançado)); sem isso, o cálculo pode apresentar erro ao buscar registros de férias que não existem para esse tipo de vínculo.

- Os **eventos e bases** utilizados pelo autônomo estão configurados com as identificações necessárias, para que o valor da parte empresa componha na GPS.

- A **Categoria de ocorrência do FGTS** do autônomo (prestação de serviço ou transporte rodoviário) está configurada de acordo com o tipo de rescisão que será utilizado.

- O **Aviso Prévio** está cadastrado na tela **Aviso Prévio **(Pessoal+ > Cadastros).

### **3. Jornada de Uso**

![rescisao-autonomo.gif](https://ajuda.sankhya.com.br/hc/article_attachments/43602482396695)

1. Acesse a tela **Cálculos **(Pessoal+ > Rotinas Folha).

1. Selecione o tipo de cálculo **Individual**.

1. Clique no tipo de folha **Rescisão**.

1. Na primeira etapa, preencha as informações gerais do cálculo.

1. Na segunda etapa, selecione o **tipo de rescisão** de acordo com a iniciativa de encerramento do contrato:

  - 
**Demissão Sem Justa Causa - Inic. Empresa**;

  - 
**Demissão a Pedido S/ Justa Causa**.

1. Preencha os campos obrigatórios identidicados com *.

1. Na seção de **Aviso Prévio**, informe os dados correspondentes e selecione:

  - 
**Dispensado**, na opção de aviso;

  - 
**Indenizado/Não exigível**, no campo **Indicador de Cumprimento de Aviso Prévio**.

1. Avance para a etapa **Calcular**.

1. Selecione o modo de cálculo e clique em **Calcular**.

1. Confira os valores apresentados e **confirme a folha**.

1. Para emitir os documentos rescisórios, expanda a opção **Documentos** e selecione **Baixar**, **Imprimir** ou **Enviar por e-mail**, conforme a necessidade.

1. Após confirmar, acesse o **Gerenciador de Folhas** (Pessoal+ > Rotinas) e [libere a folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247-Gerenciador-de-Folhas#h_01KQN3XPDJ4KAYEW7VWMBHPXCZ) para o eSocial.

1. Gere e envie o evento **S-2299 - Desligamento** pela **Central do eSocial **(Pessoal+ > Rotinas).

### **4. Pontos de Atenção**

- A opção selecionada em **Tipo de Rescisão** deve ser compatível com a **Categoria de ocorrência do FGTS** configurada no cadastro do autônomo. A divergência entre essas configurações pode afetar o cálculo da rescisão.

- Se ocorrer erro relacionado à ausência de eventos no cálculo, verifique se o vínculo **90 - Autônomo** está incluído no parâmetro **FPSEMFERIAS**.

- Se os valores da parte empresa não forem considerados conforme esperado na **GPS**, confira as configurações dos **eventos, bases e identificações** utilizadas no cadastro do autônomo. 

- O **Aviso Prévio** utilizado no cálculo deve estar previamente cadastrado na rotina correspondente.

### **5. Dicas de Usabilidade**

- Antes de confirmar a rescisão, confira os valores calculados e os dados do **Aviso Prévio**. 

- Após a confirmação, realize a liberação da folha pelo **Gerenciador de Folhas** antes de gerar o evento **S-2299** no eSocial. 

- O encerramento do contrato e o envio das informações ao eSocial fazem parte do mesmo fluxo de rescisão do **Pessoal+**, não sendo necessário utilizar uma rotina específica de desligamento exclusiva para autônomos.

## **Artigos Relacionados**

- [Lançamento de Movimento para Cálculo de Autônomo](https://ajuda.sankhya.com.br/hc/pt-br/articles/25948428448535)

- [Cálculo da folha de Autônomos](https://ajuda.sankhya.com.br/hc/pt-br/articles/43529821213335)


---

### 🔗 Links e Referências Internas:

- [libere a folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247-Gerenciador-de-Folhas#h_01KQN3XPDJ4KAYEW7VWMBHPXCZ)
- [Lançamento de Movimento para Cálculo de Autônomo](https://ajuda.sankhya.com.br/hc/pt-br/articles/25948428448535)
- [Cálculo da folha de Autônomos](https://ajuda.sankhya.com.br/hc/pt-br/articles/43529821213335)