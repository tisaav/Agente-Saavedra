# Erro ao emitir relatório de provisão 13º e férias

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37095400562967-Erro-ao-emitir-relat%C3%B3rio-de-provis%C3%A3o-13%C2%BA-e-f%C3%A9rias](https://ajuda.sankhya.com.br/hc/pt-br/articles/37095400562967-Erro-ao-emitir-relat%C3%B3rio-de-provis%C3%A3o-13%C2%BA-e-f%C3%A9rias)  
> **ID:** `37095400562967` | **Última Atualização:** 2026-07-29T13:22:06Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095400553111)

 MENSAGEM:**

Falha

Não foi possível gerar o relatório solicitado.

Motivo: net.sf.jasperreports.engine.fill.JRExpressionEvalException: Error evaluating expression :
Source text : new DecimalFormat(",0.00”).format($F{VLRPARCELA})

 

![Imagem](https://p23.zdusercontent.com/attachment/9618168/kYaEUyTO1VyEeqxvXEJNK02K0?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..3nfBahd1qwUcA-ECsxN7fA.Z2Qi6P-YS81-2W7jMm7Xd4xdil_LlMXMHTsD5LaWW-wT7ijJv-kGkFon4-kvE5xHga9Vxm0deF-h9vzp1P86852URYAEltoip-TKhDMWHYboaczpDc9Zc6pvU3muyd-1hyYzbQHjq49Lb9XeMbsxlS7U8y2Gy4yC65N4Jbxm_rfiQkyk8E5JnIhSa5oLa5pUQYWHKOWWRKoBiHsco7_JORyXI2lInFwrDjAlqw27covHFfcTmtdUaQa0Crhgjex-MXFKhC5Gwh1eVUltOSFrD2OsS8KN1iAwvLoFkojWJaY.Hpp--V5YzhtwLNHRGpjYsw)

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095400555031)

 SITUAÇÃO:**

Ao tentar emitir o relatório de Provisão de 13º e Férias, é apresentada uma mensagem de erro.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095409452951)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37118160571415)

 Apague e calcule as provisões da referência em questão, garantindo que os campos sejam corretamente alimentados e permitindo a impressão do relatório.

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37118135381783)

 **OBSERVAÇÃO: **Se houver provisões em referências futuras á que está sendo calculada, é necessário excluir essas provisões posteriores antes de recalcular.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37095400555415)

 CAUSA: **

As provisões da referência em que o relatório está sendo impresso não possuem o campo **VLRPARCELA **preenchido.

 

![image (100).png](https://ajuda.sankhya.com.br/hc/article_attachments/37118350250263)