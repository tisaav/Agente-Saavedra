# Erro: A quantidade de dias apontadas como lotação do funcionário código xxx, na empresa x, referência xxxx-xx-xx 00:00:00.0 excede a quantidade de dias da referência

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/35315524289175-Erro-A-quantidade-de-dias-apontadas-como-lota%C3%A7%C3%A3o-do-funcion%C3%A1rio-c%C3%B3digo-xxx-na-empresa-x-refer%C3%AAncia-xxxx-xx-xx-00-00-00-0-excede-a-quantidade-de-dias-da-refer%C3%AAncia](https://ajuda.sankhya.com.br/hc/pt-br/articles/35315524289175-Erro-A-quantidade-de-dias-apontadas-como-lota%C3%A7%C3%A3o-do-funcion%C3%A1rio-c%C3%B3digo-xxx-na-empresa-x-refer%C3%AAncia-xxxx-xx-xx-00-00-00-0-excede-a-quantidade-de-dias-da-refer%C3%AAncia)  
> **ID:** `35315524289175` | **Última Atualização:** 2026-07-29T13:20:53Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628669359767)

 **MENSAGEM**

Erro: A quantidade de dias apontadas como lotação do funcionário código xxx, na empresa x, referência xxxx-xx-xx 00:00:00.0 excede a quantidade de dias da referência.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628669364247)

 **SITUAÇÃO**

O erro ocorre ao acessar **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e clicar em **"Liberar para eSocial"**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628669365143)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628648085527)

 Acesse a tela **"Configuração Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários) e verifique a **data de admissão** do colaborador.
 

![Erro A quantidade de dias apontadas como lotação do funcionário código 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628648089751)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628648091799)

 Acesse a tela **"Movimentação de Tomador de Serviço"** (Pessoal+ » Rotinas Folha » Movimentação de Tomador de Serviço) e verifique a **"Data inicial da lotação"** no histórico.
 

![Erro A quantidade de dias apontadas como lotação do funcionário código 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628669375127)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628648094999)

 Alinhe as **datas de admissão** e **alocação do tomador**, garantindo que sejam iguais ou que a data de alocação seja posterior à data de admissão.
 

![Erro A quantidade de dias apontadas como lotação do funcionário código 3.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628669378711)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628669383063)

 Após o ajuste das datas, retorne ao **"Gerenciador de Folhas"** e clique novamente em **"Liberar para eSocial"**.
 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/35315535367575)

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/35628669383703)

 **CAUSA**

O erro é causado por **divergências entre as datas** de admissão do colaborador e as datas de alocação no tomador de serviço. O sistema detecta inconsistência quando a data inicial da lotação é anterior à data de admissão do funcionário.