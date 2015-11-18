'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
class Login:
	def __init__(self):
		self.__usuario=""
		self.__contrasena=""
		self.__id=0
	def datosCorrectos(self):
		return self.__usuario != "" #and self.__contrasena!= ""
		
	def setUsuario(self,usuario):
		self.__usuario=usuario
	def getUsuario(self):
		return self.__usuario

	def setContrasena(self,contrasena):
		self.__contrasena=contrasena
	def getContrasena(self):
		return self.__contrasena

	def setId(self,id):
		self.__id=id
	def getId(self):
		return self.__id