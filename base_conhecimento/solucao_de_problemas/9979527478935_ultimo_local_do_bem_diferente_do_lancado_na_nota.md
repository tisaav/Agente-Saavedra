# Último local do bem diferente do lançado na nota

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/9979527478935-%C3%9Altimo-local-do-bem-diferente-do-lan%C3%A7ado-na-nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/9979527478935-%C3%9Altimo-local-do-bem-diferente-do-lan%C3%A7ado-na-nota)  
> **ID:** `9979527478935` | **Última Atualização:** 2026-07-22T15:05:12Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/18789215791255)

**MENSAGEM**

[CORE_E01210]: Último local do bem diferente do lançado na nota. / O local do bem é diferente do último local alocado.

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/18789215798551)

**SITUAÇÃO**

Ao lançar notas de bens (venda ou demonstração) ou realizar movimentações de ativos fixos, a mensagem de erro referente à divergência entre o local do bem e o último local alocado é apresentada.

 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/18789215822103)

**CAUSA**

O erro ocorre pela divergência entre o local cadastrado no bem e o último local alocado via movimentações (validado na TCIIBE), visando garantir a integridade patrimonial, quando o campo **"Atualização do bem"** na TOP está configurado com as opções de validação ativa.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/18789215800599)

**SOLUÇÃO**

![1](https://ajuda.sankhya.com.br/hc/article_attachments/18789215806743)

 Sempre que a nota possuir bens que são validados por locais, verifique a configuração do **"Tipo de operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP). A validação do local só ocorre se o campo **"Atualização do Bem"** da TOP for igual a: 

B - Baixa/Venda
D - Transf.Entrada/Retorno
T - Transf.Saída/Remessa
 

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/9979445762711)

![2](https://ajuda.sankhya.com.br/hc/article_attachments/18789188917143)

 Caso a configuração da TOP esteja correta, acesse a **"Consulta/Movimentação de Bem"** (Imobilizado > Rotinas > Consulta/Movimentação de Bem), localize e verifique o campo **"Local"** do bem.
 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/18789188924439)

 Caso o local esteja diferente do físico, realize uma movimentação de transferência para atualizar o local antes de gerar a nota.
 

![4](https://ajuda.sankhya.com.br/hc/article_attachments/42055351247255)

 O sistema utiliza a tabela TCIIBE para validar o maior Nro. Único do bem; Ou seja, se o local da nota atual divergir do local registrado no histórico (maior NUNOTA), o bloqueio ocorrerá.
 

![5](https://ajuda.sankhya.com.br/hc/article_attachments/42055322224791)

 Para mais detalhes sobre as opções da TOP, acesse: [Tipos de Operação - TOP – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque).


---

### 🔗 Links e Referências Internas:

- [Tipos de Operação - TOP – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)