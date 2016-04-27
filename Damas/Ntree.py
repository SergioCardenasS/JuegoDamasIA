from constants import *
from reglas import *

class Tree():
	def __init__(self,matriz,nodo,nodo_fin,tipo):
		self.tipo = tipo
		self.sons = []
		self.valor = 0
		self.nodo = nodo
		self.nodo_fin = nodo_fin
		self.matriz = matriz
		self.alfa = INFINITO_NEGATIVO
		self.beta = INFINITO_POSITIVO
		self.ruta = 0

	def setAB(self,alfa,beta):
		self.alfa = alfa
		self.beta = beta

	def addNodo(self,tree,nodo_padre,nodo_inicio,nodo_fin,tipo):
		subtree = self.searchSubtree(tree, nodo_padre);
		grid = []
		for fil in range(len(subtree.matriz)):
			c = []
			for col in range(len(subtree.matriz[fil])):
				c.append(subtree.matriz[fil][col])
			grid.append(c)
		nuevo_nodo = Tree(grid,nodo_inicio,nodo_fin,tipo)
		subtree.sons.append(nuevo_nodo)

	def rutaAB(self,tree,lista):
		rt = tree.ruta
		for son in tree.sons:
			if(son == rt):
				lista.append(son)
				return son.rutaAB(son,lista)
		return lista

	def actualizarNodo(self):
		#print "Actualizando: ",self.nodo,self.nodo_fin,self.tipo
		mover_ficha(self.matriz,self.nodo,self.nodo_fin,self.tipo)
		#if(calcular_victimas(self.matriz,self.nodo,self.nodo_fin,self.tipo)):
			#self.valor+=1
		self.matriz[self.nodo[0]][self.nodo[1]] = 3

	def searchSubtree(self, tree, nodo):
		if tree.nodo == nodo:
			return tree
		for subtree in tree.sons:
			treeSearch = self.searchSubtree(subtree, nodo)
			if (treeSearch!= None):
				return treeSearch
		return None

	def setValor(self, valor):
		self.valor = valor


	def depth(self, tree):
		if len(tree.sons) == 0: 
			return 1
		return 1 + max(map(self.depth,tree.sons)) 

	def ejecutarAncho(self,tree,cont,profundidad):
		cola = []
		hijos = []
		if (profundidad==1):
			return [tree.nodo]
		elif(profundidad==2):
			for hijo in tree.sons:
				cola.append(hijo.nodo)
			return cola
		else:
			cont = 2
			cola = tree.sons
			while(cont<profundidad):
				if (len(cola) != 0):
					for hijo in cola:
						for son in hijo.sons:
							hijos.append(son)
				cont+=1
				cola = hijos
				hijos = []
		for hijo in cola:
			hijos.append(hijo.nodo)
		return hijos


	def ejecutarAnchoNodos(self,tree,cont,profundidad):
		cola = []
		hijos = []
		if (profundidad==1):
			return [tree.nodo]
		elif(profundidad==2):	
			return tree.sons
		else:
			cont = 2
			cola = tree.sons
			while(cont<profundidad):
				if (len(cola) != 0):
					for hijo in cola:
						for son in hijo.sons:
							hijos.append(son)
				cont+=1
				cola = hijos
				hijos = []
		return cola

	def grade(self, tree):
		return max(map(self.grade, tree.sons) + [len(tree.sons)])

	def printTree(self,tree,cont):
		print cont*" ",
		print tree.nodo
		for son in tree.sons:
			self.printTree(son,cont+1)

	def printMatrices(self,tree):
		for x in tree.matriz:
			print x
		print ""
		for son in tree.sons:
			self.printMatrices(son)

"""
ar = Tree((1,2),(2,2),1)
ar.addNodo(ar,(1,2),(1,1),(2,1),2)
ar.addNodo(ar,(1,2),(2,2),(2,1),2)
ar.addNodo(ar,(1,2),(3,3),(2,1),2)
ar.addNodo(ar,(1,1),(4,4),(2,1),2)
ar.addNodo(ar,(1,1),(5,5),(2,1),2)
ar.addNodo(ar,(4,4),(6,6),(2,1),2)
ar.addNodo(ar,(6,6),(7,7),(2,1),2)
ar.printTree(ar,0)
print ar.depth(ar)
print ar.ejecutarAnchoPrimero(ar,1,3)
"""