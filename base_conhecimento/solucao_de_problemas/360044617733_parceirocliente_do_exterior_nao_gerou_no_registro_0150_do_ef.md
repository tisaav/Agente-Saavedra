# Parceiro/Cliente do Exterior, não gerou no registro 0150 do EFD-Contribuições

> **Módulo:** Solucao de Problemas | **Subseção:** Fiscal e Contábil   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617733-Parceiro-Cliente-do-Exterior-n%C3%A3o-gerou-no-registro-0150-do-EFD-Contribui%C3%A7%C3%B5es](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617733-Parceiro-Cliente-do-Exterior-n%C3%A3o-gerou-no-registro-0150-do-EFD-Contribui%C3%A7%C3%B5es)  
> **ID:** `360044617733` | **Última Atualização:** 2026-07-22T15:52:34Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612047679767)

 MENSAGEM:**

Parceiro/Cliente do Exterior, não gerou no registro 0150 do EFD-Contribuições. 

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612040049687)

 SOLUÇÃO:**
Para correção deste erro, siga os passos abaixo:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612040051991)

 Acesse: *Configurações » Avançado » Preferências*:

- 
**"CODPAISBRASIL-Código do País Brasil":** informe o valor: 55 

 

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/14919266212887)

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612047690135)

 Acesse: *Configurações » Cadastros » Endereços » Países*:

Crie o cadastro do Pais do Exterior. Lembrando de verificar junto ao [BACEN](http://www.bcb.gov.br/pt-br#!/home) o código do 'Pais Domicilio Fiscal

- Exemplo:
Código do Brasil: 1058
Código do México: 4936

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612047694231)

 Acesse: *Configurações » Cadastros » Endereços » Estados*:

- Crie um Estado com as características abaixo:
Descrição: EXTERIOR
Pais: informe o cadastro feito no item 2
Sigla: EX
Código IBGE = 99

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612040061207)

 Acesse: *Configurações » Cadastros » Endereços » Cidades:*

- Crie uma Cidade com a descrição referente ao Endereço do Pais do Exterior
Cód; UF: Informe o Estado criado no item 3
Mun. domicílio fiscal= 9999999

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612040064791)

 Acesse: *Configurações » Cadastros » Parceiros*:

- Vincule a Cidade cadastrada no item 4 ao parceiro do Exterior

- Aba **"Endereço"**, campo » **"Cód. Cidade"**.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16612040068631)

CAUSA:**

Ao gerar o EFD Contribuições o parceiro do Exterior não está no Registro 1050 devido a falta de configurações da Cidade do Exterior.