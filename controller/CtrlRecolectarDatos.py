# -*- encoding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
import os,sys,time,math
sys.path.append("model")
sys.path.append("object")
sys.path.append("mindwavemobile")

from MindwaveDataPoints import RawDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader
from MindwaveDataPoints import EEGPowersDataPoint
from RecolectarDatos import RecolectarDatos
import threading
#from Hilo import Hilo

from baseDatos import BaseDatos
from login import Login

class CtrlRecolectarDatos:
	def __init__(self,login):

		self.__login=login
		self.__datos=None
		self.__neuroSky = MindwaveDataPointReader()
		self.__neuroSkyDatos=None
		self.__senal=None
		
		self.__bd=BaseDatos()
		self.__evento=None

	def conectarNeuroSky(self):
		data={"delta":-1,"tetha":-1,"lowAlpha":-1,"highAlpha":-1,"lowBeta":-1,"highBeta":-1,"lowGamma":-1,"midGamma":-1,"meditacion":-1,"atencion":-1,"id_letras":self.__datos.getIdLetra(),"id_usuario":self.__login.getId(),"ruido":-1}
		k=i=0
		self.__neuroSky.start()
		self.__neuroSkyDatos=self.__neuroSky.readNextDataPoint()
		if self.__neuroSky.isConnected():
			print("Conectado...")
			self.__datos.setConectado(True)
			self.__senal=None
			while(True):
				self.__neuroSkyDatos=self.__neuroSky.readNextDataPoint()
				if (not self.__neuroSkyDatos.__class__ is RawDataPoint):
					#print(self.__neuroSkyDatos)
					if self.__datos.getEstado():
						data["id_usuario"] =self.__login.getId()
						data["id_letras"]=self.__datos.getIdLetra()
						if (i == 0):
							data["meditacion"]=(float(self.__neuroSkyDatos.meditationValue))
							self.__datos.setMeditacion(float(self.__neuroSkyDatos.meditationValue))

						elif (i == 1):
							data["atencion"]=(float(self.__neuroSkyDatos.attentionValue))
							self.__datos.setAtencion(float(self.__neuroSkyDatos.attentionValue))

						elif (i == 2):
							data["delta"]=(float(self.__neuroSkyDatos.delta))
							self.__datos.setDelta(float(self.__neuroSkyDatos.delta))

							data["tetha"]=(float(self.__neuroSkyDatos.theta))
							self.__datos.setTheta(float(self.__neuroSkyDatos.theta))

							data["lowAlpha"]=(float(self.__neuroSkyDatos.lowAlpha))
							self.__datos.setLowAlpha(float(self.__neuroSkyDatos.lowAlpha))

							data["highAlpha"]=(float(self.__neuroSkyDatos.highAlpha))
							self.__datos.setHighAlpha(float(self.__neuroSkyDatos.lowAlpha))

							data["lowBeta"]=(float(self.__neuroSkyDatos.lowBeta))
							self.__datos.setLowBeta(float(self.__neuroSkyDatos.lowAlpha))

							data["highBeta"]=(float(self.__neuroSkyDatos.highBeta))
							self.__datos.setHighBeta(float(self.__neuroSkyDatos.lowAlpha))

							data["lowGamma"]=(float(self.__neuroSkyDatos.lowGamma))
							self.__datos.setLowGamma(float(self.__neuroSkyDatos.lowGamma))

							data["midGamma"]=(float(self.__neuroSkyDatos.midGamma))
							self.__datos.setMidGamma(float(self.__neuroSkyDatos.midGamma))
						elif (i == 3):

							self.__senal=float(self.__neuroSkyDatos.amountOfNoise)
							self.__datos.setRuido(self.__senal)
							self.__datos.setEstado(False)
							data["ruido"]=self.__senal
							#Insertando el valor de las ondas en la bd
							if not self.__datos.getProbando():
								self.__bd.insertarStreamOndas(data)
							print("*"*30)
							print(data)
							print("*"*30)
							self.__evento.set()
							if (self.__senal == 0):
								print(data)
							else:
								print("WARNING [hay mucho ruido]: %s")%self.__senal
						else:
							i = 0
							#data = []

							data["meditacion"]=float(self.__neuroSkyDatos.meditationValue)
						i = i + 1;
						#if k==3*50:
						#	break
						#k=k+1
		else:
			print("No se pudo conectar intente de nuevo...")
			self.__leerDatos.setConectado(False)
		print(data)
	def setDatos(self,datos):
		self.__datos=datos
	def setEvento(self,evento):
		self.__evento=evento


'''
d=RecolectarDatos()
d.setIdLetra(1)
evento=threading.Event()

h=Hilo(evento,d)
h.start()

log=Login()
log.setId(1)

l=CtrlRecolectarDatos(log)
l.setDatos(d)
l.conectarNeuroSky()

print("Fin")
print(d)
'''



'''
bd=BaseDatos()
r=bd.consultaGenerica("SELECT id_usuario FROM usuario WHERE nick='%s' ORDER BY id_usuario DESC LIMIT 0,1"%"a")
#r=bd.consultaGenerica("SELECT COUNT(*) FROM usuario WHERE nick='%s'"%"z")
#r=bd.cuantosHay("usuario","nick","za")
print(r)
'''