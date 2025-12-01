import pygame
import Funciones

MenuPrincipal = True
while MenuPrincipal:
    Funciones.mostrar_menu()
    try:
        opcion = int(input("seleccione una Opcion: ", ))

        if opcion == 1:
            while True:
                (ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI) = Funciones.seleccion_pj()
                Nombre = str(input("Ingrese su nombre:", ))
                break 
            MenuPrincipal = False

        #FALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        elif opcion == 2:
            print("Aqui van las estadisticas") 
        ###################################################
        
        #FALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        elif opcion == 3:
            break
        ###################################################

        else:
            print("Numero invalido")

    except ValueError:
        print("Solo numeros del 1 al 3")

#Juego

    Funciones.Juego(ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI)
