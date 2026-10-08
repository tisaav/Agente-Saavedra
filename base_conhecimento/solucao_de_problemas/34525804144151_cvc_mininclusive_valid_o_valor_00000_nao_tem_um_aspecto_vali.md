# cvc-minInclusive-valid: O valor '0.0000' não tem um aspecto válido em relação ao minInclusive '0.5' do tipo 'TS_fap'. cvc-type.3.1.3: O valor '0.0000' do elemento 'fap' não é válido.

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34525804144151-cvc-minInclusive-valid-O-valor-0-0000-n%C3%A3o-tem-um-aspecto-v%C3%A1lido-em-rela%C3%A7%C3%A3o-ao-minInclusive-0-5-do-tipo-TS-fap-cvc-type-3-1-3-O-valor-0-0000-do-elemento-fap-n%C3%A3o-%C3%A9-v%C3%A1lido](https://ajuda.sankhya.com.br/hc/pt-br/articles/34525804144151-cvc-minInclusive-valid-O-valor-0-0000-n%C3%A3o-tem-um-aspecto-v%C3%A1lido-em-rela%C3%A7%C3%A3o-ao-minInclusive-0-5-do-tipo-TS-fap-cvc-type-3-1-3-O-valor-0-0000-do-elemento-fap-n%C3%A3o-%C3%A9-v%C3%A1lido)  
> **ID:** `34525804144151` | **Última Atualização:** 2026-07-29T13:20:48Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34525778680855)

 **MENSAGEM:**

[cvc-minInclusive-valid] O valor '0.0000' não tem um aspecto válido em relação ao minInclusive '0.5' do tipo 'TS_fap'.
[cvc-type.3.1.3] O valor '0.0000' do elemento 'fap' não é válido.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34525778683927)

 **SITUAÇÃO:**

Ao tentar enviar o evento 'S-1005 – Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos' para o eSocial, o sistema apresenta um erro.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34525804138135)

 **SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34983000274455)

 Acesse a tela **"Registro Fiscal"** (Pessoal+» Cadastros» Registro Fiscal) e verifique o campo **"Fator Acidentário de Prevenção (FAP)";**

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34983005752727)

 Corrija o valor do FAP, garantindo que respeite a regra do layout do eSocial.
 

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34983000278679)

 **Observação: **o Fator Acidentário de Prevenção (FAP) deve conter 4 casas decimais.

- 

**Validação:** Preenchimento obrigatório e exclusivo por Pessoa Jurídica e: 
a) [ideEstab/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/index.html#1005_infoEstab_inclusao_ideEstab_tpInsc) = [4] e o campo [cnpjResp](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/index.html#1005_infoEstab_inclusao_dadosEstab_cnpjResp) não estiver informado; ou
b) [ideEstab/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/index.html#1005_infoEstab_inclusao_ideEstab_tpInsc) = [1, 4] e o fator informado for diferente do definido pelo órgão governamental competente para o estabelecimento ou para o CNPJ responsável pela inscrição no CNO (neste caso, deverá haver informações de processo em [procAdmJudFap](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/index.html#1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudFap)); ou
c) [ideEstab/tpInsc](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/index.html#1005_infoEstab_inclusao_ideEstab_tpInsc) = [1, 4] e o estabelecimento ou o CNPJ responsável pela inscrição no CNO não for encontrado na tabela FAP. 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/34525778685463)

 Se informado, o valor deve ser maior ou igual a **0,5000** e menor ou igual a **2,0000**. No caso da alínea "b", deve ser diferente do valor definido pelo órgão governamental competente.