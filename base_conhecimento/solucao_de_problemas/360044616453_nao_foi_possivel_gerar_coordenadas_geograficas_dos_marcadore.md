# Não foi possível gerar coordenadas geográficas dos marcadores

> **Módulo:** Solucao de Problemas | **Subseção:** Configurações  
> **Fonte Oficial:** [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616453-N%C3%A3o-foi-poss%C3%ADvel-gerar-coordenadas-geogr%C3%A1ficas-dos-marcadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616453-N%C3%A3o-foi-poss%C3%ADvel-gerar-coordenadas-geogr%C3%A1ficas-dos-marcadores)  
> **ID:** `360044616453` | **Última Atualização:** 2026-07-22T15:54:01Z

---

**

![Mensagem FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585782007319)

 MENSAGEM:**

Esta página não carregou o Google Maps corretamente" e "Não foi possível gerar coordenadas geográficas dos marcadores.

 

**

![Situação FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585782013463)

 SITUAÇÃO:**

Ao tentar efetuar a formação de carga, é apresentada a mensagem.

 

**

![Causa FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585813488279)

 CAUSA:**

Ocorre quando as configurações para usar Mapa não estão devidamente corretas.

 

**

![Solução FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585782027415)

 SOLUÇÃO:**

![1 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585813506327)

 A API KEY deve ser gerada no GOOGLE em:

[https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials) e informada no parâmetro **CHAVEGOOGLEMAP** (*Configurações » Avançado » Preferências*).

![2 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/18585782042263)

 Além disso, cada uma das 3 APIs devem ser ativadas:

- Directions API (https://console.developers.google.com/apis/library/directions-backend.googleapis.com)

- Geocoding API (https://console.developers.google.com/apis/library/geocoding-backend.googleapis.com)

- Maps JavaScript API (https://console.developers.google.com/apis/library/maps-backend.googleapis.com)

**Observação:**

O serviço do Google maps, pode sofrer alteração por parte do Fornecedor do Serviço(Google), no que se refere a cobrança para utilização do serviço, consulte informações com o Google.