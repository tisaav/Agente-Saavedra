# Todas as NF-e's emitidas estão gerando a tag <xMun> como se o parceiro fosse do exterior.

> **Módulo:** Solucao de Problemas | **Subseção:** Vendas  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865174-Todas-as-NF-e-s-emitidas-est%C3%A3o-gerando-a-tag-xMun-como-se-o-parceiro-fosse-do-exterior](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865174-Todas-as-NF-e-s-emitidas-est%C3%A3o-gerando-a-tag-xMun-como-se-o-parceiro-fosse-do-exterior)  
> **ID:** `360042865174` | **Última Atualização:** 2026-07-22T16:05:51Z

---

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453302880151)

 SOLUÇÃO:**

Para correção deste erro, seguir os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453334521751)

 Acesse: "**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"**  (Caminho de acesso:* Configurações » Avançado » Preferências*)

Parâmetro: "**CODPAISBRASIL" **- Código do País Brasil

Alterar para : **55** , salvar.

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453302885783)

 Exemplo **Antes** do ajuste:

<xBairro>VILA NOVA CONCEICAO</xBairro>
<cMun>3550308</cMun>
**<xMun>EXTERIOR</xMun>**
<UF>SP</UF>

![Marcador 2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453302885783)

 Exemplo **Depois** do Ajuste:

<xBairro>VILA NOVA CONCEICAO</xBairro>
<cMun>3550308</cMun>
**<xMun>São Paulo</xMun>**
<UF>SP</UF>

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453334529943)

 Acessar novamente a emissão da Nota, faturar novamente ou criar nova Nota e Gerar Lote.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16453302892183)

 CAUSA:**

Definição incorreta no parâmetro "**CODPAISBRASIL"**.


---

### 🔗 Links e Referências Internas:

- [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)