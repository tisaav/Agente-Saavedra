# Não é possível receber o evento

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/7921512070807-N%C3%A3o-%C3%A9-poss%C3%ADvel-receber-o-evento](https://ajuda.sankhya.com.br/hc/pt-br/articles/7921512070807-N%C3%A3o-%C3%A9-poss%C3%ADvel-receber-o-evento)  
> **ID:** `7921512070807` | **Última Atualização:** 2026-07-29T13:24:33Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16584557899031)

 MENSAGEM**:

Erro 1526 - Não é possível receber o evento.

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16584573450647)

 SITUAÇÃO:**

Ao enviar o S-2200 ocorre erro

**Ação Sugerida:** caso tenha sido enviado o evento S-2190 para o mesmo contrato de trabalho (CPF + matrícula) e se 'indRetif' do evento S-2200 for igual a [1]:
a) Os campos **"codCateg"** e **"natAtividade"** informados no evento S-2190 devem ser idênticos ao respectivos campos do evento S-2200
b) O campo **"dtAdm"** informado no evento S-2190 deve ser idêntico ao respectivo campo do evento S-2200
c) O campo **"tpRegTrab"** deve ser igual a [1] e o campo **"tpRegPrev"** deve ser igual a [1, 3]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16584573455767)

 SOLUÇÃO:**

Acesse o site do esocial e verifique com qual natureza de atividade (**Rural ou Urbana**) a admissão preliminar foi enviada.

Depois acesse a tela de **"CBO", **localize o CBO que consta no cadastro do cargo/função do colaborador e verifique qual o Tipo de horário noturno informado.

Se no cadastro estiver errado, faça o ajuste e gere o S-2200 novamente.

Caso esteja errado na admissão preliminar no portal temos 2 formas de ajustar:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16584573459479)

 Retifique a informação de Natureza de atividade direto no portal do esocial e depois envie o S-2200 novamente.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16584557910039)

 Coloque no cadastro do CBO a mesma informação que consta na admissão preliminar e envie o S-2200. Depois, ajuste o cadastro do CBO e envie uma retificação do S-2200 com a informação correta.

 

![CBO.png](https://ajuda.sankhya.com.br/hc/article_attachments/7922063466903)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16584557917463)

CAUSA:**

Esse erro ocorre quando o S-2190 foi enviado com uma natureza de atividade diferente do que consta no S-2200.