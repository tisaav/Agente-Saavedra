# No Balanço Patrimonial, o somatório do saldo inicial (VL_CTA_INI) das linhas de detalhe (IND_COD_AGL= “D”) do Ativo (IND_GRP_BAL= “A”) esta diferente do somatorio do saldo final (VL_CTA_INI) das linhas de detalhe[...]

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044576454-No-Balan%C3%A7o-Patrimonial-o-somat%C3%B3rio-do-saldo-inicial-VL-CTA-INI-das-linhas-de-detalhe-IND-COD-AGL-D-do-Ativo-IND-GRP-BAL-A-esta-diferente-do-somatorio-do-saldo-final-VL-CTA-INI-das-linhas-de-detalhe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044576454-No-Balan%C3%A7o-Patrimonial-o-somat%C3%B3rio-do-saldo-inicial-VL-CTA-INI-das-linhas-de-detalhe-IND-COD-AGL-D-do-Ativo-IND-GRP-BAL-A-esta-diferente-do-somatorio-do-saldo-final-VL-CTA-INI-das-linhas-de-detalhe)  
> **ID:** `360044576454` | **Última Atualização:** 2026-07-22T15:51:32Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612377691031)

 MENSAGEM**

No Balanço Patrimonial, o somatório do saldo inicial (VL_CTA_INI) das linhas de detalhe (IND_COD_AGL= “D”) do Ativo (IND_GRP_BAL= “A”) esta diferente do somatorio do saldo final (VL_CTA_INI) das linhas de detalhe (IND_COD_AGL= “D”) do Passivo (IND_GRP_BAL= “P”).

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612377700631)

 SITUAÇÃO**

Ao tentar validar o arquivo ECD, o seguinte erro é apresentado do validador

**Observação:** Abaixo, é citado o registro J100, ***mas*** as informações podem ser consideradas para os demais registros, a depender do caso.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612377703575)

 SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612384109975)

 Tire um balancete do ano todo da empresa que está sendo analisada, neste balancete do sistema deve-se primeiro verificar:

ATIVO BATE COM PASSIVO?

- Se a resposta for **positiva**, então a sua contabilidade está correta e pode ser que esteja faltando alguma conta para vincular ao código aglutinador do Balanço Patrimonial na rotina *Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD>> Balanço Patrimonial*

- Se a resposta for **negativa**, então isso significa que sua contabilidade está com os lançamentos errados, ou seja: não foi encerrada adequadamente, sendo necessário que se acerte os lançamentos de modo que o ativo bata com o passivo.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18612384116631)

 Faça uma comparação dos saldos das contas partindo do balancete do sistema para o balanço do arquivo txt (BLOCO J100), sugiro que se compare sempre olhando primeiro no balancete do sistema para o do txt e não ao contrário, pois no txt aparecem muito mais contas, no balanço do txt as contas estarão disponibilizadas.

Verifique quais contas são vinculadas a estes códigos na rotina Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD>> Balanço Patrimonial.