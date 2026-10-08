# O preenchimento do campo telefone fixo é obrigatório se o campo telefone celular não for preenchido

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617493-O-preenchimento-do-campo-telefone-fixo-%C3%A9-obrigat%C3%B3rio-se-o-campo-telefone-celular-n%C3%A3o-for-preenchido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617493-O-preenchimento-do-campo-telefone-fixo-%C3%A9-obrigat%C3%B3rio-se-o-campo-telefone-celular-n%C3%A3o-for-preenchido)  
> **ID:** `360044617493` | **Última Atualização:** 2026-07-22T15:52:50Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17003847300375)

 MENSAGEM:**

MS1018 - O preenchimento do campo telefone fixo é obrigatório se o campo telefone celular não for preenchido. Localização:Registro: contato - XPATH: /Reinf/evtInfoContri/infoContri/alteracao/infoCadastro/contato.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17003877265687)

 SITUAÇÃO:**

Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17003847302423)

 SOLUÇÃO:**

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17003877284375)

 Acesse: Comercial » Preferências » Empresa:

- Aba: **"EFD-Reinf"**

- Campo **"Responsável pela entrega": **informe o código do parceiro 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17003877287191)

  Acesse: Configurações » Cadastros » Parceiros:

- Aba: **"Endereço"**

- Busque o código do parceiro e preencha corretamente dados do  **"Telefone" **e** "Celular/Fax".**

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17003847310487)

 Acesse: Livros Fiscais » Conexão » Reinf » EFD - Reinf e gere novamente os movimentos através do botão **"Gerar Eventos"**. Realize uma nova transmissão do evento R1000 através do botão **"Enviar Eventos".**

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/17003877294487)

 CAUSA:**

O responsável pela entrega precisa ter os dados de telefones devidamente preenchidos no cadastro de Parceiro vinculado à empresa. Quando este não está devidamente preenchido, ocorre a rejeição.