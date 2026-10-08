# Campos 'Preço em moeda' e 'Valor Moeda' não editáveis na cotação

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/26668196552215-Campos-Pre%C3%A7o-em-moeda-e-Valor-Moeda-n%C3%A3o-edit%C3%A1veis-na-cota%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/26668196552215-Campos-Pre%C3%A7o-em-moeda-e-Valor-Moeda-n%C3%A3o-edit%C3%A1veis-na-cota%C3%A7%C3%A3o)  
> **ID:** `26668196552215` | **Última Atualização:** 2026-07-22T14:40:53Z

---

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26672669861399)

 **SITUAÇÃO:**

Ao ativar a preferência "**TRABMOECOT - Trabalhar com Moedas na Cotação?", **os campos **"Preço em moeda" **e **"Valor Moeda"** são apresentados na cotação, mas não permite edição. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26668196546455)

SOLUÇÃO:**

Para possibilitar o preenchimento dos campos mencionados, primeiro adicione uma moeda na grade.

Se não houver nenhuma moeda disponível para inserção, isso indica que o parceiro fornecedor não possui uma moeda vinculada ao seu cadastro. Podendo ser apresentado o erro **'Moeda não existe ou não pode ser usado aqui: PK[1].'**

Acesse a tela de **"Parceiros"** *(Configurações » Cadastros » Parceiros)*, abra o cadastro do parceiro fornecedor e, na aba **"Moedas p/ Portal cot."**, insira as moedas que poderão ser utilizadas para esse fornecedor.

Após o cadastro, retorne à cotação e será possível inserir uma moeda. Após a inserção da moeda, os campos estarão editáveis conforme o esperado.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/26668259376535)

CAUSA:**

Ocorre quando não existe uma moeda vinculada ao parceiro fornecedor da cotação.