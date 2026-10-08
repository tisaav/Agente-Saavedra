# Campo de preenchimento obrigatório - Campo 2 - IND_NAT_RET[Registro F600]

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360047855033-Campo-de-preenchimento-obrigat%C3%B3rio-Campo-2-IND-NAT-RET-Registro-F600](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047855033-Campo-de-preenchimento-obrigat%C3%B3rio-Campo-2-IND-NAT-RET-Registro-F600)  
> **ID:** `360047855033` | **Última Atualização:** 2026-07-22T15:32:00Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16531940525591)

 MENSAGEM:**

Campo de preenchimento obrigatório. Campo 2 - IND_NAT_RET. Registro: F600.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16531928333719)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16531928334743)

 Identifique o parceiro/CNPJ a qual o campo está sendo **"Rejeitado".** Acesse a tela de cadastro do respectivo 'Parceiro' e preencha o campo **"Natureza da Retenção na Fonte" **da aba **"Fiscal"**:

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15604217565463)

 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28454040516887)

 A informação determinada no campo **"Natureza da Retenção na Fonte"** diz respeito ao SPED Contribuições ([EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238074-EFD-Contribui%C3%A7%C3%B5es)) e será gerada no registro F600-CONTRIBUIÇÃO RETIDA NA FONTE - Campo 02: **IND_DAT_RET**. Este campo poderá ser definido dentre as seguintes opções:

- 01 - Retenção por Órgãos, Autarquias e Fundações Federais;

- 02 - Retenção por outras Entidades Adm. Pública Federal;

- 03 - Retenção por Pessoas Jurídicas de Direito Privado;

- 04 - Recolhimento por Sociedade Cooperativa;

- 05 - Retenção por Fabricante de Máquinas e Veículos;

- 99 - Outras Retenções.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16531928339863)

 Ajustada essa configuração, gere o arquivo novamente, e certifique-se que para esse parceiro o erro não mais ocorreu no respectivo validador. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16531940537367)

 CAUSA:**

Ausência de configuração do campo Natureza da Retenção na Fonte presente na aba Fiscal, do cadastro de parceiros.


---

### 🔗 Links e Referências Internas:

- [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238074-EFD-Contribui%C3%A7%C3%B5es)