# -*- coding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
# Form implementation generated from reading ui file 'aplication.ui'
#
# Created: Tue Sep 29 16:28:19 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys, os,threading,time
sys.path.append("../object")

from PyQt4 import QtCore, QtGui
from entrenamiento import Ui_Entrenamiento
from capturar import Ui_capturar
from prueba import Ui_prueba

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

class Ui_frm_app(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui_frm_app, self).__init__(parent)
        self.login=None
        self.datos=None
        self.root=None
        self.evento=None
        self.aplicacionPrueba=None

    def setupUi(self, frm_app):
        self.root=frm_app
        frm_app.setObjectName(_fromUtf8("frm_app"))
        frm_app.resize(631, 437)

        screen = QtGui.QDesktopWidget().screenGeometry()
        mysize = frm_app.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        frm_app.move(hpos, vpos)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/casco-icono-4886-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_app.setWindowIcon(icon)
        
        self.lbl_usr = QtGui.QLabel(frm_app)
        self.lbl_usr.setGeometry(QtCore.QRect(100, 20, 421, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_usr.setFont(font)
        self.lbl_usr.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.lbl_usr.setObjectName(_fromUtf8("lbl_usr"))
        self.lbl_usr_2 = QtGui.QLabel(frm_app)
        self.lbl_usr_2.setGeometry(QtCore.QRect(230, 320, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_usr_2.setFont(font)
        self.lbl_usr_2.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.lbl_usr_2.setObjectName(_fromUtf8("lbl_usr_2"))
        self.lbl_usr_3 = QtGui.QLabel(frm_app)
        self.lbl_usr_3.setGeometry(QtCore.QRect(470, 320, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_usr_3.setFont(font)
        self.lbl_usr_3.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.lbl_usr_3.setObjectName(_fromUtf8("lbl_usr_3"))


	'''self.lbl_usr_5 = QtGui.QLabel(frm_app)
        self.lbl_usr_5.setGeometry(QtCore.QRect(656, 320, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_usr_5.setFont(font)
        self.lbl_usr_5.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.lbl_usr_5.setObjectName(_fromUtf8("lbl_usr_5"))'''


	''' boton de entrenar'''
        self.pushButton = QtGui.QPushButton(frm_app)
        self.pushButton.setGeometry(QtCore.QRect(280, 110, 71, 191))
        #self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/Recolectardatos.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(600, 600))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
	'''boton de Inicar'''
        self.pushButton_2 = QtGui.QPushButton(frm_app)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 110, 81, 191))
        #self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.pushButton_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/Entrenar1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(600, 600))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

	'''boton de Inicar
        self.pushButton_4 = QtGui.QPushButton(frm_app)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 110, 81, 191))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.pushButton_4.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/cerebrooo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(400, 200))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))'''

        self.lbl_usr_4 = QtGui.QLabel(frm_app)
        self.lbl_usr_4.setGeometry(QtCore.QRect(70, 320, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_usr_4.setFont(font)
        self.lbl_usr_4.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.lbl_usr_4.setObjectName(_fromUtf8("lbl_usr_4"))
	''' boton de recolectar datos '''
	icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/Entrenar2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3 = QtGui.QPushButton(frm_app)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 110, 71, 191))
        #self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(600, 600))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(frm_app)
        QtCore.QMetaObject.connectSlotsByName(frm_app)

        self.pushButton_2.clicked.connect(self.lanzarAplicacion)
        self.pushButton.clicked.connect(self.lanzarRecolectarDatos)
        self.pushButton_3.clicked.connect(self.lanzarEntrenar)
	#self.pushButton_4.clicked.connect(self.lanzarCerrar)

    def retranslateUi(self, frm_app):
        frm_app.setWindowTitle(_translate("frm_app", "Aplicaciones", None))
        self.lbl_usr.setText(_translate("frm_app", "<html><head/><body><center><p align=\"center\">Seleccione una Opcion</p></center></body></html>", None))

        self.lbl_usr_2.setText(_translate("frm_app", "Recolectar Datos", None))
        self.lbl_usr_3.setText(_translate("frm_app", "Iniciar RNA", None))
        self.lbl_usr_4.setText(_translate("frm_app", "Entrenar RNA", None))
	#self.lbl_usr_5.setText(_translate("frm_app", "Cerrar sesion", None))

    def lanzarEntrenar(self):
        print "Abriendo [Entrenar]..."
        inicio = QtGui.QMainWindow()
        self.root.setVisible(False)
        a=Ui_Entrenamiento()

        a.setLogin(self.login)
        a.setDatos(self.datos)
        a.setEvento(self.evento)

        a.setupUi(inicio)
        inicio.show()
        self.centralWidget = QtGui.QStackedWidget()
        self.centralWidget.addWidget(a)


    '''def lanzarCerrar(self):
        print "Cerrando [Sesion]..."
        inicio = QtGui.QMainWindow()
        self.root.setVisible(False)
        a=Ui_inicio()

        a.setLogin(self.login)
        a.setDatos(self.datos)
        a.setEvento(self.evento)

        a.setupUi(inicio)
        inicio.show()
        self.centralWidget = QtGui.QStackedWidget()
        self.centralWidget.addWidget(a)'''


    def lanzarRecolectarDatos(self):
        print "Abriendo [Recolectar Datos]..."
        inicio = QtGui.QMainWindow()
        self.root.setVisible(False)
        a=Ui_capturar()
        
        print self.login.getId()

        a.setLogin(self.login)
        a.setDatos(self.datos)
        a.setEvento(self.evento)

        a.setupUi(inicio)
        inicio.show()
        self.centralWidget = QtGui.QStackedWidget()
        self.centralWidget.addWidget(a)

    def lanzarAplicacion(self):
        print "Abriendo [Aplicacion] (Probar RNA)..."
        inicio = QtGui.QMainWindow()
        self.root.setVisible(False)
        a=Ui_prueba()

        a.setLogin(self.login)
        a.setDatos(self.datos)
        a.setEvento(self.evento)

        self.aplicacionPrueba.senal.connect(a.recibirSenal)
        self.aplicacionPrueba.start()

        a.setupUi(inicio)
        inicio.show()
        self.centralWidget = QtGui.QStackedWidget()
        self.centralWidget.addWidget(a)
    

    def setLogin(self,login):
        self.login=login
    def setDatos(self,datos):
        self.datos=datos
    def setEvento(self,evento):
        self.evento=evento
    def setAplicacionPrueba(self,aplicacionPrueba):
        self.aplicacionPrueba=aplicacionPrueba
#import imagenes_rc
'''
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frm_app = QtGui.QWidget()
    ui = Ui_frm_app()
    ui.setupUi(frm_app)
    frm_app.show()
    sys.exit(app.exec_())

'''
