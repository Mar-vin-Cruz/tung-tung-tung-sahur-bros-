import pygame
import Corridos_Chidos

pygame.init()
<<<<<<< HEAD
pygame.mixer.init()

Corridos_Chidos.musica()

pantalla = pygame.display.set_mode((500,500))
=======
pantalla = pygame.display.set_mode((1000,800))
>>>>>>> 670bfd4129d2108c52eb1fec024de85e75e5ece4

Jugador = pygame.Rect(200,515,96,96)

Jugando = True
reloj = pygame.time.Clock()

# --- FONDO ---
fondo = pygame.image.load("mapa de fondo.png")
fondo = pygame.transform.scale(fondo, (2000,800))

# --- Animaciones caminar ---
CaminarD = [
    pygame.image.load("ImagenesPato/CaminarD1.png"),
    pygame.image.load("ImagenesPato/CaminarD2.png"),
]
AnimD = [pygame.transform.scale(imagen1, (96,96)) for imagen1 in CaminarD]

CaminarI = [
    pygame.image.load("ImagenesPato/CaminarI1.png"),
    pygame.image.load("ImagenesPato/CaminarI2.png"),
]
AnimI = [pygame.transform.scale(imagen2, (96,96)) for imagen2 in CaminarI]

# --- Sprites volar ---
VolarD = pygame.transform.scale(pygame.image.load("ImagenesPato/VolarD.png"), (96,96))
VolarI = pygame.transform.scale(pygame.image.load("ImagenesPato/VolarI.png"), (96,96))

# Quieto
Quieto = pygame.transform.scale(pygame.image.load("ImagenesPato/Quieto.png"), (96,96))

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
        Jugador.x += 3
        Derecha = True
        direccion = "derecha"

    elif Movimiento[pygame.K_LEFT]:
        Jugador.x -= 3
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
        # VOLANDO
        if Derecha:
            JugadorEstado = VolarD
        elif Izquierda:
            JugadorEstado = VolarI
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

    # Fondo
    pantalla.blit(fondo, (-cam_x, 0))

    # Jugador
    pantalla.blit(JugadorEstado, (Jugador.x - cam_x, Jugador.y))

    pygame.display.update()
    reloj.tick(60)
