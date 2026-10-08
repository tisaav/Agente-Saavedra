# "Cód. Cid. Inicio CT-e" e "Cód. Cid. Fim CT-e" não são permitidas para este título."

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360058996033--C%C3%B3d-Cid-Inicio-CT-e-e-C%C3%B3d-Cid-Fim-CT-e-n%C3%A3o-s%C3%A3o-permitidas-para-este-t%C3%ADtulo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058996033--C%C3%B3d-Cid-Inicio-CT-e-e-C%C3%B3d-Cid-Fim-CT-e-n%C3%A3o-s%C3%A3o-permitidas-para-este-t%C3%ADtulo)  
> **ID:** `360058996033` | **Última Atualização:** 2026-08-06T20:00:14Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251439683351)

 MENSAGEM**:

 [CORE_E02442] Ao tentar importar CT-e apresenta este erro, "As informações  de "Cód. Cid. Inicio CT-e" e "Cód. Cid. Fim CT-e" não são permitidas para este título.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251439687447)

 SOLUÇÃO:**

 

Para correção, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251439689495)

 Acesse: *Arquivos>>Cadastros>>Tipos de Operação*

- Aba: **"NF-/NFC-e"**

- Campo **"Modelo de Documento": **selecione uma das opções: 57, 63 ou 67

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251444175511)

  Na top Aba Livros Fiscais -> informe os CFOP's da operação, atualização de Livro ICMS: entrada

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251444179607)

 Se a TOP vinculada ao XML que estiver sendo importado for do Tipo de Movimento = 'Compras' irá apresentar a mensagem de erro.  Para importar CT-e pelo portal é necessário que a top seja do Tipo de Movimento 'Financeiro' .

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16251444184215)

 CAUSA:**

Erro ocorre quando as configurações da TOP vinculadas ao XML que estiver sendo importado for do Tipo de Movimento = 'Compras' .