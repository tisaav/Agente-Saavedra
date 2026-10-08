# RNTRC não é gerado no XML do MDF-e

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/41869462949911-RNTRC-n%C3%A3o-%C3%A9-gerado-no-XML-do-MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/41869462949911-RNTRC-n%C3%A3o-%C3%A9-gerado-no-XML-do-MDF-e)  
> **ID:** `41869462949911` | **Última Atualização:** 2026-07-22T13:26:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869506098199)

 MENSAGEM:**

RNTRC não é gerado no XML do MDF-e

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869462939671)

 SOLUÇÃO:**

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869506099991)

 **Verifique se o parâmetro **''RNTRCFROTAPROP''** - **''Enviar RNTRC da empresa para frota própria?''** está ativo.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869462940951)

 Acesse **Configurações » Cadastros » Veículos » aba Propriedades** e confira o estado da flag **"Veículo da empresa"** para o veículo utilizado na viagem.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869462941975)

 Com base no estado da flag, confirme onde o RNTRC deve estar cadastrado:

- 

Flag **marcada** → cadastre/confira o RNTRC em **Configurações » Cadastros » Empresas » aba Naturezas**.

- 

Flag **desmarcada** → cadastre/confira o RNTRC em **Configurações » Cadastros » Veículos » aba Propriedades**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869506103575)

 Valide o RNTRC no Portal da ANTT:

- 

[https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/](https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869506104855)

 Gere novamente o XML do MDF-e em **Comercial » Rotinas » Viagens de Transporte (MDF-e)** e confirme se o grupo de tags do RNTRC foi incluído.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869506106135)

 OBSERVAÇÃO:**

O RNTRC é único por empresa. A SEFAZ trata essa informação como opcional, mas quando enviada, é validada — se estiver inválida ou não encontrada por conta da flag mal configurada, a emissão pode ser rejeitada (erros 681 ou similares).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41869462945559)

 CAUSA:**

O sistema não decide de onde buscar o RNTRC com base no "tipo de frota" isoladamente, ele segue a flag **"Veículo da empresa"**, marcada no cadastro do veículo (Configurações » Cadastros » Veículos » aba Propriedades):

- 

**Flag marcada**: o sistema busca o RNTRC **apenas** no cadastro da Empresa (Configurações » Cadastros » Empresas » aba Naturezas), mesmo que o veículo tenha um RNTRC próprio preenchido.

- 

**Flag desmarcada**: o sistema busca o RNTRC **apenas** no cadastro do próprio Veículo.

Se o RNTRC estiver preenchido no cadastro errado em relação ao estado dessa flag, o sistema simplesmente não o encontra, mesmo com o parâmetro ''RNTRCFROTAPROP''** **ativo e o dado aparentemente correto em algum dos dois cadastros.