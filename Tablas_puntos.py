import pandas as pd
from datetime import datetime

Puntos_Record = "puntos_juego.csv"

def puntos_partida(x):

    datos={
        "Puntos":[x],
        "Fecha":[datetime.now().strftime("A - M - d H: M: S: ")]
    }

    
