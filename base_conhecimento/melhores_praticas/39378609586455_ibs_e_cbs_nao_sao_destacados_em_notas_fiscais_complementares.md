# IBS e CBS não são destacados em Notas Fiscais Complementares

> **Módulo:** Melhores Praticas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39378609586455-IBS-e-CBS-n%C3%A3o-s%C3%A3o-destacados-em-Notas-Fiscais-Complementares](https://ajuda.sankhya.com.br/hc/pt-br/articles/39378609586455-IBS-e-CBS-n%C3%A3o-s%C3%A3o-destacados-em-Notas-Fiscais-Complementares)  
> **ID:** `39378609586455` | **Última Atualização:** 2026-08-11T20:57:32Z

---

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39378609577239)

  SITUAÇÃO**

Os tributos **IBS** e **CBS** não estão sendo calculados e/ou destacados nas **Notas Fiscais Complementares** emitidas pelo sistema.

 

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39378609578903)

  SOLUÇÃO**

Para que os tributos **IBS** e **CBS** sejam destacados na nota fiscal complementar, realize as seguintes verificações e ajustes:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39378580104343)

  Acesse as **"Preferências da Empresa"** **( **Comercial » Preferências » Empresa ) e verifique **Nota Técnica da Reforma Tributária** está habilitada.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39378609579799)

  Como a TOP utilizada na nota complementar de emissão própria, possui a configuração "**Cálculo de ICMS, IPI, ISS, IBS, CBS e IS**" como "**Não calcula e Digita**", devemos inserir os valores de **"IBS"** e **"CBS" **diretamente na Central.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39378609580055)

 Na **Central de Vendas**, com a nota complementar aberta, acesse **Outras Opções > Consultar/Alterar Dados do Imposto do Item**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39378580105495)

  Inclua os impostos **IBS UF**, **IBS Município** e **CBS**, informando a **base de cálculo**, **alíquota** e **valor** de cada imposto. Salve as alterações.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39378609581975)

  Gere o **XML de conferência** pelo botão **NF-e **na opção** **"Gerar XML da NF-e em arquivo para conferência"  e valide se os tributos foram destacados corretamente. Estando as informações corretas, confirme a nota para emissão.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41944185737495)

 

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39378609584023)

  CAUSA**

Nas Notas Fiscais Complementares emitidas com uma TOP cuja configuração **"Cálculo de ICMS, IPI e ISS"** está definida como **"Não calcula e Digita"**, o sistema não realiza o cálculo automático dos tributos **IBS** e **CBS**. Nessa situação, os impostos devem ser informados manualmente nos dados do imposto do item para que sejam destacados no XML e no documento fiscal.