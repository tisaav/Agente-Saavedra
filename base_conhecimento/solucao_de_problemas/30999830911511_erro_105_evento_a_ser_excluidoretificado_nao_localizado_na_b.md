# Erro 105 - Evento a ser excluído/retificado não localizado na base do eSocial

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30999830911511-Erro-105-Evento-a-ser-exclu%C3%ADdo-retificado-n%C3%A3o-localizado-na-base-do-eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/30999830911511-Erro-105-Evento-a-ser-exclu%C3%ADdo-retificado-n%C3%A3o-localizado-na-base-do-eSocial)  
> **ID:** `30999830911511` | **Última Atualização:** 2026-07-29T13:19:06Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/31062562635671)

**Mensagem**

[105] O evento a ser excluído/retificado (alterado) não foi localizado na base de dados do eSocial. Ação Sugerida: Verifique se o número do recibo informado no evento corresponde ao número do recibo do evento original. Preencha com o número do recibo do arquivo a ser retificado.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/40923634307607)

**Situação**

Esta mensagem ocorre ao tentar enviar eventos de alteração do eSocial, especialmente os eventos **"S-1010"** (Tabela de Rubricas) e **"S-1000"** (Informações do Empregador), podendo outros eventos apresentar o mesmo erro. O erro aparece quando o sistema não consegue localizar o recibo original do evento que está sendo retificado, o que pode ocorrer após a atualização ou reconfiguração do certificado digital da empresa ou ao realizar alterações em rubricas que o sistema não localiza na base do eSocial.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/31062486646807)

**Solução**

Para corrigir o erro 105 no envio de eventos do eSocial, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/40923595696535)

 Acesse a tela **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e localize o evento que apresenta o erro.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/40923595697047)

 Desmarque a opção **"Utilizar a Data de Início Padrão do Sistema"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/40923634311575)

 Informe manualmente a **"Data de início de validade"** correta. Esta data deve corresponder à competência em que o evento foi originalmente enviado ou a uma data atual/futura válida (ex: 01/2025). Certifique-se de que a data não seja anterior ao cadastro da empresa no eSocial.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/40923634314135)

 Caso o evento tenha sido excluído manualmente no portal do eSocial, envie o evento a partir da competência anterior à exclusão.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/40923634315159)

 Gere novamente o evento com a nova data informada e realize o envio ao eSocial para verificar se foi recepcionado com sucesso.

 

![Alterar data envio eSocial](https://ajuda.sankhya.com.br/hc/article_attachments/31001140248215)

 

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/40923634321047)

**Causa**

O erro 105 ocorre quando o sistema tenta retificar um evento utilizando uma data de vigência diferente daquela existente na base do eSocial. As principais causas incluem:

- 

**Data de vigência incorreta:** Inconsistência entre a data do evento no sistema e a data registrada no eSocial.
 

1. 

**Exclusão manual no portal:** O evento foi excluído diretamente no portal do eSocial, tornando o recibo original inválido ou inexistente.
 

1. 

**Recibo não localizado:** O número do recibo não corresponde ao evento original devido a configurações obsoletas.
 

1. 

**Atualização de certificado:** Reconfigurações do certificado digital podem gerar pendências com datas que o sistema não consegue validar contra os envios anteriores.
 

1. 

**Alterações de incidência:** Ajustes em rubricas que geraram eventos de retificação com datas incompatíveis.