import pygame
from pyfiglet import Figlet
from colorama import Fore, Style
import matplotlib.pyplot as plt

fig = Figlet(font="ANSI_Shadow")
Titulo = fig.renderText("Tung Tung Bros")
Jugando = False

def mostrar_menu():
    print(Fore.GREEN + Titulo)
    print(Fore.LIGHTYELLOW_EX + "\n=======MENU=======")
    print(Fore.GREEN + "1-Jugar")
    print(Fore.BLUE + "2-Mostrar Puntajes")
    print(Fore.RED + "3-Salir")
    print(Style.RESET_ALL)
    print("------------------")

def seleccion_pj():
    PersonajeExistente = False
    while PersonajeExistente == False:
        Personajes = str(input("Selecciones un personaje (1-3):", ))

        if Personajes == '1':
            ImugQietoD = "ImagenesPato/Pato Quieto Derecha.png"
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

def Juego(ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI):
    Jugando = True
    pygame.init()
    pygame.mixer.init()
    musica()

    # -------------------------
    # VARIABLES DEL TIEMPO Y PUNTOS
    # -------------------------
    tiempo_inicial = pygame.time.get_ticks()
    Limite_tiempo = 100
    Puntos_iniciales = 1000
    Perdida_por_s = 10

    Homero = "Enemigos/Omero chino.gif"
    Posicionxy_Hitbox_H = pygame.Rect(7600,515,1,1)
    Escala_de_H = pygame.transform.scale(pygame.image.load(Homero), (96,96))

    pantalla = pygame.display.set_mode((1000,800))
    Jugador = pygame.Rect(200,515,96,96)
    reloj = pygame.time.Clock()

    fondo= pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))

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

    SaltoD = pygame.transform.scale(pygame.image.load(ImgSaltoD), (96,96))
    SaltoI = pygame.transform.scale(pygame.image.load(ImgSaltoI), (96,96))

    Quieto = pygame.transform.scale(pygame.image.load(ImgQuietoF), (96,96))

    VelEny = 0
    Gravedad = 0.5
    EnElSuelo = True
    
    Velocidad_Enemigo_H = -3
    liminete_iz_H = 7000
    liminete_der_H = 7600

    Contador = 0
    PosicionXCamara = 0
    direccion = "derecha"

    Mapa_Inicio = -2000
    Mapa_Fin = 8000  

    Vida = 1
    ImgCorazon = pygame.transform.scale(pygame.image.load("Corazon lleno.png"), (200,96))
    ImgCorazonVacio = pygame.transform.scale(pygame.image.load("Corazon Vasio.png"), (200,96))
    
    while Jugando:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                Jugando = False

        Movimiento = pygame.key.get_pressed()
        Derecha = False
        Izquierda = False

        if Movimiento[pygame.K_RIGHT]:
            Jugador.x += 11
            Derecha = True
            direccion = "derecha"

        elif Movimiento[pygame.K_LEFT]:
            Jugador.x -= 11
            Izquierda = True
            direccion = "izquierda"

        if Movimiento[pygame.K_SPACE] and EnElSuelo:
            VelEny = -10
            EnElSuelo = False

        VelEny += Gravedad
        Jugador.y += VelEny
        
        if Jugador.left < Mapa_Inicio:
           Jugador.left = Mapa_Inicio
        
        if Jugador.right > Mapa_Fin:
           Jugador.right = Mapa_Fin

        if Jugador.right >= Mapa_Fin:
           Jugando = False

        if Jugador.y >= 515:
            Jugador.y = 515
            VelEny = 0
            EnElSuelo = True

        PosicionXCamara = Jugador.x - 400

        if not EnElSuelo:
            if Derecha:
                JugadorEstado = SaltoD
            elif Izquierda:
                JugadorEstado = SaltoI
            else:
                JugadorEstado = Quieto
        else:
            if Derecha:
                Contador += 0.15
                if Contador >= len(AnimD):
                    Contador = 0
                JugadorEstado = AnimD[int(Contador)]

            elif Izquierda:
                Contador += 0.15
                if Contador >= len(AnimI):
                    Contador = 0
                JugadorEstado = AnimI[int(Contador)]

            else:
                JugadorEstado = Quieto
                Contador = 0

        # ----------------------------------
        # ACTUALIZAR TIEMPO Y PUNTOS
        # ----------------------------------
        tiempo_ms = pygame.time.get_ticks() - tiempo_inicial
        tiempo_seg = tiempo_ms // 1000
        tiempo_restante = Limite_tiempo - tiempo_seg
        puntos_actual = max(0, Puntos_iniciales - tiempo_seg * Perdida_por_s)

        if tiempo_seg >= Limite_tiempo:
            Jugando = False

        pantalla.fill((0,0,0))
        pantalla.blit(fondo, (-PosicionXCamara - 2000, 0))
        pantalla.blit(fondo, (-PosicionXCamara, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 2000, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 4000, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 6000, 0))

        pantalla.blit(JugadorEstado, (Jugador.x - PosicionXCamara, Jugador.y))
        pantalla.blit(Escala_de_H,(Posicionxy_Hitbox_H.x - PosicionXCamara, Posicionxy_Hitbox_H.y))
        
        if Vida == 1:
           pantalla.blit(ImgCorazon, (-65,-10))
        else:
           pantalla.blit(ImgCorazonVacio, (-65,-10))

        # --------------------------
        # DIBUJAR TIEMPO Y PUNTOS
        # --------------------------
        font = pygame.font.SysFont(None, 50)
        txt_tiempo = font.render(f"Tiempo: {tiempo_restante}", True, (255,255,255))
        txt_puntos = font.render(f"Puntos: {puntos_actual}", True, (255,255,255))

        pantalla.blit(txt_tiempo, (800,0))
        pantalla.blit(txt_puntos, (800,50))

        if Jugador.colliderect(Posicionxy_Hitbox_H):
            Vida -= 1

        if Vida <= 0:
            Jugando = False

        Posicionxy_Hitbox_H.x += Velocidad_Enemigo_H
        if Posicionxy_Hitbox_H.x <= liminete_iz_H:
            Velocidad_Enemigo_H = abs(Velocidad_Enemigo_H)
        elif Posicionxy_Hitbox_H.right >= liminete_der_H:
            Velocidad_Enemigo_H = -abs(Velocidad_Enemigo_H)

        pygame.display.update()
        reloj.tick(60)

def musica():
    pygame.mixer.music.load("musica/FUERZA-REGIDA-TU-SANCHO-_VIDEO-OFICIAL_.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(100)

def Despedida():
    figDespedida = Figlet(font="ANSI_Shadow")
    ADIOS = fig.renderText("ADIOS...")
    print(Fore.RED + ADIOS)
    print(Style.RESET_ALL)