# Inscrição Estadual inválida para esta UF

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615933-Inscri%C3%A7%C3%A3o-Estadual-inv%C3%A1lida-para-esta-UF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615933-Inscri%C3%A7%C3%A3o-Estadual-inv%C3%A1lida-para-esta-UF)  
> **ID:** `360044615933` | **Última Atualização:** 2026-07-22T15:54:36Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610373892247)

 MENSAGEM:**

[CORE_E05363]: Inscrição Estadual inválida para esta UF.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610382132247)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610373901591)

 Essa validação acontecerá de acordo com a configuração dos parâmetros **"****CRITICAIE"** e **"****CRITICAIEF2" ***(Caminho de acesso: Configurações » Avançado » Preferências)*:

O parâmetro Critica Inscrição Estadual? - CRITICAIE determina o comportamento do sistema quanto às numerações digitadas na Inscrição Estadual. Pode-se defini-lo de três maneiras:

- Avisa: será apresentado um alerta informando sobre a inclusão de uma IE inválida, porém o cadastro será aceito;

- Critica: o sistema irá validar a IE informada, não permitindo que seja incluída uma numeração inválida;

- Não Critica: por esta opção, o sistema não irá validar se a numeração da Inscrição Estadual é ou não inválida.

Dessa forma, caso deseje trabalhar com a validação acima, realize uma consulta desse parceiro junto ao Sintegra, identificando a Inscrição Estadual válida

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610373904919)

 Consulte o CNPJ do parceiro no SINTEGRA para verificar qual a Inscrição Estadual está vinculada ao seu CNPJ.

[http://www.sintegra.gov.br/](http://www.sintegra.gov.br/)

Através do link acima, selecione o Estado do respectivo parceiro e realize a consulta de seu CNPJ.

 

**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610382139287)

 **Identificado a Inscrição Estadual correta, altere essa informação no cadastro do parceiro:

- Tela **"Parceiros"** *(Caminho de acesso: Configurações » Cadastros), *aba **"Identificação"**.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610373908887)

 Feito o ajuste, realize um novo teste. 

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16610373911063)

CAUSA:**

Mensagem será apresentada quando informado uma Inscrição Estadual inválida no cadastro do parceiro, considerando os parâmetros CRITICAIE e CRITICAIEF2 configurados para criticar.