# E0146 Rejeição: O código de país informado para o endereço no exterior do prestador do serviço não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do prestador do

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222358594071-E0146-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-pa%C3%ADs-informado-para-o-endere%C3%A7o-no-exterior-do-prestador-do-servi%C3%A7o-n%C3%A3o-existe-ou-%C3%A9-igual-ao-c%C3%B3digo-do-Brasil-Informe-um-c%C3%B3digo-de-pa%C3%ADs-existente-e-diferente-do-c%C3%B3digo-do-Brasil-BR-para-o-endere%C3%A7o-no-exterior-do-prestador-do](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222358594071-E0146-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-pa%C3%ADs-informado-para-o-endere%C3%A7o-no-exterior-do-prestador-do-servi%C3%A7o-n%C3%A3o-existe-ou-%C3%A9-igual-ao-c%C3%B3digo-do-Brasil-Informe-um-c%C3%B3digo-de-pa%C3%ADs-existente-e-diferente-do-c%C3%B3digo-do-Brasil-BR-para-o-endere%C3%A7o-no-exterior-do-prestador-do)  
> **ID:** `37222358594071` | **Última Atualização:** 2026-07-22T14:17:50Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222358581143)

 **MENSAGEM**

E0146 Rejeição: O código de país informado para o endereço no exterior do prestador do serviço não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do prestador do serviço, conforme tabela de país ISO2.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222358581655)

 **SITUAÇÃO**

Ao tentar emitir uma NFS-e para prestador de serviço localizado no exterior, o sistema apresenta a rejeição E0146, indicando que **o código do país informado no cadastro está incorreto**, não existe ou está configurado como Brasil.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222394244759)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222394245143)

 Acesse a tela ****["Preferências"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências) e configure o parâmetro:

- 

**"CODPAISBRASIL - Código do País Brasil"**: informe o valor **55**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222394245783)

 Acesse a tela ****["Países"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600894-Pa%C3%ADses) (Configurações » Cadastros » Endereços » Países) e realize o cadastro do país do exterior:

- 

No campo **''Código do país''**, preencha com um código diferente de 55.

- 

No campo **''País Domicílio Fiscal''**, preencha conforme a **tabela do BACEN** (Anexo IX - Tabela de UF, Município e País). **Exemplo:** México = 4936

- 

Certifique-se de que o código informado **não seja 1058** (código do Brasil)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222394246551)

 Acesse a tela ****["Estados"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados) (Configurações » Cadastros » Endereços » Estados) e crie um estado com as seguintes características:

- 

**"Descrição"**: EXTERIOR

- 

**"País"**: informe o cadastro criado no passo anterior

- 

**"Sigla"**: EX

- 

**"Código IBGE"**: 99

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222394247191)

 Acesse a tela ****["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e crie uma cidade:

- 

**"Nome"**: informe o nome da cidade do exterior

- 

**"Cód. UF"**: informe o estado criado no passo anterior (EX)

- 

**"Mun. domicílio fiscal"**: preencha com **9999999** (sete dígitos 9)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222358587671)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e vincule a cidade cadastrada ao prestador de serviço do exterior:

- 

Na aba **"Endereço"**, campo **"Cód. Cidade"**, informe a cidade criada no passo anterior

- 

Marque o parceiro como **"Pessoa Jurídica"**

- 

Na aba **"Identificação"**, preencha o campo **"Identificação de Estrangeiro"** com a informação de identificação fornecida pelo prestador

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222394248087)

 Após realizar todas as configurações, **gere novamente a NFS-e**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222394248343)

 **CAUSA**

A rejeição ocorre quando o **código do país informado no cadastro do prestador de serviço** está incorreto, não existe na tabela ISO2 ou está configurado como Brasil (código 1058 ou 55). Para emissão de NFS-e para o exterior, é obrigatório informar um **código de país válido e diferente do Brasil**, conforme a tabela do BACEN.


---

### 🔗 Links e Referências Internas:

- ["Preferências"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)
- ["Países"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600894-Pa%C3%ADses)
- ["Estados"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados)
- ["Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)