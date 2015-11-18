# -*- encoding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
import sys, os,threading, time
sys.path.append("../view")
from inicio import Ui_inicio

from PyQt4 import QtCore, QtGui




class HiloInterfaz(threading.Thread):
	def __init__(self,evento,datos,login,inicio):  
		threading.Thread.__init__(self)  
		self.__evento=evento
		self.__datos=datos
		self.__login=login
		self.__interfaz=None
		self.__inicio=inicio
	def run(self):
		print "HiloInterfaz [run]..."
