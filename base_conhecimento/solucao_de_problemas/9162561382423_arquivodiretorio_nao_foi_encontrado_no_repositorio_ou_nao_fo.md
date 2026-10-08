# Arquivo/Diretório não foi encontrado no repositório, ou não foi possível lê-lo

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9162561382423-Arquivo-Diret%C3%B3rio-n%C3%A3o-foi-encontrado-no-reposit%C3%B3rio-ou-n%C3%A3o-foi-poss%C3%ADvel-l%C3%AA-lo](https://ajuda.sankhya.com.br/hc/pt-br/articles/9162561382423-Arquivo-Diret%C3%B3rio-n%C3%A3o-foi-encontrado-no-reposit%C3%B3rio-ou-n%C3%A3o-foi-poss%C3%ADvel-l%C3%AA-lo)  
> **ID:** `9162561382423` | **Última Atualização:** 2026-07-22T15:10:03Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18796821781271)

 MENSAGEM: **

[CORE_E01220] Arquivo/Diretório não foi encontrado no repositório, ou não foi possível lê-lo.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18796829399575)

 SITUAÇÃO:**

Ao tentar realizar a impressão de Cheques a mensagem é apresentada.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18796829413783)

 CAUSA:**

Quando o caminho do repositório está diferente entre o modelo e a tela Repositório de Arquivos.

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18796829430295)

 SOLUÇÃO:**

Verifique a configuração do parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER".**

Se o parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER" **estiver em branco (sem nenhum caminho), ao abrir a tela "Repositório de Arquivos", serão apresentados os arquivos da pasta ".sw_file_repository" que estão localizados dentro da pasta do usuário no C:\.

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/9162534971671)

Diante disso, é necessário verificar dentro do servidor se existe essa pasta (sw_file_repository), lembrando que dentro dela tem que ter a pasta/modelo abaixo:

*Repo://cheque/SICREDI/modelo_cheque - SICREDI.txt*

*

![mceclip2.png](https://ajuda.sankhya.com.br/hc/article_attachments/9162536399255)

*

![modelo de cheques 03-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18796821817495)

Assim, é necessário salvar ou colocar novamente esse modelo de cheque dentro dessa pasta.
Ou ainda pegar a pasta raiz e colocar naquele parâmetro, para que assim que abrir a tela de repositório de arquivo seja possível visualizar a pasta cheque.