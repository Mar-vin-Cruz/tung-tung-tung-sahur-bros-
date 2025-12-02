import pygame
from pyfiglet import Figlet
from colorama import Fore, Style
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

fig = Figlet(font="ANSI_Shadow")
Titulo = fig.renderText("Tung Tung Bros")
Jugando = False

# ==================================
#   FUNCIÓN NUEVA PARA HITBOX
# ==================================
def dibujar_hitbox(pantalla, rect, camara_x, color=(0,255,0)):
    pygame.draw.rect(
        pantalla,
        color,
        (rect.x - camara_x, rect.y, rect.width, rect.height),
        2
    )

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
            ImgQuietoD = "ImagenesPato/Pato Quieto Derecha.png"
            ImgQuietoI = "ImagenesPato/Pato Quieto Izquierda.png"
            ImgCaminandoD = "ImagenesPato/Pato Caminando Derecha.png"
            ImgCaminandoI = "ImagenesPato/Pato Caminando Izquierda.png"
            ImgQuietoF = "ImagenesPato/Pato Quieto Frente.png"
            ImgSaltoD = "ImagenesPato/Pato Salto Derecha.png"
            ImgSaltoI = "ImagenesPato/Pato Salto Izquierda.png"
            PersonajeExistente = True
            Nombre = str(input("Ingrese su nombre: "))
            
        elif Personajes == '2':
            ImgQuietoD = "ImagenesTung/Tung Quieto Derecha.png"
            ImgQuietoI = "ImagenesTung/Tung Quieto Izquierda.png"
            ImgCaminandoD = "ImagenesTung/Tung Caminando Derecha.png"
            ImgCaminandoI = "ImagenesTung/Tung Caminando Izquierda.png"
            ImgQuietoF = "ImagenesTung/Tung  Quieto Frente.png"
            ImgSaltoD = "ImagenesTung/Tung Salto Derecha.png"
            ImgSaltoI = "ImagenesTung/Tung Salto Izquierda.png"
            PersonajeExistente = True
            Nombre = str(input("Ingrese su nombre: "))

        elif Personajes == '3':
            ImgQuietoD = "ImagenesMago/Mago Quieto Derecha.png"
            ImgQuietoI = "ImagenesMago/Mago Quieto Izquierda.png"
            ImgCaminandoD = "ImagenesMago/Mago Caminando Derecha.png"
            ImgCaminandoI = "ImagenesMago/Mago Caminando Izquierda.png"
            ImgQuietoF = "ImagenesMago/Mago Quieto Frente.png"
            ImgSaltoD = "ImagenesMago/Mago Salto Derecha.png"
            ImgSaltoI = "ImagenesMago/Mago Salto Izquierda.png"
            PersonajeExistente = True
            Nombre = str(input("Ingrese su nombre: "))
         
        else: 
            print("Solo del 1 al 3")
        
    return ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI, Nombre        


