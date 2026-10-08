# Advertência 1989 - Rubrica de desconto informada sem parcela prevista

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35787549433495-Advert%C3%AAncia-1989-Rubrica-de-desconto-informada-sem-parcela-prevista](https://ajuda.sankhya.com.br/hc/pt-br/articles/35787549433495-Advert%C3%AAncia-1989-Rubrica-de-desconto-informada-sem-parcela-prevista)  
> **ID:** `35787549433495` | **Última Atualização:** 2026-07-29T13:21:03Z

---

**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309884759831)

********

| Módulo: Pessoal+ » Rotinas Folha » Central do eSocial |
| --- |

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/35787519372823)

**SITUAÇÃO**

  Ao tentar enviar os eventos de remuneração **"S-1200"**, **"S-2299"** ou **"S-2399"** para o eSocial, o sistema apresenta a advertência 1988. Ela indica que foi informado desconto de empréstimo consignado para o trabalhador, porém não há parcela registrada no Portal Emprega Brasil para a competência informada.

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/35787549419159)

**SOLUÇÃO**

Para resolver a advertência 1988, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/35787549420311)

  Exclua o cálculo da folha de pagamento do trabalhador.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/35787519374615)

  Remova o lançamento do movimento referente ao desconto de empréstimo consignado (**"rubrica 9253"**).

![3](https://ajuda.sankhya.com.br/hc/article_attachments/35787549422231)

  Confirme se os dados do contrato de empréstimo consignado estão corretos (valor da parcela, código da instituição financeira e número do contrato).

![4](https://ajuda.sankhya.com.br/hc/article_attachments/35787519378967)

  Recalcule a folha do funcionário.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/35787519378967)

  No **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas), libere a folha para o eSocial.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/35787519379351)

  Acesse a **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial), gere novamente o evento de remuneração e efetue o envio.

![6](https://ajuda.sankhya.com.br/hc/article_attachments/35787519380119)

  Após o ajuste, o evento de remuneração deverá ser recepcionado com sucesso pelo eSocial, sem a advertência.

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/35787519380631)

**CAUSA**

  A advertência 1988 ocorre quando o empregador informa um desconto de empréstimo consignado (**"rubrica 9253"**), mas não há parcela correspondente registrada no Portal Emprega Brasil para a competência informada, ou quando ocorrem divergências nos valores e dados do contrato.