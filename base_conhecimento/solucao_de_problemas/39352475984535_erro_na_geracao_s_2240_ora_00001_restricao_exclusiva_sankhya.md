# Erro na Geração S-2240 | ORA-00001: Restrição Exclusiva (SANKHYA.PK TFPS2240AGNOC.EPI) Violada

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39352475984535-Erro-na-Gera%C3%A7%C3%A3o-S-2240-ORA-00001-Restri%C3%A7%C3%A3o-Exclusiva-SANKHYA-PK-TFPS2240AGNOC-EPI-Violada](https://ajuda.sankhya.com.br/hc/pt-br/articles/39352475984535-Erro-na-Gera%C3%A7%C3%A3o-S-2240-ORA-00001-Restri%C3%A7%C3%A3o-Exclusiva-SANKHYA-PK-TFPS2240AGNOC-EPI-Violada)  
> **ID:** `39352475984535` | **Última Atualização:** 2026-09-26T01:01:52Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39352484425879)

 **MENSAGEM**

Ora-00001: restrição exclusiva (SANKHYA.PK TFPS2240AGNOC.EPI) violada

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39352484427799)

 **SITUAÇÃO**

Ao tentar gerar o evento **"S-2240"** (Condições Ambientais do Trabalho - Agentes Nocivos) no módulo **"Pessoal"** (Pessoal+ » Rotinas Folha » Central do eSocial), o sistema apresenta erro de violação de restrição exclusiva. Este erro ocorre após atualização do módulo Pessoal, impedindo a geração correta dos eventos do eSocial.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39352484428055)

 **SOLUÇÃO**

Para resolver este erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39352475983639)

 Acesse a tela **"Ambiente de Trabalho"** (Pessoal+ » Rotinas Folha » SESMT » Ambiente de Trabalho) e verifique se há funcionários cadastrados em ambientes duplicados.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41274326057111)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39352484428183)

 Identifique se existe mais de um ambiente cadastrado para o mesmo funcionário com a mesma data de início de condição. Para isso basta acessar tela **"Configuração Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários) aba Ambiente de Trabalho. 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41329841019927)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39352475983767)

 Verifique se os ambientes duplicados utilizam o mesmo agente nocivo e possuem o cadastro dos mesmos EPIs.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41329856298007)

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39352475983895)

 Exclua o ambiente incorreto ou duplicado, mantendo apenas o registro válido para o funcionário.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39352484428823)

 Realize uma nova geração do evento **"S-2240"** e verifique se o erro foi solucionado.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39352484428951)

 **CAUSA**

O erro ocorre devido à duplicidade de registros no cadastro de ambientes de trabalho. Quando um funcionário está cadastrado em dois ambientes diferentes com o mesmo início de condição, utilizando o mesmo agente nocivo e os mesmos EPIs.

Esta situação é mais comum após atualizações do módulo Pessoal, quando podem ocorrer inconsistências nos cadastros de ambientes de trabalho.