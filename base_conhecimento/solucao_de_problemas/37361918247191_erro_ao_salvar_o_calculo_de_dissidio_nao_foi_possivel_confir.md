# Erro ao Salvar o Cálculo de Dissídio: Não Foi Possível Confirmar a Folha de Pagamento

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37361918247191-Erro-ao-Salvar-o-C%C3%A1lculo-de-Diss%C3%ADdio-N%C3%A3o-Foi-Poss%C3%ADvel-Confirmar-a-Folha-de-Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/37361918247191-Erro-ao-Salvar-o-C%C3%A1lculo-de-Diss%C3%ADdio-N%C3%A3o-Foi-Poss%C3%ADvel-Confirmar-a-Folha-de-Pagamento)  
> **ID:** `37361918247191` | **Última Atualização:** 2026-07-29T13:22:15Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37449927510551)

 MENSAGEM:**

Falha ao gravar folha. ORA-20101: Dependente 1 não cadastrado.
ORA-06512: em "SANKHYA.TRG_INC_TFPVPS", line 16
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_TFPVPS'

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/37361852680855)

 

##### **

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309941114135)

 SITUAÇÃO:**

Ao realizar o cálculo e tentar salvar a folha de dissídio, o sistema impede a gravação da folha e apresenta a mensagem de erro acima, relacionada à ausência de dependente cadastrado e à execução de um gatilho no banco de dados.

 

##### **

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309941115671)

 SOLUÇÃO:**

Para corrigir o problema, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37449927518103)

 Acesse a tela **''Pessoal+'' **(Pessoal+ » Rotinas Folha » Acessos Pessoal Mais).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37449927519383)

 Localize o evento **''Plano Odontológico'' **utlizado na folha.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37449897561623)

 Na aba **''Avançado''**, desmarque a opção** ''Tem seus valores recalculados''**.

 

![image - 2026-01-05T135314.542.png](https://ajuda.sankhya.com.br/hc/article_attachments/37450097240855)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37449927523095)

 Salve o evento.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37449927525015)

 Recalcule a folha de dissídio.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37449927526551)

 Salve novamente a folha.

 

##### **Por que eventos de convênio médico e odontológico não devem ser reajustados no dissídio?**

##### O dissídio coletivo tem como finalidade **reajustar verbas** de natureza salarial, como **salário base**, **horas** **extras**, **adicionais **e **outras verbas** que compõem a remuneração do colaborador. Já os eventos de **convênio médico e odontológico** possuem natureza **indenizatória ou de desconto**, não sendo considerados verbas salariais. Por esse motivo, **não devem ser impactados pelo reajuste do dissídio**, nem configurados para recálculo nesse processo.

#####  

##### **

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309954002199)

 CAUSA:**

O erro ocorre porque o evento de plano odontológico estava **interferindo no salvamento da folha**, gerando **duplicidade de linhas de desconto** durante o cálculo do dissídio. 

Esse comportamento acontece devido à configuração do evento para recalcular valores no dissídio, o que não se aplica a eventos de natureza indenizatória ou de desconto, como convênios odontológicos.