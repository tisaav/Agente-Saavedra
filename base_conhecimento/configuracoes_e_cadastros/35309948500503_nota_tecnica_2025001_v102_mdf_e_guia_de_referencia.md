# Nota Técnica 2025.001 v1.02 (MDF-e) - Guia de Referência

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503-Nota-T%C3%A9cnica-2025-001-v1-02-MDF-e-Guia-de-Refer%C3%AAncia](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503-Nota-T%C3%A9cnica-2025-001-v1-02-MDF-e-Guia-de-Refer%C3%AAncia)  
> **ID:** `35309948500503` | **Última Atualização:** 2026-07-29T13:43:17Z

---

Tire suas dúvidas sobre as novas regras da NT 2025.001 v1.02 para emissão de MDF-e no Sankhya OM e entenda como solucionar as principais rejeições.

### **Pré-requisitos**

As adequações para a nota estão disponíveis nas versões**:**

- 

4.35b220

- 

4.34b225

- 

4.33b171

### **1. MDFe**

O **Manifesto Eletrônico de Documentos Fiscais (MDF-e) é o documento digital **emitido e armazenado eletronicamente **que consolida e legaliza o transporte de cargas em todo território nacional.** O MDF-e é emitido por:

- 

Empresas transportadoras (ETC) no transporte de carga fracionada ou lotação.

- 

Empresas que realizam o transporte de mercadoria própria, utilizando veículos próprios, arrendados, ou contratando um transportador autônomo.

- 

Situação de transporte interestadual, independentemente de ser carga fracionada ou lotação.

### **2. Nota Técnica 2025.001 v1.02**

A** Nota Técnica (NT) propõe ajustes no leiaute do MDF-e** para atender a novas exigências legais de validação, com** data de implantação a partir de 01 de Outubro de 2025.**

![Captura de tela 2025-09-29 153313.png](https://ajuda.sankhya.com.br/hc/article_attachments/35331477129239)

### **3. Alterações no Sankhya OM**

Para emissão obrigatória de MDF-e,** **o Sankhya OM conta com as atualizações trazidas pela NT 2025.001 v1.02** **para atender às suas necessidades: 
 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310557910423)

 Novo tipo de carga:** selecione a opção de carga** "Granel Pressurizada" **para uma classificação mais precisa nesse tipo de transporte. Essa opção está disponível na tela "**Viagens de Transporte (MDF-e"), **sub aba **"MDF-e", **sub aba **"Produto predominante"**. Para mais detalhes, acesse o artigo:** **[Viagens de Transportes (MDF-e).](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaprodutopredominante)

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310557910423)

 Campo CIOT:** o campo do **Código Identificador da Operação de Transporte (CIOT) deixou de ser obrigatório** na estrutura do arquivo XML do MDF-e. 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310557910423)

 Pagamento de frete:** um dos pontos de atenção trazidos com a NT 2025.001 v1.02 é a** obrigatoriedade dos dados de pagamento do frete no MDF-e sempre que a operação envolver a contratação de um transportador autônomo (TAC) ou em operações de carga lotação com veículo de terceiro. **

###  

### **4. Checklist no Sankhya OM**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310557910423)

 **Verifique a **compatibilidade de sua versão do sistema** com os requisitos da NT 2025.001 v1.02, que deve estar nas versões:** 4.35b220, 4.34b225 ou 4.33b171.**

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310557910423)

 Atualize cadastros de parceiros** na área de transporte e **complete com as informações bancárias atualizadas.**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310557910423)

 Revise as** etapas de emissão de MDF-e** e as alterações nos **campos de preenchimento.**

###  

### **5. FAQ - Perguntas Frequentes**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310557914903)

 No transporte de carga própria se aplica o pagamento?**

Se você usa um veículo e motorista próprios (CLT), as novas regras de pagamento de frete não se aplicam. **O pagamento é devido quando uma empresa com CNPJ diferente da sua, um Transportador Autônomo de Cargas (TAC), faz o frete. **

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310605242647)

 **É obrigatório informar o tipo de transportador no MDF-e?**

Esta é uma informação opcional no MDF-e rodoviário para transporte de carga própria. **Caso contrário, é necessário informar o grupo de informações de pagamento. ******[Acompanhe as informações completas do Sankhya Om neste artigo.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abavaleped%C3%A1gio)** **

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310669296791)

 **A entrada em ambiente de produção está prevista para Outubro de 2025. O que acontece se eu não me adequar a tempo?**

A **partir da data de obrigatoriedade**, o ambiente de produção da** **SEFAZ valida as novas regras e **em caso de inadequação, impede a emissão de MDF-e**.   

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310655355031)

 **Como e onde eu gero o CIOT?**

O CIOT é gerado através de uma IPEF (Instituição de Pagamento Eletrônico de Frete) homologada pela ANTT. ****[Confira neste artigo como lançar o CIOT no Sankhya OM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaciot)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35310669302551)

 **Onde encontro as informações sobre o MDFe e as validações necessárias?**

[Acesse esse link e confira todos os detalhes previstos na legislação](https://dfe-portal.svrs.rs.gov.br/Mdfe/Faq). 

###  

### **6. Solução de Rejeições **

Configurações ausentes ou incorretas da Nota Técnica 2025.001 v1.02 no Sankhya OM, podem gerar algumas rejeições. Confira abaixo uma **lista de artigos para facilitar a solução dessas rejeições:**

- [301 Rejeição: O NCM do produto predominante da carga lotação deve ser informado - MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/35299279582615)

- [302 Rejeição: As informações de pagamento devem ser informados para carga lotação - MDFe](https://ajuda.sankhya.com.br/hc/pt-br/articles/35297934404759-302)

- [303 Rejeição: Dados bancários e de pagamento devem ser informados para TAC e equiparado a TAC](https://ajuda.sankhya.com.br/hc/pt-br/articles/35298216515863)

- [304 Rejeição: CIOT deve ser informado para TAC e equiparado a TAC - MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/35298608017431)

- [Rejeição 745 - O tipo de transportador não ser informado quando não estiver informado proprietário do veículo de tração](https://ajuda.sankhya.com.br/hc/pt-br/articles/35122715417623-745-Rejei%C3%A7%C3%A3o-O-tipo-de-transportador-n%C3%A3o-pode-ser-informado-quando-n%C3%A3o-estiver-informado-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o)


---

### 🔗 Links e Referências Internas:

- [Viagens de Transportes (MDF-e).](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaprodutopredominante)
- [Acompanhe as informações completas do Sankhya Om neste artigo.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abavaleped%C3%A1gio)
- [Confira neste artigo como lançar o CIOT no Sankhya OM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaciot)
- [301 Rejeição: O NCM do produto predominante da carga lotação deve ser informado - MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/35299279582615)
- [302 Rejeição: As informações de pagamento devem ser informados para carga lotação - MDFe](https://ajuda.sankhya.com.br/hc/pt-br/articles/35297934404759-302)
- [303 Rejeição: Dados bancários e de pagamento devem ser informados para TAC e equiparado a TAC](https://ajuda.sankhya.com.br/hc/pt-br/articles/35298216515863)
- [304 Rejeição: CIOT deve ser informado para TAC e equiparado a TAC - MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/35298608017431)
- [Rejeição 745 - O tipo de transportador não ser informado quando não estiver informado proprietário do veículo de tração](https://ajuda.sankhya.com.br/hc/pt-br/articles/35122715417623-745-Rejei%C3%A7%C3%A3o-O-tipo-de-transportador-n%C3%A3o-pode-ser-informado-quando-n%C3%A3o-estiver-informado-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o)