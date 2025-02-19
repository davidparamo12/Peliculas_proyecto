from fastapi import FastAPI
import numpy as np
import pandas as pd


df = pd.read_csv(
    r"C:\Users\param\OneDrive\Escritorio\Programacion\Soy Henry\Proyecto individual 2\data_csv")

df_mes = df["release_mes"]

app = FastAPI()

# Function that performs a task


def peli_mes(mes: str):
    mes = mes.lower()
    tabla_mes = df_mes[df_mes == mes].count()
    return f"{tabla_mes} cantidad de peliculas fueron estrenadas en el mes de {mes}"


# API endpoint that calls the function
@app.get("/peli_mes/{mes}")
def get_peli_mes(mes: str):
    message = peli_mes(mes)
    return {"message": message}
