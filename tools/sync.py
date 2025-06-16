from config import movies_csv_path, movies_json_path
import json
import csv


def json_para_csv(arquivo_json: str, arquivo_csv: str):
    """Converte um arquivo JSON (lista de objetos) para CSV."""
    # Carrega os dados do JSON
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Usa as chaves do primeiro objeto como cabeçalho
    campos = list(dados[0].keys())

    # Escreve o CSV
    with open(arquivo_csv, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Arquivo CSV '{arquivo_csv}' sincronizado com sucesso!")


if __name__ == "__main__":
    json_para_csv(movies_json_path, movies_csv_path)
