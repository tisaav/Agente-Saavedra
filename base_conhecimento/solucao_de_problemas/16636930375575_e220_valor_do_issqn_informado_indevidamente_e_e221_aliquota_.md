# E220: Valor do ISSQN informado indevidamente e E221: Aliquota informada indevidamente. Possível solução

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/16636930375575-E220-Valor-do-ISSQN-informado-indevidamente-e-E221-Aliquota-informada-indevidamente-Poss%C3%ADvel-solu%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/pt-br/articles/16636930375575-E220-Valor-do-ISSQN-informado-indevidamente-e-E221-Aliquota-informada-indevidamente-Poss%C3%ADvel-solu%C3%A7%C3%A3o)  
> **ID:** `16636930375575` | **Última Atualização:** 2026-07-22T14:54:57Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16636942161303)

  MENSAGEM:**

E220: Valor do ISSQN informado indevidamente. Possível solução: O valor do ISSQN será calculado pela Prefeitura e não deve ser informado pelo contribuinte.

 

E221: Alíquota informada indevidamente. Possível solução: A alíquota do ISSQN só deve ser informada quando: o ISSQN for devido a outro município ou o prestador do serviço for optante pelo Simples Nacional e houver retenção do ISSQN. Em outras situações a alíquota a ser aplicada será determinada pela Prefeitura.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16636899305239)

 CAUSA:**

O Valor do ISS esta sendo informado no XML através da TAG  <ValorIss>e a prefeitura não aceita que seja calculado.

![VALOR ISS 10-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18979960406039)

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16636940403863)

SOLUÇÃO:**

Marque o campo "Envia o ValorISS e alíquota no XML, apenas quando o ISS for devido a outro município?" **Empresa** (*Comercial » Preferências » Empresa*) aba Documentos Fiscais Eletrônicos » NFS-e.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16676674699159)

 OBSERVAÇÃO:**

Quando a marcação **"Envia o ValorISS e alíquota no XML, apenas quando o ISS for devido a outro município?"** estiver ligada, o sistema enviará as tags ValorISS e Alíquota no XML somente se a tag <municipioincidência> for diferente do município da empresa. 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30097074505495)

 

Após a Marcação do campo, gere o lote da nota novamente e verifique se no XML não ira mais constar o a TAG <ValorIss>.

 

![STATUS 10-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/18979960422039)

 

Confira mais informações no manual das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abanfs-e)


---

### 🔗 Links e Referências Internas:

- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abanfs-e)