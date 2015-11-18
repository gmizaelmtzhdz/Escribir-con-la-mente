'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
import os, sys
sys.path.append("model")
#sys.path.append("../object")
#from login import Login
from baseDatos import BaseDatos

class CtrlLogin:
	def __init__(self,login):
		self.__login=login
		self.__bd=BaseDatos()
	def agregarUsuario(self,usuario,contrasena):
		resultado=False
		if self.__bd.cuantosHay("usuario","nick",usuario) == 0:
			id=self.__bd.agregarUsuario(usuario)
			self.__login.setId(id)
			resultado=True
		return resultado

	def autenticarse(self,usuario,contrasena):
		resultado=False
		if self.__bd.cuantosHay("usuario","nick",usuario) != 0:
			id=self.__bd.obtenerIdUsuario(usuario)
			self.__login.setId(id)
			resultado=True
		return resultado

	def validar(self,usuario,contrasena):
		resultado=False
		self.__login.setUsuario(usuario)
		self.__login.setContrasena(contrasena)
		if self.__login.datosCorrectos():
			resultado=True
		return resultado
'''	
l=Login()
print(l.getId())
c=CtrlLogin(l)
if c.validar("mizael",""):
	print(c.agregarUsuario("mizael","123")) #si ya hay un nick asi devuelve False
print(l.getId())
'''
#bd=BaseDatos()
#bd.obtenerLetras()