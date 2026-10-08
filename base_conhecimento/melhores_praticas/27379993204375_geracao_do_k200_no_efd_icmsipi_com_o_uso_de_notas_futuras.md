# Geração do K200 no EFD ICMS/IPI com o uso de notas Futuras

> **Módulo:** Melhores Praticas | **Subseção:** Fiscal e Contábil  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/27379993204375-Gera%C3%A7%C3%A3o-do-K200-no-EFD-ICMS-IPI-com-o-uso-de-notas-Futuras](https://ajuda.sankhya.com.br/hc/pt-br/articles/27379993204375-Gera%C3%A7%C3%A3o-do-K200-no-EFD-ICMS-IPI-com-o-uso-de-notas-Futuras)  
> **ID:** `27379993204375` | **Última Atualização:** 2026-07-22T14:39:40Z

---

Quando a empresa opera com notas de vendas referentes a entregas futuras, é imprescindível que o parâmetro **"GERAK200CTE"** esteja **ativado**.

Caso este parâmetro esteja **desativado**, o sistema não realiza a validação, no momento da geração do SPED, das notas futuras no que diz respeito ao **estoque**, o que pode ocasionar divergências nos saldos.

Ao manter este parâmetro **ativado**, um novo campo será disponibilizado na geração do EFD ICMS/IPI:

 

![Geração do K200 no EFD ICMSIPI com o uso de notas Futuras 1.png](https://ajuda.sankhya.com.br/hc/article_attachments/27543154412055)

 

- 

Na data do K200, deve ser informada a **última data** do mês ao qual se refere a entrega;

- 

Considerando que o arquivo foi entregue com saldo incorreto, uma vez que as notas com datas futuras não foram consideradas no estoque, recomenda-se consultar o departamento contábil para definir o procedimento adequado para a retificação.