# Erro ao gerar eventos S-1200 do eSocial [ORA-00001] Restrição exclusiva (PK_TFPS1200) violada

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/39383319777815-Erro-ao-gerar-eventos-S-1200-do-eSocial-ORA-00001-Restri%C3%A7%C3%A3o-exclusiva-PK-TFPS1200-violada](https://ajuda.sankhya.com.br/hc/pt-br/articles/39383319777815-Erro-ao-gerar-eventos-S-1200-do-eSocial-ORA-00001-Restri%C3%A7%C3%A3o-exclusiva-PK-TFPS1200-violada)  
> **ID:** `39383319777815` | **Última Atualização:** 2026-07-29T13:23:31Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/39383293943319)

 **MENSAGEM**

[ORA-00001] Restrição exclusiva (CMRPRD.PK_TFPS1200) violada

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/39383293943575)

 **SITUAÇÃO**

Ao tentar gerar os eventos **"S-1200"** (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) do **"eSocial"** para a competência de janeiro, o sistema apresenta erro indicando violação de restrição exclusiva na tabela.  

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/39383293943703)

 **SOLUÇÃO**

Para corrigir o erro, siga os passos abaixo:

![1](https://ajuda.sankhya.com.br/hc/article_attachments/39383319773591)

 Verifique se há duplicação de cadastros do funcionário na mesma empresa. Acesse a tela "Funcionários" (Configurações » Cadastros » Pessoal » Configuração Funcionários) e confirme se o colaborador possui mais de um vínculo cadastrado.

![2](https://ajuda.sankhya.com.br/hc/article_attachments/39383293944855)

 Caso identifique cadastros duplicados, verifique se ambos estão com as informações completas e consistentes, incluindo o campo "Situação no eSocial" configurado de forma equivalente entre eles.

![3](https://ajuda.sankhya.com.br/hc/article_attachments/39383319774103)

 Se o cadastro do autônomo estiver parametrizado como "Não sujeito à admissão", ajuste essa configuração para permitir o envio do evento "S-2300" (Admissão). 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/39383319774615)

 Realize uma nova geração dos eventos na "Central do eSocial" (Central do eSocial Pessoal+ » Rotinas Folha » Central do eSocial).

 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/39383319774999)

 Envie primeiro o evento "S-2300" e, na sequência, efetue o envio das folhas "S-1200".

 

![6](https://ajuda.sankhya.com.br/hc/article_attachments/39383293945623)

 Valide se os eventos foram recepcionados com sucesso no "Portal do eSocial".
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/39383319776151)

 **CAUSA**

O erro ocorre devido à duplicação de recibos **"S-1200"** na base de dados, geralmente causada por:

- 

Funcionário com cadastros duplicados na mesma empresa sem as devidas parametrizações no **"eSocial"**.

- 

Recibos perdidos durante o processamento, possivelmente em decorrência de lentidão no sistema ou no processamento do **"eSocial"**.

- 

Cadastro do funcionário autônomo parametrizado incorretamente como **"Não sujeito à admissão"**, impedindo o envio adequado dos eventos.