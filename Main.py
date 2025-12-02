import pygame
import pandas as pd
from colorama import Fore
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
            try:
                Datos = []
                with open("Estadisticas.txt", "r") as Est:
                    for linea in Est:
                        Nombre, puntos_actual, Fecha = linea.strip().split(";")
                        Datos.append({
                        "Nombres": Nombre, 
                        "Puntos" : puntos_actual,
                        "Fecha" : Fecha})
                    df = pd.DataFrame(Datos)
                    df = df.head(15)
                    df["Puntos"] = df["Puntos"].astype(int)
            
                    plt.bar(df["Nombres"], df["Puntos"], color="red", edgecolor="black")
                    plt.xlabel("Nombre")
                    plt.ylabel("Puntos")
                    plt.title("Puntuaciones")

                    for Valor1, Valor2 in enumerate (df["Puntos"]):
                        plt.text(Valor1 , Valor2 + 2, str(Valor2), ha='center', va ='bottom')
                    plt.show()

                    df = df.sort_values(by="Puntos", ascending=False)
                    print(df)
                    
            except KeyError:
                 print("No hay partidas Jugadas")

        elif opcion == '3':
            Funciones.Despedida()
            break

        else:
            print("Opcion invalida")

    except ValueError:
        print("Solo numeros del 1 al 3")

