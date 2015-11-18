# -*- coding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
# Form implementation generated from reading ui file 'inicio.ui'
#
# Created: Mon Sep 28 17:30:46 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys, os,threading,time
sys.path.append("../controller")
sys.path.append("../object")
from login import Login
from CtrlLogin import CtrlLogin
from aplication import Ui_frm_app
from RecolectarDatos import RecolectarDatos


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

class Ui_inicio(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui_inicio, self).__init__(parent)

        self.login=None
        self.datos=None
        self.root=None
        self.evento=None
        self.aplicacionPrueba=None

    def setupUi(self, inicio):
        self.root=inicio

        inicio.setObjectName(_fromUtf8("inicio"))
        inicio.resize(723, 480)

        screen = QtGui.QDesktopWidget().screenGeometry()
        mysize = inicio.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        inicio.move(hpos, vpos)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/casco-icono-4886-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inicio.setWindowIcon(icon)
        
        self.centralWidget = QtGui.QWidget(inicio)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(390, 60, 331, 301))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/icono2.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.lbl_usr = QtGui.QLabel(self.centralWidget)
        self.lbl_usr.setGeometry(QtCore.QRect(10, 160, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_usr.setFont(font)
        self.lbl_usr.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.lbl_usr.setObjectName(_fromUtf8("lbl_usr"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        
        self.ln_user = QtGui.QLineEdit(self.centralWidget)
        self.ln_user.setGeometry(QtCore.QRect(200, 160, 181, 31))
        self.ln_user.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ln_user.setObjectName(_fromUtf8("ln_user"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 310, 101, 81))
        #self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/boton1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(600,600))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(140, 400, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        inicio.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(inicio)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 723, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        inicio.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(inicio)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        inicio.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(inicio)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        inicio.setStatusBar(self.statusBar)

        self.retranslateUi(inicio)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), inicio.abrirPrincipal)
        QtCore.QMetaObject.connectSlotsByName(inicio)

        self.pushButton.clicked.connect(self.ingresar)

    def retranslateUi(self, inicio):
        inicio.setWindowTitle(_translate("inicio", "RedesNeuronales-Inicio", None))
        self.lbl_usr.setText(_translate("inicio", "Usuario:", None))
       
        self.label_3.setText(_translate("inicio", "INICIAR", None))

    def ingresar(self):
        #self.datos.setEstado(True)
        self.login.setUsuario(self.ln_user.text())
        ctrl=CtrlLogin(self.login)
        resultado=ctrl.autenticarse(self.login.getUsuario(),self.login.getContrasena())
        
        print resultado
        print "Id usuario: %s"%str(self.login.getId())

        if resultado:
            print "Abriendo [Bienvenida(aplication.py)]..."
            inicio = QtGui.QMainWindow()
            self.root.setVisible(False)
            a=Ui_frm_app()
            
            a.setLogin(self.login)
            a.setDatos(self.datos)
            a.setEvento(self.evento)
            a.setAplicacionPrueba(self.aplicacionPrueba)

            a.setupUi(inicio)

            inicio.show()

            self.centralWidget = QtGui.QStackedWidget()
            self.root.setCentralWidget(self.centralWidget)
            self.centralWidget.addWidget(a)
        
            self.root.setCentralWidget(a)
            
            
    def registrarse(self):
        self.login.setUsuario(self.ln_user.text())
      
        ctrl=CtrlLogin(self.login)
        resultado=ctrl.autenticarse(self.login.getUsuario())

        print resultado
        print self.login.getId()

        if resultado:
            pass
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

    d=RecolectarDatos()
    d.setIdLetra(1)

    log=Login()
    log.setId(1)

    evento=threading.Event()


    app = QtGui.QApplication(sys.argv)
    inicio = QtGui.QMainWindow()
    ui = Ui_inicio()
    
    ui.setLogin(log)
    ui.setDatos(d)
    ui.setEvento(evento)
    
    ui.setupUi(inicio)
    inicio.show()
    sys.exit(app.exec_())

'''
