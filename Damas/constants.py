# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)
BEIGE = (255, 253, 208)
MARRON = (172, 112, 61)
BEIGE_OSCURO = (239, 221, 111)
NEGRO_CLARO = (80, 80, 80)
#Botones
LEFT = 1
RIGHT = 3
#Pantalla
width = 900
height = 600
# Establecemos el margen entre las celdas.
MARGEN = 1
#Margen de grid
xGrid = 20
yGrid = 20
widthGrid = 560
heightGrid = 550
#numero de bloques
tam = 8
#Largo y alto de los bloques
LARGO = (widthGrid/tam)- 2*MARGEN
ALTO = (heightGrid/tam)- 2*MARGEN
#Fichas
FICHAS_BEIGE = 10
FICHAS_NEGRO = 10
FICHA_BEIGE = 1
FICHA_NEGRO = 2
VACIO = 3
#Espacio entre puntos
SALTO = ((MARGEN+LARGO)*2 +MARGEN + xGrid)-((MARGEN+LARGO) +MARGEN + xGrid)
#Juego 
TURNO = 1
#Nombre de los jugadores
J1 = "Player 1(Beige)"
J2 = "Player 2(Negras)"
#Niveles	
EASY = 2
MEDIUM = 4
HARD = 8
#INFINITOS
INFINITO_NEGATIVO = -10000
INFINITO_POSITIVO =  10000