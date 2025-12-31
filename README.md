# media-log

> ⚠️ **Note:** This repository is written entirely in **Portuguese (pt-BR)**. It contains my personal records of movies, series, and games I have watched.

Este repositório é uma coleção pessoal de mídias consumidas (filmes, séries e jogos) organizadas com informações como título, ano e, quando possível, outras informações como data em que assisti, notas e uma breve review. Você pode conferir o banco de dados completo na pasta `database`, com cada tipo de mídia armazenado em um arquivo separado. Todos os registros estão disponíveis em dois formatos: `JSON` e `CSV`, para facilitar o uso e a visualização.

> ℹ️ **Dica:** O arquivo CSV é bom para vizualizar usando um editor de planilhas como o Microsoft Excel.

Sobre as séries, elas são cadastradas apenas quando eu terminar de assistir. Isso significa que apenas serão cadastradas séries que já terminaram, seja por que foram finalizadas ou canceladas. Isso evita registros inconsistentes de séries que ainda estão em andamento.

Já os jogos, eu irei cadastrar após “zerar”, ou seja, completar sua história principal. Aqui, o foco é em títulos baseados em narrativa. Jogos sandbox ou abertos (como Minecraft, The Sims ou Stardew Valley), embora eu goste bastante, normalmente não serão cadastrados. Mas podem haver exceções.

## Sobre as Notas e Avaliações

As avaliações contidas neste repositório representam minha opinião pessoal. Não pretendo impor juízo universal sobre nenhuma obra. Além disso, não avalio filmes/séries/jogos com base na ideologia que apresentam. Um filme pode conter ideias equivocadas, ofensivas ou ultrapassadas (como racismo, machismo ou discursos problemáticos) e ainda assim ter um grande valor cinematográfico ou simplesmente oferecer entretenimento de qualidade. Por isso, a nota se refere à minha experiência com a mídia, e não a um endosso de valores.

### Sistema de Notas

Os registros que contêm uma nota seguem o sistema descrito abaixo. Ele foi originalmente criado para filmes, mas aqui também é aplicado a séries e jogos. As notas vão de 0 a 10 e representa não apenas a qualidade técnica da obra, mas principalmente o **impacto emocional e artístico** que ela teve em mim.

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

As notas atribuídas aqui não devem ser usadas para comparar diretamente uma obra com outra. Uma nota 8 não significa necessariamente que, por exemplo, um filme é melhor do que outro que recebeu 7. O contexto, o momento em que assisti, meu envolvimento emocional e vários fatores subjetivos influenciam minha experiência.

## 🗂️ Estrutura dos Dados

Cada entrada do arquivo CSV (ou o json) representa um filme, série ou jogo. Os campos variam de acordo com o tipo de mídia, conforme descrito abaixo.

### Filmes

| Campo            | Descrição                                                                         |
| ---------------- | --------------------------------------------------------------------------------- |
| `imdbID`         | Código único do filme no IMDb (ex: `tt4154796`)                                   |
| `Title`          | Título do filme                                                                   |
| `Year`           | Ano de lançamento                                                                 |
| `Rating10`       | Nota dada ao filme usando a escala de 0 a 10                                      |
| `Review`         | Análise do filme                                                                  |
| `FirstWatched`   | Data em que o filme foi assistido pela primeira vez (`YYYY-MM-DD` ou `YYYY`)      |
| `LastWatched`    | Data mais recente em que o filme foi assistido(`YYYY-MM-DD` ou `YYYY`)            |
| `SafeForParents` | `True` ou `False`. Se é seguro para assistir com pais (Sem cenas constrangedoras) |
| `ForKids`        | `True`, `False`. Se é uma obra feita e apropriada para crianças                   |

### Séries

| Campo            | Descrição                                                                         |
| ---------------- | --------------------------------------------------------------------------------- |
| `imdbID`         | Código único da série no IMDb (ex: `tt0436992`)                                   |
| `Title`          | Título da série                                                                   |
| `Year`           | Ano de lançamento                                                                 |
| `Rating10`       | Nota dada a série usando a escala de 0 a 10                                       |
| `Review`         | Análise da série                                                                  |
| `SafeForParents` | `True` ou `False`. Se é seguro para assistir com pais (Sem cenas constrangedoras) |
| `ForKids`        | `True`, `False`. Se é uma obra feita e apropriada para crianças                   |

### Jogos

| Campo            | Descrição                                                                         |
| ---------------- | --------------------------------------------------------------------------------- |
| `imdbID`         | Código único do jogo no IMDb (ex: `tt5838588`)                                    |
| `Title`          | Título do jogo                                                                    |
| `Year`           | Ano de lançamento                                                                 |
| `Rating10`       | Nota dada ao jogo usando a escala de 0 a 10                                       |
| `Review`         | Análise do jogo                                                                   |
| `SafeForParents` | `True` ou `False`. Se é seguro para assistir com pais (Sem cenas constrangedoras) |
| `ForKids`        | `True`, `False`. Se é uma obra feita e apropriada para crianças                   |
