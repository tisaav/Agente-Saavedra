# E0432 Rejeição: O valor do desconto condicionado informado na DPS deve ser menor que o valor do serviço e maior que zero.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225193517975-E0432-Rejei%C3%A7%C3%A3o-O-valor-do-desconto-condicionado-informado-na-DPS-deve-ser-menor-que-o-valor-do-servi%C3%A7o-e-maior-que-zero](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225193517975-E0432-Rejei%C3%A7%C3%A3o-O-valor-do-desconto-condicionado-informado-na-DPS-deve-ser-menor-que-o-valor-do-servi%C3%A7o-e-maior-que-zero)  
> **ID:** `37225193517975` | **Última Atualização:** 2026-07-22T14:16:08Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225193489559)

 **MENSAGEM**

E0432 Rejeição: O valor do desconto condicionado informado na DPS deve ser menor que o valor do serviço e maior que zero.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225209877015)

 **SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** com desconto condicionado, o usuário recebe a rejeição E0432. Isso ocorre quando o **valor do desconto condicionado** informado na DPS (Declaração de Prestação de Serviços) está **igual ou maior que o valor total do serviço**, ou quando o desconto está **igual a zero**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225193493911)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225209878935)

 Acesse a tela ****[''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)** **(Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225209881111)

 Na aba **''NFS-e''**, localize o campo **''Desconto Condicionado para NFS-e''**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225193504151)

 Verifique qual opção está selecionada no campo:

- 

**"Não usa"**: o desconto será tratado como incondicionado;

- 

**"Financeiro"**: busca o desconto do título financeiro;

- 

**"Nota"**: busca o desconto informado nos itens da nota;

- 

**"Ambos"**: soma os descontos do financeiro e da nota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225209882519)

 Acesse a tela ****[''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225209884055)

 Localize a nota fiscal que será emitida.

**

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225209889559)

 Verifique o valor do desconto condicionado informado**. De acordo com a opção configurada, proceda da seguinte forma:

- 

**Opção “Financeiro” selecionada: **Acesse a aba **“Financeiro”** na grade de rodapé e verifique o campo **“Vlr. Desconto”** do título.

- 

**Opção “Nota” selecionada: **Verifique o campo **“Vlr. Desconto”** nos **itens da nota** e o campo **“Total Desc. Serviços”** na aba **“Totais”**.

- 

**Opção “Ambos” selecionada: **Some os valores de desconto informados no financeiro e na nota.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225209889559)

 Certifique-se de que o **valor do desconto condicionado seja maior que zero** e **inferior ao valor total do serviço prestado**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225150408471)

 Caso o desconto informado seja **igual ou superior ao valor do serviço**, ajuste-o para que fique **dentro dos limites permitidos pela Sefaz**.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225150409239)

 Após realizar os ajustes necessários, **emita novamente a NFS-e** e verifique se a rejeição foi solucionada.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225209891735)

 **CAUSA**

A rejeição ocorre quando o **valor do desconto condicionado** informado na tag **<DescontoCondicionado>** do XML da NFS-e está **igual a zero**, **igual ao valor total do serviço** ou **maior que o valor do serviço**. A Sefaz exige que o desconto condicionado seja **maior que zero e menor que o valor do serviço**, garantindo que sempre haja um valor líquido a ser cobrado pela prestação do serviço.


---

### 🔗 Links e Referências Internas:

- [''Tipos de Operação - TOP''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [''Central de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)