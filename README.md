# movie-ratings

> ⚠️ **Note:** This repository is written entirely in **Portuguese (pt-BR)**. It contains my personal reviews and ratings of movies.

Este repositório contém uma **coleção pessoal de filmes que assisti**, organizados com alguns dados relevantes como título, ano e, quando possível, notas, data em que foi visto e uma breve review.

Nem todos os filmes têm review ou notas. Muitos eu assisti há muito tempo e estou apenas registrando.

## 🗂️ Estrutura dos Dados

Cada entrada do arquivo CSV (ou o json) contém os seguintes campos:

| Campo            | Descrição                                                                         |
| ---------------- | --------------------------------------------------------------------------------- |
| `imdbID`         | Código único do filme no IMDb (ex: `tt0111161`)                                   |
| `Title`          | Título do filme                                                                   |
| `Year`           | Ano de lançamento                                                                 |
| `Rating10`       | Nota dada ao filme usando a escala de 0 a 10                                      |
| `Review`         | Análise do filme                                                                  |
| `WatchedDate`    | Data em que o filme foi assistido (`DD-MM-AAAA` ou `AAAA`)                        |
| `SafeForParents` | `True` ou `False`. Se é seguro para assistir com pais (Sem cenas constrangedoras) |
| `SafeForKids`    | `True`, `False`. Se é apropriado para crianças (plot voltado para crianças)       |

## 🌟 Sistema de Notas – **Rating10**

A nota vai de 0 a 10 e representa não apenas a qualidade técnica do filme, mas principalmente o **impacto emocional e artístico** que ele teve em mim.

| Nota   | Descrição                                                                                                                                        |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0**  | 💀 **Um erro da humanidade** – Era melhor ele nunca ter sido feito. Uma ofensa ao cinema e um desserviço a humanidade                            |
| **1**  | 🗑️ **Terrível** – Quase nenhum mérito. Difícil de assistir até o fim                                                                             |
| **2**  | 🚫 **Muito ruim** – Fracassa em quase tudo. Pouco proveito                                                                                       |
| **3**  | 😬 **Ruim** – Algumas boas ideias, mas falha bastante. Difícil de recomendar                                                                     |
| **4**  | 😕 **Fraco** – Tem momentos bons, mas o saldo é negativo                                                                                         |
| **5**  | 😐 **Morno** – Definitivamente um dos filmes já feitos. Sem graça                                                                                |
| **6**  | 🙂 **Ok** – Um bom filme. Funciona, cumpre o que promete, mas não impressiona nem surpreende                                                     |
| **7**  | 👍 **Bom** – Bem feito e envolvente. Recomendável                                                                                                |
| **8**  | 👏 **Muito bom** – Destaque claro. Tecnicamente ou emocionalmente marcante                                                                       |
| **9**  | 🔥 **Excelente** – Um dos grandes. Fica na memória. Merece ser visto e revisto                                                                   |
| **10** | 🧠❤️ **Absolute cinema** – Uma obra-prima, não apenas dentro do seu gênero, mas para todo o cinema. Marcante, criativo e emocionalmente poderoso |

## ❗ Sobre as Notas e Avaliações

As notas atribuídas aqui não devem ser usadas para comparar diretamente um filme com outro. Uma nota 8 não significa necessariamente que um filme é melhor do que outro que recebeu 7. O contexto, o momento em que assisti, meu envolvimento emocional e vários fatores subjetivos influenciam minha experiência.

As avaliações contidas neste repositório representam minha opinião pessoal. Não pretendo impor juízo universal sobre nenhuma obra. Além disso, não avalio os filmes com base na ideologia que apresentam. Um filme pode conter ideias equivocadas, ofensivas ou ultrapassadas (como racismo, machismo ou discursos problemáticos) e ainda assim ter um grande valor cinematográfico ou simplesmente oferecer entretenimento de qualidade. Por isso, a nota se refere à minha experiência com o filme, e não a um endosso de valores.
