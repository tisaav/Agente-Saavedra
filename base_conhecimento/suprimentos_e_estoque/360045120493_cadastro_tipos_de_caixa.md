# Cadastro Tipos de Caixa

> **Módulo:** Suprimentos e Estoque | **Subseção:** WMS  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120493-Cadastro-Tipos-de-Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120493-Cadastro-Tipos-de-Caixa)  
> **ID:** `360045120493` | **Última Atualização:** 2026-07-29T14:16:19Z

---

```text
**

![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42311606995607)

 Módulo: **WMS > Cadastros
```

![CTC1.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896506143127)

Nesta tela, você poderá inserir as seguintes informações:

- Unid. de Medida;

- Altura;

- Largura;

- Comprimento;

- Metros Cúbicos;

- Peso da Caixa vazia;

- Código de Barras.

**Observação:** o parâmetro** "Registrar tipo de caixas na conferência por pedido - WMSUSAREGCAIXA"** quando ligado, na formação de volumes será requerido o Código de Barras da caixa.

Na Conferência, ao bipar o checkout, é necessário bipar a caixa antes de iniciar a conferência dos produtos. 

Após o fechamento de cada volume, você deve bipar a caixa novamente.

![clip2549.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896522076055)

            

![clip2550.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896523351959)

Na recontagem, foi criada a coluna **"Desc. Caixa"** onde é exibido o campo **"Descr. Abreviada"** do cadastro do Tipo de Caixa.

**Observação:** caso seja criado um novo volume, será requerido o Código de barras da caixa.

![clip2551.png](https://ajuda.sankhya.com.br/hc/article_attachments/8896524493463)

**Nota:** ao final da Conferência, o sistema soma o Peso e o M3 dos item do pedido juntamente com o de cada caixa bipada e exibe o resultado no pedido.

## Parâmetros que influenciam nesta rotina

Para o uso desta tela, desative os seguintes parâmetros:

- "**Formação de Volumes após a conferência por pedido - FORMVOLPOSCONF" **e

- 
"**Preserva a quantidade do Volume pedido ? - PRESERQTDVOL"**

Quanto aos parâmetros a seguir, estes deverão ser habilitados:

- 
**"****Detalhar volumes em conferências p/pedido no WMS? - DETALHAVOLWMS"; **

- 
**"****Registrar tipo de caixas na conferência por pedido - WMSUSAREGCAIXA" **e

- 
**"****No faturamento, somar na nota o Peso e M3 dos pedi - FATSOMAPESOM3P"**

Você pode selecionar a opção desejada no parâmetro **"****Somar Quantidade de Volumes por ? - SOMAQTDVOL"**