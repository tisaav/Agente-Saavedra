# Geração Automática - Obrigações do ICMS e ICMS ST a Recolher

> **Módulo:** Configurações e Cadastros | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109513-Gera%C3%A7%C3%A3o-Autom%C3%A1tica-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109513-Gera%C3%A7%C3%A3o-Autom%C3%A1tica-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher)  
> **ID:** `360045109513` | **Última Atualização:** 2026-07-29T13:55:46Z

---

No sistema, é possível realizar uma alimentação automática da tela [Obrigações do ICMS e ICMS ST a Recolher](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133) por meio de procedimentos realizados na tela [Geração de Lote GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053). Observe:

Primeiramente, ligue o parâmetro **"Gera obrigações do ICMS e ICMS ST automaticamente. - GEROBGICMSSTAUT" **e após isso, na tela Geração de Lote GNRE, no botão **"Novo Lote"**, efetue uma busca pelos financeiros que deverão compor o XML:

![mceclip0.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411316760087)

Ao clicar no referido botão o pop-up **"Gerar XML do Lote de GNRE"** será aberto:

![mceclip1.png](https://ajuda.sankhya.com.br/hc/article_attachments/4411316803351)

Após a geração do lote, o lançamento da obrigação de ICMS e ST só será realizado na tela Obrigações do ICMS e ICMS ST a Recolher nos impostos listados no campo **"Tipo Apuração"** quando o **"Status do lote"** for retornado como **"Lote processado com sucesso"**. Caso esse status seja apresentado com alguma pendência, erro de validação ou apenas de Lote enviado, o referido lançamento não será gerado.

![status_do_lote.png](https://ajuda.sankhya.com.br/hc/article_attachments/12801072426391)

**Atenção Consultor Sankhya:** Na tela Geração de Lote GNRE é possível gerar o lote de financeiros que já possuam lote gerado. Nesse caso, novos registros serão gerados na tela Obrigações do ICMS e ICMS ST a Recolher. Não existe uma relação dos registros criados na TGFOIR com o lote gerado, logo não é possível excluir estes registros. 

Dessa forma, caso seja gerado o lote de financeiros que já possuam lote gerado e possuam registros na TGFOIR, se desejado, a exclusão desses registros deverá ser feita manualmente na tela Obrigações do ICMS e ICMS ST a Recolher.


---

### 🔗 Links e Referências Internas:

- [Obrigações do ICMS e ICMS ST a Recolher](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133)
- [Geração de Lote GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053)