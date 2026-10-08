# Nota Fiscal Eletrônica com status 'Aguardando Autorização'

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833-Nota-Fiscal-Eletr%C3%B4nica-com-status-Aguardando-Autoriza%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833-Nota-Fiscal-Eletr%C3%B4nica-com-status-Aguardando-Autoriza%C3%A7%C3%A3o)  
> **ID:** `360043004833` | **Última Atualização:** 2026-07-22T16:10:19Z

---

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16458013799319)

 SITUAÇÃO:**

Esta mensagem ocorre quando a causa/tratativa de Nota Fiscal Eletrônica está pendente de autorização, ou seja, notas onde a coluna 'Status NF-e' no Portal de Vendas encontra-se como 'Aguardando Autorização' (STATUSNFE = E).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16458013804055)

 SOLUÇÃO:**

 

**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457966612887)

 **Através da Chave NF-e gerada para a respectiva nota, acesse o site da SEFAZ NACIONAL e realize a **Consulta** dessa, através do link [http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=](http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457966616343)

 Repita a consulta através da opção “Portais Estaduais da NF-e”, selecionando o Estado da Empresa emissora e buscando a opção de Consulta NF-e por chave de acesso.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16458013818135)

 Caso a respectiva NF-e esteja AUTORIZADA nos ambientes acima:

- Selecione a nota no "**PORTAL DE VENDAS" **(Caminho de acesso:* Comercial » Consulta*), no botão NF-e, acesse a opção “**Consulta situação atual da nota**”.

- Será exibida uma caixa de diálogo informando que a situação da nota no sistema está diferente da situação atual da SEFAZ.

- Clique em sim e confira a mudança do Status NF-e de Aguardando autorização para APROVADA.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457966621463)

 Caso a respectiva NF-e esteja INEXISTENTE nos ambientes citados.

- De forma geral, a SEFAZ de cada Estado possui um prazo mínimo de **24 horas** para que o processamento da respectiva NF-e ocorra, dessa forma, o ideal é aguardar esse prazo, utilizando a opção Buscar Autorização do botão NF-e para solicitar o retorno dessa autorização.

- Caso o prazo de 24 horas tenha passado, e a aprovação não tenha ocorrido, será necessário uma análise do log de envio dessa NF-e junto ao Service Desk. Se essa equipe comprovar o não recebimento da NF-e junto à SEFAZ, os mesmos farão a liberação/exclusão da nota.

- Se essa equipe comprovar o recebimento da NF-e junto à SEFAZ, será informado o número de recebimento ao cliente (nRec), para que junto ao Contador seja solicitada uma análise desse número junto à SEFAZ, autorizando ou não sua exclusão.

**

![Atenção FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16458013824791)

 IMPORTANTE:**

Ressaltamos que mesmo após o prazo de 24 horas a liberação de exclusão dessa NF-e é uma responsabilidade do cliente e só será realizada mediante **formalização de autorização via e-mail**, visto que não é possível que a Jiva/Sankhya se responsabilize por possíveis processamentos futuros de um documento já entregue.

Segue modelo de e-mail a ser direcionado.

*Eu, (NOME DO RESPONSÁVEL PELA AUTORIZAÇÃO), responsável pela Empresa (NOME DAEMPRESA), s**olicito a alteração de STATUSNFE das notas de número único 'XXXXX' e 'YYYYY' de Aguardando Autorização para Aguardando correção, de forma que a exclusão e/ou reprocessamento dessas notas possa ser liberada em meu sistema.*

*Estou ciente que esta alteração sem a consulta prévia à SEFAZ através do número de recebimento gerado nessa, pode resultar em divergências entre as informações presentes no meu sistema e na Secretaria da Fazenda.*

*Caso essa divergência seja detectada, além de impactos fiscais, estou ciente que o Help Desk não se responsabilizará pelo retorno desses dados ao sistema, por se tratar de um procedimento realizado diretamente no banco de dados, dessa forma um consultor da Franquia será acionado.*

                                                                                                                                              

Caso o cliente por algum motivo interno não possa aguardar o respectivo prazo e necessite liberar a nota de imediato, busque em nossa Central o tópico 'Pendente de Retorno', para que utilize esse processo na tentativa de uma aprovação que não impacte a nota não autorizada.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16457966626455)

 CAUSA:**

O status NF-e 'Aguardando Autorização', em sua maioria, ocorre quando o documento é enviado à SEFAZ, porém não acontece a autorização imediata como abaixo:

- O sistema direcionou os dados da respectiva NF-e.

- A SEFAZ confirmou o recebimento.

- Nessa confirmação foi gerado um número de recebimento (nRec).

- Contudo, a SEFAZ não retornou os dados de autorização da mesma (Isso pode ocorrer por alguma indisponibilidade momentânea do Órgão).