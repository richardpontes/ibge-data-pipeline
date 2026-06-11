import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

resposta = requests.get(url)

dados = resposta.json()

for estado in dados:
    print(
        estado["id"],
        estado["sigla"],
        estado["nome"],
        estado["regiao"]["nome"]
    )