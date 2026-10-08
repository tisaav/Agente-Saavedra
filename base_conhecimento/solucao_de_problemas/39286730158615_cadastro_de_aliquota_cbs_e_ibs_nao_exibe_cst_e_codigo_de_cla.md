# Cadastro de Alíquota CBS e IBS - Não exibe CST e Código de Classificação Tributária

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39286730158615-Cadastro-de-Al%C3%ADquota-CBS-e-IBS-N%C3%A3o-exibe-CST-e-C%C3%B3digo-de-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286730158615-Cadastro-de-Al%C3%ADquota-CBS-e-IBS-N%C3%A3o-exibe-CST-e-C%C3%B3digo-de-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria)  
> **ID:** `39286730158615` | **Última Atualização:** 2026-09-11T19:42:29Z

---

## 

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286700921751)

 **MENSAGEM**

Os campos **"CST"** e **"Código de Classificação Tributária"** não são exibidos na tela de cadastro de alíquotas de IBS ou CBS.

## 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286700922263)

 **SITUAÇÃO**

Ao acessar as telas **"Alíquotas de IBS"** (Livros Fiscais >> Cadastros >> Alíquotas de IBS) ou **"Alíquotas de CBS"** (Livros Fiscais >> Cadastros >> Alíquotas de CBS), na guia **"Tributação"**, o usuário não consegue visualizar ou preencher os campos **"CST"** e **"Código de Classificação Tributária"** no grupo **"Dados de Tributação".**

## 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286700922903)

 **SOLUÇÃO**

Para resolver esta situação, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286700924567)

 Acesse a tela **"Alíquotas de IBS"** ou **"Alíquotas de CBS"** (Livros Fiscais >> Cadastros >> Alíquotas de IBS ou Livros Fiscais >> Cadastros >> Alíquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286700925207)

 Navegue até a guia **"Tributação"**. 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286730148247)

 Localize o grupo **"Dados de Tributação"**, que deve conter os campos **"CST"** e **"Código de Classificação Tributária"**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286730148631)

 Verifique se os campos estão visíveis e habilitados para preenchimento. Caso não estejam, seleciona a seguinte opção: "Mais opções" >> "Atualizar tabelas RTC". 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/39443832786839)

O job passa a ser executado de forma imediata e com recorrência mensal, substituindo a periodicidade diária adotada até janeiro. Essa opção está disponível a partir da versão 5.30.0 do Livros Fiscais e permite forçar a atualização das tabelas de IBS e CBS de forma imediata, sendo eficaz para correções pontuais como a ocorrida em seu ambiente. 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39443848825367)

** Ressaltamos, no entanto, que essa funcionalidade não deve ser utilizada com frequência, pois existe uma limitação de uso (**uma execução a cada 7 dias**) e sua aplicação é recomendada apenas para casos excepcionais, como este. Em condições normais, as atualizações são realizadas automaticamente pelo job mensal, não sendo necessária intervenção manual.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286730149783)

 Preencha obrigatoriamente os campos **"CST"** e **"Código de Classificação Tributária"**, selecionando valores válidos das tabelas **"TLFCSTIC"** e **"TLFCLASTRIBIC"**, respectivamente.
 

## 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39286700929303)

 **CAUSA**

A ausência dos campos **"CST"** e **"Código de Classificação Tributária"** pode ocorrer devido a:

- 

**Configuração incorreta da tela**: o grupo **"Dados de Tributação"** pode não estar configurado corretamente na guia **"Tributação"**.
 

1. 

**Versão desatualizada do sistema**: versões anteriores podem não conter a estrutura completa dos campos obrigatórios para a reforma tributária.
 

1. 

As tabelas **TLFCLASTRIBIC** e **TLFCSTIC** não foram devidamente alimentadas, o que está impedindo o cadastramento das alíquotas de **IBS** e **CBS**.

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/39443848825367)

 OBSERVAÇÃO:** Esse comportamento pode ocorrer em bases novas, nas quais o Job responsável por alimentar as tabelas de RTC (`TLFCLASTRIBIC` e `TLFCSTIC`) ainda não foi executado. Esse Job é processado automaticamente uma vez por mês — em ambientes recém-implantados, pode haver um intervalo até a primeira execução. Nesses casos, use a opção **"Atualizar tabelas RTC"** em **''Mais opções''**, na tela de Alíquotas de IBS/CBS) para forçar a atualização imediatamente.