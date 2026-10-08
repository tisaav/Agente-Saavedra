# Erro ao baixar e enviar holerites de primeira parcela e 2ª décimo terceiro salário

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39352194027927-Erro-ao-baixar-e-enviar-holerites-de-primeira-parcela-e-2%C2%AA-d%C3%A9cimo-terceiro-sal%C3%A1rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/39352194027927-Erro-ao-baixar-e-enviar-holerites-de-primeira-parcela-e-2%C2%AA-d%C3%A9cimo-terceiro-sal%C3%A1rio)  
> **ID:** `39352194027927` | **Última Atualização:** 2026-07-29T13:22:51Z

---

**

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39352181942807)

 MENSAGEM**

Falha. Não foi possível fazer o download. Motivo: Unable to get value for field 'FPRELATHOLDECIM' of class 'java.awt.Image'

 

**

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39352194017687)

 SITUAÇÃO**

Ao tentar **"baixar ou enviar por e-mail"** os holerites referentes à primeira parcela e segunda parcela do décimo terceiro salário, o sistema apresenta erro e não permite a conclusão da operação. O problema ocorre durante a geração do relatório de holerite do décimo terceiro.

 

**

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39352194018071)

 SOLUÇÃO**

Para corrigir o erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39352194018967)

 Acesse a tela **"Parâmetros"** (Configurações » Avançado » Preferências).

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39352181943703)

 Localize o parâmetro **"Relatório Holerite Décimo Terceiro"** (FPRELATHOLDECIM).

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41357173258135)

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39352181943959)

 Verifique se o campo (FPRELATHOLDECIM) está preenchido com algum código de relatório personalizado.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39352194020247)

 Limpe o conteúdo do parâmetro, deixando-o NULL (vazio). Isso fará com que o sistema considere o relatório padrão da fonte do sistema.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41357143371415)

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41357173262359)

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39352181946391)

 Salve as alterações realizadas no parâmetro.

 

### Como medida complementar, verifique também o caminho da pasta padrão de relatórios:

- Ainda na tela **Preferências**, localize o parâmetro **"FPPASTAPADRAO"** (Caminho da pasta padrão de relatórios folha)

- Verifique se o caminho está correto e acessível

**Para capturar o caminho correto:**

- Acesse **Configurações » Avançado » Administração do Servidor**

- Localize o campo **"JAVA HOME"**

- Copie o caminho até o nome "java"

- Retorne às Preferências e cole o caminho no parâmetro **FPPASTAPADRAO**

**Formato esperado:**

- 
**Windows**: `C:\suapasta\sankhya-om\jboss\bin\`

- 
**Linux**: `/home/suapasta/relatorios/`

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39352181946903)

 Acesse novamente a tela de (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e realize uma nova geração do relatório.

![7](https://ajuda.sankhya.com.br/hc/article_attachments/39352194021399)

 Tente realizar o **"download ou envio por e-mail"** dos holerites. O erro não deverá mais ocorrer.
 

 

**

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39352194022679)

 CAUSA**

O erro ocorre porque o parâmetro (FPRELATHOLDECIM) estava configurado com um código de relatório personalizado que não está disponível ou apresenta incompatibilidade. Quando o parâmetro está preenchido incorretamente, o sistema não consegue localizar ou processar o relatório especificado, gerando falha no download e envio dos holerites do décimo terceiro salário.