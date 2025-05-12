import pygame
import random
import sys

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Game")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Tamaño del bloque (segmento de la serpiente)
TAM_BLOQUE = 20

# Velocidad del juego
reloj = pygame.time.Clock()
FPS = 10

# Función para generar una posición aleatoria para la comida
def generar_comida():
    x = random.randint(0, (ANCHO - TAM_BLOQUE) // TAM_BLOQUE) * TAM_BLOQUE
    y = random.randint(0, (ALTO - TAM_BLOQUE) // TAM_BLOQUE) * TAM_BLOQUE
    return (x, y)

# Variables de la serpiente
serpiente = [(100, 100)]
direccion = (TAM_BLOQUE, 0)  # Empieza yendo a la derecha

comida = generar_comida()

def dibujar_elementos():
    ventana.fill(NEGRO)
    for segmento in serpiente:
        pygame.draw.rect(ventana, VERDE, (*segmento, TAM_BLOQUE, TAM_BLOQUE))
    pygame.draw.rect(ventana, ROJO, (*comida, TAM_BLOQUE, TAM_BLOQUE))
    pygame.display.flip()

# Bucle principal
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

    # Mover la serpiente
    nueva_cabeza = (serpiente[0][0] + direccion[0], serpiente[0][1] + direccion[1])

    # Colisión con los bordes o consigo misma
    if (
        nueva_cabeza[0] < 0 or nueva_cabeza[0] >= ANCHO or
        nueva_cabeza[1] < 0 or nueva_cabeza[1] >= ALTO or
        nueva_cabeza in serpiente
    ):
        print("¡Has perdido!")
        pygame.quit()
        sys.exit()

    serpiente.insert(0, nueva_cabeza)

    # Verificar si ha comido
    if nueva_cabeza == comida:
        comida = generar_comida()
    else:
        serpiente.pop()  # Eliminar la cola

    dibujar_elementos()
    reloj.tick(FPS)
