# Vendedor não existe ou não pode ser usado aqui: PK[]

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615533-Vendedor-n%C3%A3o-existe-ou-n%C3%A3o-pode-ser-usado-aqui-PK](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615533-Vendedor-n%C3%A3o-existe-ou-n%C3%A3o-pode-ser-usado-aqui-PK)  
> **ID:** `360044615533` | **Última Atualização:** 2026-07-22T15:55:07Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806421488535)

 MENSAGEM:**

Vendedor não existe ou não pode ser usado aqui: PK[]

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806421489815)

 SOLUÇÃO:**

De acordo com as possíveis causas da mensagem, seguem os procedimentos para correções:

 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806413375511)

 Código informado incorretamente:

- Certifique-se que o código do vendedor informado no campo **"Vendedor"** está correto.

 

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806413381527)

 Vendedor **INATIVO**:

- Acesse a tela **"Vendedores/Compradores"*** (Caminho de acesso: Configurações » Cadastros)* e confirme se o campo **"Ativo"** encontra-se marcado para o vendedor que está sendo utilizado.

- Em caso negativo, sintonize internamente se essa inativação procede ou se poderá ser ajustada.

 

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806421496087)

 TOP com** restrição:**

Se a situação ocorre em lançamentos através do Portal (Vendas/Compras/Mov.Interna), anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo:

- Acesse o cadastro de TOP’s *(Caminho de acesso: Comercial » Arquivo » Cadastros).*

- Acione o botão 'Outras Opções' » '**Restrições/Exceções**'.

- Verifique se existem regras vinculadas para Vendedor/Comprador.

**Restrições:** Se o vendedor **não **estiver incluído nessa lista, a mensagem será apresentada.

**Exceções: **Se o vendedor estiver incluído nessa lista, a mensagem será apresentada.

 

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806413387799)

 Central de Certificações:

- Caso a empresa utilize o módulo de 'Central de Certificação', observe se na tela de "**Central de Certificações**" *(Caminho de acesso: Comercial > Avançado > Certificações > Central de Certificações)* existe alguma regra definida para a empresa utilizada e se o usuário da operação está com alguma restrição vinculada (Tela "**Usuários"/ **Aba "**Validações"**).

- Em caso positivo, sintonize internamente para compreender a necessidade dessa regra no processo da empresa e, assim, altere os dados do seu lançamento ou desative a regra.

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16806413389975)

 CAUSA:**

Mensagem apresentada ao tentar executar alguma rotina do sistema com determinado código vendedor, que possui restrições de usabilidade e/ou encontra-se inativo.