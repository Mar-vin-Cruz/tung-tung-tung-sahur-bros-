import pygame

# ============================
#        MENU
# ============================
Jugando2 = False 
while Jugando2 == False:
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

# ============================
#        JUEGO
# ============================

pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((1000,800))

Jugador = pygame.Rect(200,515,1,1)

# VIDAS (solo 1 vida ahora)
vida = 1   # <<------ SOLO 1 VIDA
Jugando = True
reloj = pygame.time.Clock()

# OBJETOS
PlataformaImagen = "Objetos/PlataformaUa.png"
Plataforma = pygame.Rect(7800,400,96,96)
ImgPla = pygame.transform.scale(pygame.image.load(PlataformaImagen), (96,96))

# FONDOS
fondo1 = pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))
fondo2 = pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))
fondo3 = pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))
fondo4 = pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))

# ENEMIGO (Homero)
Homero = "Enemigos/Omero chino.gif"
Posicionxy_Hitbox_H = pygame.Rect(7800,515,1,1)  # HITBOX AJUSTADA AL TAMAÑO REAL
Escala_de_H = pygame.transform.scale(pygame.image.load(Homero), (128,128))

# ====== CORAZONES ======
ImgCorazon = pygame.transform.scale(pygame.image.load("Corazon lleno.png"), (150,100))
ImgCorazonVacio = pygame.transform.scale(pygame.image.load("Corazon Vasio.png"), (150,100))

# Animaciones caminar
CaminarD = [
    pygame.image.load(ImgCaminandoD),
    pygame.image.load(ImgQuietoD),
]
AnimD = [pygame.transform.scale(i, (96,96)) for i in CaminarD]

CaminarI = [
    pygame.image.load(ImgCaminandoI),
    pygame.image.load(ImgQuietoI),
]
AnimI = [pygame.transform.scale(i, (96,96)) for i in CaminarI]

# Saltos
SaltoD = pygame.transform.scale(pygame.image.load(ImgSaltoD), (96,96))
SaltoI = pygame.transform.scale(pygame.image.load(ImgSaltoI), (96,96))

# Quieto
Quieto = pygame.transform.scale(pygame.image.load(ImgQuietoF), (96,96))

# Fisicas
VelEny = 0
Gravedad = 0.5
EnElSuelo = True

Contador = 0
cam_x = 0
direccion = "derecha"

# ============================
#       LOOP PRINCIPAL
# ============================

while Jugando:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Jugando = False

    Movimiento = pygame.key.get_pressed()
    Derecha = False
    Izquierda = False

    # Movimiento horizontal
    if Movimiento[pygame.K_RIGHT]:
        Jugador.x += 16
        Derecha = True
        direccion = "derecha"

    elif Movimiento[pygame.K_LEFT]:
        Jugador.x -= 16
        Izquierda = True
        direccion = "izquierda"

    # Salto
    if Movimiento[pygame.K_SPACE] and EnElSuelo:
        VelEny = -10
        EnElSuelo = False

    VelEny += Gravedad
    Jugador.y += VelEny

    if Jugador.y >= 515:
        Jugador.y = 515
        VelEny = 0
        EnElSuelo = True

    # Cámara
    cam_x = Jugador.x - 400

    # ANIMACIONES
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

    # ============================
    #    COLISIÓN CON HOMERO (SIN INVENCIBILIDAD)
    # ============================

    if Jugador.colliderect(Secreto):
        vida -= 1
        Jugador.x -= 40  # Retroceso
        print("HOMERO TE HIZO DAÑO!")

    if vida <= 0:
        print("MORISTE! Homero te destruyó.")
        Jugando = False

    # ============================
    #        DIBUJAR
    # ============================
    pantalla.fill((0,0,0))

    pantalla.blit(fondo1, (-cam_x, 0))
    pantalla.blit(fondo2, (-cam_x + 2000, 0))
    pantalla.blit(fondo3, (-cam_x + 4000, 0))
    pantalla.blit(fondo4, (-cam_x + 6000, 0))

    pantalla.blit(JugadorEstado, (Jugador.x - cam_x, Jugador.y))
    pantalla.blit(ImgSecreto,(Secreto.x - cam_x, Secreto.y))
    pantalla.blit(ImgPla, (Plataforma.x - cam_x, Plataforma.y))

    # DIBUJAR CORAZÓN ÚNICO
    if vida == 1:
        pantalla.blit(ImgCorazon, (20,20))
    else:
        pantalla.blit(ImgCorazonVacio, (20,20))

    pygame.display.update()
    reloj.tick(60)


