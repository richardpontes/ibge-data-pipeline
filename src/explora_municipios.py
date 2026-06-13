import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

response = requests.get(url)

dados = response.json()

print("Tipo:", type(dados))
print("Quantidade:", len(dados))
print("\nPrimeiro município:")
print(dados[0])