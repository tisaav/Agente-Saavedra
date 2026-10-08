# Erro na geração de exclusão do evento s-1200

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/43546305505431-Erro-na-gera%C3%A7%C3%A3o-de-exclus%C3%A3o-do-evento-s-1200](https://ajuda.sankhya.com.br/hc/pt-br/articles/43546305505431-Erro-na-gera%C3%A7%C3%A3o-de-exclus%C3%A3o-do-evento-s-1200)  
> **ID:** `43546305505431` | **Última Atualização:** 2026-09-18T11:33:23Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546251770647)

 **MENSAGEM**

[989] Não é possível retificar/excluir o evento. Existe evento de pagamento associado que será impactado pelo evento retificador/exclusão. Demonstrativos impactados: n:198:12.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546305495447)

 **SITUAÇÃO**

O erro ocorre ao tentar **"excluir ou retificar o evento S-1200"** (remuneração) de um colaborador no esocial, quando já existe um evento s-1210 (pagamentos de rendimentos do trabalho) vinculado à mesma referência. O sistema impede a exclusão/retificação do s-1200 enquanto houver um s-1210 relacionado, pois o pagamento já foi informado ao esocial.

O eSocial exige que a exclusão ou alteração dos eventos siga uma ordem cronológica: primeiro é preciso excluir ou retificar o evento de pagamento (S-1210) antes de alterar ou excluir o evento de remuneração correspondente.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546305495703)

 **SOLUÇÃO**

Para realizar a exclusão do evento s-1200, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546251772439)

  Acesse a **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e localize o evento S-1210 referente ao mesmo colaborador e referência do S-1200 que deseja excluir.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546251773079)

  Exclua o evento s-1210. Caso o sistema informe que existe um evento finalizado para o funcionário em uma referência posterior, será necessário excluir também os eventos S-1210 e S1200 dessas referências posteriores.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546251775255)

  Após excluir os eventos S-1210 (e, se necessário, S-1200) das referências posteriores, retorne à referência original e exclua o S-1210 e, em seguida, o S-1200 desejado.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546305498391)

  Libere novamente as folhas para o esocial no **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas). Liberação para eSocial.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546305500311)

  Reenvie os eventos S -1200 e S-1210 conforme a necessidade do processo.

 

**"Observação"**: se a empresa for do regime de competência, exclua o S-1210 da referência do evento de remuneração que está tentando excluir. Se for regime de caixa, exclua o S-1210 do mês do pagamento.

 

### Pontos de Atenção

- O eSocial trabalha de forma cronológica: sempre exclua ou retifique primeiro o evento de pagamento (S-1210) antes de alterar o evento de remuneração.

- Se a empresa for regime de caixa, pode ser necessário excluir o S-1210 de meses posteriores, caso o pagamento de uma competência tenha sido realizado em outro mês.

- Após todo o processo, confira se os eventos foram aceitos sem erros na Central do eSocial.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/43546305500695)

 **CAUSA**

O erro ocorre porque o esocial não permite a exclusão ou retificação de um evento de remuneração (S-1200) quando já existe um evento de pagamento (S-1210) vinculado à mesma referência. Para garantir a integridade das informações, exclua primeiro o evento de pagamento antes de excluir ou retificar o evento de remuneração correspondente.