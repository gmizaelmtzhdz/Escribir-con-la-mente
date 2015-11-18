# -*- encoding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
from pyfann import libfann
from login import Login
import inspect, sys, os, math, time
import threading
sys.path.append("../model")
sys.path.append("../object")
from baseDatos import BaseDatos
from RecolectarDatos import RecolectarDatos
from random import randint
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Aplicacion(QtCore.QObject,threading.Thread):
	senal = QtCore.pyqtSignal(str)
	def __init__(self):
		threading.Thread.__init__(self)
		super(Aplicacion, self).__init__()
		self.__bd=BaseDatos()
		#self.__path="../files/"
		self.__path="files/"
		self.__rna=None
		self.__letras=self.__bd.obtenerLetrasValor()
		
		self.__letra_normalizado={"a":"00000","b":"00001","c":"00010","d":"00011","e":"00100","f":"00101","g":"00110","h":"00111","i":"01000","j":"01001","k":"01010","l":"01011","m":"01100","n":"01101","ñ":"01110","o":"01111","p":"10000","q":"10001","r":"10010","s":"10011","t":"10100","u":"10101","v":"10110","w":"10111","x":"11000","y":"11001","z":"11010"}

		self.__string=""
		self.__datos=None
		self.__evento=None
		self.__interfaz=None
		self.__letra=""
	@QtCore.pyqtSlot()
	def activarSenal(self):
		self.senal.emit("%s"%self.__letra)

	def run(self):
		print "Hilo [Probando Aplicacion]"		
		while True:
			if self.__datos.getProbando():
				self.__evento.wait()

				deltaMax=3473322.0
				thetaMax=3072570.0
				lowAlphaMax=809805.0
				highAlphaMax=762007.0
				lowBetaMax=643499.0
				highBetaMax=679478.0
				lowGammaMax=456807.0
				midGammaMax=433577.0

				deltaMin=3.0
				thetaMin=3.0
				lowAlphaMin=0.0
				highAlphaMin=0.0
				lowBetaMin=0.0
				highBetaMin=1.0
				lowGammaMin=1.0
				midGammaMin=1.0
				
				delta=(self.__datos.getDelta() - deltaMin)/(deltaMax - deltaMin)
				theta=(self.__datos.getTheta() - thetaMin)/(thetaMax - thetaMin)
				lowAlpha=(self.__datos.getLowAlpha() - lowAlphaMin)/(lowAlphaMax - lowAlphaMin)
				highAlpha=(self.__datos.getHighAlpha() - highAlphaMin)/(highAlphaMax - highAlphaMin)
				lowBeta=(self.__datos.getLowBeta() - lowBetaMin)/(lowBetaMax - lowBetaMin)
				highBeta=(self.__datos.getHighBeta() - highBetaMin)/(highBetaMax - highBetaMin)
				lowGamma=(self.__datos.getLowGamma() - lowGammaMin)/(lowGammaMax - lowGammaMin)
				midGamma=(self.__datos.getMidGamma() - midGammaMin)/(midGammaMax - midGammaMin)


				ondas=[delta,theta,lowAlpha,highAlpha,lowBeta,highBeta,lowGamma,midGamma]
				
				self.__letra=self.convertirSenalALetra(ondas)
				self.__string=self.__string + self.__letra
				print "*"*10
				print self.__string
				self.__datos.setEstado(True)
				self.activarSenal()
				time.sleep(0.3)
				self.__evento.clear()
			else:
				self.__string=""
				self.__datos.setString(self.__string)
	def convertirSenalALetra(self,datos):
		self.__ruta=self.__bd.obtenerArchivoErrorMinimoNormalizado()
		self.__rna= libfann.neural_net()
		self.__rna.create_from_file(self.__path+self.__ruta)
		resultado = self.__rna.run(datos)
		#print (self.__letras)
		#return
		#print resultado
		#return
		resultado[0]=1 if resultado[0]>0.0505 else 0
		resultado[1]=1 if resultado[1]>0.105 else 0
		resultado[2]=1 if resultado[2]>0.105 else 0
		resultado[3]=1 if resultado[3]>0.115 else 0
		resultado[4]=1 if resultado[4]>0.09 else 0
		resultado=str(resultado[0])+str(resultado[1])+str(resultado[2])+str(resultado[3])+str(resultado[4])
		#resultado="".join(bin(int(14))[2:].zfill(5))
		#print resultado
		#resultado = round(resultado)
		letraCorrecta=''
		auxBool=False
		for letra, valor in self.__letras.items():
			#print "".join(bin(int(valor))[2:].zfill(5))==resultado
			#print valor;
			#if valor==resultado:
			if "".join(bin(int(valor))[2:].zfill(5))==resultado:
				letraCorrecta=letra
				auxBool=True
				break
		if not auxBool:
			random=randint(0,26)
			random="".join(bin(int(random))[2:].zfill(5))
			#print "Random ==>"+str(random)
			for letra, valor in self.__letras.items():
				if "".join(bin(int(valor))[2:].zfill(5))==random:
					letraCorrecta=letra
					break
		return letraCorrecta
	
	def setDatos(self,datos):
		self.__datos=datos
	def setEvento(self,evento):
		self.__evento=evento
	def setInterfaz(self,interfaz):
		self.__interfaz=interfaz
'''
z=Aplicacion()
d=[0.001, 0.0007755, 0.0040491, 0.01403792, 0.003824403, 0.0129511, 0.0050546, 0.0061811]
bd=BaseDatos()
registros=bd.auxiliarOndasNormalizadas()
for i in registros:
	d[0]=i[0]
	d[1]=i[1]
	d[2]=i[2]
	d[3]=i[3]
	d[4]=i[4]
	d[5]=i[5]
	d[6]=i[6]
	d[7]=i[7]
	print z.convertirSenalALetra(d).decode('cp1252'),
'''
#d=[0.0292625007953, 0.0181542013567, 0.0229586134934 ,0.0240286506554, 0.0147226336016, 0.0282643856966 ,0.012574265662, 0.00489879513626]
#d=[0.00104395824282, 0.000775572998083, 0.004049122937 ,0.0140379287854, 0.00382440376753 ,0.0129511374189, 0.00505466215417, 0.00618115393841]
#d=[0.00322083862726 ,0.00518231172827 ,0.00798463827712, 0.00676765436538, 0.00706605604671, 0.00524079549418, 0.00818947211727, 0.00416305330553]
#print z.convertirSenalALetra(d)