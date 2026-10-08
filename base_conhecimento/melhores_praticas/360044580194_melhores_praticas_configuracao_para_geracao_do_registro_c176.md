# Melhores Práticas - Configuração para geração do registro C176 - Ressarcimento de ICMS e Fundo de Combate à Pobreza (FCP) em operações com substituição tributária

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580194-Melhores-Pr%C3%A1ticas-Configura%C3%A7%C3%A3o-para-gera%C3%A7%C3%A3o-do-registro-C176-Ressarcimento-de-ICMS-e-Fundo-de-Combate-%C3%A0-Pobreza-FCP-em-opera%C3%A7%C3%B5es-com-substitui%C3%A7%C3%A3o-tribut%C3%A1ria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580194-Melhores-Pr%C3%A1ticas-Configura%C3%A7%C3%A3o-para-gera%C3%A7%C3%A3o-do-registro-C176-Ressarcimento-de-ICMS-e-Fundo-de-Combate-%C3%A0-Pobreza-FCP-em-opera%C3%A7%C3%B5es-com-substitui%C3%A7%C3%A3o-tribut%C3%A1ria)  
> **ID:** `360044580194` | **Última Atualização:** 2026-07-22T15:51:10Z

---

*"Este registro deve ser informado quando da escrituração de documento fiscal, que acoberte operação que represente desfazimento de substituição tributária realizada em operações anteriores.*
*O documento informado neste registro deverá ser diferente do documento informado no registro pai (C100), pois é o documento referente à(s) última(s) aquisição(ões) da mercadoria e à retenção do imposto.*
*A obrigatoriedade e a forma de escrituração deste registro serão definidas pela UF de domicílio do contribuinte, inclusive sobre a apresentação dos campos CHAVE_NFE_RET; COD_PART_NFE_RET; SER_NFE_RET;*
*NUM_NFE_RET; ITEM_NFE_RET, COD_MOT_RES e VL_UNIT_RES_FCP_ST."*

*Fonte: Guia Prático EFD-ICMS/IPI – Versão 3.0 Atualização: 07/05/2018*

Visando facilitar o entendimento bem como as configurações a serem realizadas para a geração do registro, ilustramos em alguns passos os procedimentos a serem realizados.

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19195701521559)

 Comercial » Rotinas » Central de Compras

Realizado o lançado de uma nota de compra em operação interestadual de São Paulo-SP para o Paraná-PR com incidência de ICMS-ST:

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19195715496087)

 Comercial » Rotinas » Central de Vendas

Realizado o lançamento de uma nota de venda deste mesmo produto em uma operação interestadual do Paraná-PR para o estado  Goiás-GO com a incidência do ICMS:

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19195715499031)

 Livros Fiscais » Arquivos » Geração ICMS/IPI

Gerado as duas notas nos livros fiscais. 

Com base nesse caso de testes pode-se constatar até aqui que:

- Comprou-se 10 unidades do produto 8905 com ST pago antecipadamente, então tivemos:

Vlr. Unit.: 100,00 (100*10=1000)

Base de ST: 1.465,00

Vlr. de ST: 143,70

-  Vendeu-se 5 unidades do produto 8905 com ICMS Normal, então tivemos:

Vlr. Uint.: 200,00 (200*5=1000)

Base de ICMS: 1.000,00

Vlr. de ICMS: 70,00

Neste caso cabe ao contribuinte solicitar o ressarcimento do ICMS-ST, veja abaixo como proceder parar gerar o registro C176, vinculado ao registro C100/C170 da nota de venda.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19195701533463)

 Livros Fiscais » Arquivos » Cadastro Livro ICMS/IPI

Selecione a nota que deu saída no produto, acesse a aba Notas p/ressarcimento de ST e inclua a(s) nota(s) de compra que deu entrada no(s) produto(s) com o ICMS-ST já pago e que portanto gera(m) o direito a restituição, tomando-se nosso caso de testes como base, segue o exemplo:

Esse procedimento faz com que o registro C176 seja gerado no EFD ICMS/IPI conforme veremos a seguir.

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19195715505047)

 Comercial » Preferências » Empresa

Na aba EFD- Escrituração Fiscal Digital deve-se marcar a geração dos registros: C170/C173/C176:

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/19195715506199)

 Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI

Solicitar a geração do o arquivo EFD conforme segue:

Estando no cadastro de ICMS/IPI>> Aba Notas p/Ressarcimento de ST os dados devidamente preenchidos, estes irão para o registro C176 conforme segue:

|C176|1|111534||28122018|000000001|5,000|100,000|732,500||1||||||0,000||1||||||||