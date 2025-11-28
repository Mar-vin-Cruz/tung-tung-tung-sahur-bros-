from pyfiglet import Figlet
from colorama import Fore, Style
import pandas as pd
import matplotlib.pyplot as plt
fig = Figlet(font="ANSI_Shadow")
Titulo = fig.renderText("Tung Tung Bros")


def mostrar_menu():
    print(Fore.GREEN + Titulo)
    print("\n=======MENU=======")
    print(Fore.CYAN + "1-Registrare")
    print(Fore.BLUE + "2-Jugar")
    print(Fore.GREEN + "3-Mostrar Puntaje")
    print(Fore.RED + "4-salir")
    print(Style.RESET_ALL)
    print("------------------")

def Datos():
       with open("Estadisticas.txt", "a") as f:
        Jugador = str(input("Jugador: "))
        f.write(f"{Jugador}\n")
        print("== Jugador registrado con éxito ==")

       #Codigo principal
        while True:
            mostrar_menu()
            opcion = int(input("seleccione una Opcion: "))
            Peronajes = int(input("Selecciones un personaje (1-3):"))

            if opcion == "1":
               Datos()
            
            elif opcion == "2":
              
              try:
                    if Peronajes == 1:
                       PImgQuietoD = "ImagenesPato/Pato Quieto Derecha.png"
                       PImgQuietoI = "ImagenesPato/Pato Quieto Izquierda.png"
                       PImgCaminandoD = "ImagenesPato/Pato Caminando Derecha.png"
                       PImgCaminandoI = "ImagenesPato/Pato Caminando Izquierda.png"
                       PImgQuietoF = "ImagenesPato/Pato Quieto Frente.png"
                       PImgSaltoD = "ImagenesPato/Pato Salto Derecha.png"
                       PImgSaltoI = "ImagenesPato/Pato Salto Izquierda.png"
                    
                    elif Peronajes == 2:
                        TImgQuietoD = "ImagenesTung/Tung Quieto Derecha.png"
                        TImgQuietoI = "ImagenesTung/Tung Quieto Izquierda.png"
                        TImgCaminandoD = "ImagenesTung/Tung Caminando Derecha.png"
                        TImgCaminandoI = "ImagenesTung/Tung Caminando Izquierda.png"
                        TImgQuietoF = "ImagenesTung/Tung  Quieto Frente.png"
                        TImgSaltoD = "ImagenesTung/Tung Salto Derecha.png"
                        TImgSaltoI = "ImagenesTung/Tung Salto Izquierda.png"
                  
                    elif Peronajes == 3:
                        MImgQuietoD = ""
                        MImgQuietoI = ""
                        MImgCaminandoD = ""
                        MImgCaminandoI = ""
                        MImgQuietoF = ""
                        MImgSaltoD = ""
                        MImgSaltoI = ""
              except FileNotFoundError:        
                  print("Primero elija el personaje")          


            elif opcion == "3":
              try:
                #Falta definir puntuacion
                df = Datos()
                print(df)
                colores = [ 'blue', 'orange', 'green', 'red', 'purple', 
                            'brown', 'pink', 'gray', 'olive', 'cyan'
                        ]
                plt.figure(figsize=(12, 7))
                plt.bar(df["Jugador"], df["Puntuacion"], color=colores)
                plt.title("Puntuacion de los jugadores")
                plt.xlabel("Nombre de los jugadores")
                plt.ylabel("Puntuacion")
                plt.grid(axis="y", linestyle="--", alpha=0.6)
                plt.ticklabel_format(style='plain', axis='y')
                plt.savefig("grafica_Score.png")
                plt.show()
              except SyntaxError:
                  print("Juege una partida para ver la puntuacion")
            
