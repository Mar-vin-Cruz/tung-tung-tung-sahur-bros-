import pygame

pygame.init()
pantalla = pygame.display.set_mode((500,500))

Jugador = pygame.Rect(200,350,96,96)

Jugando = True
reloj = pygame.time.Clock()

# --- FONDO ---
fondo = pygame.image.load("mapa de fondo.png").convert()
fondo = pygame.transform.scale(fondo, (2000, 500))

# --- Animaciones caminar ---
CaminarD = [
    pygame.image.load("CaminarD1.png"),
    pygame.image.load("CaminarD2.png"),
]
AnimD = [pygame.transform.scale(img, (96,96)) for img in CaminarD]

CaminarI = [
    pygame.image.load("CaminarI1.png"),
    pygame.image.load("CaminarI2.png"),
]
AnimI = [pygame.transform.scale(img, (96,96)) for img in CaminarI]

# --- Sprites volar ---
VolarD = pygame.transform.scale(pygame.image.load("VolarD.png"), (96,96))
VolarI = pygame.transform.scale(pygame.image.load("VolarI.png"), (96,96))

# Quieto
Quieto = pygame.transform.scale(pygame.image.load("Quieto.png"), (96,96))

# Físicas
vel_y = 0
gravedad = 0.5
en_suelo = True

# Animación
c_walk = 0

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
    if Movimiento[pygame.K_UP] and en_suelo:
        vel_y = -10
        en_suelo = False

    # --- Gravedad ---
    vel_y += gravedad
    Jugador.y += vel_y

    # Suelo
    if Jugador.y >= 350:
        Jugador.y = 350
        vel_y = 0
        en_suelo = True

    # --- Cámara ---
    cam_x = Jugador.x - 250

    # --- ANIMACIONES ---
    if not en_suelo:
        # VOLANDO
        if direccion == "derecha":
            JugadorEstado = VolarD
        else:
            JugadorEstado = VolarI

    else:
        # CAMINANDO DERECHA
        if Derecha:
            c_walk += 0.15
            if c_walk >= len(AnimD):
                c_walk = 0
            JugadorEstado = AnimD[int(c_walk)]

        # CAMINANDO IZQUIERDA
        elif Izquierda:
            c_walk += 0.15
            if c_walk >= len(AnimI):
                c_walk = 0
            JugadorEstado = AnimI[int(c_walk)]

        # QUIETO
        else:
            JugadorEstado = Quieto
            c_walk = 0

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