def Juego(ImgQuietoD, ImgQuietoI, ImgCaminandoD, ImgCaminandoI, ImgQuietoF, ImgSaltoD, ImgSaltoI, Nombre):
    Jugando = True
    pygame.init()
    pygame.mixer.init()
    musica()
    
    Plataforma = "Objetos/PlataformaUa.png"
    Escala_de_P = pygame.transform.scale(pygame.image.load(Plataforma), (96,96))
 
    #Posicion plataformas
    Plataformas = [pygame.Rect(0,595,10000,20),#Piso,
                   pygame.Rect(250,520,96,20),#Plataforma ejemplo,
                   pygame.Rect(5300,515,96,20),
                   pygame.Rect(800,535,96,20),#M
                   pygame.Rect(600,435,96,20),#M
                   pygame.Rect(800,335,96,20),#M
                   pygame.Rect(600,235,96,20),#M
                   pygame.Rect(800,135,96,20),#M


    ]
    # -------------------------
    # VARIABLES DEL TIEMPO Y PUNTOS
    # -------------------------
    tiempo_inicial = pygame.time.get_ticks()
    Limite_tiempo = 100
    Puntos_iniciales = 1000
    Perdida_por_s = 10
    
    #Enemigos
    Homero = "EnemigosIMG/Omero chino.gif"
    Posicionxy_Hitbox_H = pygame.Rect(4500,520,48,80)
    Escala_de_H = pygame.transform.scale(pygame.image.load(Homero), (96,96))

    Cj = "EnemigosIMG/CJ.png"
    Posicionxy_Hitbox_CJ = pygame.Rect(4000,520,48,80)
    Escala_de_CJ = pygame.transform.scale(pygame.image.load(Cj), (96,96))

    Tralalero = "EnemigosIMG/tralalero tralala.png"
    Posicionxy_Hitbox_TRL = pygame.Rect(3500,520,80,80)
    Escala_de_TRL = pygame.transform.scale(pygame.image.load(Tralalero), (128,96))

    
    Doom = "EnemigosIMG/doom derecha .png"
    Posicionxy_Hitbox_D = pygame.Rect(3000,520,48,80)
    Escala_de_D = pygame.transform.scale(pygame.image.load(Doom), (96,128))
    
    Boo = "EnemigosIMG/enemigo volador .png"
    Posicionxy_Hitbox_N = pygame.Rect(2500,520,100,100)
    Escala_de_N = pygame.transform.scale(pygame.image.load(Boo), (128,128))

    DragonCaneloni = "EnemigosIMG/dragomcaneloni.png"
    Posicionxy_Hitbox_DC = pygame.Rect(6000,520,130,100)
    Escala_de_DC = pygame.transform.scale(pygame.image.load(DragonCaneloni), (200,200))
    
    Cr7 = "EnemigosIMG/Chilena de cr7.png"
    Posicionxy_Hitbox_7 = pygame.Rect(5500,450,32,128)
    Escala_de_7 = pygame.transform.scale(pygame.image.load(Cr7), (200,200))

    Messi = "EnemigosIMG/messi.png"
    Posicionxy_Hitbox_10 = pygame.Rect(350,450,96,128)
    Escala_de_10 = pygame.transform.scale(pygame.image.load(Messi), (200,200))

    LaGrandreCombinacion = "EnemigosIMG/LagrandeCombinacion.png"
    Posicionxy_Hitbox_LGC = pygame.Rect(6000,500,96,96)
    Escala_de_LGC = pygame.transform.scale(pygame.image.load(LaGrandreCombinacion), (128,128))

    Marvin = "EnemigosIMG/Marvin.png"
    Posicionxy_Hitbox_M = pygame.Rect(1000,100,96,600)
    Escala_de_M = pygame.transform.scale(pygame.image.load(Marvin), (200,1000))

   
    pantalla = pygame.display.set_mode((1000,800))
    Jugador = pygame.Rect(200,515,48,80)
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
    
    # Rangos de enemigos
    #Homero
    Velocidad_Enemigo_H = -3
    liminete_iz_H = 4300
    liminete_der_H = 4900

    #Cj 
    Velocidad_Enemigo_CJ = -3
    liminete_iz_CJ = 3800
    liminete_der_CJ = 4300

    #Tralalero
    Velocidad_Enemigo_TRL = -3
    liminete_iz_TRL = 3200
    liminete_der_TRL = 3800

    #DOOM
    Velocidad_Enemigo_D = -3
    liminete_iz_D = 2700
    liminete_der_D = 3200

    #No me demandes nintendo :(
    Velocidad_Enemigo_N = -3
    liminete_Sube_N = 300  
    liminete_Baja_N = 515
    
    #Dragon Caneloni 
    Velocidad_Enemigo_DC = -3
    liminete_Sube_DC = 300  
    liminete_Baja_DC = 515

    #La grande Combu
    Velocidad_Enemigo_LGC = -3
    liminete_iz_LGC = 5700
    liminete_der_LGC = 6300
    

    Contador = 0
    PosicionXCamara = 0
    direccion = "derecha"

    Mapa_Inicio = 0
    Mapa_Fin = 9450

    Vida = 1
    ImgCorazon = pygame.transform.scale(pygame.image.load("Corazon lleno.png"), (200,96))
    ImgCorazonVacio = pygame.transform.scale(pygame.image.load("Corazon Vasio.png"), (200,96))

    # ==================================
    #   VARIABLE NUEVA PARA HITBOX
    # ==================================
    mostrar_hitbox = False
    
    while Jugando:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                Jugando = False

            # ==================================
            #   TOGGLE HITBOX (NUEVO)
            # ==================================
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_h:
                    mostrar_hitbox = not mostrar_hitbox

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
            VelEny = -11
            EnElSuelo = False

        VelEny += Gravedad
        Jugador.y += VelEny
        
        if Jugador.left < Mapa_Inicio:
           Jugador.left = Mapa_Inicio
        
        if Jugador.right > Mapa_Fin:
           Jugador.right = Mapa_Fin

        if Jugador.right >= Mapa_Fin:
           with open("Estadisticas.txt", "a") as f:
                Fecha = (datetime.now().strftime("%d-%m-%Y"))
                f.write(f"{Nombre};{puntos_actual};{Fecha}\n")
                print("== Venta agregada con éxito ==")
           Jugando = False

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

        #Colision con piso y plataformas
        for P in Plataformas:
            if Jugador.colliderect(P):   # <-- Usa el BOTTOM del jugador
                if VelEny > 0:
                    Jugador.bottom = P.top
                    VelEny = 0
                    EnElSuelo = True
                elif VelEny < 0: 
                    Jugador.top = P.bottom
                    VelEny = 0
                
        # --------------------------
        # TIEMPO Y PUNTOS
        # --------------------------
        tiempo_ms = pygame.time.get_ticks() - tiempo_inicial
        tiempo_seg = tiempo_ms // 1000
        tiempo_restante = Limite_tiempo - tiempo_seg
        puntos_actual = max(0, Puntos_iniciales - tiempo_seg * Perdida_por_s)

        if tiempo_seg >= Limite_tiempo:
            with open("Estadisticas.txt", "a") as f:
                Fecha = (datetime.now().strftime("%d-%m-%Y"))
                f.write(f"{Nombre};{puntos_actual};{Fecha}\n")
                print("== Venta agregada con éxito ==")
            Jugando = False

        pantalla.fill((0,0,0))
        pantalla.blit(fondo, (-PosicionXCamara - 2000, 0))
        pantalla.blit(fondo, (-PosicionXCamara, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 2000, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 4000, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 6000, 0))
        pantalla.blit(fondo, (-PosicionXCamara + 8000, 0))

        pantalla.blit(JugadorEstado, (Jugador.x - PosicionXCamara-23, Jugador.y))
        pantalla.blit(Escala_de_H,(Posicionxy_Hitbox_H.x - PosicionXCamara -30, Posicionxy_Hitbox_H.y -15))
        pantalla.blit(Escala_de_CJ,(Posicionxy_Hitbox_CJ.x - PosicionXCamara -30, Posicionxy_Hitbox_CJ.y -15))
        pantalla.blit(Escala_de_TRL,(Posicionxy_Hitbox_TRL.x  - PosicionXCamara -30, Posicionxy_Hitbox_TRL.y -15))
        pantalla.blit(Escala_de_D,(Posicionxy_Hitbox_D.x - PosicionXCamara -30, Posicionxy_Hitbox_D.y -15))
        pantalla.blit(Escala_de_N,(Posicionxy_Hitbox_N.x - PosicionXCamara -10, Posicionxy_Hitbox_N.y -15))
        pantalla.blit(Escala_de_DC,(Posicionxy_Hitbox_DC.x - PosicionXCamara -25, Posicionxy_Hitbox_DC.y -30))
        pantalla.blit(Escala_de_7,(Posicionxy_Hitbox_7.x - PosicionXCamara-100 , Posicionxy_Hitbox_7.y ))
        pantalla.blit(Escala_de_LGC,(Posicionxy_Hitbox_LGC.x - PosicionXCamara-15 , Posicionxy_Hitbox_LGC.y -10))
        pantalla.blit(Escala_de_P,(Plataformas[1].x - PosicionXCamara , Plataformas[1].y -15 ))
        pantalla.blit(Escala_de_P,(Plataformas[2].x - PosicionXCamara , Plataformas[2].y -10 ))
        pantalla.blit(Escala_de_P,(Plataformas[3].x - PosicionXCamara , Plataformas[3].y -10 ))
        pantalla.blit(Escala_de_P,(Plataformas[4].x - PosicionXCamara , Plataformas[4].y -10))
        pantalla.blit(Escala_de_P,(Plataformas[5].x - PosicionXCamara , Plataformas[5].y -10 ))
        pantalla.blit(Escala_de_P,(Plataformas[6].x - PosicionXCamara , Plataformas[6].y -10 ))
        pantalla.blit(Escala_de_P,(Plataformas[7].x - PosicionXCamara , Plataformas[7].y  -10))
        pantalla.blit(Escala_de_10,(Posicionxy_Hitbox_10.x - PosicionXCamara-30 , Posicionxy_Hitbox_10.y -50))
        pantalla.blit(Escala_de_M,(Posicionxy_Hitbox_M.x - PosicionXCamara-30 , Posicionxy_Hitbox_M.y ))
        

        # ==================================
        #   MOSTRAR HITBOX (NUEVO)
        # ==================================
        if mostrar_hitbox:
            dibujar_hitbox(pantalla, Jugador, PosicionXCamara, (0,255,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_H, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_CJ, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_TRL, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_D, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_N, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_DC, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_7, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_10, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_M, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Posicionxy_Hitbox_LGC, PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Plataformas[1], PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Plataformas[2], PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Plataformas[3], PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Plataformas[4], PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Plataformas[5], PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Plataformas[6], PosicionXCamara, (255,0,0))
            dibujar_hitbox(pantalla, Plataformas[7], PosicionXCamara, (255,0,0))
        
        if Vida == 1:
           pantalla.blit(ImgCorazon, (-65,-10))
        else:
           pantalla.blit(ImgCorazonVacio, (-65,-10))

        font = pygame.font.SysFont(None, 50)
        txt_tiempo = font.render(f"Tiempo: {tiempo_restante}", True, (255,255,255))
        txt_puntos = font.render(f"Puntos: {puntos_actual}", True, (255,255,255))

        pantalla.blit(txt_tiempo, (800,0))
        pantalla.blit(txt_puntos, (800,50))
        
        #Coliciones con enemigos
        if Jugador.colliderect(Posicionxy_Hitbox_H):
            Vida -= 1
        
        if Jugador.colliderect(Posicionxy_Hitbox_TRL):
            Vida -= 1
        
        if Jugador.colliderect(Posicionxy_Hitbox_D):
            Vida -= 1
        
        if Jugador.colliderect(Posicionxy_Hitbox_CJ):
            Vida -= 1
        if Jugador.colliderect(Posicionxy_Hitbox_N):
            Vida -= 1
        if Jugador.colliderect(Posicionxy_Hitbox_7):
            Vida -= 1
        if Jugador.colliderect(Posicionxy_Hitbox_10):
            Vida -= 1
        if Jugador.colliderect(Posicionxy_Hitbox_LGC):
            Vida -= 1
        if Jugador.colliderect(Posicionxy_Hitbox_DC):
            Vida -= 1
        if Jugador.colliderect(Posicionxy_Hitbox_M):
            Vida -= 1

        if Vida <= 0:

            with open("Estadisticas.txt", "a") as f:
                Fecha = (datetime.now().strftime("%d-%m-%Y"))
                f.write(f"{Nombre};{puntos_actual};{Fecha}\n")
                print("== Venta agregada con éxito ==")
            
            Jugando = False
        
        #Rango de movimiento de Enemigos
        #Homero
        Posicionxy_Hitbox_H.x += Velocidad_Enemigo_H
        if Posicionxy_Hitbox_H.x <= liminete_iz_H:
            Velocidad_Enemigo_H = abs(Velocidad_Enemigo_H)
        elif Posicionxy_Hitbox_H.right >= liminete_der_H:
            Velocidad_Enemigo_H = -abs(Velocidad_Enemigo_H)
        
        #Cj
        Posicionxy_Hitbox_CJ.x += Velocidad_Enemigo_CJ
        if Posicionxy_Hitbox_CJ.x <= liminete_iz_CJ:
            Velocidad_Enemigo_CJ = abs(Velocidad_Enemigo_CJ)
        elif Posicionxy_Hitbox_CJ.right >= liminete_der_CJ:
            Velocidad_Enemigo_CJ = -abs(Velocidad_Enemigo_CJ)

        #Tralalero
        Posicionxy_Hitbox_TRL.x += Velocidad_Enemigo_TRL
        if Posicionxy_Hitbox_TRL.x <= liminete_iz_TRL:
            Velocidad_Enemigo_TRL = abs(Velocidad_Enemigo_TRL)
        elif Posicionxy_Hitbox_TRL.right >= liminete_der_TRL:
            Velocidad_Enemigo_TRL = -abs(Velocidad_Enemigo_TRL)
        
        #Doom
        Posicionxy_Hitbox_D.x += Velocidad_Enemigo_D
        if Posicionxy_Hitbox_D.x <= liminete_iz_D:
            Velocidad_Enemigo_D = abs(Velocidad_Enemigo_D)
        elif Posicionxy_Hitbox_D.right >= liminete_der_D:
            Velocidad_Enemigo_D = -abs(Velocidad_Enemigo_D)
        #Boo
        Posicionxy_Hitbox_N.y += Velocidad_Enemigo_N
        if Posicionxy_Hitbox_N.y <= liminete_Sube_N:
            Velocidad_Enemigo_N = abs(Velocidad_Enemigo_N)
        elif Posicionxy_Hitbox_N.y >= liminete_Baja_N:
            Velocidad_Enemigo_N = -abs(Velocidad_Enemigo_N)
        
        #Dracon caneloni
        Posicionxy_Hitbox_DC.y += Velocidad_Enemigo_DC
        if Posicionxy_Hitbox_DC.y <= liminete_Sube_DC:
            Velocidad_Enemigo_DC = abs(Velocidad_Enemigo_DC)
        elif Posicionxy_Hitbox_DC.y >= liminete_Baja_DC:
            Velocidad_Enemigo_DC = -abs(Velocidad_Enemigo_DC)

        #La grande 
        Posicionxy_Hitbox_LGC.x += Velocidad_Enemigo_LGC
        if Posicionxy_Hitbox_LGC.x <= liminete_iz_LGC:
            Velocidad_Enemigo_LGC = abs(Velocidad_Enemigo_LGC)
        elif Posicionxy_Hitbox_LGC.right >= liminete_der_LGC:
            Velocidad_Enemigo_LGC = -abs(Velocidad_Enemigo_LGC)
        
       

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
