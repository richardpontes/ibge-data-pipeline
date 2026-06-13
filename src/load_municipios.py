import csv
import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="ibge_pipeline",
    user="postgres",
    password="richard7"
)

cursor = conexao.cursor()

with open("data/municipios.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for municipio in leitor:
        cursor.execute(
            """
            INSERT INTO municipios (id, nome, estado_id)
            VALUES (%s, %s, %s)
            """,
            (
                int(municipio["id"]),
                municipio["nome"],
                int(municipio["estado_id"])
            )
        )

conexao.commit()

print("Municípios carregados com sucesso!")

conexao.close()