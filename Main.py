'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
import sys, os, threading, time, Queue
sys.path.append("controller")
sys.path.append("view")
sys.path.append("object")

from RecolectarDatos import RecolectarDatos
from login import Login
from inicio import Ui_inicio
from aplicacionPrueba import Aplicacion
from Hilo import Hilo
from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
	try:
		d=RecolectarDatos()
		d.setIdLetra(1)
		d.setProbando(False)

		log=Login()
		#log.setId(0)

		evento=threading.Event()
		queue = Queue.Queue()

		h=Hilo(evento,d,log)
		h.start()

		prueba=Aplicacion()
		prueba.setDatos(d)
		prueba.setEvento(evento)

		app = QtGui.QApplication(sys.argv)
		inicio = QtGui.QMainWindow()
		ui = Ui_inicio()

		ui.setLogin(log)
		ui.setDatos(d)
		ui.setEvento(evento)
		ui.setAplicacionPrueba(prueba)
		
		ui.setupUi(inicio)

		inicio.show()
		sys.exit(app.exec_())

	except KeyboardInterrupt:
		sys.exit(0)