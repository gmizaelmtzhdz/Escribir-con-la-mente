# -*- encoding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
import sys, os, threading, time, Queue
class HiloProbandoAplicacion(threading.Thread):
	def __init__(self):  
		threading.Thread.__init__(self) 
		self.datos=None
		self.root=None
		self.interfaz=None
	def run(self):
		#self.interfaz.textEdit.setText("Hola mundo")
		self.interfaz.setText("Hola mundo")
	def setDatos(self,datos):
		self.datos=datos
	def setInterfaz(self,interfaz):
		self.interfaz=interfaz