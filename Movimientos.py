#Archivo para hacer los def del movimiento de los personajes
import pygame

pygame.init()
pantalla = pygame.display.set_mode((500,500))
Jugador = pygame.Rect(0,0,96,96)
Jugando = True
reloj = pygame.time.Clock()
reloj.tick(60)

#Movimientos
CaminarD= [
pygame.image.load("CaminarD1.png"),
pygame.image.load("CaminarD1.png"),
pygame.image.load("CaminarD2.png"),
pygame.image.load("CaminarD1.png"),
pygame.image.load("CaminarD1.png"),
]
AnimD = [pygame.transform.scale(ImagenD, (96,96)) for ImagenD in CaminarD]

CaminarI= [
pygame.image.load("CaminarI1.png"),
pygame.image.load("CaminarI1.png"),
pygame.image.load("CaminarI2.png"),
pygame.image.load("CaminarI1.png"),
pygame.image.load("CaminarI1.png"),
]
AnimI = [pygame.transform.scale(ImagenI, (96,96)) for ImagenI in CaminarI]
Contador1 = 0
Contador2 = 0

Quieto = pygame.image.load("Quieto.png")
Quieto = pygame.transform.scale(Quieto, (96,96))

Derecha = False
Izquierda = False

while Jugando == True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Jugando = False 
    
    Movimiento = pygame.key.get_pressed()
    
    #Control

    #Derecha
    if Movimiento[pygame.K_RIGHT]:
        Jugador.x += 1
        Derecha = True
        Izquierda = False

    #Izquierda
    elif Movimiento[pygame.K_LEFT]:
        Jugador.x -= 1
        Izquierda = True
        Derecha = False

    else:
        Derecha = False
        Izquierda = False
        EstQuieto = True
    
        
    if Derecha == True:
        Contador1 += 0.2
        if Contador1 >= len(CaminarD):
            Contador1 = 0
        JugadorEstado = AnimD[int(Contador1)]

    elif Izquierda == True:
        Contador2 += 0.2
        if Contador2 >= len(CaminarI):
            Contador2 = 0
        JugadorEstado = AnimI[int(Contador2)]

    elif EstQuieto :
        JugadorEstado = Quieto

    reloj.tick(60)
    pantalla.fill((0,0,0))
    pantalla.blit(JugadorEstado,Jugador)
    pygame.display.update()