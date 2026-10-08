# E0686 Rejeição: A alíquota do PIS deve ser igual ou maior que 0 e menor ou igual a 100%.

> **Módulo:** Solucao de Problemas | **Subseção:** Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária   
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/37227188958871-E0686-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-PIS-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100](https://ajuda.sankhya.com.br/hc/pt-br/articles/37227188958871-E0686-Rejei%C3%A7%C3%A3o-A-al%C3%ADquota-do-PIS-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100)  
> **ID:** `37227188958871` | **Última Atualização:** 2026-07-22T14:14:27Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227188941079)

 **MENSAGEM**

E0686 Rejeição: A alíquota do PIS deve ser igual ou maior que 0 e menor ou igual a 100%.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227172193559)

 **SITUAÇÃO**

Ao emitir um documento fiscal (NF-e ou NFC-e), o sistema **rejeitou a nota** informando que a alíquota de PIS configurada está **fora do intervalo permitido**.

 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227188943255)

 **SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227172195735)

 Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e identifique o produto utilizado no documento fiscal rejeitado.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227172197015)

 Na aba **"Impostos"**, verifique o valor informado no campo **"Grupo PIS"**.

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227172197655)

 Acesse a tela **"Alíquotas de PIS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS).

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227188951703)

 Localize o cadastro de alíquota correspondente ao **"Grupo PIS"** identificado no passo 2, filtrando por:

- 

Empresa

- 

TOP (Tipo de Operação)

- 

Parceiro

- 

Tipo (Saída/Entrada)

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227172200599)

 Verifique o valor informado no campo** "Alíquota''** e certifique-se de que está **entre 0% e 100%**.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227172201623)

 Caso o valor esteja **fora do intervalo permitido**, ajuste a alíquota para um valor válido (entre 0 e 100).

![7 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227172202519)

 Consulte o **contador responsável** para confirmar a alíquota correta de PIS e o **"Código de situação tributária - CST"** adequado para a operação.

![8 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37226833845015)

 Após realizar os ajustes necessários, **fature novamente** o documento fiscal ou **redigite o item** na nota e gere um novo lote para transmissão.

 

**

![Observação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37616413907735)

 OBSERVAÇÕES:**

- 

O **cálculo de PIS e COFINS é obrigatório** para todas as movimentações de venda, mesmo que a incidência seja zero.

- 

Recomenda-se sempre **criar regras específicas** para o respectivo tipo de movimento.

- 

Revise também as marcações de PIS no cadastro da **"Empresa"** (Comercial » Preferências » Empresa) e no **"TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/37227188956311)

 **CAUSA**

A rejeição ocorre porque foi informada uma **alíquota de PIS inválida** no cadastro de **"Alíquotas de PIS"**, com valor **menor que 0% ou maior que 100%**. A Sefaz valida que todas as alíquotas de impostos devem estar dentro do intervalo permitido (entre 0 e 100), e qualquer valor fora deste range resulta na rejeição do documento fiscal.