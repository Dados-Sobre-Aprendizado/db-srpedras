import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

conn = psycopg2.connect("postgresql://sys-user:reezzjdJr-2ORsgr2CK4hQ@artful-elf-13228.j77.aws-us-east-1.cockroachlabs.cloud:26257/livrariadb?sslmode=verify-full")

try:
    with conn.cursor() as cur:
        # Get column names from the cursor description
        cur.execute("SELECT * FROM public.livros LIMIT 5;")
        column_names = [desc[0] for desc in cur.description]

        # Fetch all rows
        rows = cur.fetchall()

        # Create a Pandas DataFrame
        df = pd.DataFrame(rows, columns=column_names)

        # Print the DataFrame
        print(df)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()