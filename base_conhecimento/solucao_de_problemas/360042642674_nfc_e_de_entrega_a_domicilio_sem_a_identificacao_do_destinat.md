# NFC-e de entrega a domicílio sem a identificação do destinatário

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042642674-NFC-e-de-entrega-a-domic%C3%ADlio-sem-a-identifica%C3%A7%C3%A3o-do-destinat%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042642674-NFC-e-de-entrega-a-domic%C3%ADlio-sem-a-identifica%C3%A7%C3%A3o-do-destinat%C3%A1rio)  
> **ID:** `360042642674` | **Última Atualização:** 2026-07-22T16:07:25Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444062467095)

 MENSAGEM:**

[787-Rejeição]: NFC-e de entrega a domicílio sem a identificação do destinatário.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444037822999)

 SOLUÇÃO:**

Sempre que houver entrega em domicílio, é obrigatório informar os dados do destinatário da NFC-e.

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444062471447)

 Acesse "**[Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)**

(Caminho de acesso: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*)

- Aba: "**NF-e/NFC-e"**

- Indicador de Presença para NF-e/NFC-e: = **4-NFC-e com entrega em domicilio**

Quando a TOP estiver configurada com a opção 4, o parceiro da nota deverá ser devidamente registrado com os dados do endereço para que seja preenchido no XML da NFC-e o endereço de entrega.

Ou seja, não deverá ser utilizado um parceiro *'genérico'*, e sim um parceiro *'real'*, com os dados de endereço devidamente configurados.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444037825559)

 Após os ajustes, gere lote da NFC-e novamente.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444037827479)

 CAUSA:**

Quando for emitida uma NFC-e com o indicador de presença do comprador como "4 - NFC-e em operação com entrega a domicílio" e não for informado os dados do destinatário, será retornado a rejeição.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444062478615)

 OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)