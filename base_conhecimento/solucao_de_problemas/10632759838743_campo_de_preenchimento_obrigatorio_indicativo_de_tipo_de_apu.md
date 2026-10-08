# Campo de preenchimento obrigatório - Indicativo de tipo de apuração de IR

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/10632759838743-Campo-de-preenchimento-obrigat%C3%B3rio-Indicativo-de-tipo-de-apura%C3%A7%C3%A3o-de-IR](https://ajuda.sankhya.com.br/hc/pt-br/articles/10632759838743-Campo-de-preenchimento-obrigat%C3%B3rio-Indicativo-de-tipo-de-apura%C3%A7%C3%A3o-de-IR)  
> **ID:** `10632759838743` | **Última Atualização:** 2026-07-29T13:16:31Z

---

O campo "Incidência p/ IRRF" da aba eSocial deve estar preenchido, quando houver incidência de IRRF para o cálculo. (Mensagem de erro: Campo de preenchimento obrigatório - Indicativo de tipo de apuração de IR).
 

### 

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309766511383)

**SITUAÇÃO**

Esta mensagem aparece ao tentar salvar a configuração de eventos de folha de pagamento quando há inconsistência entre as configurações da aba **"Avançado"** (onde a incidência de IRRF está marcada) e da aba **"eSocial"** (onde o campo **"Incidência p/ IRRF"** está vazio ou incorreto).
 

### 

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309760984727)

**SOLUÇÃO**

Para corrigir o erro, ajuste a configuração do evento seguindo os passos abaixo:
 

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41065080934551)

 Acesse a tela **"Cadastro de Eventos"** (Pessoal >> Cadastros >> Eventos) e localize o evento que está apresentando o erro.

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41065080935319)

 Abra o evento e acesse a aba **"Avançado"**. Verifique se a opção **"IRRF"** está marcada para incidir.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41065080936215)

![3 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41065057914775)

 Acesse a aba **"eSocial"** e localize o campo **"Incidência p/ IRRF"**.

![Imagem](https://ajuda.sankhya.com.br/hc/article_attachments/41065080936855)

![4 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41065057915287)

 Preencha o campo **"Incidência p/ IRRF"** com o código correto conforme a Tabela 21 do eSocial (Tabela S-1010). Para eventos personalizados, utilize os códigos apropriados. 
 

![5 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41065057916183)

 Salve as alterações realizadas no evento.

![6 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/41065080939287)

 Envie o evento **S-1010** (Tabela de Rubricas) da rubrica alterada. Se o evento já foi transmitido anteriormente, será necessário retificar o **S-1010** com validade retroativa sempre que houver ajuste na aba e-social.
 

**Observação importante:** Eventos padrões do sistema possuem configurações automáticas. Para eventos personalizados, é fundamental realizar a configuração manual correta em ambas as abas para garantir a consistência dos valores enviados ao e-social com o valores apresentado no resumo de folha.
 

### 

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/42309760985367)

**CAUSA**

O erro ocorre devido à inconsistência entre as configurações das abas **"Avançado"** e **"eSocial"**. Quando o campo **"IRRF"** está marcado para incidir na aba **"Avançado"**, o sistema exige que o campo **"Incidência p/ IRRF"** na aba **"eSocial"** esteja preenchido com um código válido da tabela oficial do eSocial. A ausência ou erro neste preenchimento impede a validação do envio das informações fiscais.