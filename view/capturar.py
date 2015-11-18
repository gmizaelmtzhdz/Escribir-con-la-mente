# -*- coding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
# Form implementation generated from reading ui file 'capturar.ui'
#
# Created: Tue Sep 29 17:56:50 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys, os,threading,time
sys.path.append("../controller")
sys.path.append("../model")
sys.path.append("../object")

from baseDatos import BaseDatos
from RecolectarDatos import RecolectarDatos
from login import Login

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

class Ui_capturar(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui_capturar, self).__init__(parent)

        self.login=None
        self.datos=None
        self.root=None
        self.evento=None

        self.bd=BaseDatos()

        self.letras={}
        self.letras= self.bd.obtenerLetras()
        self.letrasAuxiliar = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        self.index=0
        print self.letras
        #print self.letras["\xf1"]
        #print self.letras["a"]
    def setupUi(self, Form):
        self.root=Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(654, 466)

        screen = QtGui.QDesktopWidget().screenGeometry()
        mysize = Form.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        Form.move(hpos, vpos)

        self.label = QtGui.QLabel(Form)
        #self.label.setGeometry(QtCore.QRect(150, 10, 351, 321))
        self.label.setGeometry(QtCore.QRect(150, 10, 400, 351))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(360)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 390, 161, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 390, 161, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.setVisible(False)
        self.pushButton.clicked.connect(self.iniciarCapturarRecoleccion)

        self.pushButton_2.clicked.connect(self.capturar)
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "c:", None))
        self.pushButton.setText(_translate("Form", "INICIAR RECOLECCION", None))
        self.pushButton_2.setText(_translate("Form", "CAPTURAR", None))

    def iniciarCapturarRecoleccion(self):
        font = QtGui.QFont()
        font.setPointSize(360)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(True)
        self.index=0
        self.label.setText(self.letrasAuxiliar[self.index].upper().decode("utf-8"))
        #self.index=self.index + 1

    def capturar(self):
        self.intercambiarLetra()
    def intercambiarLetra(self):
        if self.index < len(self.letras):
            if self.letrasAuxiliar[self.index]=='ñ':
                self.datos.setIdLetra(self.letras["\xf1"])
                print "Index: %s, Id: %s,Letra: ñ"%(str(self.index),str(self.letras["\xf1"]))
            else:
                print "Index: %s, Id: %s,Letra: %s"%(str(self.index),str(self.letras[self.letrasAuxiliar[self.index]]),self.letrasAuxiliar[self.index])
                self.datos.setIdLetra(self.letras[self.letrasAuxiliar[self.index]])
            if self.index!=len(self.letras)-1: 
                self.label.setText(self.letrasAuxiliar[self.index+1].upper().decode("utf-8"))
            else:
                self.finCapturarDatos()
            print "Id letra Datos: %s"%self.datos.getIdLetra()
            self.index=self.index + 1
            self.datos.setEstado(True)
        else:
            self.finCapturarDatos()
    def finCapturarDatos(self):
        font = QtGui.QFont()
        font.setPointSize(150)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("FIN")
        self.pushButton_2.setText("Datos Capturados")
        self.reiniciarCaptura()
    def reiniciarCaptura(self):
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(False)
    def setLogin(self,login):
        self.login=login
    def setDatos(self,datos):
        self.datos=datos
    def setEvento(self,evento):
        self.evento=evento
'''
if __name__ == "__main__":
    import sys
    d=RecolectarDatos()
    d.setIdLetra(1)

    log=Login()
    log.setId(1)

    evento=threading.Event()


    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_capturar()

    ui.setLogin(log)
    ui.setDatos(d)
    ui.setEvento(evento)

    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

'''