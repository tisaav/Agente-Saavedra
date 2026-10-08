# O somatório dos campos 'Valor da obrigação a recolher' dos registros E116, não é igual à soma dos campos 'Valor total de ICMS a recolher' e 'Valores recolhidos ou a recolher, extrapuração' do registro E110

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617693-O-somat%C3%B3rio-dos-campos-Valor-da-obriga%C3%A7%C3%A3o-a-recolher-dos-registros-E116-n%C3%A3o-%C3%A9-igual-%C3%A0-soma-dos-campos-Valor-total-de-ICMS-a-recolher-e-Valores-recolhidos-ou-a-recolher-extrapura%C3%A7%C3%A3o-do-registro-E110](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617693-O-somat%C3%B3rio-dos-campos-Valor-da-obriga%C3%A7%C3%A3o-a-recolher-dos-registros-E116-n%C3%A3o-%C3%A9-igual-%C3%A0-soma-dos-campos-Valor-total-de-ICMS-a-recolher-e-Valores-recolhidos-ou-a-recolher-extrapura%C3%A7%C3%A3o-do-registro-E110)  
> **ID:** `360044617693` | **Última Atualização:** 2026-07-22T15:52:36Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589043733143)

 MENSAGEM:**

O somatório dos campos 'Valor da obrigação a recolher' dos registros E116, não é igual à soma dos campos 'Valor total de ICMS a recolher' e 'Valores recolhidos ou a recolher, extrapuração' do registro E110.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589028642711)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589028648855)

 **Acesse a tela** "Empresa"*** (Caminho de acesso: Comercial » Preferências):*

- Selecione a empresa, acesse a aba: **"EFD-Escrituração Fiscal Digital"**

- Selecione **"Tipo de Escrituração"** - EFD

- Painel: Blocos e Registros *»* Selecione o Bloco 'E'.

- No Painel: 'Registros' verifique se para o registro E116 está marcada a opção **"Gerar Registro'"**. Caso não esteja efetuar a marcação e seguir para o passo seguinte.

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15328242588951)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589043739159)

 Acesse: **"Obrigações do ICMS e ICMS ST a Recolher"*** (Caminho de acesso: Livros Fiscais » Avançado » Escrituração Fiscal Digital ).*

- Preencha os campos com os dados pertinentes ao recolhimento de ICMS e ICMS-ST e salve os registros, com o aval do contador da empresa.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589043751447)

 Acesse: **"Registro de Apuração do ICMS"*** (Caminho de acesso: Livros Fiscais » Relatórios).*

- Preencha os campos respectivo a empresa e período.
Clique em **'Abrir'** para visualizar os lançamentos feito na rotina de **"Obrigações do ICMS e ICMS ST a Recolher"**,  confira os valores na Guia de **"Demonstrativos"** para ICMS e ICMS-ST'.

1. Após a validação clique em **'Salvar'.**

1. Lembrando que, cada alteração feita na tela de **"Obrigações do ICMS e ICMS ST a Recolher"**, sempre é necessário acessar a tela de **"Registro de Apuracão do ICMS"**, clicar em **abrir **e **salvar**, antes de gerar o arquivo EFD-Fiscal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589043756567)

 Acesse **"EFD - Escrituração Fiscal Digital - ICMS/IPI"*** (Caminho de acesso: Livros Fiscais » Conexão)*, gere novamente o arquivo e valide no PVA.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16589028672535)

 CAUSA:**

Mensagem apresentada quando se possui obrigações a recolher referente a ICMS e ICMS-ST, porém não foi informada a obrigação a recolher e não salvou a Apuração do ICMS.