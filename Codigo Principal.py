import pygame

# ============================
#        MENU
# ============================
Jugando2 = False 
while Jugando2 == False:
    # Usamos un mensaje que no bloquee el input en el Immersive
    print("Seleccione una Opcion:")
    print("1: Jugar")
    print("2: Puntajes")
    print("3: Salir")
    opcion = str(input("seleccione una Opcion: "))
    
    if opcion == '1':
        print("\n1: Pato")
        print("2: TungTungsahur")
        print("3: Mago")
        print("4: Amongus")

        Personajes = str(input("Selecciones un personaje (1-4):", ))

        # --- Carga de imágenes ---
        # Asegúrate de que las rutas de las imágenes son correctas en tu proyecto
        ImgQuietoD = ImgQuietoI = ImgCaminandoD = ImgCaminandoI = ImgQuietoF = ImgSaltoD = ImgSaltoI = None

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
            ImgQuietoF = "ImagenesTung/Tung Quieto Frente.png"
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
        
        else:
            print("Selección de personaje no válida.")
            continue # Volver al inicio del menú si la selección es inválida

    elif opcion == '2':
        print("Puntajes no implementado aún.")
    elif opcion == '3':
        print("Gracias por jugar")
        break
    else:
        print("Opción no válida.")

# Si salimos del bucle del menú por '3', terminamos.
if Jugando2 == False and opcion != '1':
    exit()

# ============================
#        JUEGO
# ============================

pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((1000,800))

# ----------------------------
# Ajustes del Jugador
# ----------------------------
Jugador = pygame.Rect(200, 515, 48, 80) # Posición inicial en el suelo

#Puntos y tiempo
Limite_tiempo = 180
Puntos_iniciales = 1000
Perdida_por_s = 10
Bonificador = 0.2


# VIDAS
vida = 1
Jugando = True
tiempo_agotado = False
puntos_actual = Puntos_iniciales
puntos_final = 0
tiempo_inicial = pygame.time.get_ticks()
reloj = pygame.time.Clock()

Velocidad_Enemigo_H = -3
Velocidad_Enemigo_G = -2
liminete_iz_H = 7000
liminete_der_H = 7800
liminete_iz_G = 2000
liminete_der_G = 2800

# OBJETOS
Plataforma = "Objetos/PlataformaUa.png"

# *** CORRECCIÓN CRUCIAL DE PLATAFORMA ***
# 1. Definimos la posición Y real donde se debe dibujar la imagen y colisionar.
#    Antes la imagen se dibujaba en (550 - 76 = 474).
# 2. La altura se aumenta de 1px a 20px para asegurar la colisión.
PLATFORM_TOP_Y = 560 
PLATFORM_WIDTH = 96 
PLATFORM_HEIGHT = 20

# La hitbox ahora está en la posición visible de la plataforma y es más gruesa.
Posicionxy_Hitbox_P = pygame.Rect(250, PLATFORM_TOP_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

# La imagen de la plataforma debe coincidir con el tamaño de la hitbox.
Escala_de_P = pygame.transform.scale(pygame.image.load(Plataforma), (PLATFORM_WIDTH, 96)) # Alto de la imagen 96px

# FONDOS (Simplificado para evitar errores de archivo)
# Asumo que tienes "mapa de fondo.png" o uso un color de fondo temporal.
try:
    fondo1 = pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))
    fondo2 = pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))
    fondo3 = pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))
    fondo4 = pygame.transform.scale(pygame.image.load("mapa de fondo.png"), (2000,800))
    USAR_IMAGENES_FONDO = True
except pygame.error:
    print("Advertencia: No se encontró 'mapa de fondo.png'. Usando fondo azul.")
    USAR_IMAGENES_FONDO = False

# ENEMIGO (Homero)
# ... (resto del código de enemigos, asumo que las rutas son válidas)
Homero = "Enemigos/Omero chino.gif"
Posicionxy_Hitbox_H = pygame.Rect(7000,515,96,96)
Escala_de_H = pygame.transform.scale(pygame.image.load(Homero), (96,96))

# ENEMIGO (Green)
Green = "Enemigos/Grenn_quieto.png"
Posicionxy_Hitbox_G = pygame.Rect(2000,515,96,96)
Escala_de_G = pygame.transform.scale(pygame.image.load(Green), (96,96))

