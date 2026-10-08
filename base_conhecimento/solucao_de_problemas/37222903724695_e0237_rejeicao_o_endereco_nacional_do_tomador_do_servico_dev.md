# E0237 Rejeição: O endereço nacional do tomador do serviço deve ser informado na DPS quando o valor do ISSQN for retido pelo tomador, exceto se o emitente da DPS é o próprio tomador do serviço.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37222903724695-E0237-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-tomador-do-servi%C3%A7o-deve-ser-informado-na-DPS-quando-o-valor-do-ISSQN-for-retido-pelo-tomador-exceto-se-o-emitente-da-DPS-%C3%A9-o-pr%C3%B3prio-tomador-do-servi%C3%A7o](https://ajuda.sankhya.com.br/hc/pt-br/articles/37222903724695-E0237-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-tomador-do-servi%C3%A7o-deve-ser-informado-na-DPS-quando-o-valor-do-ISSQN-for-retido-pelo-tomador-exceto-se-o-emitente-da-DPS-%C3%A9-o-pr%C3%B3prio-tomador-do-servi%C3%A7o)  
> **ID:** `37222903724695` | **Última Atualização:** 2026-07-22T14:17:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38324582340247)

 MENSAGEM**

E0237 Rejeição: O endereço nacional do tomador do serviço deve ser informado na DPS quando o valor do ISSQN for retido pelo tomador, exceto se o emitente da DPS é o próprio tomador do serviço.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222918942103)

 **SITUAÇÃO**

Ao tentar emitir uma **NFS-e (Documento de Prestação de Serviços)** com **retenção de ISSQN pelo tomador**, o sistema apresenta a rejeição E0237 porque **o endereço completo do tomador do serviço não foi informado** corretamente no cadastro ou na nota fiscal.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222918942231)

 **SOLUÇÃO**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222903720343)

 Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **cadastro do tomador do serviço** que está sendo utilizado na NFS-e.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222903720855)

 Na aba **''Endereço''**, verifique se os **dados de endereço do tomador** estão completos e corretos, incluindo:

- 

**Logradouro**

- 

**Número**

- 

**Bairro**

- 

**Cidade**

- 

**UF (Estado)**

- 

**CEP**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222918944407)

 Caso algum campo esteja **vazio ou incorreto**, preencha ou corrija as informações e salve o cadastro.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222918945175)

 Acesse a tela** ''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222918945559)

 Na grade **''Rodapé''**, na aba **''Impostos''**, verifique se o campo **"Cidade" **está preenchido corretamente com a **cidade onde ocorreu a prestação do serviço**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222918945815)

 Confirme se o campo **"Tipo de Retenção do ISS"** está configurado corretamente:

- 

Se o tomador **retém o ISS**, o campo deve estar marcado como **"Retido pelo tomador''**.

- 

Se o tomador **não retém o ISS**, altere para **"Não retido''**.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38324579267095)

 Após realizar os ajustes necessários, **emita novamente a NFS-e**.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37222918947479)

 **CAUSA**

A rejeição ocorre porque a **SEFAZ exige que o endereço completo do tomador do serviço seja informado** quando há **retenção de ISSQN pelo tomador**. Esta validação garante a **identificação correta do responsável tributário** e a **localização da prestação do serviço** para fins de arrecadação municipal. A exceção ocorre apenas quando **o emitente da DPS é o próprio tomador do serviço**, situação em que o endereço já está implícito no cadastro do emitente.