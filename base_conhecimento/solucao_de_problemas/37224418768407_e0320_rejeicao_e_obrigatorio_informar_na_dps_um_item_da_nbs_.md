# E0320 Rejeição: É obrigatório informar na DPS um item da NBS para casos de importação de serviço.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224418768407-E0320-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-na-DPS-um-item-da-NBS-para-casos-de-importa%C3%A7%C3%A3o-de-servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224418768407-E0320-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-informar-na-DPS-um-item-da-NBS-para-casos-de-importa%C3%A7%C3%A3o-de-servi%C3%A7o)  
> **ID:** `37224418768407` | **Última Atualização:** 2026-07-22T14:16:37Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224418734487)

 **MENSAGEM**

E0320 Rejeição: É obrigatório informar na DPS um item da NBS para casos de importação de serviço.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224434469015)

 **SITUAÇÃO**

Ao tentar processar um **Documento de Prestação de Serviço (DPS)** referente a uma **importação de serviço**, o sistema apresenta a rejeição informando que o **código NBS não foi informado**. O usuário estava lançando uma operação de importação de serviço e não preencheu o campo obrigatório referente ao **item da Nomenclatura Brasileira de Serviços (NBS)** no documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224434471319)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224418747287)

 Acesse o **"Serviço"** (Configurações » Cadastros » Produtos » Serviço) e localize o serviço que está sendo importado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224434475543)

 Na aba **"Impostos"**, verifique se o campo **"Código NBS"** está preenchido corretamente com o código correspondente ao serviço prestado.

- 

Caso o campo esteja vazio, preencha-o com o **código NBS apropriado** conforme a Nomenclatura Brasileira de Serviços.

- 

Consulte a **"Lista de Serviços"** (Comercial » Arquivo » Cadastros » Lista de Serviços) para identificar o código correto, se necessário.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224418752023)

 Acesse a tela ****[''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e verifique o Documento de Prestação de Serviço (DPS) que apresentou a rejeição.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224434483095)

 Verifique se o serviço vinculado ao documento possui o **código NBS preenchido** no cadastro. Caso necessário, edite o item e vincule o serviço correto com o código NBS já cadastrado.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224418753431)

 Após os ajustes, **gere novamente o lote** do Documento de Prestação de Serviço para envio à Sefaz.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224418755095)

 Para conferência, verifique se o **código NBS foi gerado corretamente** no XML do documento fiscal antes do envio.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224434488087)

 **CAUSA**

A rejeição ocorre quando o **campo "Código NBS"** não é informado no **Cadastro de Serviço** para operações de **importação de serviço**. De acordo com a legislação da Reforma Tributária e as regras de validação da Sefaz, é **obrigatório informar o item da NBS** no Documento de Prestação de Serviço (DPS) quando se trata de importação de serviços, garantindo a correta identificação e tributação da operação.


---

### 🔗 Links e Referências Internas:

- [''Portal de Vendas''](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)