import pygame
import random
import sys

# Inicialización
pygame.init()

# Tamaño de pantalla y bloques
ANCHO, ALTO = 600, 400
TAM_BLOQUE = 20

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Game")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Reloj y fuente
reloj = pygame.time.Clock()
FPS = 10
fuente = pygame.font.SysFont("arial", 25)

# Función para mostrar texto en pantalla
def mostrar_texto(texto, x, y, color=BLANCO, centro=False):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    if centro:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    ventana.blit(superficie, rect)

# Generar comida
def generar_comida():
    x = random.randint(0, (ANCHO - TAM_BLOQUE) // TAM_BLOQUE) * TAM_BLOQUE
    y = random.randint(0, (ALTO - TAM_BLOQUE) // TAM_BLOQUE) * TAM_BLOQUE
    return (x, y)

# Pantalla de inicio
def pantalla_inicio():
    while True:
        ventana.fill(NEGRO)
        mostrar_texto("SNAKE GAME", ANCHO // 2, ALTO // 2 - 50, centro=True)
        mostrar_texto("Presiona ESPACIO para comenzar", ANCHO // 2, ALTO // 2, centro=True)
        mostrar_texto("Presiona ESC para salir", ANCHO // 2, ALTO // 2 + 40, centro=True)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Función principal del juego
def juego():
    serpiente = [(100, 100)]
    direccion = (TAM_BLOQUE, 0)
    comida = generar_comida()
    puntuacion = 0
    pausa = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direccion != (0, TAM_BLOQUE):
                    direccion = (0, -TAM_BLOQUE)
                elif evento.key == pygame.K_DOWN and direccion != (0, -TAM_BLOQUE):
                    direccion = (0, TAM_BLOQUE)
                elif evento.key == pygame.K_LEFT and direccion != (TAM_BLOQUE, 0):
                    direccion = (-TAM_BLOQUE, 0)
                elif evento.key == pygame.K_RIGHT and direccion != (-TAM_BLOQUE, 0):
                    direccion = (TAM_BLOQUE, 0)
                elif evento.key == pygame.K_p:
                    pausa = not pausa

        if pausa:
            mostrar_texto("PAUSA - Presiona P para continuar", ANCHO // 2, ALTO // 2, centro=True)
            pygame.display.flip()
            reloj.tick(5)
            continue

        # Mover serpiente
        nueva_cabeza = (serpiente[0][0] + direccion[0], serpiente[0][1] + direccion[1])

        # Colisiones
        if (
            nueva_cabeza[0] < 0 or nueva_cabeza[0] >= ANCHO or
            nueva_cabeza[1] < 0 or nueva_cabeza[1] >= ALTO or
            nueva_cabeza in serpiente
        ):
            mostrar_texto("¡Perdiste! Puntuación: {}".format(puntuacion), ANCHO // 2, ALTO // 2, centro=True)
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        serpiente.insert(0, nueva_cabeza)

        if nueva_cabeza == comida:
            puntuacion += 1
            comida = generar_comida()
        else:
            serpiente.pop()

        # Dibujar
        ventana.fill(NEGRO)
        for segmento in serpiente:
            pygame.draw.rect(ventana, VERDE, (*segmento, TAM_BLOQUE, TAM_BLOQUE))
        pygame.draw.rect(ventana, ROJO, (*comida, TAM_BLOQUE, TAM_BLOQUE))
        mostrar_texto(f"Puntuación: {puntuacion}", 10, 10)
        pygame.display.flip()
        reloj.tick(FPS)

# Ejecutar juego
pantalla_inicio()
juego()