# CORAZÓN
ImgCorazon = pygame.transform.scale(pygame.image.load("Corazon lleno.png"), (150,100))
ImgCorazonVacio = pygame.transform.scale(pygame.image.load("Corazon Vasio.png"), (150,100))

# Animaciones (Asumo que las rutas de imágenes son válidas)
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

SaltoD = pygame.transform.scale(pygame.image.load(ImgSaltoD), (96,96))
SaltoI = pygame.transform.scale(pygame.image.load(ImgSaltoI), (96,96))
Quieto = pygame.transform.scale(pygame.image.load(ImgQuietoF), (96,96))

VelEny = 0
Gravedad = 0.5
EnElSuelo = True

Contador = 0
cam_x = 0
direccion = "derecha"

DEBUG_DRAW_HITBOXES = True

# ============================
#       LOOP PRINCIPAL
# ============================

while Jugando:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Jugando = False

        tiempo_de_juego_ms = pygame.time.get_ticks() - tiempo_inicial
        tiempo_de_juego_seg = tiempo_de_juego_ms // 1000

        tiempo_res_seg = Limite_tiempo - tiempo_de_juego_seg

    #Perdida de puntos
        puntos_actual = max(0, Puntos_iniciales -(tiempo_de_juego_seg * Perdida_por_s))

        if tiempo_de_juego_seg >= Limite_tiempo:
          Jugador = False
          tiempo_agotado = True
        

    Movimiento = pygame.key.get_pressed()
    Derecha = False
    Izquierda = False

    if Movimiento[pygame.K_RIGHT]:
        Jugador.x += 16
        Derecha = True
        direccion = "derecha"

    elif Movimiento[pygame.K_LEFT]:
        Jugador.x -= 16
        Izquierda = True
        direccion = "izquierda"

    if Movimiento[pygame.K_SPACE] and EnElSuelo:
        VelEny = -10
        EnElSuelo = False

    # Aplicar gravedad
    VelEny += Gravedad
    Jugador.y += VelEny

    # ===== COLISIÓN CON PLATAFORMA (LÓGICA CORRECTA) =====
    # Si colisiona con la plataforma:
    if Jugador.colliderect(Posicionxy_Hitbox_P):
        # Si el jugador estaba cayendo (VelEny > 0) y su posición anterior (Jugador.bottom - VelEny)
        # estaba por encima del top de la plataforma, significa que aterrizó.
        if VelEny > 0 and (Jugador.bottom - VelEny) <= Posicionxy_Hitbox_P.top:
            Jugador.bottom = Posicionxy_Hitbox_P.top # Lo reposicionamos en la cima
            VelEny = 0
            EnElSuelo = True
        # Esto previene que el jugador suba y se pegue a la parte inferior de la plataforma (colisión por debajo)
        elif VelEny < 0:
            Jugador.top = Posicionxy_Hitbox_P.bottom
            VelEny = 0
    
    # IMPORTANTE: Reajustamos EnElSuelo a FALSO si no hay colisión ni en el suelo principal
    # para que la gravedad siga aplicando hasta el siguiente chequeo.
    else:
        # Solo se pone en False si no está ya en el suelo principal (y=515)
        if Jugador.y < 515:
             EnElSuelo = False 
             
    # Suelo Principal (siempre debe ir al final, es la colisión final)
    if Jugador.y >= 515:
        Jugador.y = 515
        VelEny = 0
        EnElSuelo = True

    cam_x = Jugador.x - 400

    # Animación
    if not EnElSuelo:
        if direccion == "derecha":
            JugadorEstado = SaltoD
        elif direccion == "izquierda":
            JugadorEstado = SaltoI
        else:
            # Si salta pero no se mueve horizontalmente, usa la imagen quieta
            if direccion == "derecha": JugadorEstado = SaltoD
            else: JugadorEstado = SaltoI # Si la última dirección fue a la izquierda, usa la imagen de salto I
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

    # Colisiones enemigos
    if Jugador.colliderect(Posicionxy_Hitbox_H):
        vida -= 1

    if Jugador.colliderect(Posicionxy_Hitbox_G):
        vida -= 1

    if vida <= 0:
        Jugando = False

    # Movimiento Homero
    Posicionxy_Hitbox_H.x += Velocidad_Enemigo_H
    if Posicionxy_Hitbox_H.x <= liminete_iz_H:
        Velocidad_Enemigo_H = abs(Velocidad_Enemigo_H)
    elif Posicionxy_Hitbox_H.right >= liminete_der_H:
        Velocidad_Enemigo_H = -abs(Velocidad_Enemigo_H)

    # Movimiento Green
    Posicionxy_Hitbox_G.x += Velocidad_Enemigo_G
    if Posicionxy_Hitbox_G.x <= liminete_iz_G:
        Velocidad_Enemigo_G = abs(Velocidad_Enemigo_G)
    elif Posicionxy_Hitbox_G.right >= liminete_der_G:
        Velocidad_Enemigo_G = -abs(Velocidad_Enemigo_G)

    # --- DIBUJO ---
    pantalla.fill((0,0,0))
    
    # Dibujar fondos
    if USAR_IMAGENES_FONDO:
        pantalla.blit(fondo1, (-cam_x, 0))
        pantalla.blit(fondo2, (-cam_x + 2000, 0))
        pantalla.blit(fondo3, (-cam_x + 4000, 0))
        pantalla.blit(fondo4, (-cam_x + 6000, 0))
    else:
        # Fondo azul si no hay imagen
        pantalla.fill((135, 206, 235)) 
    
    # Dibujar objetos
    pantalla.blit(JugadorEstado, (Jugador.x - cam_x, Jugador.y))
    pantalla.blit(Escala_de_H,(Posicionxy_Hitbox_H.x - cam_x, Posicionxy_Hitbox_H.y))
    pantalla.blit(Escala_de_G,(Posicionxy_Hitbox_G.x - cam_x, Posicionxy_Hitbox_G.y))

    # IMAGEN PLATAFORMA: Ahora se dibuja en Posicionxy_Hitbox_P.y
    # porque la Hitbox ya está en la altura correcta (474).
    pantalla.blit(Escala_de_P, (Posicionxy_Hitbox_P.x - cam_x, Posicionxy_Hitbox_P.y))

    if vida == 1:
        pantalla.blit(ImgCorazon, (20,20))
    else:
        pantalla.blit(ImgCorazonVacio, (20,20))
    
    #Dibujar puntos y tiempo
    F_hud = pygame.font.Font(None, 40)

    texto_puntos = F_hud.render(f"Puntos:{puntos_actual}", True, (255, 255, 255))
    pantalla.blit(texto_puntos, (550, 40))

    #tiempo restante ms
    minutos = max(0, tiempo_res_seg) //60
    segundos = max(0, tiempo_res_seg) % 60

    texto_tiempo = F_hud.render(f"Tiempo: {minutos:02}:{segundos:02}", True, (255, 255, 255))
    pantalla.blit(texto_tiempo, (500, 20))

    # DIBUJO DE HITBOXES (MUY ÚTIL PARA DEBUGGING)
    if DEBUG_DRAW_HITBOXES:
        # Jugador (Blanco)
        pygame.draw.rect(pantalla, (255,255,255), (Jugador.x - cam_x, Jugador.y, Jugador.width, Jugador.height), 2)
        # Plataforma (Verde) - Ahora es más gruesa y está alineada con la imagen
        pygame.draw.rect(pantalla, (0,255,0), (Posicionxy_Hitbox_P.x - cam_x, Posicionxy_Hitbox_P.y, Posicionxy_Hitbox_P.width, Posicionxy_Hitbox_P.height), 2)
        # Enemigos (Rojo)
        pygame.draw.rect(pantalla, (255,0,0), (Posicionxy_Hitbox_H.x - cam_x, Posicionxy_Hitbox_H.y, Posicionxy_Hitbox_H.width, Posicionxy_Hitbox_H.height), 2)
        pygame.draw.rect(pantalla, (255,0,0), (Posicionxy_Hitbox_G.x - cam_x, Posicionxy_Hitbox_G.y, Posicionxy_Hitbox_G.width, Posicionxy_Hitbox_G.height), 2)

    pygame.display.update()
    reloj.tick(60)