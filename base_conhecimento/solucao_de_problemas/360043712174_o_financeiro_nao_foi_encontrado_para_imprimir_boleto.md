# O Financeiro não foi encontrado para imprimir boleto

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712174-O-Financeiro-n%C3%A3o-foi-encontrado-para-imprimir-boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712174-O-Financeiro-n%C3%A3o-foi-encontrado-para-imprimir-boleto)  
> **ID:** `360043712174` | **Última Atualização:** 2026-07-22T16:00:49Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292624482711)

 **MENSAGEM:**

[CORE_E01398]: O Financeiro não foi encontrado para imprimir boleto.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292624488471)

 SOLUÇÃO:**

Revise as configurações abaixo, de acordo com o lançamento efetuado, e caso algum deles não seja respeitado, a mensagem será apresentada na tentativa de impressão de boleta.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292595205655)

 Acesse: Configurações » Cadastros » Bancários » Contas

Aba: **"Boleto(s)/Duplicatas"**

- Emite: marcado

- Impressora: informe o nome da Impressora

- Tipo Impressora: selecione uma das opções

- Modelo: configure em '**Financeiro » Relatórios » Modelos de Boleto(s)**', um modelo padrão ou personalizado, e vincule em '**Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)**', para ser informado neste campo

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292595212183)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação

Aba: **"Características"**
Subtipo: **Diferente** de 'A vista'

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292624522135)

 Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba: **"Impressão"**

Campo **"Imprimir Boleto/Duplicata"**: **Diferente** de 'Proibido'

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292595243031)

 Acesse: Financeiro » Rotinas » Movimentação Financeira

Certifique-se que o(s) titulo(s) não estejam Baixados - Campo** "Data de Baixa"** e **"Valor de Baixa"** - preenchidos e Data de Vencimento não seja igual data de negociação.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292624539031)

 Acesse: Configurações » Cadastros » Parceiros

Aba: **"Informações"**

**Geração de boleto nas centrais:** use as opções disponíveis para impressão e envio de boleto por e-mail pela Central de Vendas

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292624550423)

 Após os ajustes, considere efetuar a impressão do boleto novamente.

 

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292595273367)

 IMPORTANTE:**

Para tipo de negociação à vista, ou seja, Data de Vencimento igual data de negociação, a impressão de boleto ocorrerá somente através da rotina 'Impressão de Boletos'. Para mais detalhes: [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17292595289239)

 CAUSA:**

Ocorre quando uma das opções acima estão em desacordo para a geração de boleto.


---

### 🔗 Links e Referências Internas:

- [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094)