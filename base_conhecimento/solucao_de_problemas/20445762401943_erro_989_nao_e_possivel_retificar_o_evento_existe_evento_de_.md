# Erro 989- Não é possível retificar o evento. Existe evento de pagamento associado  - Pessoal +/W

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/20445762401943-Erro-989-N%C3%A3o-%C3%A9-poss%C3%ADvel-retificar-o-evento-Existe-evento-de-pagamento-associado-Pessoal-W](https://ajuda.sankhya.com.br/hc/pt-br/articles/20445762401943-Erro-989-N%C3%A3o-%C3%A9-poss%C3%ADvel-retificar-o-evento-Existe-evento-de-pagamento-associado-Pessoal-W)  
> **ID:** `20445762401943` | **Última Atualização:** 2026-08-18T20:04:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20445733757975)

 **MENSAGEM:**

[Erro 989]: Não é possível retificar o evento. Existe evento de pagamento associado que será impactado pelo evento retificador. Recibos impactados: R.
Ação Sugerida: Retificar ou excluir o evento de Pagamento que contenha o demonstrativo de pagamento que está causando a inconsistência e tentar enviar o evento novamente.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20445762355223)

SOLUÇÃO:**

Acesse a tela **Gerenciador de folhas*** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) * campo **Liberação para o Esocial**.

![Gerenciador de folha 09-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20446422305815)

É necessário bloquear a liberação da folha filtrando pela referencia, empresa e funcionário.

![Liberação Esocial 09-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20446422325655)

Após bloquear com sucesso. Acesse a tela **Central do Esocial** *(Pessoal+ » Rotinas Folha » Central do eSocial)* faça uma  nova geração dos eventos.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/20445762364823)

Envie o S-1210 de alteração ou exclusão com sucesso, depois envie o S-1200/S-2299 de alteração.

Em seguida acesse o Gerenciador de Folhas novamente e realize a Liberação do Eventos para envio ao eSocial.

![Gerenciador de folha 09-01.png](https://ajuda.sankhya.com.br/hc/article_attachments/20446422305815)

Gere novamente os eventos e envie novamente o S-1210 com todas as datas de pagamento corretas. 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20445762370071)

CAUSA:**

O eSocial trabalha de forma cronológica, para alterar o evento de remuneração folha (S-1200, S-2299, S-2399), é preciso excluir ou alterar primeiramente o pagamento (S-1210). 

Ocorre quando o envio do S-1200/S-2299/S-2399, que é de alteração, está sendo alterado depois que já enviou o S-1210 relativo ao pagamento da folha.

**Exemplo:** 

Folha Normal da referência  01/2023 com pagamento em 31/01/2023.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20445762379543)

  É enviado o S-1200 (Folha Normal) e, em seguida, o S-1210(Pagamento);

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/20445733779479)

 É gerada uma alteração na folha de pagamento, então é necessário excluir o S-1210 para enviar o S-1200.