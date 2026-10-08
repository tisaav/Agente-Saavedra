# Apenas empresas inscritas neste município podem efetuar retenção de ISSQN

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/8338467554199-Apenas-empresas-inscritas-neste-munic%C3%ADpio-podem-efetuar-reten%C3%A7%C3%A3o-de-ISSQN](https://ajuda.sankhya.com.br/hc/pt-br/articles/8338467554199-Apenas-empresas-inscritas-neste-munic%C3%ADpio-podem-efetuar-reten%C3%A7%C3%A3o-de-ISSQN)  
> **ID:** `8338467554199` | **Última Atualização:** 2026-07-22T15:12:12Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593740574871)

 MENSAGEM: **

E039: Apenas empresas inscritas neste município podem efetuar retenção de ISSQN. 

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593732559127)

 SITUAÇÃO:**

Ao tentar emitir nota fiscal para fora do município, com parceiros que retém ISS, a mensagem é apresentada.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593740579991)

SOLUÇÃO:**

O tomador do serviço não foi encontrado na base de dados do município, não sendo permitida a retenção. Acerte o CNPJ e/ou Inscrição Municipal ou altere o campo ISSQN Retido para 2 (Sem retenção de ISSQN). No exemplo abaixo no cadastro do parceiro, estava marcado para reter ISS, então foi alterado para não reter.

 

![Apenas empresas inscritas neste município podem efetuar 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593732567063)

 

Compare o XML da NFS-e emitida na prefeitura com a NFS-e emitida no sistema.

Verifique se foi preenchido o campo **"Cidade"** no rodapé da nota (neste deve ser informada a cidade onde ocorreu a prestação do serviço), caso não tenha sido, faça o devido preenchimento.

Referente a primeira situação: **TAG NaturezaOperacao>2</NaturezaOperacao> **
Essa informação é configurada no sistema no cadastro da **TOP** *(Caminho de acesso à tela: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)*, na aba NFS-e campo: Cód. Natureza Oper. ISS (NFS-e). 

 

![Apenas empresas inscritas neste município podem efetuar 2.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593732569239)

 

Alterado esse campo para que seja destacado no XML a opção 2, assim como  consta no arquivo XML gerado pelo site da NF-e aprovada na Prefeitura, e verificando nas preferências da empresa se está configurado o ambiente de produção para emissão de NFS-e, a nota será aprovada com sucesso.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16593740590359)

CAUSA: **

Emitir nota fora do município para parceiros que retém ISS e as configurações estejam incorretas.