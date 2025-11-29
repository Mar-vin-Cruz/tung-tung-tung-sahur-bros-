import pygame
import Corridos_Chidos
import Menu

Jugando2 = False 
while Jugando2 == False:
    Menu.mostrar_menu()
    opcion = str(input("seleccione una Opcion: "))
    if opcion == '1':
        print("1: Pato")
        print("2: TungTungsahur")
        print("3: Mago")
        print("4: Amongus")



        Personajes = str(input("Selecciones un personaje (1-3):", ))

        if Personajes == '1':
            ImgQuietoD = "ImagenesPato/Pato Quieto Derecha.png"
            ImgQuietoI = "ImagenesPato/Pato Quieto Izquierda.png"
            ImgCaminandoD = "ImagenesPato/Pato Caminando Derecha.png"
            ImgCaminandoI = "ImagenesPato/Pato Caminando Izquierda.png"
            ImgQuietoF = "ImagenesPato/Pato Quieto Frente.png"
            ImgSaltoD = "ImagenesPato/Pato Salto Derecha.png"
            ImgSaltoI = "ImagenesPato/Pato Salto Izquierda.png"
            Jugando2 = True
            
        
        elif Personajes == '2':
            ImgQuietoD = "ImagenesTung/Tung Quieto Derecha.png"
            ImgQuietoI = "ImagenesTung/Tung Quieto Izquierda.png"
            ImgCaminandoD = "ImagenesTung/Tung Caminando Derecha.png"
            ImgCaminandoI = "ImagenesTung/Tung Caminando Izquierda.png"
            ImgQuietoF = "ImagenesTung/Tung  Quieto Frente.png"
            ImgSaltoD = "ImagenesTung/Tung Salto Derecha.png"
            ImgSaltoI = "ImagenesTung/Tung Salto Izquierda.png"
            Jugando2 = True

        elif Personajes == '3':
            ImgQuietoD = "ImagenesMago/Mago Quieto Derecha.png"
            ImgQuietoI = "ImagenesMago/Mago Quieto Izquierda.png"
            ImgCaminandoD = "ImagenesMago/Mago Caminando Derecha.png"
            ImgCaminandoI = "ImagenesMago/Mago Caminando Izquierda.png"
            ImgQuietoF = "ImagenesMago/Mago Quieto Frente.png"
            ImgSaltoD = "ImagenesMago/Mago Salto Derecha.png"
            ImgSaltoI = "ImagenesMago/Mago Salto Izquierda.png"
            Jugando2 = True

        elif Personajes== '4':
            ImgQuietoD = "ImagenesAmongas/Amongus Quieto Derecha.png"
            ImgQuietoI = "ImagenesAmongas/Amongus Quieto Izquierda.png"
            ImgCaminandoD = "ImagenesAmongas/Amongus Caminando Derecha.png"
            ImgCaminandoI = "ImagenesAmongas/Amongus Caminando Izquierda.png"
            ImgQuietoF = "Enemigos/Grenn_quieto.png"
            ImgSaltoD = "ImagenesAmongas/Amongus Caminando Derecha.png"
            ImgSaltoI = "ImagenesAmongas/Amongus Caminando Izquierda.png"
            Jugando2 = True

    elif opcion == '2':
         print("Puntajes")
    elif opcion == '3':
         print("Gracias por jugar")
         break

pygame.init()
pygame.mixer.init()
Corridos_Chidos.musica()

pantalla = pygame.display.set_mode((1000,800))

Jugador = pygame.Rect(200,515,96,96)

Jugando = True
reloj = pygame.time.Clock()

#objetos(eje x,y,resolucion de pixeles)
PlataformaImagen = "Objetos/PlataformaUa.png"
Plataforma = pygame.Rect(7800,400,96,96)
ImgPla = pygame.transform.scale(pygame.image.load(PlataformaImagen), (96,96))

# --- FONDO ---
fondo1 = pygame.image.load("mapa de fondo.png")
fondo1= pygame.transform.scale(fondo1, (2000,800))

fondo2 = pygame.image.load("mapa de fondo.png")
fondo2 = pygame.transform.scale(fondo2, (2000,800))

fondo3 = pygame.image.load("mapa de fondo.png")
fondo3 = pygame.transform.scale(fondo3, (2000,800))

fondo4 = pygame.image.load("mapa de fondo.png")
fondo4 = pygame.transform.scale(fondo4, (2000,800))

# enemigos
Homero = "Enemigos/Omero chino.gif"
Secreto = pygame.Rect(7800,515,96,96)
ImgSecreto = pygame.transform.scale(pygame.image.load(Homero), (96,96))

# --- Animaciones caminar ---
CaminarD = [
    pygame.image.load(ImgCaminandoD),
    pygame.image.load(ImgQuietoD),
]
AnimD = [pygame.transform.scale(imagen1, (96,96)) for imagen1 in CaminarD]

CaminarI = [
    pygame.image.load(ImgCaminandoI),
    pygame.image.load(ImgQuietoI),
]
AnimI = [pygame.transform.scale(imagen2, (96,96)) for imagen2 in CaminarI]

# Varibles de saltos
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
cam_x = 0

# Dirección
direccion = "derecha"

while Jugando:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Jugando = False

    Movimiento = pygame.key.get_pressed()

    Derecha = False
    Izquierda = False

    # --- Movimiento horizontal ---
    if Movimiento[pygame.K_RIGHT]:
        Jugador.x += 10
        Jugador.x += 6
        Derecha = True
        direccion = "derecha"

    elif Movimiento[pygame.K_LEFT]:
        Jugador.x -= 10
        Jugador.x -= 6
        Izquierda = True
        direccion = "izquierda"

    # --- Salto ---
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
    cam_x = Jugador.x - 400

    # --- ANIMACIONES ---
    if not EnElSuelo:
        # Brincando
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

    # Posicion de los fondos
    
    pantalla.blit(fondo1, (-cam_x, 0))
    pantalla.blit(fondo2, (-cam_x + 2000, 0))
    pantalla.blit(fondo3, (-cam_x + 4000, 0))
    pantalla.blit(fondo4, (-cam_x + 6000, 0))

    # Posicion de las cosas
    pantalla.blit(JugadorEstado, (Jugador.x - cam_x, Jugador.y))
    pantalla.blit(ImgSecreto,(Secreto.x - cam_x, Secreto.y))
    pantalla.blit(ImgPla, (Plataforma.x - cam_x, Plataforma.y))

    pygame.display.update()
    reloj.tick(60)
