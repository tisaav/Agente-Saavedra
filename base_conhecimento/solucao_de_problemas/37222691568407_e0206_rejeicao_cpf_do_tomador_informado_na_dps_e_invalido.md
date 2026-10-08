# E0206 Rejeição: CPF do tomador informado na DPS é inválido.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222691568407-E0206-Rejei%C3%A7%C3%A3o-CPF-do-tomador-informado-na-DPS-%C3%A9-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222691568407-E0206-Rejei%C3%A7%C3%A3o-CPF-do-tomador-informado-na-DPS-%C3%A9-inv%C3%A1lido)  
> **ID:** `37222691568407` | **Última Atualização:** 2026-07-22T14:17:35Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222691551767)

 **MENSAGEM**

E0206 Rejeição: CPF do tomador informado na DPS é inválido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222675652631)

 **SITUAÇÃO**

A mensagem de rejeição é apresentada durante o processo de **transmissão da DPS** (Documento de Prestação de Serviços) quando o **CPF do tomador do serviço** cadastrado no sistema está **inválido, incorreto ou preenchido de forma inadequada**, impedindo que a SEFAZ processe adequadamente o documento fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222675652887)

 **SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222691554327)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **tomador do serviço** informado na DPS.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222675654039)

 Na aba **"Identificação"**, no campo **"CNPJ / CPF"**, verifique se o CPF está preenchido corretamente:

- 

O CPF deve conter **11 dígitos numéricos**, sem pontos, traços ou espaços em branco;

- 

Certifique-se de que o CPF informado é **válido** e possui o dígito verificador correto;

- 

Não utilize CPF com **sequências numéricas repetidas** (exemplo: 000.000.000-00 ou 111.111.111-11).

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222691559959)

 Caso o tomador seja **pessoa jurídica**, verifique se o campo está preenchido com o **CNPJ** ao invés do CPF. Corrija a informação conforme o tipo de pessoa cadastrada.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222675663383)

 Após corrigir o CPF, **salve as alterações** no cadastro do parceiro.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222675663895)

 Retorne ao documento fiscal e **re-digite o cabeçalho da DPS** para que as informações atualizadas do tomador sejam carregadas.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222675664151)

 **Transmita novamente a DPS** para a SEFAZ. 
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222675664535)

 **CAUSA**

A rejeição ocorre quando o **CPF do tomador do serviço** informado na DPS está **inválido, incorreto ou com formatação inadequada**. Isso pode acontecer quando o CPF é preenchido com apenas zeros, possui sequência numérica incorreta, apresenta dígito verificador inválido ou contém caracteres especiais e espaços. A SEFAZ valida rigorosamente os dados de identificação dos participantes do documento fiscal, e qualquer inconsistência no CPF impede o processamento da DPS.