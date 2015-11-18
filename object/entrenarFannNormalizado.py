# -*- encoding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
from pyfann import libfann
from login import Login
from escribirArchivo import EscribirArchivo
import inspect, sys, os
sys.path.append("../model")
from baseDatos import BaseDatos

class CtrlEntrenarRNANormalizado:
	def __init__(self):
		self.__coneccion=1
		self.__tasa_aprendizaje=0.7
		self.__numero_entradas=0
		self.__numero_salidas=0
		self.__neuronas_capa_oculta=0
		self.__error_deseado=0
		self.__epocas=0
		self.__iteraciones_entre_reporte=1000
		self.__red=None

		self.__error_real=0
		self.__url_prueba=None
		self.__url_guardar=None
		
		self.__path="../files/"
		#self.__path="files/"

		self.__bd=BaseDatos()
		self.__interfaz=None
	def entrenar(self):
		print("Entrenando ...")		
		self.__red=libfann.neural_net()
		self.__red.create_sparse_array(self.__coneccion,(self.__numero_entradas,self.__neuronas_capa_oculta,self.__numero_salidas))
		self.__red.set_learning_rate(self.__tasa_aprendizaje)
		self.__red.set_activation_function_hidden(libfann.SIGMOID_SYMMETRIC_STEPWISE)
		self.__red.set_activation_function_output(libfann.SIGMOID_SYMMETRIC_STEPWISE)
		self.__red.train_on_file(self.__path+self.__url_prueba, self.__epocas,self.__iteraciones_entre_reporte, self.__error_deseado)
		self.__error_real=self.__red.get_MSE()
		
		datos={"numerodeneuronas":self.__neuronas_capa_oculta,"error":self.__error_real,"tipo":"normalizado"}
		id=self.__bd.agregarEntrenamiento(datos)
		
		print("id: %s"%(str(id)))
		self.__url_guardar="mizael_rna%s.net"%(id)
		self.__bd.actualizarRegistroEntrenamiento(self.__url_guardar,id)
		self.__red.save(self.__path + self.__url_guardar)
		if self.__interfaz != None:
			self.__interfaz.lineEdit_4.setText("%s"%str(self.__error_real))
	def entrenarGamma(self):
		print("Entrenando Gamma...")		
		self.__red=libfann.neural_net()
		self.__red.create_sparse_array(self.__coneccion,(self.__numero_entradas,self.__neuronas_capa_oculta,self.__numero_salidas))
		self.__red.set_learning_rate(self.__tasa_aprendizaje)
		self.__red.set_activation_function_hidden(libfann.SIGMOID_SYMMETRIC_STEPWISE)
		self.__red.set_activation_function_output(libfann.LINEAR)
		self.__red.train_on_file(self.__path+self.__url_prueba, self.__epocas,self.__iteraciones_entre_reporte, self.__error_deseado)
		self.__error_real=self.__red.get_MSE()
		
		datos={"numerodeneuronas":self.__neuronas_capa_oculta,"error":self.__error_real,"tipo":"gamma"}
		id=self.__bd.agregarEntrenamiento(datos)
		
		print("id: %s"%(str(id)))
		self.__url_guardar="mizael_rna%s.net"%(id)
		self.__bd.actualizarRegistroEntrenamiento(self.__url_guardar,id)
		self.__red.save(self.__path + self.__url_guardar)
		if self.__interfaz != None:
			self.__interfaz.lineEdit_4.setText("%s"%str(self.__error_real))

	def setConeccion(self,conexion):
		self.__coneccion=conexion
	def setTasaAprendizaje(self,tasa_aprendizaje):
		self.__tasa_aprendizaje=tasa_aprendizaje
	def setNumeroEntradas(self,numero_entradas):
		self.__numero_entradas=numero_entradas
	def setNumeroSalidas(self,numero_salidas):
		self.__numero_salidas=numero_salidas
	def setNeuronasCapaOculta(self,neuronas_capa_oculta):
		self.__neuronas_capa_oculta=neuronas_capa_oculta
	def setErrorDeseado(self,error_deseado):
		self.__error_deseado=error_deseado
	def setEpocas(self,epocas):
		self.__epocas=epocas
	def setIteracionesEntreReporte(self,iteraciones_entre_reporte):
		self.__iteraciones_entre_reporte=iteraciones_entre_reporte
	def setErrorReal(self,error_real):
		self.__error_real=error_real
	def setUrlPrueba(self,url_prueba):
		self.__url_prueba=url_prueba
	def setUrlGuardar(self,url_guardar):
		self.__url_guardar=url_guardar
	def setInterfaz(self,interfaz):
		self.__interfaz=interfaz


	def getConeccion(self):
		return self.__coneccion
	def getTasaAprendizaje(self):
		return self.__tasa_aprendizaje
	def getNumeroEntradas(self):
		return self.__numero_entradas
	def getNumeroSalidas(self):
		return self.__numero_salidas
	def getNeuronasCapaOculta(self):
		return self.__neuronas_capa_oculta
	def getErrorDeseado(self):
		return self.__error_deseado
	def getEpocas(self):
		return self.__epocas
	def getIteracionesEntreReporte(self):
		return self.__iteraciones_entre_reporte
	def getErrorReal(self):
		return self.__error_real
	def getUrlPrueba(self):
		return self.__url_prueba
	def getUrlGuardar(self):
		return self.__url_guardar
	def getInterfaz(self):
		return self.__interfaz

'''

#Entrenar para todos los valores
o=CtrlEntrenarRNANormalizado()
o.setConeccion(1)
o.setTasaAprendizaje(0.7)
o.setNumeroEntradas(8)
o.setNumeroSalidas(5)
#Cambian el # de neuronas y error deseado
o.setNeuronasCapaOculta(15)
o.setErrorDeseado(0.001)
#Cambian el # de epocas
o.setEpocas(130000)
o.setIteracionesEntreReporte(10000)
o.setUrlPrueba("rna_normalizado.data")
o.entrenar()
'''
'''
#Entrenar para las Gamma 
g=CtrlEntrenarRNANormalizado()
g.setConeccion(1)
g.setTasaAprendizaje(0.7)
g.setNumeroEntradas(2)
g.setNumeroSalidas(1)
#Cambian el # de neuronas y error deseado
g.setNeuronasCapaOculta(150)
g.setErrorDeseado(0.9)
#Cambian el # de epocas
g.setEpocas(30000)
g.setIteracionesEntreReporte(10000)
g.setUrlPrueba("rna_gamma_normalizado.data")
g.entrenarGamma()
'''