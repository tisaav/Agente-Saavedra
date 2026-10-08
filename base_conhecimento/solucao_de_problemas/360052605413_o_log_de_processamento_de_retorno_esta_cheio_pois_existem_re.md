# O log de processamento de retorno está cheio, pois existem registros de processamentos realizados á mais de 90 dias

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360052605413-O-log-de-processamento-de-retorno-est%C3%A1-cheio-pois-existem-registros-de-processamentos-realizados-%C3%A1-mais-de-90-dias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052605413-O-log-de-processamento-de-retorno-est%C3%A1-cheio-pois-existem-registros-de-processamentos-realizados-%C3%A1-mais-de-90-dias)  
> **ID:** `360052605413` | **Última Atualização:** 2026-07-22T15:29:40Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15935758440983)

 MENSAGEM:**

O log de processamento de retorno está cheio, pois existem registros de processamentos realizados á mais de 90 dias.
Isso pode causar lentidão no processamento e é altamente recomendável que você realize uma limpeza.

 

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15935734357655)

 SOLUÇÃO:**

1. A mensagem acima trata-se de um aviso. Caso opte por **"Remover os arquivos mais antigos"**, o que é altamente recomendável : Os registros que serão eliminados automaticamente por esta rotina, são dados de log gerados ao processar os arquivos de retorno, estes são apresentados num pop-up na tela ao término da execução, mostrando quais registros foram processados ou não.

1. Acontece que, tais registros, a longo prazo, não são necessários para análise, porém ocupam um espaço significativo no banco de dados.

1. Então com esta opção, poderá ser feita a limpeza automática de tais registros, para não afetar o espaço na base de dados, bem como o desempenho desta rotina. Sendo que a eliminação destes dados não constitui em risco de perda de informações necessárias para as consultas dos títulos financeiros.