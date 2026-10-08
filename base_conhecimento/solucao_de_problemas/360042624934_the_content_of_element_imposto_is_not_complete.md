# The content of element 'imposto' is not complete

> **Módulo:** Solucao de Problemas | **Subseção:** Mensagens de validação da SEFAZ  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624934-The-content-of-element-imposto-is-not-complete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624934-The-content-of-element-imposto-is-not-complete)  
> **ID:** `360042624934` | **Última Atualização:** 2026-07-22T16:08:37Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444315786647)

 MENSAGEM:**

Erros encontrados:cvc-complex-type.2.4.b: The content of element 'imposto' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":II, "http://www.portalfiscal.inf.br/nfe":**PIS**}' is expected”

Erros encontrados:cvc-complex-type.2.4.b: The content of element 'imposto' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":II, "http://www.portalfiscal.inf.br/nfe":**COFINS**}' is expected”

Erros encontrados:cvc-complex-type.2.4.b: The content of element 'imposto' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":II, "http://www.portalfiscal.inf.br/nfe":**CSSL**}' is expected”

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444315788055)

 SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444279850775)

 Tela : "**[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades)" **(Caminho de acesso: *Comercial » Preferências » Empresa*)
Aba: "**Propriedades"**, marque os campos:

- **"Calcula PIS?"**

- **"Calcula COFINS?"**

- **"Calcula CSLL?"**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444279854871)

 Tela: "**[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: *Comercial » Arquivo » Cadastros » Tipos de Operação - TOP*)
Aba: "**Impostos"**, marque os campos:

- "**Tem PIS"**

- **"Tem COFINS"**

- **"Tem CSLL"**

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444279855895)

 Tela: "****[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)" (Caminho de acesso: *Configurações » Cadastros » Produtos » Produtos*)
Aba: "**Impostos"**, preencha os campos:

- "**Grupo PIS**"

- "**Grupo COFINS**"

Obrigatoriamente, os impostos PIS/COFINS devem  estar devidamente configurados, mesmo que a incidência seja 0(zero), pois para NF-e este imposto é exigido e o cálculo é feito no ato da CONFIRMAÇÃO da Nota.

Para CSLL, verifique com a Contabilidade se o imposto é devido, se não, deixe desmarcado.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444315792535)

 Caso necessite criar ou dar manutenção nas Alíquotas de PIS/COFINS/CSLL, acesse:

- 
**"[Alíquotas de PIS"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434) **(Caminho de acesso: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS*)

- "****[Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813)" (Caminho de acesso: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS*)

- "****[Alíquotas de CSLL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109933)" (Caminho de acesso: *Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de CSLL*)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444315793943)

 Após os ajustes inutilize a Nota e fature novamente, depois gerar Lote.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16444315797655)

 CAUSA:**

Para PIS/COFINS, o calculo é obrigatório, mesmo que a Incidência do imposto seja 0(zero),  então esta erro ocorre quando não é devidamente configurado a Incidência de um ou todos os Impostos da mensagem de erro (PIS/COFINS/CSLL).


---

### 🔗 Links e Referências Internas:

- [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
- [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)
- [Alíquotas de PIS"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434)
- [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813)
- [Alíquotas de CSLL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109933)