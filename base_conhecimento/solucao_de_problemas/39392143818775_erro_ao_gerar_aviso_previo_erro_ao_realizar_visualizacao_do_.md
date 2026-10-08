# Erro ao Gerar Aviso Prévio - Erro ao Realizar Visualização do Relatório

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39392143818775-Erro-ao-Gerar-Aviso-Pr%C3%A9vio-Erro-ao-Realizar-Visualiza%C3%A7%C3%A3o-do-Relat%C3%B3rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/39392143818775-Erro-ao-Gerar-Aviso-Pr%C3%A9vio-Erro-ao-Realizar-Visualiza%C3%A7%C3%A3o-do-Relat%C3%B3rio)  
> **ID:** `39392143818775` | **Última Atualização:** 2026-09-27T18:24:22Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39392122645783)

 **MENSAGEM**

Erro ao realizar visualização do relatório. Motivo: null

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39392122646423)

 **SITUAÇÃO**

Ao tentar baixar ou visualizar o PDF do aviso prévio através do sistema, o usuário recebe uma mensagem de erro informando que não foi possível realizar a visualização do relatório, sem apresentar detalhes específicos sobre a causa (motivo: null).

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39392143808535)

 **SOLUÇÃO**

Para corrigir o erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39392143810455)

 Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências) e localize o parâmetro **"Aviso Prévio Trabalhado Iniciativa da Empresa" (FPRELATAVIPREVE)**.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39392143811095)

 Verifique se o parâmetro **"FPRELATAVIPREVE"** está preenchido com algum valor numérico, como **"105"**.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39392143811607)

 Remova o valor do parâmetro **"FPRELATAVIPREVE"**, deixando-o em branco ou com o valor "**0"** .

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39392143812119)

 Salve as alterações realizadas no parâmetro.

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39392143812631)

 Retorne à tela de **"Geração do Aviso Prévio"** (Pessoal Arquivo Rescisão Aviso Prévio) e tente realizar novamente o download ou visualização do relatório em PDF.
 

**Caso o erro apresente para demais tipos de aviso basta fazer o mesmo processo. **

**FPRELTAVIPREVED **- Aviso Prévio Dispensado Empresa 

**FPRELTAVIPREVFD **- Aviso Prévio Dispensado Iniciativa do Empregado 

**FPRELTAVIPREVEI **- Aviso Prévio Indenizado Iniciativa da Empresa 

**FPRELTAVIPREVFT **- Aviso Prévio Trabalhado Iniciativa Funcionário 

**FPRELTAVIPREVFI **- Aviso Prévio Indenizado Funcionário 

**FPRELTAVIPREQFI **- Aviso Indenizado Quebra Contrato Funcionário

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39392143813399)

 **CAUSA**

O erro ocorre porque o parâmetro **"FPRELATAVIPREVE"** está configurado com um valor incompatível ou inexistente no sistema (como "105"), impedindo que o relatório seja gerado corretamente. Ao remover esse valor incorreto, o sistema utiliza o formato padrão de relatório, permitindo a visualização e download do PDF do aviso prévio sem erros.