import csv
import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="ibge_pipeline",
    user="postgres",
    password="richard7"
)

cursor = conexao.cursor()

with open("data/estados.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for estado in leitor:
        cursor.execute(
            """
            INSERT INTO estados (id, sigla, nome, regiao)
            VALUES (%s, %s, %s, %s)
            """,
            (
                int(estado["id"]),
                estado["sigla"],
                estado["nome"],
                estado["regiao"]
            )
        )

conexao.commit()

print("Estados carregados com sucesso!")

conexao.close()