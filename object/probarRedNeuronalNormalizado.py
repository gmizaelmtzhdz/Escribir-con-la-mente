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

auxiliar=[]



np=EscribirArchivo()
np.setUrl("prueba_normalizado.data")
np.setNumeroEntradas(8)
np.setNumeroSalidas(5)
np.escribirEnArchivoParaProbarRedNeuronalNormalizados()

bd=BaseDatos()
#primer elemento: # de neuronas
#segundo elemento: error
#tercer elemento: url del archivo de ese entrenamiento
print bd.obtenerErroresMenoresDeEntrenamientoNormalizado()[0][2]


errores=bd.obtenerErroresMenoresDeEntrenamientoNormalizado()
for k in range(len(errores)):
	ann = libfann.neural_net()
	ann.create_from_file("../files/"+errores[k][2])
	ann.reset_MSE()
	
	test_data = libfann.training_data()
	test_data.read_train_from_file("../files/prueba_normalizado.data")
	entradas=test_data.get_input()
	salidas=test_data.get_output()
	for i in range(0,len(entradas)):
		ann.test(entradas[i], salidas[i])
	auxiliar.append(ann.get_MSE())

print auxiliar
print "%s - %s - %s - %s"%("Neuronas".rjust(8),"Archivo".rjust(15),"Error Entrenamiento".rjust(16),"Error Prueba")
for z in range(len(errores)):
	print "%s - %s - %s - %s"%(str(errores[z][0]).rjust(8),str(errores[z][2]).rjust(15),str(errores[z][1]).rjust(16),str(auxiliar[z]))
