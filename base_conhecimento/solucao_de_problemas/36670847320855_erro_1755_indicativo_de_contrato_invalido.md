# Erro 1755 - Indicativo de Contrato inválido

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/36670847320855-Erro-1755-Indicativo-de-Contrato-inv%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/36670847320855-Erro-1755-Indicativo-de-Contrato-inv%C3%A1lido)  
> **ID:** `36670847320855` | **Última Atualização:** 2026-08-18T19:53:30Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670847320215)

** MENSAGEM:**

Erro 1755 - Indicativo de Contrato inválido. Ação sugerida: Quando a Identificação do Contribuinte Responsável Direto for informada, o Indicativo de Contrato deve ser igual a 'N'. 

Elemento: /eSocial/evtProcTrab/ideTrab/infoContr/indContr [S]

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670859966615)

** SITUAÇÃO:**

Mensagem de erro apresentada ao tentar realizar o envio do evento S-2500 pela Central do eSocial.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670859966999)

** SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36689891839255)

 Acesse a tela ****[''Processo Trabalhista''](https://ajuda.sankhya.com.br/hc/pt-br/articles/11592868813719-Processo-Trabalhista)** **(Pessoal+ » Rotinas Folha » Processo Trabalhista).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36689891841431)

 No campo** ''****Declarante'', **verifique se a opção** “Há responsabilidade indireta?” **está desativada.

- 

Se este campo estiver marcado, o erro 1755 será apresentado. 

 

![image (72).png](https://ajuda.sankhya.com.br/hc/article_attachments/36689909916695)

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36689891846679)

 Ajuste o campo conforme indicado e **exclua o processo**.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36689891848471)

 Cadastre o processo novamente para que a alteração seja validada.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/36670847320599)

** CAUSA:**

O erro ocorre porque o campo “Há responsabilidade indireta”  está marcado.

Quando marcado, o sistema entende que deve gerar o evento **S-2500 – Responsabilidade Indireta**, que é utilizado apenas quando há **determinação judicial** **para pagamento por parte de um responsável indireto** (subsidiário ou solidário).


---

### 🔗 Links e Referências Internas:

- [''Processo Trabalhista''](https://ajuda.sankhya.com.br/hc/pt-br/articles/11592868813719-Processo-Trabalhista)