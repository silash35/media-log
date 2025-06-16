from config import movies_csv_path, movies_json_path, MovieEntry
import json
import os
from sync import json_para_csv

# Preencha os campos da nova entrada aqui
nova_linha: MovieEntry = {
    "imdbID": "tt0000000",
    "Title": "Legally",
    "Year": 2025,
    "Rating10": 6.0,
    "Review": """Teste""",
    "WatchedDate": 2025,
    "SafeForParents": False,
    "SafeForKids": False,
}

# Verifica se o arquivo existe e carrega os dados existentes
if os.path.exists(movies_json_path):
    with open(movies_json_path, "r", encoding="utf-8") as f:
        dados = json.load(f)
else:
    dados = []

# Adiciona a nova linha
dados.append(nova_linha)

# Salva de volta no JSON
with open(movies_json_path, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print(f'Entrada "{nova_linha["Title"]}" adicionada com sucesso!')

# Converte o JSON atualizado para CSV
json_para_csv(movies_json_path, movies_csv_path)
