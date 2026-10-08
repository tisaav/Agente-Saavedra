# Arquivo não encontrado

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9777856531863-Arquivo-n%C3%A3o-encontrado](https://ajuda.sankhya.com.br/hc/pt-br/articles/9777856531863-Arquivo-n%C3%A3o-encontrado)  
> **ID:** `9777856531863` | **Última Atualização:** 2026-07-22T15:06:16Z

---

**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/15854155782679)

 MENSAGEM:**

[CORE_E05442] Arquivo não encontrado.

**

![2](https://ajuda.sankhya.com.br/hc/article_attachments/15854192800919)

 CAUSA:**

Quando o arquivo físico não existe no diretório.

**

![3](https://ajuda.sankhya.com.br/hc/article_attachments/15854192801815)

 SOLUÇÃO:**

Acesse a tela **Preferências** *(Caminho de acesso à tela: Configurações » Avançado » Preferências), *informe a chave '**FREPBASEFOLDER**-Diretório base para o repositório de arquivos' e confira se no caminho informado o arquivo realmente existe.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/15854124876567)

**O sistema verifica o arquivo da seguinte forma:**
> De acordo com o parâmetro 'FREPBASEFOLDER' será definido o diretório base para o repositório de arquivos. (Ex: C:)

> Após o diretório base configurado, serão criados os diretórios filhos para anexo: \Sistema\Anexos\

> Com base nesse caminho, o arquivo será feito o upload em: nome do diretório que é o mesmo do campo: NOMEINSTANCIA-TSIANX e a chave que é o mesmo do campo: CHAVEARQUIVO-TSIANX.

(Ex: C:\Sistema\Anexos\CabecalhoLaudo\92fcfe8a8d6cb8990cb003cc196b7919.txt)

> Caso o arquivo não esteja no diretório, a mensagem de erro realmente aparecerá, ou seja, o registro que existe na tabela: TSIANX é somente para saber qual arquivo será baixado, porém deverá ter o arquivo físico no diretório.