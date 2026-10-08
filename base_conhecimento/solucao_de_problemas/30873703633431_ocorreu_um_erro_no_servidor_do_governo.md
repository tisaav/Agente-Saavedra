# Ocorreu um erro no servidor do governo

> **Módulo:** Solucao de Problemas | **Subseção:** Financeiro  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/30873703633431-Ocorreu-um-erro-no-servidor-do-governo](https://ajuda.sankhya.com.br/hc/pt-br/articles/30873703633431-Ocorreu-um-erro-no-servidor-do-governo)  
> **ID:** `30873703633431` | **Última Atualização:** 2026-07-22T14:34:35Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30873711886871)

 **MENSAGEM:**
[FIN_E00502] Ocorreu um erro no servidor do governo.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30873711887255)

SOLUÇÃO:**

Verifique na tela **"****URLs para Serviços"** (*Caminho: Livros Fiscais » Conexão » URLs para Serviços*) se há um cadastro com o código **0 (zero),** no campo **"****Cód. Unidade Federativa"** e se a configuração está correta. O sistema interpreta o código 0 (zero) como uma definição válida para todas as unidades federativas (UFs).

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/30873703630231)

As URLs a serem utilizadas são as seguintes:

 

**Homologação**

- 
**Recepção:** [https://www.testegnre.pe.gov.br/gnreWS/services/GnreLoteRecepcaoConsulta](https://www.testegnre.pe.gov.br/gnreWS/services/GnreLoteRecepcaoConsulta)

- 
**Consulta:** [https://www.testegnre.pe.gov.br/gnreWS/services/GnreResultadoLote](https://www.testegnre.pe.gov.br/gnreWS/services/GnreResultadoLote)

**Produção**

- 
**Recepção:** [https://www.gnre.pe.gov.br/gnreWS/services/GnreLoteRecepcaoConsulta](https://www.gnre.pe.gov.br/gnreWS/services/GnreLoteRecepcaoConsulta)

- 
**Consulta:** [https://www.gnre.pe.gov.br/gnreWS/services/GnreResultadoLote](https://www.gnre.pe.gov.br/gnreWS/services/GnreResultadoLote)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/30873711888279)

CAUSA:**
Ocorre quando não existe uma configuração com o código **0** na tela Urls para Serviços ou quando a Url inserida está incorreta.