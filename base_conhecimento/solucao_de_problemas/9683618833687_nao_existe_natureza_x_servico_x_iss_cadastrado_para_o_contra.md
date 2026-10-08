# Não existe 'Natureza x Serviço x ISS' cadastrado para o Contrato: X, Empresa: X e Natureza: null

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9683618833687-N%C3%A3o-existe-Natureza-x-Servi%C3%A7o-x-ISS-cadastrado-para-o-Contrato-X-Empresa-X-e-Natureza-null](https://ajuda.sankhya.com.br/hc/pt-br/articles/9683618833687-N%C3%A3o-existe-Natureza-x-Servi%C3%A7o-x-ISS-cadastrado-para-o-Contrato-X-Empresa-X-e-Natureza-null)  
> **ID:** `9683618833687` | **Última Atualização:** 2026-07-22T15:06:30Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/16777470798999)

**MENSAGEM**

[SVC_E00334]: Não existe **"Natureza x Serviço x ISS"** cadastrado para o Contrato: X, Empresa: X e Natureza: null.
 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/16777470804887)

**SITUAÇÃO**

Ao tentar realizar o faturamento de um contrato, o sistema bloqueia a operação e apresenta a mensagem de exceção informando que não existe o vínculo entre **"Natureza x Serviço x ISS"** cadastrado para o contrato específico.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/16777484440343)

**CAUSA**

O erro ocorre porque a natureza de operação utilizada no contrato não possui o vínculo cadastrado com o serviço correspondente. O sistema exige que, para contratos de serviço que envolvem cálculo de **"ISS"**, exista uma relação configurada entre a natureza de operação, o serviço prestado e a tributação de **"ISS"** aplicável. Sem esse vínculo, o sistema não consegue identificar as regras tributárias necessárias para processar o faturamento, bloqueando a operação.
 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16777470807447)

**SOLUÇÃO**

Verifique se as alíquotas de **"ISS"** e o serviço estão corretas nas seguintes telas:
 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/16777450867223)

 Na tela **"Natureza x Serviço"** (Contratos e Serviços >> Arquivos >> Cadastros >> Naturezas >> Natureza x Serviço)
 

![Natureza x Serviço](https://ajuda.sankhya.com.br/hc/article_attachments/9683406422039)

 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/16777470813975)

 Na tela **"Natureza de Receita e Despesas"** (Configurações >> Cadastros >> Gerencial >> Natureza de Receitas e Despesas), aba **"Serviços autorizados"**.
 

![Natureza de Receita e Despesas](https://ajuda.sankhya.com.br/hc/article_attachments/16777470817687)

 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/16777470819479)

 Na tela **"Faturamento de contratos"** (Contratos e Serviços >> Rotinas >> Faturamento de Contratos), aba **"Filtro Personalizado"**, campo **"Considerar contratos/perfil/serviço"**.
 

![Faturamento de contratos](https://ajuda.sankhya.com.br/hc/article_attachments/16777470822423)

 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/16777470827927)

 A opção **"Considerar contratos/perfil/serviço"** funciona da seguinte maneira:
 

- 

Caso o parceiro possua um perfil vinculado e este tenha um perfil de consumo, na nota gerada no faturamento do contrato com essa opção marcada serão gerados também itens para cada produto desse perfil de consumo do parceiro.
 

1. 

Se esta opção estiver desmarcada e o parâmetro **"Contrato para software? - CONTSOFT"** estiver ligado, o sistema validará se existe **"ISS"** cadastrado para a relação Natureza x Serviço e incluirá um item na nota com valor zero para o serviço encontrado na relação com a natureza.
 

1. 

Caso a opção esteja desmarcada, considere marcar e realizar o teste.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/40213462041111)

 Após realizar as configurações, tente executar novamente o faturamento do contrato.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16777484440343)

 CAUSA:**

Quando as configurações necessárias de Narureza X Serviço X ISS não estão devidamente configurados.