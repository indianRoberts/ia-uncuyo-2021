
import numpy as np
import random


class env:
	life=0
	point=0
	###################################################
	def __init__(self,sizeX,sizeY,dirt_rate):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.init_posX = random.randint(0,sizeX-1)
		self.init_posY = random.randint(0,sizeY)-1
		
		self.matrix = np.zeros((sizeX,sizeY)) 
		
		#se crean las casillas sucias
		self.dirty = int(dirt_rate * (sizeX * sizeY)) +1
		clean=0
		while (clean < self.dirty):
			i = random.randint(0,sizeX-1)
			j = random.randint(0,sizeY-1)
			if (self.matrix[i][j] == 0):
				self.matrix[i][j] = 1
				clean += 1
		print("mapa previo:")
		env.print_env(self)
	###########################################
	def accept_action(self,action,posX,posY):
		#print(posX,posY)

		if (action == "izquierda"):
			if ( posY-1 >= 0 ):
				return True
			return False
		elif (action == "derecha"):
			if (posY+1 < self.sizeY):
				return True
			return False	
		elif (action == "arriba"):
			if (posX-1 >= 0):
				return True
			return False
		elif (action == "abajo"):
			if (posX+1 < self.sizeX):
				return True
			return False
		elif (action == "limpiar"):
			if (self.is_dirty(posX,posY) == True):
				self.point= self.point + 1
				self.matrix[posX][posY] = 0	
			
  	###########################################
	def is_dirty(self,x,y):
		if (self.matrix[x][y] == 1):	
			return True
		return False
	############################################
	def get_performance(self):
		return self.point/self.life
	############################################# 	  
	def print_env(self):
		for a in range(0,self.sizeX):
			print(self.matrix[a])
		print(" ")

