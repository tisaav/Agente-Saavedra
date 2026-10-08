# E0061: Verificação da situação da nota

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360055968653-E0061-Verifica%C3%A7%C3%A3o-da-situa%C3%A7%C3%A3o-da-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055968653-E0061-Verifica%C3%A7%C3%A3o-da-situa%C3%A7%C3%A3o-da-nota)  
> **ID:** `360055968653` | **Última Atualização:** 2026-07-22T15:28:08Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586832193175)

 MENSAGEM**:

Erro NFS- E prefeitura de Londrina:

E0061: Verificação da situação da nota
Possível solução: Para esta nota a situação pode estar como: Tributado Tomador(tt).

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586832203671)

 CAUSA:
**Ocorre quando a situação enviada à prefeitura esta incorreto na tag SITUAÇAO.

Ex: *<situacao>tp</situacao> *onde deveria ser *<situacao>tt</situacao>*

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586832224023)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586848834711)

 Acesse o Tipo de Operação em Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
Aba: [Natureza da Operação ISS/Município](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanaturezadaoperaoissmunicpio)
Observação: *a ativação do parâmetro **"Utilizar Cód. Nat. Operação ISS por Top/Empresa - NATOPEISSTOPEMP"** fará com que a aba **"Natureza da Operação ISS/Município"** seja apresentada no Cadastro de Tipos de Operação - TOP,*

**Preencha o campo:** Empresa, para que possa ser selecionado uma das opções de Natureza de Operação, e selecione a opção 'Tributado Tomador (tt).

*Exemplo de script - Solicitar apoio de um consultor para alinhar com a prefeitura os códigos que são aceitos, para a correta criação do script.*

**Insert into TGFNAS (CODNATOPER, SEQUENCIA, CODMUNFIS, DESCRNATOPER) Values ('0', 1, 4300604, 'Tributada Integralmente');**

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18586848843159)

Após os ajustes , excluir a nota e fazer uma nova nota e transmiti-lo.


---

### 🔗 Links e Referências Internas:

- [Natureza da Operação ISS/Município](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanaturezadaoperaoissmunicpio)