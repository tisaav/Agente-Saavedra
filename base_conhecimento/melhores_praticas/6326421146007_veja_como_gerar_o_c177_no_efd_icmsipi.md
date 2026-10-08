# Veja como gerar o C177 no EFD ICMS/IPI

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/6326421146007-Veja-como-gerar-o-C177-no-EFD-ICMS-IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/6326421146007-Veja-como-gerar-o-C177-no-EFD-ICMS-IPI)  
> **ID:** `6326421146007` | **Última Atualização:** 2026-07-22T15:16:41Z

---

REGISTRO C177: COMPLEMENTO DE ITEM - OUTRAS INFORMAÇÕES (código 01, 55) -
(VÁLIDO A PARTIR DE 01/01/2019)

Este registro deverá ser apresentado somente pelos contribuintes obrigados por legislação específica de cada UF, com o objetivo de agregar informações adicionais ao item, de acordo com tabela a ser publicada pela UF.

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/6325858193687)

 

**1° Passo**

Na tela **"Empresa"** *(Caminho de acesso: Comercial » Preferências » Empresa),* aba **"EFD - Escrituração Fiscal digital"**, sub aba **"Bloco e Registro"** configure e marque para gerar.

 

![Como gerar o C177 no EFD ICMSIPI 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16448419087383)

 

**2° Passo**

Foi criada uma nova tela, denominada **"Cadastros Incentivos Fiscais/Financeiros",** nela será possível configurar os diversos incentivos que por ventura a empresa tenha, atendendo a uma necessidade de geração de vários incentivos ao mesmo tempo.

 

![Como gerar o C177 no EFD ICMSIPI 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16448414103575)

 

**3° Passo**

Tela **"Produtos"** *(Caminho de acesso: Configurações » Cadastros » Produtos » Produtos)* configure os campos **"Cód. Apur. Inc. PRODEPE/FUNCRESCE"** e **"Indicador Esp. Inc. PRODEPE/FUNCRESCE"** com a opção** ** **'Com Incentivos';**

 

![Como gerar o C177 no EFD ICMSIPI 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/16448419090839)

 

**4° Passo **

Na tela  Empresa *(Caminho de acesso: Comercial » Preferências » Empresa)*, aba **"Livros Fiscais"**, marque o campo **"Beneficiário de Incentivo PRODEPE/FUNCRESCE?"**;

 

![Como gerar o C177 no EFD ICMSIPI 4.png](https://ajuda.sankhya.com.br/hc/article_attachments/16448414106903)

 

**5° Passo**

No cadastro de CFOP *(Caminho de acesso: Comercial » Arquivo » Cadastros » CFOP)*, marque o campo **"Tipo de Operação PRODEPE"** igual a **"Operação Incentivada"**. 

* Configure para o CFOP que usar no lançamento da nota.

 

![Como gerar o C177 no EFD ICMSIPI 5.png](https://ajuda.sankhya.com.br/hc/article_attachments/16448414108311)

 

![Como gerar o C177 no EFD ICMSIPI 6.png](https://ajuda.sankhya.com.br/hc/article_attachments/16448414109463)

 

**Importante:** O código que vai ser gerado no campo 2 do C177 é gerado através da tabela COD_INF_ITEM Código da informação adicional, de acordo com tabela a ser publicada pela SEFAZ, conforme tabela definida no item 5.6.

Ele será formado a partir da combinação da UF que a cidade no cadastro de empresa pertence, mais a configuração Indicador de Enquadramento (tela cadastro de incentivo) e também o Indicador de Sub-apuração ( tela cadastro de incentivo).