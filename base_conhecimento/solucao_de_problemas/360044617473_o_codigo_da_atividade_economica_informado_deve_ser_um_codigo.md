# O código da atividade econômica informado deve ser um código válido da tabela 9

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617473-O-c%C3%B3digo-da-atividade-econ%C3%B4mica-informado-deve-ser-um-c%C3%B3digo-v%C3%A1lido-da-tabela-9](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617473-O-c%C3%B3digo-da-atividade-econ%C3%B4mica-informado-deve-ser-um-c%C3%B3digo-v%C3%A1lido-da-tabela-9)  
> **ID:** `360044617473` | **Última Atualização:** 2026-07-22T15:52:53Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416187286679)

 MENSAGEM:**

[MS1106]: O código da atividade econômica informado deve ser um código válido da tabela 9.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416153518871)

 SITUAÇÃO:**
Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416187290647)

 SOLUÇÃO:**

Considere o comportamento da aplicação, conforme abaixo:

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416153521943)

 Serviço:**
*Configurações » Cadastros » Produtos » Serviço*

 

**

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416153521943)

 Produto:**
*Configurações » Cadastros » Produtos » Produtos*

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416153522967)

 O sistema verifica se o produto ou serviço possui o campo 'Enquadrado no Reintegra/Prev'(Aba: Impostos) configurado:

 

![O_c_digo_da_atividade_econ_mica_informado_deve_ser_um_c_digo_1.png](https://ajuda.sankhya.com.br/hc/article_attachments/14996664602775)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416187293719)

 Se estiver configurado, o sistema verifica se o campo **"Cód. Atividade CPRB (Reintegra/Prev.)"** está preenchido. Este campo estando preenchido, ele o utiliza como código de atividade. 

Não estando preenchido o campo Cód. Atividade CPRB (Reintegra/Prev.) o sistema verifica se o campo **"Código Atividade Reintegra"** está preenchido e se estiver o sistema o utiliza como código de atividade.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416187294999)

 Se o campo Código Atividade Reintegra não estiver preenchido, ele verifica se trata-se de receita oriunda da venda de um produto e ou serviço.

- Se Produto: sendo a receita oriunda da venda de um produto ele considera o conteúdo do campo 'NCM' da aba Geral do cadastro do produto;

- Se Serviço: sendo a receita oriunda da venda de um serviço ele verifica o conteúdo do campo 'CNAE' informado na aba Impostos do cadastro de serviços;

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416153527575)

 Estando o campo **"CNAE"** preenchido ele o utiliza como código de atividade. Caso contrário, não estando o campo CNAE preenchido, ele utiliza o conteúdo do campo **"Código Atividade Prest. Serviços e Produtos"** informado na aba **"Reintegra Previdência"** da tela **"Preferencias Empresas"**.

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416153528343)

 Caso o campo **"Enquadrado no Reintegra/Prev"** não esteja configurado ele utiliza o conteúdo do campo Código Atividade Prest. Serviços e Produtos informado na aba Reintegra Previdência da tela Preferencias Empresas *(Caminho de acesso: Comercial » Preferências » Empresa).*

 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416153531159)

 Efetue os devidos ajustes, de acordo com a considerações acima, caso tenha dúvidas quanto à informação do Código CNAE, busque orientações do Contador para obter o valor correto.

 

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416203867927)

 Após os ajustes, transmita novamente o Reinf.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16416203874327)

 CAUSA:**

Ocorre quando informamos um 'Código de Atividades, Produtos e Serviços Sujeitos à CPRB' não constante na tabela 9 disponível no 'Anexo I dos Leiautes da EFD-Reinf - Tabelas', disponível no link: [http://sped.rfb.gov.br/arquivo/download/2779](http://sped.rfb.gov.br/arquivo/download/2779)