from pyfiglet import Figlet
from colorama import Fore, Style
import matplotlib.pyplot as plt
import pygame

fig = Figlet(font="ANSI_Shadow")
Titulo = fig.renderText("Tung Tung Bros")
Jugando = False

#Menu principal
def mostrar_menu():
    print(Fore.GREEN + Titulo)
    print(Fore.LIGHTYELLOW_EX + "\n=======MENU=======")
    print(Fore.GREEN + "1-Jugar")
    print(Fore.BLUE + "2-Mostrar Puntajes")
    print(Fore.RED + "3-Salir")
    print(Style.RESET_ALL)
    print("------------------")

#Seleccionar personajes(Imagenes)
def seleccion_pj():
        PersonajeExistente = False
        while PersonajeExistente == False:
            Personajes = str(input("Selecciones un personaje (1-3):", ))

            if Personajes == '1':
            
                    ImgQuietoD = "ImagenesPato/Pato Quieto Derecha.png"
                    ImgQuietoI = "ImagenesPato/Pato Quieto Izquierda.png"
                    ImgCaminandoD = "ImagenesPato/Pato Caminando Derecha.png"
                    ImgCaminandoI = "ImagenesPato/Pato Caminando Izquierda.png"
                    ImgQuietoF = "ImagenesPato/Pato Quieto Frente.png"
                    ImgSaltoD = "ImagenesPato/Pato Salto Derecha.png"
                    ImgSaltoI = "ImagenesPato/Pato Salto Izquierda.png"
                    PersonajeExistente = True
            
            elif Personajes == '2':
                    ImgQuietoD = "ImagenesTung/Tung Quieto Derecha.png"
                    ImgQuietoI = "ImagenesTung/Tung Quieto Izquierda.png"
                    ImgCaminandoD = "ImagenesTung/Tung Caminando Derecha.png"
                    ImgCaminandoI = "ImagenesTung/Tung Caminando Izquierda.png"
                    ImgQuietoF = "ImagenesTung/Tung  Quieto Frente.png"
                    ImgSaltoD = "ImagenesTung/Tung Salto Derecha.png"
                    ImgSaltoI = "ImagenesTung/Tung Salto Izquierda.png"
                    PersonajeExistente = True

            elif Personajes == '3':
                    ImgQuietoD = "ImagenesMago/Mago Quieto Derecha.png"
                    ImgQuietoI = "ImagenesMago/Mago Quieto Izquierda.png"
                    ImgCaminandoD = "ImagenesMago/Mago Caminando Derecha.png"
                    ImgCaminandoI = "ImagenesMago/Mago Caminando Izquierda.png"
                    ImgQuietoF = "ImagenesMago/Mago Quieto Frente.png"
                    ImgSaltoD = "ImagenesMago/Mago Salto Derecha.png"
                    ImgSaltoI = "ImagenesMago/Mago Salto Izquierda.png"
                    PersonajeExistente = True
            else: 
                print("Solo del 1 al 3")
        
        return ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI        

#Abrir juego    
def Juego(ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI):
    Jugando = True
    pygame.init()
    pygame.mixer.init()
    musica()
    Homero = "Enemigos/Omero chino.gif"
    Posicionxy_Hitbox_H = pygame.Rect(7800,515,96,96)  # HITBOX AJUSTADA AL TAMAÑO REAL
    Escala_de_H = pygame.transform.scale(pygame.image.load(Homero), (96,96))
    pantalla = pygame.display.set_mode((1000,800))
    Jugador = pygame.Rect(200,515,96,96)
    reloj = pygame.time.Clock()

    # --- FONDO ---
    fondo= pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))

    # --- Animaciones caminar ---
    CaminarD = [
        pygame.image.load(ImgQuietoD),
        pygame.image.load(ImgCaminandoD),
    ]
    AnimD = [pygame.transform.scale(imagen1, (96,96)) for imagen1 in CaminarD]

    CaminarI = [
        pygame.image.load(ImgQuietoI),
        pygame.image.load(ImgCaminandoI),
    ]
    AnimI = [pygame.transform.scale(imagen2, (96,96)) for imagen2 in CaminarI]

    #Variables de salto
    SaltoD = pygame.transform.scale(pygame.image.load(ImgSaltoD), (96,96))
    SaltoI = pygame.transform.scale(pygame.image.load(ImgSaltoI), (96,96))

    # Quieto
    Quieto = pygame.transform.scale(pygame.image.load(ImgQuietoF), (96,96))

    # Físicas
    VelEny = 0
    Gravedad = 0.5
    EnElSuelo = True

    # Animación
    Contador = 0

    # Cámara
    PosicionXCamara = 0

    # Dirección
    direccion = "derecha"

    while Jugando:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                Jugando = False

        Movimiento = pygame.key.get_pressed()

        Derecha = False
        Izquierda = False

        # Velocidad De desplasamiento Jugador
        if Movimiento[pygame.K_RIGHT]:
            Jugador.x += 5
            Derecha = True
            direccion = "derecha"

        elif Movimiento[pygame.K_LEFT]:
            Jugador.x -= 5
            Izquierda = True
            direccion = "izquierda"

        # Velocidad de salto jugador
        if Movimiento[pygame.K_SPACE] and EnElSuelo:
            VelEny = -10
            EnElSuelo = False

        # --- Gravedad ---
        VelEny += Gravedad
        Jugador.y += VelEny

        # Suelo
        if Jugador.y >= 515:
            Jugador.y = 515
            VelEny = 0
            EnElSuelo = True

        # --- Cámara ---
        PosicionXCamara = Jugador.x - 400

        # --- ANIMACIONES ---
        if not EnElSuelo:
            # Saltar
            if Derecha:
                JugadorEstado = SaltoD
            elif Izquierda:
                JugadorEstado = SaltoI
            else:
                JugadorEstado = Quieto

        else:
            # CAMINANDO DERECHA
            if Derecha:
                Contador += 0.15
                if Contador >= len(AnimD):
                    Contador = 0
                JugadorEstado = AnimD[int(Contador)]

            # CAMINANDO IZQUIERDA
            elif Izquierda:
                Contador += 0.15
                if Contador >= len(AnimI):
                    Contador = 0
                JugadorEstado = AnimI[int(Contador)]

            # QUIETO
            else:
                JugadorEstado = Quieto
                Contador = 0

        # =====================
        #      DIBUJAR
        # =====================
        pantalla.fill((0,0,0))

        # Posicion de los Fondos
        pantalla.blit(fondo, (-PosicionXCamara - 2000, 0))
        pantalla.blit(fondo, (-PosicionXCamara, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 2000, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 4000, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 6000, 0))

        # Posicion del Jugador
        pantalla.blit(JugadorEstado, (Jugador.x - PosicionXCamara, Jugador.y))
        pygame.display.update()
        reloj.tick(60)

#Musica del Juego
def musica():
 pygame.mixer.music.load("musica/FUERZA-REGIDA-TU-SANCHO-_VIDEO-OFICIAL_.wav")
 pygame.mixer.music.play(-1)
 pygame.mixer.music.set_volume(100)

#Despedida
def Despedida():
    figDespedida = Figlet(font="ANSI_Shadow")
    ADIOS = fig.renderText("ADIOS...")
    print(Fore.RED + ADIOS)
    print(Style.RESET_ALL)
     