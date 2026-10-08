# E0499 Rejeição: O código de país informado para o endereço no exterior do fornecedor não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do fornecedor, conforme ta

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225964570007-E0499-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-pa%C3%ADs-informado-para-o-endere%C3%A7o-no-exterior-do-fornecedor-n%C3%A3o-existe-ou-%C3%A9-igual-ao-c%C3%B3digo-do-Brasil-Informe-um-c%C3%B3digo-de-pa%C3%ADs-existente-e-diferente-do-c%C3%B3digo-do-Brasil-BR-para-o-endere%C3%A7o-no-exterior-do-fornecedor-conforme-ta](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225964570007-E0499-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-pa%C3%ADs-informado-para-o-endere%C3%A7o-no-exterior-do-fornecedor-n%C3%A3o-existe-ou-%C3%A9-igual-ao-c%C3%B3digo-do-Brasil-Informe-um-c%C3%B3digo-de-pa%C3%ADs-existente-e-diferente-do-c%C3%B3digo-do-Brasil-BR-para-o-endere%C3%A7o-no-exterior-do-fornecedor-conforme-ta)  
> **ID:** `37225964570007` | **Última Atualização:** 2026-07-22T14:15:26Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225980412183)

 **MENSAGEM**

E0499 Rejeição: O código de país informado para o endereço no exterior do fornecedor não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do fornecedor, conforme tabela de país ISO2.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225980412695)

 **SITUAÇÃO**

Ao tentar emitir um documento fiscal eletrônico (NF-e ou NFS-e) para um **fornecedor do exterior**, o sistema apresenta a rejeição E0499, indicando que o código do país informado no cadastro do fornecedor está **incorreto, inexistente ou igual ao código do Brasil**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225964560663)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225964561303)

 Acesse a tela ****["Preferências"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225980416023)

 Localize o parâmetro **"CODPAISBRASIL - Código do País Brasil"**.

- 

Certifique-se de que este parâmetro esteja preenchido com o valor **"55"**, que corresponde ao código do Brasil no sistema.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225980418327)

 Acesse a tela **"Países"** (Configurações » Cadastros » Endereços » Países).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225980419735)

 Verifique se o país do exterior está cadastrado corretamente:

- 

No campo **"País Domicílio Fiscal"**, informe o código de quatro dígitos conforme a **Tabela do Banco Central do Brasil (BACEN)**.

- 

Consulte o Anexo IX - Tabela de UF, Município e País para obter o código correto.

- 

Certifique-se de que o código informado seja **diferente de 1058** (código do Brasil). 

Exemplo: Para o México, o código é **"4936"**.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225980421911)

 Acesse a tela **"Estados"** (Configurações » Cadastros » Endereços » Estados), crie ou verifique o cadastro do estado do exterior:

- 

No campo **"Descrição"**, informe **"EXTERIOR"**.

- 

No campo **"País"**, vincule o país cadastrado no passo anterior.

- 

No campo **"Sigla"**, informe **"EX"**.

- 

No campo **"Código IBGE"**, informe **"99"**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225964565783)

 Acesse a tela **"Cidades"** (Configurações » Cadastros » Endereços » Cidades) e crie ou verifique o cadastro da cidade do exterior:

- 

No campo **"Descrição"**, informe o nome da cidade do exterior.

- 

No campo **"Cód. UF"**, vincule o estado criado no passo anterior (com sigla **"EX"**).

- 

No campo **"Mun. domicílio fiscal"**, informe **"9999999"** (sete dígitos 9).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38166605537943)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do fornecedor do exterior:

- 

Na aba **"Endereço"**, no campo **"Cód. Cidade"**, vincule a cidade cadastrada no passo anterior.

- 

Na aba **"Identificação"**, no campo **"Identificação de Estrangeiro"**, preencha com a informação de identificação fornecida pelo parceiro (documento equivalente ao CNPJ/CPF no país de origem).

- 

Certifique-se de que o parceiro esteja marcado como **"Pessoa Jurídica"**, para evitar erros de validação de CPF.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38166610151191)

 Após realizar todos os ajustes nos cadastros, gere novamente o documento fiscal eletrônico (NF-e ou NFS-e).

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225980424343)

 **CAUSA**

A rejeição E0499 ocorre quando o **código do país informado no cadastro do fornecedor** está incorreto, inexistente na tabela do BACEN ou igual ao código do Brasil (1058). O sistema valida se o código do país do destinatário/fornecedor está de acordo com a **Tabela de Países do Banco Central** e se, em operações com o exterior, o código é diferente do código brasileiro. Caso o cadastro esteja incompleto ou com informações divergentes, o documento fiscal é rejeitado pela Sefaz.


---

### 🔗 Links e Referências Internas:

- ["Preferências"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)