# Erro 721 - Não foi possível registrar o evento atual pois existe(m) evento(s) cadastrado(s) com data de ocorrência posterior para esse trabalhador que se tornarão inconsistentes em caso de recepção deste.

> **Módulo:** Solucao de Problemas | **Subseção:** Pessoal+  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/34524407270295-Erro-721-N%C3%A3o-foi-poss%C3%ADvel-registrar-o-evento-atual-pois-existe-m-evento-s-cadastrado-s-com-data-de-ocorr%C3%AAncia-posterior-para-esse-trabalhador-que-se-tornar%C3%A3o-inconsistentes-em-caso-de-recep%C3%A7%C3%A3o-deste](https://ajuda.sankhya.com.br/hc/pt-br/articles/34524407270295-Erro-721-N%C3%A3o-foi-poss%C3%ADvel-registrar-o-evento-atual-pois-existe-m-evento-s-cadastrado-s-com-data-de-ocorr%C3%AAncia-posterior-para-esse-trabalhador-que-se-tornar%C3%A3o-inconsistentes-em-caso-de-recep%C3%A7%C3%A3o-deste)  
> **ID:** `34524407270295` | **Última Atualização:** 2026-07-29T13:20:46Z

---

![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/34524407258263)

**Mensagem**

Erro 721 - Não foi possível registrar o evento atual pois existe(m) evento(s) cadastrado(s) com data de ocorrência posterior para esse trabalhador que se tornarão inconsistentes em caso de recepção deste

 

![Situação](https://ajuda.sankhya.com.br/hc/article_attachments/34524407260311)

**Situação**

Ao tentar gerar ou enviar o evento S-2299 de rescisão/desligamento para o eSocial, o sistema retorna mensagens de erro que impedem a transmissão. Essas situações ocorrem devido a inconsistências cadastrais, duplicidade de registros, problemas com eventos anteriores (como S-2205, S-2206, S-2230) com data posterior ao desligamento ou configurações incorretas de rubricas.

 

![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/34524407263767)

**Solução**

 

![1](https://ajuda.sankhya.com.br/hc/article_attachments/34982105939863)

 Verifique o histórico de envio do S-2205 e S-2206 na tela  **"Configuração Funcionários" (Configurações » Cadastros » Pessoal » Configuração Funcionários** os campos Data de Alteração - S-2205 e Data de Alteração - S-2206/2306 ou portal eSocial se existe eventos enviados após a data de desligamento. 

![2](https://ajuda.sankhya.com.br/hc/article_attachments/34982127840663)

 Exclua ou retifique eventos posteriores (S-2205, S-2206, S-2230, etc.) no sistema através da tela Central do e-social (Pessoal+ » Rotinas Folha » Central do eSocial) ícone recibo busca pelo evento e exclua o evento. 

![3](https://ajuda.sankhya.com.br/hc/article_attachments/34982105944471)

 Tente enviar o S-2299 novamente.
 

![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/34524378252439)

**Causa**

O eSocial exige uma hierarquia cronológica. A existência de eventos de alteração, afastamento ou pagamento com data posterior à demissão, ou inconsistências na sequência de eventos de folha, bloqueia o encerramento do vínculo.