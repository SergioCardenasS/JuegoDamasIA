from constants import *
from Ntree import *
from functions import *
from reglas import *
import random
import sys


def encontrar_fichas(matriz,ficha):
	lista = []
	for x in range(len(matriz)):
			for y in range(len(matriz[x])):
				if (matriz[x][y] == ficha):
					lista.append((x,y))
	return lista


def podaAB(tree,alfa,beta):
	tree.setAB(alfa,beta)
	dth = tree.depth(tree)
	print "Estamos en :",tree.nodo,dth
	
	for son in tree.sons:
		val = podaAB(son,tree.alfa,tree.beta)
		if(dth%2==0):#MINIMOS beta pares
			print "Minimos "
			print val,dth
			"""if(val>tree.alfa):
				tree.valor = val
				tree.ruta = son
				#return tree.valor"""
			if(tree.beta>=val):
				print "tree valor a :",val
				tree.beta=val
				tree.valor=val
				tree.ruta = son
		else: #MAXIMOS alfa impares
			print "Maximos"
			"""if(val<tree.beta):
				tree.valor = val
				tree.ruta = son
				#return tree.valor"""
			if(tree.alfa<=val):
				print "tree valor a :",val
				tree.alfa = val
				tree.valor= val
				tree.ruta = son
	print "Retornamos ", tree.valor
	print "Profundid: ",tree.depth(tree)
	return tree.valor

def CrearArbol(matriz,nivel,tipo):
	grid = matriz
	treeAB = Tree(grid,(0,0),(0,0),tipo)
	cont = 1
	padre = (0,0)
	# Creamos el primer nivel
	fichas = encontrar_fichas(grid,tipo)
	for ficha in fichas:
		jugadas = posibles_jugadas(grid,ficha,tipo)
		for jugada in jugadas:
			print jugada,
			treeAB.addNodo(treeAB,padre,ficha,jugada,tipo)

	act = treeAB.ejecutarAnchoNodos(treeAB,1,cont+1)
	for hijo in act:
		hijo.actualizarNodo()

	cont+=1
	while(cont<nivel):
		padres = treeAB.ejecutarAncho(treeAB,1,cont)
		nodos = treeAB.ejecutarAnchoNodos(treeAB,1,cont)
		if(cont%2==0):
			for padre in range(len(padres)):
				nodo = nodos[padre]
				fichas = encontrar_fichas(nodo.matriz,FICHA_BEIGE)
				for ficha in fichas:
					jugadas = posibles_jugadas(nodo.matriz,ficha,FICHA_BEIGE)
					for jugada in jugadas:
						nodo.addNodo(nodo,nodo.nodo,ficha,jugada,FICHA_BEIGE)
			act = treeAB.ejecutarAnchoNodos(treeAB,1,cont+1)
			for hijo in act:
				hijo.actualizarNodo()
			cont+=1
		else:
			for padre in range(len(padres)):
				nodo = nodos[padre]
				fichas = encontrar_fichas(nodo.matriz,FICHA_NEGRO)
				for ficha in fichas:
					jugadas = posibles_jugadas(nodo.matriz,ficha,FICHA_NEGRO)
					for jugada in jugadas:
						nodo.addNodo(nodo,nodo.nodo,ficha,jugada,FICHA_NEGRO)
			act = treeAB.ejecutarAnchoNodos(treeAB,1,cont+1)
			for hijo in act:
				hijo.actualizarNodo()
			cont+=1

	nodos = treeAB.ejecutarAnchoNodos(treeAB,1,cont)
	print "Cont: ",cont
	if(cont%2==0):
		for nodo in nodos:
			if(nodo.nodo_fin[0]==0):
				nodo.setValor(100)
			else:
				"""if(len(encontrar_fichas(nodo.matriz,FICHA_NEGRO))>len(encontrar_fichas(nodo.matriz,FICHA_BEIGE))):
					nodo.setValor(1)
				elif(len(encontrar_fichas(nodo.matriz,FICHA_NEGRO))==len(encontrar_fichas(nodo.matriz,FICHA_BEIGE))):
					nodo.setValor(0)
				else:
					nodo.setValor(-1)"""
				#print len(encontrar_fichas(nodo.matriz,FICHA_NEGRO))-len(encontrar_fichas(nodo.matriz,FICHA_BEIGE))
				nodo.setValor(len(encontrar_fichas(nodo.matriz,FICHA_BEIGE)) - len(encontrar_fichas(nodo.matriz,FICHA_NEGRO)))
				#nodo.setValor(len(encontrar_fichas(nodo.matriz,FICHA_NEGRO)) - len(encontrar_fichas(nodo.matriz,FICHA_BEIGE)))
	else:
		for nodo in nodos:
			if(nodo.nodo_fin[0]==7):
				nodo.setValor(-100)
			else:
				"""if(len(encontrar_fichas(nodo.matriz,FICHA_BEIGE))>len(encontrar_fichas(nodo.matriz,FICHA_NEGRO))):
					nodo.setValor(-1)
				elif(len(encontrar_fichas(nodo.matriz,FICHA_BEIGE))==len(encontrar_fichas(nodo.matriz,FICHA_NEGRO))):
					nodo.setValor(0)
				else:
					nodo.setValor(1)"""
				#print len(encontrar_fichas(nodo.matriz,FICHA_BEIGE))-len(encontrar_fichas(nodo.matriz,FICHA_NEGRO))
				#nodo.setValor(len(encontrar_fichas(nodo.matriz,FICHA_BEIGE)) - len(encontrar_fichas(nodo.matriz,FICHA_NEGRO)))
				nodo.setValor(len(encontrar_fichas(nodo.matriz,FICHA_NEGRO)) - len(encontrar_fichas(nodo.matriz,FICHA_BEIGE)))
	return treeAB


# MAX = jugada enemiga = len de mis fichas - len de sus fichas
# MIN = jugada mia = len de sus fichas - len de mis fichas
""" 
1 jugada inicial	 MAX
2 jugada mia 		MIN
3 jugada enemiga     MAX
4 jugada mia 		MIN
5 jugada enemiga     MAX
"""



grid = [[0,1,0,3,0,1,0,3],
        [1,0,1,0,1,0,3,0],
        [0,1,0,2,0,1,0,3],
        [3,0,3,0,2,0,3,0],
        [0,3,0,3,0,3,0,3],
      	[3,0,3,0,3,0,3,0],
        [0,1,0,2,0,3,0,3],
        [2,0,3,0,3,0,3,0]]

#CalcularJugadasIA(grid,3,FICHA_BEIGE)

nivel = 4
treeAB = CrearArbol(grid,nivel,FICHA_NEGRO)
hijos = treeAB.ejecutarAnchoNodos(treeAB,1,2)
podaAB(treeAB,INFINITO_NEGATIVO,INFINITO_POSITIVO)
lista = treeAB.rutaAB(treeAB,[])

for hijo in lista:
	print hijo.nodo
	for fila in hijo.matriz:
		for col in fila:
			print col,
		print ""
	print ""

treeAB.printTree(treeAB,nivel)

for hijo in hijos:
	print hijo.nodo, hijo.valor, hijo.depth(hijo)
	for fila in hijo.matriz:
		for col in fila:
			print col,
		print ""
	print ""

def Aleatorio(matriz, tipo):
	jugadas = []
	lista = encontrar_fichas(matriz, tipo)
	while(len(jugadas)==0):
		ficha = random.randrange(0,len(lista),1)
		jugadas = posibles_jugadas(matriz, lista[ficha], tipo)
	index = random.randrange(0,len(jugadas),1)
	jugada = jugadas[index]
	return (lista[ficha],jugada)