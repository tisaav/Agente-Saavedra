# Campo "serviço -> descrição" é obrigatório

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/4421069379351-Campo-servi%C3%A7o-descri%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3rio](https://ajuda.sankhya.com.br/hc/pt-br/articles/4421069379351-Campo-servi%C3%A7o-descri%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3rio)  
> **ID:** `4421069379351` | **Última Atualização:** 2026-07-22T15:19:30Z

---

Campo "servico -> descricao" é obrigatório

 

### 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41975996816919)

**SITUAÇÃO**

Ao tentar emitir uma **"Nota Fiscal de Serviço Eletrônica (NFS-e)"**, o sistema apresenta a mensagem de erro informando que o campo **"servico -> descricao"** é obrigatório. A nota fica com status **"Aguardando Correção"** e, ao consultar o JSON da nota, identifica-se que o campo **"servico -> descricao"** está vazio ou não está sendo enviado corretamente, mesmo que haja informações de descrição do serviço.

 

### 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286531026327)

**CAUSA**

O erro ocorre quando o campo **"Conteúdo a ser enviado na descrição da NFS-e"** não está configurado nas preferências da empresa, ou está configurado de forma inadequada. Adicionalmente, pode ser causado por:

- 

Incompatibilidade na estrutura do **"JSON"** enviado à prefeitura quando o **"Código CNAE"** está preenchido no cadastro do produto/serviço e a nota contém múltiplos itens com valor.

- 

Ausência de informações configuradas nos campos de **"Tipo de Serviço"**.

- 

Outras causas: incompatibilidade entre o código de serviço municipal e as regras da prefeitura, uso de CEP inválido ou genérico.

 

### 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16286531032727)

**SOLUÇÃO**

Para corrigir este erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/41976007096343)

 Acesse a tela **"Serviço"** (Configurações >> Cadastros >> Produtos >> Serviço), localize o serviço utilizado na nota e acesse a aba **"Impostos"**. Se necessário, remova o **"Código CNAE"** ou ajuste o campo **"Tipo de Serviço"**.
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/41976007100695)

 Acesse a tela **"Empresa"** (Comercial>> Preferenciais) e localize a empresa emissora da nota.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/41976007102231)

 Clique na aba **"Documentos Eletrônicos"**.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/41976007103383)

 Acesse a aba**"NFS-e"** e localize o campo **"Conteúdo a ser enviado na descrição da NFS-e"**.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/41976007104279)

 Configure este campo com uma das opções disponíveis, como **"Descrição do Produto/Serviço"** ou **"Observações"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41976007108119)

 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/41975996830487)

 Salve as alterações realizadas.
 

![7](https://ajuda.sankhya.com.br/hc/article_attachments/41976007110167)

 Retorne à nota que apresentou o erro, duplique-a e exclua a nota anterior com erro (ou redigite os itens, conforme necessário).
 

![8](https://ajuda.sankhya.com.br/hc/article_attachments/41975996832791)

 Confirme a nova nota e verifique se o erro foi corrigido.
 

**Dicas Adicionais:**

- 

**CEP:** Certifique-se de que o CEP informado é válido e reconhecido na base oficial dos Correios.

- 

**Configurações de Cidade:** Verifique as configurações específicas da cidade na tela **"Cidades"** (Configurações >> Cadastros >> Endereços >> Cidades), na aba **"NFS-e"**, especialmente os campos relacionados ao envio de quantidade, valor unitário e itens separados no JSON.