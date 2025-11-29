from pyfiglet import Figlet
from colorama import Fore, Style
import matplotlib.pyplot as plt


fig = Figlet(font="ANSI_Shadow")
Titulo = fig.renderText("Tung Tung Bros")
Jugando = False

def mostrar_menu():
    print(Fore.GREEN + Titulo)
    print("\n=======MENU=======")
    print(Fore.BLUE + "1-Jugar")
    print(Fore.CYAN + "2-Mostrar Puntaje")
    print(Fore.RED + "3-salir")
    print(Style.RESET_ALL)
    print("------------------")


def Registro():
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
    
