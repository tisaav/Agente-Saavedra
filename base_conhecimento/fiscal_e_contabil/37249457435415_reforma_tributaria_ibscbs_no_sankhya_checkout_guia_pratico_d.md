# Reforma Tributária (IBS/CBS) no Sankhya Checkout: Guia Prático de Configuração

> **Módulo:** Fiscal e Contábil | **Subseção:** Sistemas atendidos  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37249457435415-Reforma-Tribut%C3%A1ria-IBS-CBS-no-Sankhya-Checkout-Guia-Pr%C3%A1tico-de-Configura%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37249457435415-Reforma-Tribut%C3%A1ria-IBS-CBS-no-Sankhya-Checkout-Guia-Pr%C3%A1tico-de-Configura%C3%A7%C3%A3o)  
> **ID:** `37249457435415` | **Última Atualização:** 2026-09-23T14:26:58Z

---

##### Com a chegada da Reforma Tributária, o **Sankhya Om** e o **Sankhya Checkout** foram atualizados para suportar os novos impostos **IBS** e **CBS**. Este guia apresenta um passo a passo para garantir que suas vendas de balcão (NFC-e) estejam corretamente configuradas e em conformidade.

####  

#### **Requisitos Mínimos (Obrigatório)**

Antes de iniciar a configuração, verifique se os sistemas estão atualizados:

- 

**Sankhya W:** Módulo de Livros Fiscais atualizado para a versão **5.16.4** ou superior.

- 

**Sankhya Checkout:** Atualizado para a **última versão disponível** no ****[''Portal de Downloads Sankhya''](https://downloads.sankhya.com.br).

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481380936599)

 OBSERVAÇÃO****:** Sem essas versões, os novos campos de impostos não estarão disponíveis para cálculo ou transmissão, impossibilitando a emissão correta das NFC-e.

 

#### **Passo 1: Configuração Inicial no Sankhya Om**

##### **1. Habilite a Nota Técnica**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481402429591)

 Acesse a tela ****[''Empresa''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481380940695)

 Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NF-e/NFC-e''**, sub-aba **''****Nota Técnica NF-e''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481402433687)

 Ative a NT **2025.002-RTC - v1.10**.

 

##### **2. Configure o Tipo de Operação (TOP)**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481402429591)

 Acesse a tela ****[''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481380940695)

 Localize a TOP utilizada para as vendas NFC-e.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481402433687)

 Na aba **''Impostos''**, marque as opções:

- Tem **CBS**

- Tem **IBS**

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481380936599)

 OBSERVAÇÃO:** Caso os campos não estejam visíveis na tela, basta torná-los visíveis por meio do botão **''Configuração da Tela''**.

 

##### **3. Configure as Regras de IBS e CBS**

O IBS e o CBS devem obrigatoriamente utilizar o mesmo **CST** (000, 200 ou 410) e ao respectivo código de classificação tributária (**CCLASSTRIB**).

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481402429591)

 Configure as **alíquotas** de IBS e CBS conforme a legislação vigente:

- 

**''******[Cadastro de Alíquotas IBS — Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199)**''**

- 

**''******[Cadastro de Alíquotas CBS — Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895)**''**

 

#### **Passo 2: Preparação do Sankhya Checkout**

Para que o Sankhya Checkout entenda as novas regras, é necessário sincronização dos dados:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481402429591)

 Acesse a tela ****[''Administração do Checkout''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout)** **(Configurações » Sankhya Checkout » Administração de Checkout).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481380940695)

 Realize o **cálculo dos impostos** para a empresa correspondente.

- 

Essa ação prepara a carga de dados do **Sankhya Om** para o **Checkout**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481402433687)

 No **terminal do Sankhya Checkout**, execute a opção ''**Sincronização de Atualizações''**.

- 

Esse procedimento **baixa as novas tabelas de IBS e CBS** para o banco de dados local do caixa. Garantindo que o Checkout reconheça corretamente os novos impostos.

 

#### **O que mudou na emissão da nota?**

Ao finalizar uma venda no **Sankhya Checkout**, o sistema agora gera o **XML da NFC-e** incluindo as novas **tags de tributação (IBS e CBS)**.

#####  

##### **Cenários principais validados:**

- 

**CST 000 (Tributada)**: Cálculo integral de IBS e CBS.

- 

**CST 200 (Redução)**: Cálculo sobre a base reduzida.

- 

**CST 410 (Isento/Imune)**: Tags geradas com valor zero.

##### 
**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37481380936599)

 OBSERVAÇÃO: **Atualmente, o **Imposto Seletivo (IS)** e o **Regime Monofásico** ainda não estão implementados no **Sankhya Checkout**. Dessa forma, produtos sujeitos a essa tributação devem ser tratados de acordo com a orientação contábil aplicável durante o período de transição.


---

### 🔗 Links e Referências Internas:

- [''Portal de Downloads Sankhya''](https://downloads.sankhya.com.br)
- [''Empresa''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa)
- [''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Cadastro de Alíquotas IBS — Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199)
- [Cadastro de Alíquotas CBS — Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/33822014543895)
- [''Administração do Checkout''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout)