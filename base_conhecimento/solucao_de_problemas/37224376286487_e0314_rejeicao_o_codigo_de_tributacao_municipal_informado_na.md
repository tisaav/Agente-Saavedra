# E0314 Rejeição: O código de tributação municipal informado não existe ou não está administrado pelo município de incidência do ISSQN na data de competência informada na DPS.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37224376286487-E0314-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-municipal-informado-n%C3%A3o-existe-ou-n%C3%A3o-est%C3%A1-administrado-pelo-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-na-data-de-compet%C3%AAncia-informada-na-DPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/37224376286487-E0314-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-municipal-informado-n%C3%A3o-existe-ou-n%C3%A3o-est%C3%A1-administrado-pelo-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-na-data-de-compet%C3%AAncia-informada-na-DPS)  
> **ID:** `37224376286487` | **Última Atualização:** 2026-09-21T15:14:20Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/37224376270231)

**MENSAGEM**

[GW3000 / E0314] O código de tributação municipal informado é inválido, não existe ou não está administrado pelo município de incidência do ISSQN na data de competência informada na DPS.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/37224376274327)

**SITUAÇÃO**

Ao tentar emitir ou aprovar uma Nota Fiscal de Serviço Eletrônica (NFS-e), o sistema apresenta erro de validação (como GW3000 ou E0314), informando que o código de tributação municipal utilizado não é válido, está incorreto ou não está cadastrado no município de incidência do ISSQN na data de competência do documento. Esta mensagem ocorre especialmente ao tentar gerar o lote de NFS-e pelo Padrão Nacional.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/37224376277527)

**SOLUÇÃO**

Para resolver estes erros, siga os passos abaixo para ajustar o cadastro do serviço:

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/37224376279703)

  Acesse a tela **"Serviço"** (Configurações >> Cadastros >> Produtos).
 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/37224391808279)

  Localize o serviço utilizado na NFS-e rejeitada e acesse a aba **"Impostos"** e em seguida **"Alíquota de ISS"**.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/37224376280599)

  No campo **"Cód. Trib. Município NFS-e"**, ajuste o formato conforme a regra do Padrão Nacional. Note que o formato pode variar por município:

- 

**Formato Padrão Nacional:** Algumas prefeituras exigem a estrutura com pontos (ex: 01.02.01). Regra geral de conversão: pegue o código do item da lista de serviço e acrescente **.01** ao final (ex: serviço 14.01 vira 14.01.01).
 

1. 

**Formato Numérico:** Outras prefeituras exigem apenas números (Ex: 250301). Consulte o manual da sua prefeitura.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/37224391810583)

  Acesse o **"Portal Nacional" ou o Portal da Prefeitura **(caso o município não tenha migrado para o Emissor Nacional) e valide se o código está cadastrado, ativo e válido para a data de competência.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/37224391812119)

  Verifique se o campo **"Código NBS"** na aba **"Impostos"** está preenchido corretamente (ex: 118025000) e se o **"CNAE"** contém apenas números. 
 

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37224391814551)

  Após realizar os ajustes, redigite o item na nota fiscal para confirmar as alterações realizadas e gere um novo lote para envio.
 

**Observações Importantes:**

- 

Se o município ainda não migrou para o Emissor Nacional, desmarque a opção **"Emitir NFS-e Padrão Nacional"** na tela **Empresa** (Comercial >> Preferências)** -> Documentos Fiscais Eletrônicos -> NFS-e.**
 

1. 

O item deve estar cadastrado na tela **"Serviço"**, e não na tela **"Produtos"**.
 

1. 

Verifique se o serviço possui desdobramento no código de tributação; caso positivo, revise a parametrização.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/37224391816599)

**CAUSA**

Estes erros ocorrem devido a divergências no **Padrão Nacional da NFS-e**, que exige formatos específicos para o código de tributação municipal e validações rigorosas com a data de competência. As causas principais incluem:

- 

Código de tributação municipal inexistente, inativo ou com formatação incorreta (ex: uso de caracteres especiais ou formato antigo descontinuado após a Reforma Tributária).
 

1. 

Divergência entre o código informado e a data de competência do serviço.
 

1. 

Município de incidência do ISSQN informado incorretamente.
 

1. 

Código NBS não preenchido ou incorreto.
 

1. 

Tentativa de emitir NFS-e pelo Emissor Nacional em municípios que ainda não migraram para este modelo.