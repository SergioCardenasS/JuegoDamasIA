import pygame
from constants import *
from functions import *
from reglas import *
from algoritmoAB import *
from Ntree import *

def main():
	grid = crear_tablero()
	# Inicializamos pygame
	pygame.init()
	# Establecemos el LARGO y ALTO de la pantalla
	DIMENSION_VENTANA = [width, height]
	pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
	#Titulo
	pygame.display.set_caption("Damas")
	done = False
	reloj = pygame.time.Clock()
	TURNO = 1
	PUSH = 0
	jugadas = []
	ficha_seleccionada = [0,(0,0)]

	while not done:
		for evento in pygame.event.get(): 
			if (evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == 27)):
				done = True
			#Beige
			elif (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT and TURNO == 1):
				jugadas = []
				pos = pygame.mouse.get_pos()
				columna_inicio = ((pos[0]- xGrid)/ (LARGO + MARGEN))
				fila_inicio = ((pos[1]-yGrid) / (ALTO + MARGEN))
				if(columna_inicio>-1 and columna_inicio<tam and fila_inicio >-1 and fila_inicio <tam):
					if (grid[fila_inicio][columna_inicio] == 1):
						grid[fila_inicio][columna_inicio] = 3
						ficha_seleccionada[0]=FICHA_BEIGE
						ficha_seleccionada[1]=(fila_inicio,columna_inicio)
						jugadas = posibles_jugadas(grid,(fila_inicio,columna_inicio),FICHA_BEIGE)
						PUSH = 1

			elif (evento.type == pygame.MOUSEBUTTONUP and evento.button == LEFT and TURNO==1 and PUSH==1):
				pos = pygame.mouse.get_pos()
				columna_destino = ((pos[0]- xGrid)/ (LARGO + MARGEN))
				fila_destino = ((pos[1]-yGrid) / (ALTO + MARGEN))
				if(columna_destino>-1 and columna_destino<tam and fila_destino>-1 and fila_destino<tam):
					if ((fila_destino,columna_destino)in jugadas):
						jugadas = []
						mover_ficha(grid,(fila_inicio,columna_inicio),(fila_destino,columna_destino),FICHA_BEIGE)
						TURNO = 2
						if(fila_destino == 7):
							TURNO = 3
					else:
						grid[fila_inicio][columna_inicio] = 1
				else:
					grid[fila_inicio][columna_inicio] = 1
				ficha_seleccionada = [0,(0,0)]
				PUSH = 0
			#Negras
			elif (TURNO == 2):
				nivel = 5
				negro = encontrar_fichas(grid,FICHA_NEGRO)
				if(len(negro)!=0 or TURNO == 3):
					treeAB = CrearArbol(grid,nivel,FICHA_NEGRO)
					hijos = treeAB.ejecutarAnchoNodos(treeAB,1,nivel)
					podaAB(treeAB,INFINITO_NEGATIVO,INFINITO_POSITIVO)
					jugada = treeAB.rutaAB(treeAB,[])

					nodo = jugada[0]

					inicio = nodo.nodo
					fin = nodo.nodo_fin

					mover_ficha(grid,inicio,fin,FICHA_NEGRO)
					grid[inicio[0]][inicio[1]] = 3
					TURNO = 1
					if(fin[0] == 0):
						TURNO = 4
			"""
			elif (TURNO == 2):
				negro = encontrar_fichas(grid,FICHA_NEGRO)
				if(len(negro)!=0 or TURNO == 3):
					jugada = Aleatorio(grid,FICHA_NEGRO)
					inicio = jugada[0]
					fin = jugada[1]
					mover_ficha(grid,inicio,fin,FICHA_NEGRO)
					grid[inicio[0]][inicio[1]] = 3
					TURNO = 1
					if(fin[0] == 0):
						TURNO = 4
			"""
			"""elif (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT and TURNO == 2):
				jugadas = []
				pos = pygame.mouse.get_pos()
				columna_inicio = ((pos[0]- xGrid)/ (LARGO + MARGEN))
				fila_inicio = ((pos[1]-yGrid) / (ALTO + MARGEN))
				if(columna_inicio>-1 and columna_inicio<tam and fila_inicio>-1 and fila_inicio<tam):
					if (grid[fila_inicio][columna_inicio] == 2):
						grid[fila_inicio][columna_inicio] = 3
						ficha_seleccionada[0]=FICHA_NEGRO
						ficha_seleccionada[1]=(fila_inicio,columna_inicio)
						jugadas = posibles_jugadas(grid,(fila_inicio,columna_inicio),FICHA_NEGRO)
						PUSH = 1
			elif (evento.type == pygame.MOUSEBUTTONUP and evento.button == LEFT and TURNO == 2 and PUSH==1):
				pos = pygame.mouse.get_pos()
				columna_destino = ((pos[0]- xGrid)/ (LARGO + MARGEN))
				fila_destino = ((pos[1]-yGrid) / (ALTO + MARGEN))
				if(columna_destino>-1 and columna_destino<tam and fila_destino>-1 and fila_destino<tam):
					if ((fila_destino,columna_destino)in jugadas):
						jugadas = []
						mover_ficha(grid,(fila_inicio,columna_inicio),(fila_destino,columna_destino),FICHA_NEGRO)
						TURNO = 1
					else:
						grid[fila_inicio][columna_inicio] = 2
				else:
					grid[fila_inicio][columna_inicio] = 2
				ficha_seleccionada = [0,(0,0)]
				PUSH = 0
			"""
				
		# Establecemos el fondo de pantalla.
		pantalla.fill(NEGRO)
		beige = encontrar_fichas(grid,FICHA_BEIGE)
		negro = encontrar_fichas(grid,FICHA_NEGRO)
		if(len(beige)==0 or TURNO == 4):
			text_jugada(pantalla,"Ganador NEGRAS",600,50)
		elif(len(negro)==0 or TURNO == 3):
			text_jugada(pantalla,"Ganador BEIGE",600,50)
		#Textos 
		if(TURNO==1):
			text_jugada(pantalla,"TURNO : "+J1,600,20)
		else:
			text_jugada(pantalla,"TURNO : "+J2,600,20)
		#Grid
		for fila in range(tam):
			for columna in range(tam):
				if(fila%2==0):
					if(columna%2==0):
						color = BEIGE
					else:
						color = MARRON
				else:
					if(columna%2==0):
						color = MARRON
					else:
						color = BEIGE
				xRect = (MARGEN+LARGO) * columna + MARGEN + xGrid
				yRect = (MARGEN+ALTO) * fila + MARGEN + yGrid
				if (xRect < heightGrid and yRect < widthGrid):
					pygame.draw.rect(pantalla,color, [xRect, yRect, LARGO, ALTO])
				if(grid[fila][columna]==1):
					pygame.draw.circle(pantalla,BEIGE_OSCURO,(xRect+SALTO/2,yRect+SALTO/2),ALTO/2)
				elif(grid[fila][columna]==2):
					pygame.draw.circle(pantalla,NEGRO_CLARO,(xRect+SALTO/2,yRect+SALTO/2),ALTO/2)
				if (ficha_seleccionada[0]==FICHA_BEIGE):
					x_rect = (MARGEN+LARGO) * ficha_seleccionada[1][1] + MARGEN + xGrid
					y_rect = (MARGEN+ALTO) * ficha_seleccionada[1][0] + MARGEN + yGrid
					pygame.draw.circle(pantalla,BEIGE_OSCURO,(x_rect+SALTO/2,y_rect+SALTO/2),ALTO/2,1)
				elif(ficha_seleccionada[0]==FICHA_NEGRO):
					x_rect = (MARGEN+LARGO) * ficha_seleccionada[1][1] + MARGEN + xGrid
					y_rect = (MARGEN+ALTO) * ficha_seleccionada[1][0] + MARGEN + yGrid
					pygame.draw.circle(pantalla,NEGRO_CLARO,(x_rect+SALTO/2,y_rect+SALTO/2),ALTO/2,1)
				for element in jugadas:
					x_rect = (MARGEN+LARGO) * element[1] + MARGEN + xGrid
					y_rect = (MARGEN+ALTO) * element[0] + MARGEN + yGrid
					pygame.draw.circle(pantalla,ROJO,(x_rect+SALTO/2,y_rect+SALTO/2),ALTO/2,1)


		# Limitamos a 20 fotogramas por segundo.
		reloj.tick(50)
		# Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
		pygame.display.flip()

	pygame.quit()

main()
