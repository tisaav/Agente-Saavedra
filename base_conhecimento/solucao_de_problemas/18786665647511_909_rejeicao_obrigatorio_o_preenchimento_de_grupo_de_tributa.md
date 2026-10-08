# 909 Rejeição: Obrigatório o preenchimento de Grupo de Tributacao do ICMS monofasica sobre combustiveis [nItem:x]

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/18786665647511-909-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3rio-o-preenchimento-de-Grupo-de-Tributacao-do-ICMS-monofasica-sobre-combustiveis-nItem-x](https://ajuda.sankhya.com.br/hc/pt-br/articles/18786665647511-909-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3rio-o-preenchimento-de-Grupo-de-Tributacao-do-ICMS-monofasica-sobre-combustiveis-nItem-x)  
> **ID:** `18786665647511` | **Última Atualização:** 2026-07-22T14:52:06Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18786665635351)

 **MENSAGEM:**

909 Rejeição: Obrigatório o preenchimento de Grupo de Tributacao do ICMS monofasica sobre combustiveis [nItem:x]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18786645318935)

SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19056436324759)

 Realize a consulta abaixo para verificar se produto tem rastreio de estoque ST.

SELECT UFS.UF, UFS.CODIBGE, MAX(VAS.NUNOTAORIG) FROM TGFVAS VAS
INNER JOIN TGFITE ITE ON ITE.NUNOTA = VAS.NUNOTAORIG AND ITE.SEQUENCIA = VAS.SEQUENCIAORIG
INNER JOIN TGFCAB CAB ON CAB.NUNOTA = ITE.NUNOTA
INNER JOIN TGFPAR PAR ON PAR.CODPARC = CAB.CODPARC
INNER JOIN TSIUFS UFS ON UFS.CODUF = (SELECT CID.UF FROM TSICID CID WHERE CID.CODCID = PAR.CODCID)
WHERE ITE.CODPROD = XXXX  AND VAS.NUNOTA = XXXX
GROUP BY UFS.UF, UFS.CODIBGE
ORDER BY 3 DESC

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19056427090583)

 Para que o grupo de TAGs seja gerado corretamente no XML da NF-e, acesse a tela **“Produtos”** (Configurações » Cadastros » Produtos » Produtos) e verifique se os produtos classificados como gás estão devidamente configurados.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38473334695063)

 Na aba **''Rastreamento por Empresa''** confirme:

- 

O **código da empresa** incluído;

- 

O campo **“Tipo de Rastreamento”** deve estar definido como **“RASTREAR”**, conforme imagem abaixo:

 

![Produtos 14-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19056427087511)

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38473334696215)

 Além da configuração no cadastro do produto, o processo de rastreamento deve estar ativado no sistema por meio da tela **“Ativar/Reprocessar Rastreamento de Estoque/ST” **(Livros Fiscais » Avançado » Rastreamento de Estoque/ST » Ativar/Reprocessar Rastreamento de Estoque/ST).

 

![ativar reprocessar 14-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19056436331543)

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38473387058967)

 Após selecionar o **produto** e a **empresa** desejados, clique em **“Processar”** para efetivar a configuração. O processamento deve ser concluído **sem retornar nenhum erro**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38739547040535)

 Após a execução correta, o XML deverá gerar o grupo de TAGs conforme exemplo abaixo:

```text
<origComb>
   <indImport>0</indImport>
   <cUFOrig>43</cUFOrig>
   <pOrig>100.0</pOrig>
</origComb>
```

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18786645321239)

CAUSA:**

O produto não está com o processo **“Ativar/Reprocessar Rastreamento de Estoque/ST”** ativo no sistema. Nessa situação, o grupo de TAGs não é gerado no XML, ocasionando rejeição na validação.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/38473387063447)

 OBSERVAÇÃO:**

Quando a nota for do **tipo de movimento Transferência**, além das configurações mencionadas anteriormente, é necessário que o campo **“Atualização de Livro ICMS”** esteja configurado como **“Ambos”**, conforme a imagem abaixo:

 

![Livro fiscal 14-11.png](https://ajuda.sankhya.com.br/hc/article_attachments/19056427107735)

 

Se for:

- 

**Nota de venda** → o campo deve estar marcado como **“Livro de Saída”**;

- 

**Nota de compra** → o campo deve estar marcado como **“Livro de Entrada”**.

Para mais detalhes sobre o processo de rastreamento, consulte a documentação ****[''Rastreabilidade de Estoque/ICMS-ST''](https://ajuda.sankhya.com.br/hc/pt-br/articles/5818008318231)**.**


---

### 🔗 Links e Referências Internas:

- [''Rastreabilidade de Estoque/ICMS-ST''](https://ajuda.sankhya.com.br/hc/pt-br/articles/5818008318231)