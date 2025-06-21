from config import movies_csv_path, movies_json_path, MovieEntry
import json
import os
from sync import json_para_csv
from validate import validar_e_ordenar

# Preencha os campos da nova entrada aqui
nova_linha: MovieEntry = MovieEntry(
    {
        "imdbID": "tt6208148",
        "Title": "Legally",
        "Year": 2025,
        "Rating10": 6.0,
        "Review": """Teste""",
        "FirstWatched": 2025,
        "LastWatched": 2025,
        "SafeForParents": False,
        "SafeForKids": False,
    }
)

# Verifica se o arquivo existe e carrega os dados existentes
if os.path.exists(movies_json_path):
    with open(movies_json_path, "r", encoding="utf-8") as f:
        dados = json.load(f)
else:
    dados = []

# Verifica se já existe imdbID igual
if any(filme.get("imdbID") == nova_linha["imdbID"] for filme in dados):
    raise ValueError(
        f'Já existe um filme com imdbID "{nova_linha["imdbID"]}". Não foi possível adicionar.'
    )


# Adiciona a nova linha
dados.append(nova_linha)

# Valida e ordena os dados
dados = [validar_e_ordenar(linha) for linha in dados]

# Salva de volta no JSON
with open(movies_json_path, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print(f'Entrada "{nova_linha["Title"]}" adicionada com sucesso!')

# Converte o JSON atualizado para CSV
json_para_csv(movies_json_path, movies_csv_path)
