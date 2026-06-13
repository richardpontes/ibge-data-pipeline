import requests
import csv

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

resposta = requests.get(url)

dados = resposta.json()

with open("data/estados.csv", mode="w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["id", "sigla", "nome", "regiao"])

    for estado in dados:
        escritor.writerow([
            estado["id"],
            estado["sigla"],
            estado["nome"],
            estado["regiao"]["nome"]
        ])

print("Arquivo estados.csv gerado com sucesso!")