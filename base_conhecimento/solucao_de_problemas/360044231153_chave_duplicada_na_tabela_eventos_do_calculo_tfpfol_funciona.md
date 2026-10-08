# Chave duplicada na tabela "Eventos do Cálculo (TFPFOL)" funcionário XXX - Evento 901 - sequencia 700"

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044231153-Chave-duplicada-na-tabela-Eventos-do-C%C3%A1lculo-TFPFOL-funcion%C3%A1rio-XXX-Evento-901-sequencia-700](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044231153-Chave-duplicada-na-tabela-Eventos-do-C%C3%A1lculo-TFPFOL-funcion%C3%A1rio-XXX-Evento-901-sequencia-700)  
> **ID:** `360044231153` | **Última Atualização:** 2026-07-29T13:21:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363395991319)

 MENSAGEM:**

Chave duplicada na tabela "Eventos do Cálculo (TFPFOL)" funcionário XXX - Evento 901 - sequencia 700"

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363406721815)

 SITUAÇÃO:**

Ao confirmar a Folha Complementar de um Funcionário, apresenta a mensagem.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363395996311)

 SOLUÇÃO:**

Para correção, siga  os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363406723351)

 Acesse: MGEPessoal » Avançado » Preferencias » Todas Preferências

Parâmetro: **"****FPINSSMESAMES - Calcula INSS Complementar pela diferença mensal":** ligado

 

**

![FPINSSMESAMES.png](https://ajuda.sankhya.com.br/hc/article_attachments/12655665953815)

**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363406726423)

 Acesse: MGEPessoal » Arquivos » Eventos

Aba: **"Incidências"**

Tem seus valores recalculados: marcado

Aba: **"Propriedades"**

Campo: **"Fórmula = 901"**

Avançado » Fórmulas de Cálculo: Mantenha a fórmula do evento de INSS conforme padrão Sankhya atualizado.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363396000535)

 Após os ajustes, saia do sistema, acesse novamente e posteriormente realize o cálculo da folha complementar.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16363396002327)

CAUSA**

Ocorre quando a fórmula de INSS está desatualizada e o evento de INSS está sendo calculado duas vezes na mesma referência, sendo necessário conferir a marcação de recálculo do evento, e o parâmetro FPINSSMESAMES.