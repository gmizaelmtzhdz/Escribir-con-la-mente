# -*- encoding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
import os,sys
sys.path.append("../model")
from baseDatos import BaseDatos
class EscribirArchivo:
	def __init__(self):
		self.__path="../files/"

		self.__numero_pruebas=0
		self.__numero_entradas=0
		self.__numero_salidas=0
		self.__string=""
		self.__bd=BaseDatos()
		self.__archivo=None
		self.__url=""
		
	def prepararDatos(self):
		registros=self.__bd.obtenerRegistrosOndas()
		self.__numero_pruebas=len(registros)
		auxiliar=""
		#print "LOngitud: %s"%str(len(registros))
		#return;
		contador=0;
		for i in registros:
			#print contador
			if contador==len(registros)-1:
				#print "ultimo"
				auxiliar = auxiliar + "%s %s %s %s %s %s %s %s\n%s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
			else:
				auxiliar = auxiliar + "%s %s %s %s %s %s %s %s\n%s\n"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
			contador=contador+1
		print "Longitud de registros: %s"%str(len(registros))
		self.__string="%s %s %s\n%s"%(self.__numero_pruebas,self.__numero_entradas,self.__numero_salidas,auxiliar)
	def prepararDatosNormalizados(self):
		registros=self.__bd.obtenerRegistrosOndasNormalizados()
		self.__numero_pruebas=len(registros)
		auxiliar=""
		#print "LOngitud: %s"%str(len(registros))
		#return;
		contador=0;
		for i in registros:
			#print contador
			if contador==len(registros)-1:
				#print "ultimo"
				#bin(int(i[8]))[2:].zfill(5)
				#bin(int(i))[2:].zfill(5)
				auxiliar = auxiliar + "%s %s %s %s %s %s %s %s\n%s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]," ".join(bin(int(i[8]))[2:].zfill(5)))
			else:
				auxiliar = auxiliar + "%s %s %s %s %s %s %s %s\n%s\n"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]," ".join(bin(int(i[8]))[2:].zfill(5)))
			contador=contador+1
		print "Longitud de registros: %s"%str(len(registros))
		self.__string="%s %s %s\n%s"%(self.__numero_pruebas,self.__numero_entradas,self.__numero_salidas,auxiliar)
	def prepararDatosParaProbarRedNeuronal(self):
		registros=self.__bd.obtenerRegistrosOndasPruebaDeLaRedNeuronal()
		self.__numero_pruebas=len(registros)
		auxiliar=""
		#print "LOngitud: %s"%str(len(registros))
		#return;
		contador=0;
		for i in registros:
			#print contador
			if contador==len(registros)-1:
				#print "ultimo"
				auxiliar = auxiliar + "%s %s %s %s %s %s %s %s\n%s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
			else:
				auxiliar = auxiliar + "%s %s %s %s %s %s %s %s\n%s\n"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
			contador=contador+1
		print "Longitud de registros: %s"%str(len(registros))
		self.__string="%s %s %s\n%s"%(self.__numero_pruebas,self.__numero_entradas,self.__numero_salidas,auxiliar)
	def prepararDatosParaProbarRedNeuronalNormalizados(self):
		registros=self.__bd.obtenerRegistrosOndasPruebaDeLaRedNeuronalNormalizados()
		self.__numero_pruebas=len(registros)
		auxiliar=""
		#print "LOngitud: %s"%str(len(registros))
		#return;
		contador=0;
		for i in registros:
			#print contador
			if contador==len(registros)-1:
				#print "ultimo"
				auxiliar = auxiliar + "%s %s %s %s %s %s %s %s\n%s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]," ".join(bin(int(i[8]))[2:].zfill(5)))
			else:
				auxiliar = auxiliar + "%s %s %s %s %s %s %s %s\n%s\n"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]," ".join(bin(int(i[8]))[2:].zfill(5)))
			contador=contador+1
		print "Longitud de registros: %s"%str(len(registros))
		self.__string="%s %s %s\n%s"%(self.__numero_pruebas,self.__numero_entradas,self.__numero_salidas,auxiliar)
	def prepararDatosParaProbarRedNeuronalGamma(self):
		registros=self.__bd.obtenerRegistrosOndasPruebaDeLaRedNeuronalGamma()
		self.__numero_pruebas=len(registros)
		auxiliar=""
		#print "LOngitud: %s"%str(len(registros))
		#return;
		contador=0;
		for i in registros:
			#print contador
			if contador==len(registros)-1:
				#print "ultimo"
				auxiliar = auxiliar + "%s %s\n%s"%(i[0],i[1],i[2])
			else:
				auxiliar = auxiliar + "%s %s\n%s\n"%(i[0],i[1],i[2])
			contador=contador+1
		print "Longitud de registros: %s"%str(len(registros))
		self.__string="%s %s %s\n%s"%(self.__numero_pruebas,self.__numero_entradas,self.__numero_salidas,auxiliar)
	def prepararDatosGamma(self):
		print "DATOS [GAMMA]..."
		registros=self.__bd.obtenerRegistrosOndasGamma()
		self.__numero_pruebas=len(registros)
		auxiliar=""
		#print registros;
		print "LOngitud: %s"%str(len(registros))
		#return;
		contador=0;
		for i in registros:
			#print i
			#print contador
			if contador==len(registros)-1:
				#print "ultimo"  
				auxiliar = auxiliar + "%s %s\n%s"%(i[0],i[1],i[2])
			else:
				auxiliar = auxiliar + "%s %s\n%s\n"%(i[0],i[1],i[2])
			contador=contador+1
		print "Longitud de registros: %s"%str(len(registros))
		self.__string="%s %s %s\n%s"%(self.__numero_pruebas,self.__numero_entradas,self.__numero_salidas,auxiliar)
		#print self.__string;
	def prepararDatosGammaNormalizado(self):
		print "DATOS [GAMMA]..."
		registros=self.__bd.obtenerRegistrosOndasGammaNormalizado()
		self.__numero_pruebas=len(registros)
		auxiliar=""
		#print registros;
		print "LOngitud: %s"%str(len(registros))
		#return;
		contador=0;
		for i in registros:
			#print i
			#print contador
			if contador==len(registros)-1:
				#print "ultimo"  
				auxiliar = auxiliar + "%s %s\n%s"%(i[0],i[1],i[2])
			else:
				auxiliar = auxiliar + "%s %s\n%s\n"%(i[0],i[1],i[2])
			contador=contador+1
		print "Longitud de registros: %s"%str(len(registros))
		self.__string="%s %s %s\n%s"%(self.__numero_pruebas,self.__numero_entradas,self.__numero_salidas,auxiliar)
		#print self.__string;

	def escribirEnArchivo(self):
		self.prepararDatos()
		self.__archivo=open( self.__path+self.__url,"w")
		self.__archivo.write(self.__string)
		self.__archivo.close()
	def escribirEnArchivoNormalizado(self):
		self.prepararDatosNormalizados()
		self.__archivo=open( self.__path+self.__url,"w")
		self.__archivo.write(self.__string)
		self.__archivo.close()
	def escribirEnArchivoParaProbarRedNeuronal(self):
		self.prepararDatosParaProbarRedNeuronal()
		self.__archivo=open( self.__path+self.__url,"w")
		self.__archivo.write(self.__string)
		self.__archivo.close()
	def escribirEnArchivoParaProbarRedNeuronalNormalizados(self):
		self.prepararDatosParaProbarRedNeuronalNormalizados()
		self.__archivo=open( self.__path+self.__url,"w")
		self.__archivo.write(self.__string)
		self.__archivo.close()
	def escribirEnArchivoParaProbarRedNeuronalGamma(self):
		self.prepararDatosParaProbarRedNeuronalGamma()
		self.__archivo=open( self.__path+self.__url,"w")
		self.__archivo.write(self.__string)
		self.__archivo.close()
	def escribirEnArchivoGamma(self):
		self.prepararDatosGamma()
		self.__archivo=open( self.__path+self.__url,"w")
		self.__archivo.write(self.__string)
		self.__archivo.close()
	def escribirEnArchivoGammaNormalizado(self):
		self.prepararDatosGammaNormalizado()
		self.__archivo=open( self.__path+self.__url,"w")
		self.__archivo.write(self.__string)
		self.__archivo.close()
	def setNumeroPruebas(self,numero_pruebas):
		self.__numero_pruebas=numero_pruebas
	def setNumeroEntradas(self,numero_entradas):
		self.__numero_entradas=numero_entradas
	def setNumeroSalidas(self,numero_salidas):
		self.__numero_salidas=numero_salidas
	def setUrl(self,url):
		self.__url=url

	def getNumeroPruebas(self):
		return self.__numero_pruebas
	def getNumeroEntradas(self):
		return self.__numero_entradas
	def getNumeroSalidas(self):
		return self.__numero_salidas
	def getUrl(self):
		return self.__url
'''
e=EscribirArchivo()
e.setUrl("rna.data")
e.setNumeroEntradas(8)
e.setNumeroSalidas(1)
e.escribirEnArchivo()
'''
'''
g=EscribirArchivo();
g.setUrl("rna_gamma.data");
g.setNumeroEntradas(2)
g.setNumeroSalidas(1)
g.escribirEnArchivoGamma()

n=EscribirArchivo()
n.setUrl("rna_normalizado.data")
n.setNumeroEntradas(8)
n.setNumeroSalidas(5)
n.escribirEnArchivoNormalizado()

np=EscribirArchivo()
np.setUrl("prueba_normalizado.data")
np.setNumeroEntradas(8)
np.setNumeroSalidas(1)
np.escribirEnArchivoParaProbarRedNeuronalNormalizados()

gn=EscribirArchivo();
gn.setUrl("rna_gamma_normalizado.data");
gn.setNumeroEntradas(2)
gn.setNumeroSalidas(1)
gn.escribirEnArchivoGammaNormalizado()
'''

