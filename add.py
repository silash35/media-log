import json
import os
from sync import json_para_csv

# Caminho do arquivo JSON
json_path = "movies.json"

# Preencha os campos da nova entrada aqui
nova_linha = {
    "imdbID": "tt3666526",
    "Title": "Copa",
    "Year": 2014,
    "Rating10": 7.0,
    "Review": """Teste""",
    "WatchedDate": "2025",
    "SafeForParents": False,
    "SafeForKids": False
}

# Verifica se o arquivo existe e carrega os dados existentes
if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        dados = json.load(f)
else:
    dados = []

# Adiciona a nova linha
dados.append(nova_linha)

# Salva de volta no JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("Nova entrada adicionada com sucesso!")

# Converte o JSON atualizado para CSV
json_para_csv(json_path, "movies.csv")
