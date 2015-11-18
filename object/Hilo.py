# -*- encoding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
import sys, os, threading, time, Queue
sys.path.append("controller")
sys.path.append("view")

from CtrlRecolectarDatos import CtrlRecolectarDatos as Controlador
from RecolectarDatos import RecolectarDatos
from login import Login
from PyQt4 import QtCore, QtGui
from inicio import Ui_inicio
from HiloInterfaz import HiloInterfaz
from aplicacionPrueba import Aplicacion
from prueba import Ui_prueba

class Hilo(threading.Thread):
	def __init__(self,evento,datos,login):  
		threading.Thread.__init__(self)  
		self.__evento=evento
		self.__datos=datos
		self.__login=login
		self.__recolectarDatos=Controlador(self.__login)
		self.__recolectarDatos.setDatos(self.__datos)
		self.__recolectarDatos.setEvento(self.__evento)
	def run(self):
		print("Hilo [run]...")
		self.__recolectarDatos.conectarNeuroSky()
		#print("Iniciando...%s"%self.getName)
		#time.sleep(15)
		#self.__datos.setEstado(True)
		'''
		while True:
			print("Iniciando...%s"%getName)
			#self.__evento.wait()
			time.sleep(15)
			self.__datos.setEstado(True)
		'''
'''
if __name__ == "__main__":
	try:
		d=RecolectarDatos()
		d.setIdLetra(1)
		d.setProbando(False)

		log=Login()
		log.setId(1)

		evento=threading.Event()
		queue = Queue.Queue()

		h=Hilo(evento,d,log)
		h.start()

		prueba=Aplicacion()
		prueba.setDatos(d)
		prueba.setEvento(evento)
		#prueba.start()

		app = QtGui.QApplication(sys.argv)
		inicio = QtGui.QMainWindow()
		ui = Ui_inicio()
		#ui = Ui_prueba()

		d.setInterfaz(ui)

		ui.setLogin(log)
		ui.setDatos(d)
		ui.setEvento(evento)
		ui.setAplicacionPrueba(prueba)
		
		ui.setupUi(inicio)

		inicio.show()
		sys.exit(app.exec_())
		
		

		#l=CtrlRecolectarDatos(log)
		#l.setDatos(d)
		#l.conectarNeuroSky()

		print("Fin")
		print(d)
	except KeyboardInterrupt:
		sys.exit(0)
'''
#cd Documentos/FACULTAD\ 7mo\ SEMESTRE/PROYECTO\ LEER\ CON\ LA\ MENTE/Python/object