# (visto Fer) A folha do Autônomo ou do Pró Labore está ficando sem eventos.

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/32401173681431--visto-Fer-A-folha-do-Aut%C3%B4nomo-ou-do-Pr%C3%B3-Labore-est%C3%A1-ficando-sem-eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/32401173681431--visto-Fer-A-folha-do-Aut%C3%B4nomo-ou-do-Pr%C3%B3-Labore-est%C3%A1-ficando-sem-eventos)  
> **ID:** `32401173681431` | **Última Atualização:** 2026-07-29T13:19:50Z

---

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32401173672471)

** MENSAGEM:**

Falha - A tabela de férias (TFPFER) encontra-se vazia para o funcionário. Esta é uma configuração inválida dado que na admissão é realizada a inserção do primeiro período aquisitivo do funcionário.

 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32401178860183)

** SITUAÇÃO:**

Essa situação ocorre especificamente quando:

- O trabalhador está cadastrado com vínculo de autônomo ou pró labore, porém, esses vínculos não estão incluídos no parâmetro** FPSEMFERIAS**, que define os vínculos sem direito a férias.

- Como resultado, o sistema interpreta que o autônomo ou pró labore tem direito a férias e, por isso, tenta acessar registros na tabela TFPFER que, nesse caso, está vazia, resultando em erro no processamento.**
**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32401178861335)

** SOLUÇÃO:**

Acesse a tela **"Preferências"** *(Configurações» Avançado » Preferências) *e no **parâmetro FPSEMFERIAS** inclua os vínculos que não têm direito a férias: 

- 02 - Estagiário 

- 80 - Diretor Sem Vínculo Empregatício

- 90 - Profissional Autônomo

- 99- Pensionistas

**

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/32404395068823)

**

Após a inclusão correta dos vínculos no parâmetro, o sistema não buscará mais registros de férias para esses vínculos, permitindo que o cálculo da folha seja realizado sem erros.

 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/32401178855703)

** CAUSA:**

Ao realizar o cálculo, o sistema tenta localizar um período aquisitivo de férias na tabela** TFPFER**. Esse registro é criado automaticamente no momento da admissão de empregados que têm direito a férias.

No entanto, trabalhadores autônomos ou pró labore não têm direito a férias. Por isso, eles não devem gerar registros na tabela  TFPFER. Se esse tipo de vínculo não for corretamente classificado como **“sem direito a férias”**, o sistema tentará localizar um período aquisitivo que não existe, o que causa uma falha no processamento.