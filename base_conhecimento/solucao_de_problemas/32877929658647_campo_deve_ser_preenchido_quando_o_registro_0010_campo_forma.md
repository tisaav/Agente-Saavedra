# Campo deve ser preenchido quando o registro 0010, campo forma_trib, for igual a 8 ou 9 (Imune ou Isento de IRPJ)

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32877929658647-Campo-deve-ser-preenchido-quando-o-registro-0010-campo-forma-trib-for-igual-a-8-ou-9-Imune-ou-Isento-de-IRPJ](https://ajuda.sankhya.com.br/hc/pt-br/articles/32877929658647-Campo-deve-ser-preenchido-quando-o-registro-0010-campo-forma-trib-for-igual-a-8-ou-9-Imune-ou-Isento-de-IRPJ)  
> **ID:** `32877929658647` | **Última Atualização:** 2026-07-22T14:30:05Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33154446858263)

 MENSAGEM: **

Erro apresentado no relatório da ECF: Campo deve ser preenchido quando o registro 0010, campo forma_trib, for igual a 8 ou 9 (Imune ou Isento de IRPJ).

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33154438144023)

SOLUÇÃO:**

Acesse a tela **''Empresa''** (Contabilidade> Preferências), aba '**'ECF- Escrituração Contábil Fiscal'' **e sub-aba **''Parâmetros de tributação''**. 

![Marcador 1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33154758613399)

 O campo** ''Apuração do IRPJ para Imunes ou Isentas''** só deve ser preenchido quando o campo** ''Forma de tributação''** for** imune ou isenta.**

 

![image (1).png](https://ajuda.sankhya.com.br/hc/article_attachments/33154446860951)

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/33154605168407)

****AMBIENTE E CAUSA DO ERRO:** 

**Registro com erro**: 0010 

**Campo com erro**: FORMA_APUR_I

**Conteúdo atual**: O campo Apuração do IRPJ para Imunes ou Isentas está com valor **D**, mas **não deveria. **Pois, ele deve ser preenchido **s****omente quando a Forma de tributação, no campo forma_trib, estiver igual a 8 ou 9.**