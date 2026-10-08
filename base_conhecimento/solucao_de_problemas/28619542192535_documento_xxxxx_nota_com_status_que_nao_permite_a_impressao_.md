# Documento XXXXX. Nota com status que não permite a impressão. Favor verificar o documento. NFe ignorada na impressão

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/28619542192535-Documento-XXXXX-Nota-com-status-que-n%C3%A3o-permite-a-impress%C3%A3o-Favor-verificar-o-documento-NFe-ignorada-na-impress%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/28619542192535-Documento-XXXXX-Nota-com-status-que-n%C3%A3o-permite-a-impress%C3%A3o-Favor-verificar-o-documento-NFe-ignorada-na-impress%C3%A3o)  
> **ID:** `28619542192535` | **Última Atualização:** 2026-07-22T14:37:45Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/28619516698391)

** MENSAGEM**

A nota fiscal eletrônica encontra-se com status **"Enviada"**, mas não é possível realizar sua impressão. O sistema apresenta erro ao selecionar as impressoras, ignora a nota durante a tentativa de impressão ou exibe a mensagem: **"Documento XXXX: Nota com status que não permite a impressão"**.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39448691766807)

** SITUAÇÃO**

Ao tentar realizar a impressão, o sistema apresenta erro ao selecionar as impressoras ou informa que o documento não pode ser impresso devido ao status atual. O problema ocorre por inconsistências na aprovação SEFAZ, falta de modelo de impressão vinculado ao TOP, XML incompleto na tabela TGFNFE ou falta de configuração no Web Connection.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/28619542177303)

** SOLUÇÃO**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39448691770519)

 Verifique o **"Status da nota fiscal"** na tela "Portal de vendas" (Comercial >> Consulta >> Portal de vendas), "Portal de compras"(Comercial >> Consulta >> Portal de compras) ou "Portal de mov. interna"(Comercial >> Consulta >> Portal de mov.interna). Certifique-se de que a nota está com status **"Aprovada"** pela SEFAZ.

 

OBS: Se estiver com o status diferente de aprovada, necessário validar o motivo da não aprovação. EX:  rejeições, erro de configuração(impostos e etc..).

 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39448691773079)

 Verificação do modelo(Caso a nota esteja aprovada): 

Acesse a tela **"Tipos de Operação"** (Configurações >> Cadastros >> Tipos de Operação) e localize o **"TOP"** utilizado na nota.

 -Na aba **"Impressão"**, verifique o campo **"Modelo de Impressão"**. Certifique-se de que há um modelo válido vinculado.

 -Caso não haja modelo cadastrado, acesse a tela **"Modelo de Impressão (Nota/Pedido)"** (Comercial >> Preferências >> Modelo de Impressão (Nota/Pedido)), baixe o modelo padrão disponível e configure conforme a necessidade da empresa.

 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39448680311703)

 Caso a nota seja antiga e o erro persista, realize a **"Impressão diretamente pelo portal da SEFAZ"**, pois o XML pode estar inconsistente devido a atualizações de layout.

 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39448691780759)

 Verifique se o serviço **"Web Connection"** está configurado corretamente. Caso necessário, reconfigure o serviço para restabelecer a comunicação entre o sistema e as impressoras.

 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39448691782935)

 Após as configurações, tente realizar a impressão novamente.

 

**Observações importantes:**

- 

Não utilize o modelo de DANFE para notas de terceiros.
 

1. 

Não realize aprovações via banco de dados; utilize sempre a rotina de **"Buscar autorização"**.
 

1. 

Se não tiver conhecimento técnico, solicite auxílio a um consultor.
 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/28619542182039)

** CAUSA**

- 

Ausência de modelo de impressão ou configuração incorreta do Web Connection.
 

1. 

Nota sem aprovação SEFAZ ou com status de aprovação não sincronizado.
 

1. 

Inconsistência na tabela TGFNFE causada por alterações manuais via banco de dados.
 

1. 

XML inconsistente devido a atualizações de layout de notas antigas.