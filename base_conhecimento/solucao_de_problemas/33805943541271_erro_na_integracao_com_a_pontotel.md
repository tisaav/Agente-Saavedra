# Erro na integração com a PontoTel

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/33805943541271-Erro-na-integra%C3%A7%C3%A3o-com-a-PontoTel](https://ajuda.sankhya.com.br/hc/pt-br/articles/33805943541271-Erro-na-integra%C3%A7%C3%A3o-com-a-PontoTel)  
> **ID:** `33805943541271` | **Última Atualização:** 2026-07-29T13:20:33Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/42309880284183)

**MENSAGEM**

Ao acessar a tela **"Configurações de Gateway"** (Configurações >> Avançado >> Configurações Gateway), o sistema pode exibir diferentes tipos de erros:

• Erro imediato ao abrir a tela ou ao validar a integração com a PontoTel
• Falha no carregamento de recursos (404 Not Found)
• Erros de JavaScript (TypeError, ReferenceError)
• Token ausente ou inválido
• Tela permanece em modo de edição sem permitir salvamento
• Registros de aplicações não são exibidos

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/34012105622039)

**SITUAÇÃO**

Esses erros ocorrem quando o usuário tenta acessar a tela **"Configurações de Gateway"** para cadastrar ou visualizar aplicações integradas, ou ao validar o link no campo **"Endereço Sankhya"**. A tela realiza validações contínuas de comunicação com o gateway, e qualquer falha nessa comunicação impede o funcionamento adequado da funcionalidade.

As situações mais comuns incluem:

• Tentativa de cadastrar nova aplicação em base de testes
• Verificação de configurações de integrações existentes (como PontoTel ou Mercos)
• Acesso após atualização do sistema ou mudança de datacenter
• Utilização de IP interno para acessar a base

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/34012132096151)

**SOLUÇÃO**

A solução varia conforme a causa do erro. Siga as orientações abaixo de acordo com sua situação:

**Para validação do link "Endereço Sankhya":**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/34012132097047)

 Copie o link do campo **"Endereço Sankhya"** na tela **"Configurações de Gateway"** e cole no navegador.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/34012132098327)

 Verifique o resultado do teste:
• Se o link abrir corretamente, a porta de integração está funcionando.
• Se o link não funcionar, revise as configurações de segurança do servidor, como firewall ou regras de rede, que possam estar bloqueando conexões externas.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/34012132099607)

 Após realizar os ajustes necessários, repita o teste acessando novamente o link no navegador para confirmar se a comunicação foi restabelecida.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/34012105628567)

**Para erros relacionados ao firewall (infraestrutura):**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/34012132097047)

 Entre em contato com o provedor de infraestrutura responsável pelo firewall.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/34012132098327)

 Solicite a liberação dos IPs do gateway:
• **"Ambiente de Produção"**: Porta 40014.
• **"Ambiente Sandbox"**: Mesma porta configurada na base.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/34012132099607)

 Aguarde a confirmação e teste novamente o acesso.

**Para erros de acesso via IP interno:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/34012132097047)

 Crie um DNS público para a base que está apresentando o erro.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/34012132098327)

 Acesse a aplicação utilizando o endereço externo/DNS público.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/34012132099607)

 Realize as configurações necessárias na tela **"Configurações de Gateway"**.

![4](https://ajuda.sankhya.com.br/hc/article_attachments/42309869192727)

 Mantenha o endereço público acessível.

**Para erros após atualização ou mudança de datacenter:**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/34012132097047)

 Acesse a tela **"Configurações de Gateway"** utilizando o IP externo.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/34012132098327)

 Atualize as informações, especialmente o link de comunicação com o banco de dados.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/34012132099607)

 Salve as alterações.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/34012132102679)

**CAUSA**

Os erros na tela **"Configurações de Gateway"** podem ter diferentes causas:

**1. Restrições de rede/firewall:** Bloqueios de conexões externas impedem a comunicação do Gateway.

**2. Acesso via IP interno:** O Gateway exige que o endereço seja público e acessível externamente.

**3. Alterações no ambiente Cloud:** Mudanças como atualização de sistema ou relocação de datacenter exigem a atualização do link de comunicação com o banco de dados.

**4. Configuração de URL desatualizada:** URLs desatualizadas no IP externo impedem o reflexo correto nos ambientes de acesso.