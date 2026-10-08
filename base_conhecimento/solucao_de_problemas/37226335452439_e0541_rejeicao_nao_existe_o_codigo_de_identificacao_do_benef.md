# E0541 Rejeição: Não existe o código de identificação do benefício municipal informado na DPS para o município de incidência do ISSQN.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37226335452439-E0541-Rejei%C3%A7%C3%A3o-N%C3%A3o-existe-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-benef%C3%ADcio-municipal-informado-na-DPS-para-o-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN](https://ajuda.sankhya.com.br/hc/pt-br/articles/37226335452439-E0541-Rejei%C3%A7%C3%A3o-N%C3%A3o-existe-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-benef%C3%ADcio-municipal-informado-na-DPS-para-o-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN)  
> **ID:** `37226335452439` | **Última Atualização:** 2026-07-22T14:15:08Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226335437591)

 **MENSAGEM**

E0541 Rejeição: Não existe o código de identificação do benefício municipal informado na DPS para o município de incidência do ISSQN.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226335438359)

 **SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviços Eletrônica), o sistema retorna a mensagem de rejeição informando que **o código de benefício municipal informado não existe** ou não está cadastrado para o município onde o serviço está sendo prestado.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226335439255)

 **SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226335439639)

 Verifique se o **código de benefício fiscal municipal** informado na operação está correto e corresponde ao município de incidência do ISSQN.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226319896599)

 Acesse a tela **"Tipo de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize o TOP utilizado na emissão da NFS-e.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226319897879)

 Na aba **"NFS-e"**, verifique se o campo **"Cód. Natureza Oper. ISS (NFS-e)"** está preenchido corretamente:

- 

Certifique-se de que o código informado está **cadastrado e ativo** no município de prestação do serviço.

- 

Caso o código esteja incorreto ou inexistente, **remova-o** ou **substitua-o** pelo código válido conforme legislação municipal.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226319899159)

 Consulte o **manual da Prefeitura do município** de incidência do ISSQN para validar quais códigos de benefício fiscal são aceitos e em quais situações podem ser aplicados.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226335442455)

 Caso o benefício fiscal não se aplique à operação, **remova o código **do cadastro do TOP e configure corretamente o campo **"Regime Especial de Tributação ISS"** na tela** ''Empresa''** (Comercial » Preferências » Empresa).

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38295550888855)

 Após realizar os ajustes necessários, **emita novamente a NFS-e** para validar se a rejeição foi solucionada.
 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226319907095)

 **CAUSA**

A rejeição ocorre porque o **código de benefício fiscal municipal informado** na Declaração de Prestação de Serviços (DPS) **não está cadastrado, não é válido ou não é aceito** pela prefeitura do município onde o ISSQN está sendo recolhido. Isso pode acontecer quando:

- 

O código foi digitado incorretamente.

- 

O código não existe na base de dados da prefeitura.

- 

O benefício fiscal não se aplica ao tipo de serviço ou operação realizada.

- 

O município de incidência do ISSQN não reconhece o código informado.