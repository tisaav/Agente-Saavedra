# Erro ao Confirmar Folha de Pagamento de Rescisão Complementar

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39353528751895-Erro-ao-Confirmar-Folha-de-Pagamento-de-Rescis%C3%A3o-Complementar](https://ajuda.sankhya.com.br/hc/pt-br/articles/39353528751895-Erro-ao-Confirmar-Folha-de-Pagamento-de-Rescis%C3%A3o-Complementar)  
> **ID:** `39353528751895` | **Última Atualização:** 2026-09-17T13:30:48Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39353528740119)

 **MENSAGEM**

Ao tentar confirmar a folha de pagamento de rescisão complementar, o sistema pode apresentar diferentes mensagens de erro, tais como:

- 

Erro relacionado a eventos de desconto de plano de saúde sendo calculados indevidamente

- 

ORA-20101: Dependente não cadastrado. ORA-06512: em "SANKHYA.TRG_INC_TFPVPS" ORA-04088: erro durante a execução do gatilho 'SANKHYA TRG_INC_TFPVPS'

- 

Bloqueio na confirmação devido a movimentações duplicadas

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39353503017239)

 **SITUAÇÃO**

A situação ocorre quando o usuário tenta **"Confirmar o cálculo da folha de rescisão complementar"** após realizar ajustes salariais, reajustes ou correções em rescisões já processadas. O erro impede a finalização do processo de confirmação da folha, bloqueando a integração com o financeiro e o envio ao eSocial.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39353528742167)

 **SOLUÇÃO**

Para resolver o erro ao confirmar a folha de rescisão complementar, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39353503018263)

 Avalie o calculo que esta tentando salvar, verifique se tem duplicidade de eventos, principalmente relacionado a plano de saúde.  

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39353503019415)

 Verifique se existem lançamentos duplicados na tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento) na referência do calculo.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39353528744471)

 Exclua os lançamentos duplicados ou os eventos indevidos que estejam causando o erro. Para isso:

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39353503020439)

 Após excluir os eventos indevidos, realize o recálculo da folha de rescisão complementar.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39353528746903)

 Tente **"Confirmar a folha"** novamente. O processo deve ser concluído sem erros.

 

**Observação importante:** Caso a rescisão complementar tenha sido calculada em uma referência diferente da data de pagamento, certifique-se de que o processo está sendo realizado na competência correta. 

Caso tenha dúvidas de como realizar o cálculo da rescisão complementar basta acessar o artigo ****[Como realizar a rescisão complementar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/34436377981079-Como-realizar-a-rescis%C3%A3o-complementar)

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39353503021719)

 **CAUSA**

O erro ocorre devido à presença de eventos duplicados ou lançamentos indevidos na movimentação da rescisão complementar. Isso pode acontecer quando:

- 

Eventos de desconto (como plano de saúde) são calculados automaticamente na competência da rescisão complementar, mesmo que não devessem estar presentes.

- 

Há movimentações duplicadas para o mesmo evento na folha de rescisão.

- 

A rescisão foi recalculada após já ter sido enviada ao eSocial, gerando inconsistências nos lançamentos.

- 

A competência de cálculo não corresponde à competência de pagamento da rescisão complementar.


---

### 🔗 Links e Referências Internas:

- [Como realizar a rescisão complementar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/34436377981079-Como-realizar-a-rescis%C3%A3o-complementar)