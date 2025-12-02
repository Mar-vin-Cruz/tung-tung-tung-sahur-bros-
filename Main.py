import pygame
import pandas as pd
from colorama import Fore, Style
import matplotlib.pyplot as plt
import Funciones



MenuPrincipal = True
while MenuPrincipal:
    Funciones.mostrar_menu()
    try:
        opcion = str(input(Fore.GREEN + "seleccione una Opcion:", ))

        if opcion == '1':
            while True:
                (ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI, Nombre) = Funciones.seleccion_pj()
                break 

            MenuPrincipal = False

            # AQUI VA — SOLO SE EJECUTA SI SE ELIGE OPCIÓN 1
            Funciones.Juego(
                ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI,
                ImgQuietoF, ImgSaltoD, ImgSaltoI, Nombre
            )

        elif opcion == '2':
            Datos = []
            with open("Estadisticas.txt", "r") as Est:
                for linea in Est:
                    Nombre, puntos_actual, Fecha = linea.strip().split(";")
                    Datos.append({
                    "Nombres": Nombre, 
                    "Puntos" : puntos_actual,
                    "Fecha" : Fecha})
                df = pd.DataFrame(Datos)
                df = df.sort_values(by="Puntos")
                df = df.head(15)
                plt.bar(df["Nombres"], df["Puntos"], color="red", edgecolor="black")
                plt.xlabel("Nombre")
                plt.ylabel("Puntos")
                plt.title("Puntuaciones")
                plt.show()

                df = df.sort_values(by="Puntos", ascending=False)
                df = df.head(15)
                print(df)

       
        elif opcion == '3':
            break

        else:
            print("Numero invalido")

    except ValueError:
        print("Solo numeros del 1 al 3")

#El fabi se chingo su codigo