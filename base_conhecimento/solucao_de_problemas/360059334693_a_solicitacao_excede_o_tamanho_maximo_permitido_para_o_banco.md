# A solicitação excede o tamanho máximo permitido para o banco de dados, que é de 11 GB

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360059334693-A-solicita%C3%A7%C3%A3o-excede-o-tamanho-m%C3%A1ximo-permitido-para-o-banco-de-dados-que-%C3%A9-de-11-GB](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059334693-A-solicita%C3%A7%C3%A3o-excede-o-tamanho-m%C3%A1ximo-permitido-para-o-banco-de-dados-que-%C3%A9-de-11-GB)  
> **ID:** `360059334693` | **Última Atualização:** 2026-07-22T15:26:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251993108375)

 MENSAGEM**:

[ORA-12953]: A solicitação excede o tamanho máximo permitido para o banco de dados, que é de 11 GB.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251993113239)

 SOLUÇÃO**:

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453225931031)

 Ações Paliativas, para liberar espaço no Banco de Dados**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251993123351)

 Limpe, exclua informações de tabelas temporárias

Tabelas: TSILOG, TSILAC, TSIACM, TSIRLG, TSILGT, TSIACM, TSISESSAOITERACAO, TSILRE, TSIESTATSERVICO, TSIPARLGT, DDL_LOG, TSIREGMOD, TGFLIV_EXC, TSIATA TIPO = 'I' 

 

Comando:

```text
TRUNCATE TABLE TSILOG;
/
TRUNCATE TABLE TSILGT;
/
TRUNCATE TABLE TSILAC;
/
TRUNCATE TABLE TSIACM;
/
ALTER TABLE TSIACM DROP CONSTRAINT FK_TSIACM_TSIRLG;
/
TRUNCATE TABLE TSIRLG; 
/
ALTER TABLE TSIACM ADD (CONSTRAINT FK_TSIACM_TSIRLG FOREIGN KEY (CODUSU, SEQACESSO) REFERENCES TSIRLG (CODUSU,SEQACESSO));
/
TRUNCATE TABLE TSISESSAOITERACAO;
/
TRUNCATE TABLE TSILRE;
/
TRUNCATE TABLE TSIESTATSERVICO;
/
TRUNCATE TABLE TSIPARLGT;
/
TRUNCATE TABLE DDL_LOG;
/
TRUNCATE TABLE TSIREGMOD;
/
TRUNCATE TABLE TGFLIV_EXC;
/
DELETE TSIATA WHERE TIPO = 'I';
```

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16252018314263)

 Exclua Bases que não estão em uso, por Exemplo: Base de Homologação, Teste, Treinamento

(Recomendável que as ações acima sejam feitas por equipe específica DBA/TI da empresa, terceiro ou  contratado serviços da Sankhya de TI.)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16252018318487)

 Verifique outras tablespaces no banco de dados, que não são do servidor de uso de aplicações Sankhya e também estão consumindo espaço no banco e proceda com a devida manutenção.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251993140759)

 No sistema SankhyaOM/JivaEVo, ajuste o parâmetro **"****DIASVENCTFILE-Dias p/ vencimento de arquivos temporários" **(Configurações » Avançado » Preferências). Configura-se em dias, para que o sistema exclua arquivos temporários, dependendo do fluxo de transações, isso pode 'retardar', mas não impedir que volte a ocorrer a mensagem novamente.

 

**

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/28453225931031)

 Ação definitiva, para espaço em banco de dados**

Considere comprar a licença do Banco De Dados, para que não sofra limitação de espaço em banco de dados.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251993153175)

 CAUSA**:

Ocorre quando o cliente está usando uma aplicação de banco gratuita/free, geralmente Oracle XE, no qual este tem limitação de tamanho de alocação de dados no banco de dados que é 11GB.