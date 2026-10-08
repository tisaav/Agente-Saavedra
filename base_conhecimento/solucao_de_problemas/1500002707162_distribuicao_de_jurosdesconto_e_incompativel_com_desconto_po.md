# Distribuição de Juros/Desconto é incompatível com Desconto por item, saiba mais

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002707162-Distribui%C3%A7%C3%A3o-de-Juros-Desconto-%C3%A9-incompat%C3%ADvel-com-Desconto-por-item-saiba-mais](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002707162-Distribui%C3%A7%C3%A3o-de-Juros-Desconto-%C3%A9-incompat%C3%ADvel-com-Desconto-por-item-saiba-mais)  
> **ID:** `1500002707162` | **Última Atualização:** 2026-07-22T15:25:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302510232983)

 MENSAGEM**:

[CORE_E02347]: Distribuição de Juros/Desconto é incompatível com Desconto por item.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302510233623)

 SOLUÇÃO:**

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302560549527)

 Escolha entre** desabilitar o parâmetro** **"DISTJURO"**, de acordo com sua necessidade de uso e compreendendo o funcionamento desse, conforme detalhado abaixo, **ou refaça o lançamento inserindo o desconto exclusivamente pelo rodapé da nota**.

- Tela **"Preferências"**

- Chave: **"DISTJURO"**

- A documentação do Parâmetro DISTJURO quando está ativada habilita a opção de distribuir juros entre produtos, acessada através do menu Outras Opções, na tela de lançamento da Central de Atendimento ao Fornecedor e Cliente. Se não estiver ativada, a opção passa de "Distribuir Juros entre produtos" para "Distribuir Desconto entre produtos".

- 
**Com o parâmetro habilitado e inserindo desconto/juros no rodapé do lançamento**, o campo do item deve permanecer vazio, pois o sistema distribuirá o desconto/juros inserido no rodapé entre os itens e caso lá já haja valor lançado, ocorrerá o erro acima. Assim, o usuário deverá escolher entre desabilitar o parâmetro de acordo com sua necessidade de uso ou refazer o lançamento inserindo o desconto exclusivamente pelo rodapé.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16302560550551)

 CAUSA:**

 O incidente é um comportamento do sistema, ocorrendo no desconto dado por ITEM e pelo parâmetro DISTJURO estar ligado, de tal modo, ocorre a incompatibilidade. Pois, a documentação do presente  parâmetro exige que seja feito o desconto pelo rodapé e não pelos itens, utilizando assim o parâmetro **"****DISTJDCONF"** para distribuir o desconto pelos itens na confirmação.