import pygame
import Funciones

MenuPrincipal = True
while MenuPrincipal:
    Funciones.mostrar_menu()
    try:
        opcion = int(input("seleccione una Opcion: "))

        if opcion == 1:
            while True:
                (ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI, Nombre) = Funciones.seleccion_pj()
                break 

            MenuPrincipal = False

            # AQUI VA — SOLO SE EJECUTA SI SE ELIGE OPCIÓN 1
            Funciones.Juego(
                ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI,
                ImgQuietoF, ImgSaltoD, ImgSaltoI, Nombre
            )

        elif opcion == 2:
            with open("Estadisticas.txt", "r") as f:
                for linea in f:
                    Nombre, puntos_actual, Fecha = linea.strip().split(";")
                    print(f"{Nombre}: {puntos_actual}: {Fecha}")
            print("Aqui van las estadisticas")

        elif opcion == 3:
            break

        else:
            print("Numero invalido")

    except ValueError:
        print("Solo numeros del 1 al 3")

#El fabi se chingo su codigo