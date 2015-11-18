'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
class RecolectarDatos:
	def __init__(self):
		self.__idletra=None

		self.__meditacion=0.0
		self.__atencion=0.0
		
		self.__delta=0.0
		self.__theta=0.0
		self.__lowAlpha=0.0
		self.__highAlpha=0.0
		self.__lowBeta=0.0
		self.__highBeta=0.0
		self.__lowGamma=0.0
		self.__midGamma=0.0

		self.__estado= False
		self.__conectado=False
		self.__probando=False
		self.__datos=[]
		self.__ruido=None

		self.__string=""
		self.interfaz=None

	def setIdLetra(self,letra):
		self.__letra=letra
	def setMeditacion(self,meditacion):
		self.__meditacion=meditacion
	def setAtencion(self,atencion):
		self.__atencion=atencion
	def setDelta(self,delta):
		self.__delta=delta
	def setTheta(self,theta):
		self.__theta=theta
	def setLowAlpha(self,alpha):
		self.__lowAlpha=alpha
	def setHighAlpha(self,alpha):
		self.__highAlpha=alpha
	def setLowBeta(self,beta):
		self.__LowBeta=beta
	def setHighBeta(self,beta):
		self.__highBeta=beta
	def setLowGamma(self,gamma):
		self.__lowGamma=gamma
	def setMidGamma(self,gamma):
		self.__midGamma=gamma
	def setEstado(self,estado):
		self.__estado=estado
	def setConectado(self,conectado):
		self.__conectado=conectado
	def setDatos(self,datos):
		self.__datos.append(datos)
	def setRuido(self,ruido):
		self.__ruido=ruido
	def setProbando(self,probando):
		self.__probando=probando
	def setString(self,string):
		self.__string=string
	def setInterfaz(self,interfaz):
		self.interfaz=interfaz


	def getIdLetra(self):
		return self.__letra
	def getMeditacion(self):
		return self.__meditacion
	def getAtencion(self):
		return self.__atencion
	def getDelta(self):
		return self.__delta
	def getTheta(self):
		return self.__theta
	def getLowAlpha(self):
		return self.__lowAlpha
	def getHighAlpha(self):
		return self.__highAlpha
	def getLowBeta(self):
		return self.__lowBeta
	def getHighBeta(self):
		return self.__highBeta
	def getLowGamma(self):
		return self.__lowGamma
	def getMidGamma(self):
		return self.__midGamma
	def getEstado(self):
		return self.__estado
	def getConectado(self):
		return self.__conectado
	def getDatos(self):
		return self.__datos
	def getRuido(self):
		return self.__ruido
	def getProbando(self):
		return self.__probando
	def getString(self):
		return self.__string
	def getInterfaz(self):
		return self.interfaz