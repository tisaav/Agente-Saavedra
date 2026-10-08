# Resumo de Operações com Cartão

> **Módulo:** Fiscal e Contábil | **Subseção:** Rotinas descontinuadas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595154-Resumo-de-Opera%C3%A7%C3%B5es-com-Cart%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595154-Resumo-de-Opera%C3%A7%C3%B5es-com-Cart%C3%A3o)  
> **ID:** `360044595154` | **Última Atualização:** 2026-09-23T19:41:27Z

---

# Tela Resumo de Operações com Cartão

**Módulo:** Livros Fiscais › Arquivos

**Caminho de acesso:** Menu Principal › Livros Fiscais › Arquivos › Resumo de Operações com Cartão

**Neste artigo**

- [O que é e para que serve](#oque)

- [Como usar a tela](#comousar)

- [Aba Reg. 1600](#reg1600)

- [Aba Reg. 1601](#reg1601)

- [Pontos de atenção](#atencao)

## O que é e para que serve

A **Tela Resumo de Operações com Cartão** possibilita a inserção manual dos dados referentes aos registros `1600` e `1601`, relativos às operações realizadas com cartão. Os dados informados aqui são usados no tratamento manual desses registros na geração da EFD. A tela **não** gera o arquivo da EFD — ela apenas registra os valores que serão levados aos registros 1600 e 1601 na geração.

![Tela Resumo de Operações com Cartão com os campos Empresa e Referência e as abas Reg. 1600 e Reg. 1601](https://ajuda.sankhya.com.br/hc/article_attachments/4419356823575)

## Como usar a tela

Informe inicialmente a **Empresa** e a data de referência no campo **Referência**. Em seguida, preencha os dados nas abas **Reg. 1600** e/ou **Reg. 1601**, conforme os registros que deseja cadastrar.

**ℹ️ Nota**

Para que os dados desta tela sejam usados na geração, as marcações **Gerar registro 1600 pelo Resumo de Operações com Cartão?** e **Gerar registro 1601 pelo Resumo de Operações com Cartão?** devem estar habilitadas na tela ****[EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI#abaopes), aba **Configurações › Sub-aba Opções**. Cada marcação vale para o seu registro.

[↑ Voltar ao início](#sumario)

## Aba Reg. 1600

Para o cadastro do registro `1600`, preencha os campos:

- 
**Parc. Administradora** — a administradora de cartão da operação.

- 
**Valor das Vendas a Débito** — o valor das vendas realizadas na função débito.

- 
**Valor das Vendas a Crédito** — o valor das vendas realizadas na função crédito.

Quando a marcação **Gerar registro 1600 pelo Resumo de Operações com Cartão?** estiver habilitada na tela EFD, o sistema utiliza os dados desta aba para tratar de forma manual as informações do registro `1600` na geração do arquivo.

![Aba Reg. 1600 com os campos Parc. Administradora, Valor das Vendas a Débito e Valor das Vendas a Crédito](https://ajuda.sankhya.com.br/hc/article_attachments/4419363110423)

[↑ Voltar ao início](#sumario)

## Aba Reg. 1601

Para o cadastro do registro `1601`, preencha os campos:

- 
**Parc. Administradora** — a administradora de cartão da operação.

- 
**Parc. Intermediador** — o intermediador da operação.

- 
**Valor Bruto Vendas** — o valor total bruto referente às vendas e/ou prestação de serviços com incidência de ICMS, incluindo operações com imunidade do imposto.

- 
**Valor Bruto Serviços** — o valor total bruto referente à prestação de serviços com incidência de ISS.

- 
**Valor Outros** — o valor total de operações, deduzindo os valores dos campos **Valor Bruto Vendas** e **Valor Bruto Serviços**.

Quando a marcação **Gerar registro 1601 pelo Resumo de Operações com Cartão?** estiver habilitada na tela EFD, o sistema utiliza os dados desta aba para tratar de forma manual as informações do registro `1601` na geração do arquivo.

![Aba Reg. 1601 com os campos Parc. Administradora, Parc. Intermediador, Valor Bruto Vendas, Valor Bruto Serviços e Valor Outros](https://ajuda.sankhya.com.br/hc/article_attachments/4419363133463)

[↑ Voltar ao início](#sumario)

## Pontos de atenção

- São duas marcações independentes na tela EFD (uma para o `1600` e outra para o `1601`); habilite a que corresponde ao registro que deseja tratar por esta tela.

- O campo **Valor Outros** do registro `1601` é obtido por dedução: valor total de operações menos **Valor Bruto Vendas** e **Valor Bruto Serviços**.

- No registro `1601`, o **Valor Bruto Vendas** refere-se a operações com incidência de ICMS e o **Valor Bruto Serviços** a serviços com incidência de ISS.


---

### 🔗 Links e Referências Internas:

- [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI#abaopes)