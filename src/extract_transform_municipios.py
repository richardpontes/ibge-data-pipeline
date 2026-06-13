import csv
import requests

URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

dados = requests.get(URL).json()

municipios = []

for municipio in dados:

    uf = municipio["regiao-imediata"]["regiao-intermediaria"]["UF"]

    municipios.append({
        "id": municipio["id"],
        "nome": municipio["nome"],
        "estado_id": uf["id"],
        "estado_sigla": uf["sigla"]
    })

with open("data/municipios.csv", "w", newline="", encoding="utf-8") as arquivo:

    writer = csv.DictWriter(
        arquivo,
        fieldnames=[
            "id",
            "nome",
            "estado_id",
            "estado_sigla"
        ]
    )

    writer.writeheader()
    writer.writerows(municipios)

print(f"Quantidade: {len(municipios)}")
print("CSV gerado com sucesso!")