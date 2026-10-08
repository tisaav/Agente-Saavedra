# E0444 Rejeição: O valor percentual de dedução/redução informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37225496637335-E0444-Rejei%C3%A7%C3%A3o-O-valor-percentual-de-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-pode-reduzir-o-valor-da-BC-de-forma-que-resulte-no-valor-do-ISSQN-a-uma-al%C3%ADquota-efetiva-menor-que-2-exceto-para-os-c%C3%B3digos-relativos-aos-servi%C3%A7os-7-02-7-05-e-16-01](https://ajuda.sankhya.com.br/hc/pt-br/articles/37225496637335-E0444-Rejei%C3%A7%C3%A3o-O-valor-percentual-de-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-pode-reduzir-o-valor-da-BC-de-forma-que-resulte-no-valor-do-ISSQN-a-uma-al%C3%ADquota-efetiva-menor-que-2-exceto-para-os-c%C3%B3digos-relativos-aos-servi%C3%A7os-7-02-7-05-e-16-01)  
> **ID:** `37225496637335` | **Última Atualização:** 2026-07-22T14:15:56Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225496611607)

 **MENSAGEM**

E0444 Rejeição: O valor percentual de dedução/redução informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225479565463)

 **SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o sistema retornou a rejeição **E0444**, relacionada ao **percentual de dedução ou redução da Base de Cálculo do ISSQN** informado no documento.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225496616087)

 **SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225496617367)

 Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225479569303)

 Localize o cadastro da alíquota utilizada na operação que gerou a rejeição.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225496620567)

 Verifique o **percentual de redução da Base de Cálculo do ISSQN** informado no cadastro da alíquota.

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225496621719)

 Calcule a **alíquota efetiva** resultante da aplicação do percentual de redução, utilizando a fórmula: 

```text
Alíquota Efetiva = (Base de Cálculo Reduzida / Base de Cálculo Original) × Alíquota do ISSQN
```

 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225479577495)

 Certifique-se de que a **alíquota efetiva resultante seja igual ou superior a 2%**. Caso contrário, ajuste o percentual de redução da Base de Cálculo para que a alíquota efetiva não fique abaixo deste limite.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37673723506839)

 Se o serviço prestado corresponder aos **códigos 7.02, 7.05 ou 16.01**, verifique se o código de serviço está corretamente informado na DPS, pois estes são exceções à regra e podem ter alíquota efetiva inferior a 2%.

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37673759817111)

 Após realizar os ajustes necessários, **reemita a DPS** com as informações corrigidas.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37225479580439)

 **CAUSA**

A rejeição ocorre porque a **Sefaz valida que a alíquota efetiva do ISSQN**, após a aplicação de deduções ou reduções na Base de Cálculo, **não pode ser inferior a 2%**, conforme estabelecido pela legislação tributária. Esta regra visa garantir uma **arrecadação mínima do imposto municipal** sobre serviços. A exceção aplica-se apenas aos serviços com códigos **7.02, 7.05 e 16.01**, que possuem tratamento tributário diferenciado. Quando o sistema identifica que o percentual de dedução/redução informado resulta em uma alíquota efetiva abaixo do limite estabelecido, e o serviço não está entre as exceções, a DPS é rejeitada com a mensagem **E0444**.