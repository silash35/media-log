import csv

# Caminho do arquivo CSV
csv_path = "movies.csv"

# Preencha os campos da nova linha aqui
nova_linha = {
    "imdbID": "tt20969586",
    "Title": "Thunderbolts",
    "Year": 2025,
    "Rating10": 7.8,
    "Review": """""",
    "WatchedDate": "02/05/2025",
    "SafeForParents": "true",
    "SafeForKids": "false"
}

# Lê os nomes das colunas (cabeçalho)
with open(csv_path, "r", newline="", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    campos = leitor.fieldnames

# Adiciona a nova linha no final do CSV
with open(csv_path, "a", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writerow(nova_linha)

print("Nova linha adicionada com sucesso!")
