# Desconto de bloqueio judicial não aplicado na competência

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39368098565399-Desconto-de-bloqueio-judicial-n%C3%A3o-aplicado-na-compet%C3%AAncia](https://ajuda.sankhya.com.br/hc/pt-br/articles/39368098565399-Desconto-de-bloqueio-judicial-n%C3%A3o-aplicado-na-compet%C3%AAncia)  
> **ID:** `39368098565399` | **Última Atualização:** 2026-07-29T13:23:10Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39368098563095)

 **MENSAGEM**

O desconto de bloqueio judicial não foi aplicado no cálculo da folha mensal para a matrícula do funcionário.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39368062846487)

 **SITUAÇÃO**

Ao calcular a folha mensal de um funcionário, o sistema não considerou o desconto referente ao bloqueio judicial, mesmo havendo um lançamento mensal ativo configurado em parcelas. A competência específica foi desconsiderada na sequência de descontos, resultando na ausência do valor.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39368062846743)

 **SOLUÇÃO**

Para corrigir a ausência do desconto de bloqueio judicial na competência, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39368098563351)

Acesse a tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento) e verifique se existe o lançamento da parcela correspondente à competência em questão para o funcionário.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41273578943639)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39368098563735)

Caso identifique que a parcela está ausente, acesse a aba: Lançamento, ainda na tela: ''Lançamento de movimento'' (Pessoal+ » Rotinas Folha » Lançamento de Movimento) na competência desejada e efetue o lançamento da parcela devida (para esta ação, é necessário que o cálculo mensal esteja descartado para o respectivo funcionário). 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41273558328471)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39368098564119)

Realize a importação do lançamento na competência desejada, informando os dados do evento de bloqueio judicial (valor da parcela, número da parcela e matrícula do funcionário). Conforme evidenciado acima. 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39368062847127)

 Valide se o lançamento foi inserido corretamente para a competência e salve.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39368098564631)

 Execute novamente o **"Cálculo da Folha Mensal"** para o funcionário e confirme se o desconto de bloqueio judicial foi aplicado com sucesso.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39368062848151)

 **CAUSA**

O problema ocorre quando o lançamento mensal de uma parcela específica não é registrado no sistema. Como o evento de bloqueio judicial foi configurado como movimento mensal em parcelas, cada competência requer um lançamento individual. Se uma competência não receber o lançamento correspondente, o sistema não consegue identificar o desconto a ser aplicado, fazendo com que aquela parcela seja pulada na sequência de descontos. Isso pode acontecer por esquecimento no processo manual de lançamento das parcelas ou por falha na importação automática dos movimentos mensais.

**Em casos de movimento fixo, para que ocorra o lançamento para competência posterior a atual precisará estar fechada afim de que o evento seja levado ao cálculo.**