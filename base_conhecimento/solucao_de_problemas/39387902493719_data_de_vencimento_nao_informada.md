# Data de vencimento não informada

> **Módulo:** Solucao de Problemas | **Subseção:** Compras e Estoque  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39387902493719-Data-de-vencimento-n%C3%A3o-informada](https://ajuda.sankhya.com.br/hc/pt-br/articles/39387902493719-Data-de-vencimento-n%C3%A3o-informada)  
> **ID:** `39387902493719` | **Última Atualização:** 2026-07-22T13:30:31Z

---

### 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39387902479767)

 SITUAÇÃO

Ao importar um arquivo XML de CT-e pelo **Portal de Importação** (**Comercial > Rotinas > Portal de Importação de XML**), o sistema pode exibir a mensagem: **"Data de Vencimento não informada."**

Essa mensagem impede a conclusão da importação e ocorre quando o campo **Dt. Vencimento** não está preenchido ou quando as preferências de importação estão configuradas para solicitar a data ao usuário, mas nenhuma data é informada.

### 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39387902480407)

 SOLUÇÃO

Para concluir a importação, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39387902481687)

 Acesse o **"Portal de Importação"** (Comercial » Rotinas » Portal de importação de XML) e localize o CT-e que apresentou o erro.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39387922792343)

 Na grade principal, preencha manualmente o campo **Dt. Vencimento** com a data desejada para o vencimento do título financeiro.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39387902482583)

 Confirme a importação. O sistema processará o CT-e sem novas ocorrências.
 

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42094565368215)

**Configurar o preenchimento automático da data de vencimento**

Caso deseje evitar o preenchimento manual em futuras importações:

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39387902484375)

 No **Portal de Importação**, clique em **Outras Opções > Preferências de Importação de CT-e.**

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39387922794135)

 No campo **Expira em**, altere a opção **Solicitar ao usuário** para uma das seguintes alternativas: 

- 

**Data Atual:**  utiliza data atual

- 

**Data de Negociação :** utiliza a data de negociação do documento. 

- 

**Data de Vencimento :** utiliza a data de vencimento informada no XML. 

- 

**Data Solicitada :** utiliza uma data específica configurada. 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39387922795671)

 Salve as alterações. A partir dessa configuração, o sistema preencherá automaticamente a data de vencimento conforme a regra selecionada.
 

### 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39387902487959)

 CAUSA

O problema ocorre quando o campo **Expira em** está configurado como **Solicitar ao usuário** e nenhuma data de vencimento é informada durante a importação do CT-e.