# A conta XX, é exclusiva da empresa YY

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360059539993-A-conta-XX-%C3%A9-exclusiva-da-empresa-YY](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059539993-A-conta-XX-%C3%A9-exclusiva-da-empresa-YY)  
> **ID:** `360059539993` | **Última Atualização:** 2026-07-22T15:26:46Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16252821767575)

 MENSAGEM**:

[CORE_E02804]  A conta XX, é exclusiva da empresa YY.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16252821771799)

 SOLUÇÃO**:

Veja um exemplo, para explanar a solução do problema

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16252821775127)

 Acesse o cadastro de **["Conta"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) **Bancaria em: Configurações » Cadastros » Bancários » Contas

Identifique o código da conta bancaria vinculado à parcelas do Tipo de Negociação

 

![A_conta_XX____exclusiva_da_empresa_YY_-_1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14606130114711)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16252797363607)

 Acesse o cadastro de ****["Tipo de Negociação"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) em: *Comercial » Arquivo » Cadastros » Tipos de Negociação*
Aba: **"Parcelas"**

 

![A_conta_XX____exclusiva_da_empresa_YY_-_2.png](https://ajuda.sankhya.com.br/hc/article_attachments/14606138833815)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16252821787415)

 Acesse a Nota em: *Comercial » Rotinas » Central de Vendas*

Verifique a empresa do cabeçalho da nota, e caso esteja diferente da empresa exclusiva da conta bancária, considere ajustar as Parcelas do Tipo de Negociação.

 

![A_conta_XX____exclusiva_da_empresa_YY_-_3.png](https://ajuda.sankhya.com.br/hc/article_attachments/14606396630679)

 

Ou Seja: 
Empresa da Conta Bancaria: Empresa 6 - Conta marcada como Exclusiva
Empresa da parcela do Tipo de Negociação como X-Constante Exclusiva = 6 
Empresa do cabeçalho da Nota = Empresa 6

Dessa forma, o cabeçalho da nota será salvo com sucesso.

![constante_exclusiva.gif](https://ajuda.sankhya.com.br/hc/article_attachments/360097849214)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16252821789975)

 CAUSA**: 

Ocorre quando a Conta Bancaria, vinculada a uma das parcelas do Tipo de Negociação, é exclusiva da Empresa diferente da empresa do cabeçalho da nota, quando o Tipo de Negociação, está configurado na aba: **"Parcelas a opção"**
Campo **"Tipo de Empresa":** X-Constante Exclusiva e 
Empresa: Código da empresa diferente do código vinculado a conta bancaria


---

### 🔗 Links e Referências Internas:

- ["Conta"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)
- ["Tipo de Negociação"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)