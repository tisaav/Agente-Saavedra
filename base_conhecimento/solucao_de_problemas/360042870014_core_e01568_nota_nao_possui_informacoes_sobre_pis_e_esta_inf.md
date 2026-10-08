# [CORE_E01568] Nota não possui informações sobre PIS, e esta informação é obrigatória para NFe

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042870014--CORE-E01568-Nota-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-PIS-e-esta-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-NFe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042870014--CORE-E01568-Nota-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-PIS-e-esta-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-NFe)  
> **ID:** `360042870014` | **Última Atualização:** 2026-07-22T16:05:29Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115389741591)

 MENSAGEM:**

[CORE_E01568] Nota não possui informações sobre PIS, e esta informação é obrigatória para NFe.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115389750807)

 SOLUÇÃO:**

Para solucionar essa rejeição é necessário que as configurações para o cálculo desse imposto sejam devidamente realizadas, conforme orientações de seu Contador. Vale ressaltar que, independente de isenção, a exceção deverá estar devidamente configurada, com o CST correspondente.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115389753879)

 Tela **"******[Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**" ***(Caminho de acesso: Comercial » Arquivos » Cadastros) -* Aba **"Impostos"**, campo **"Tem PIS": **marcado;  Aba **"Livro Fiscal"**, campo **"Atualização de Livro de ICMS": **deve atualizar livro de entrada ou saída, conforme o tipo de movimento da TOP.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115398875927)

 Tela **"******[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**" ***(Caminho de acesso: Comercial » Preferências) - *Aba **"Propriedades"**, campo **"Calcula PIS": **marcado

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115389761943)

 Tela **"******[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)**"** *(Caminho de acesso: Configurações » Cadastros) - *Aba **"Impostos"**, campo **"Grupo PIS": **informe o grupo

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115389764631)

 Tela** "******[Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS)**"** *(Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas). *Configure exceção para o Grupo vinculado no produto.

 

Realizadas tais configurações, caso a nota tenha gerado Número Nota, aconselhamos sua inutilização e o faturamento de uma nova NF-e.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16115398883223)

 CAUSA:**

Por se tratar de uma Nota Fiscal Eletrônica, é imprescindível que se tenha o cálculo de PIS. Mesmo que a incidência da Alíquota seja 0 (zero) é preciso criar uma Alíquota com incidência zero, para que no ato da confirmação/aprovação da NF-e seja gerado os dados de PIS no XML da NF-e.


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)
- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)
- [Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS)