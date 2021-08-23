
import random

class Agent:
	def __init__(self,env):
		self.env = env
		self.i = env.init_posX
		self.j = env.init_posY
		self.think()
       
	def up(self):
		mov = self.env.accept_action("arriba",self.i,self.j)
		if (mov == True):
			self.i=self.i-1 #sube 1 pos en i
			return True
		return False
	def down(self):
		mov = self.env.accept_action("abajo",self.i,self.j)
		if (mov == True):
			self.i=self.i+1 #baja 1 pos en i
			return True
		return False
	def left(self):
		mov = self.env.accept_action("izquierda",self.i,self.j)
		if (mov == True):
			self.j=self.j-1 #retrocede 1 pos en j
			return True
		return False	
	def right(self):
		mov = self.env.accept_action("derecha",self.i,self.j)
		if (mov == True):
			self.j=self.j+1 #avanza 1 pos en j
			return True
		return False
	def suck(self):
		self.env.accept_action("limpiar",self.i,self.j)

	def think(self): # implementa las acciones a seguir por el agente
		
		while (self.env.life < 1000):
			x=False
			rand = random.randint(0,4)
						
			if (rand == 0): # arriba
				x = self.up()				

			elif (rand == 1): # abajo
				x=self.down()	
			
			elif (rand == 2):  # izquierda
				x=self.left()	
			
			elif (rand == 3):  # derecha
				x=self.right()
				
			elif (rand == 4):  # nohacernada
				self.env.life += 1  
			
			if (x==True): #si es posible moverse, se fija si puede limpiar y suma una vida útil
				self.suck()
				self.env.life += 1
			
		print("mapa después de pasar el agente:")
		self.env.print_env()
		print("posiciones sucias: " , int(self.env.dirty), " de 1000")	
		print("Performance: ", self.env.get_performance())
