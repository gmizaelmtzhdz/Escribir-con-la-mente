# -*- coding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
# Form implementation generated from reading ui file 'prueba.ui'
#
# Created: Tue Sep 29 18:19:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys, os, threading, time
sys.path.append("../object")
from RecolectarDatos import RecolectarDatos
from aplicacionPrueba import Aplicacion
from HiloProbandoAplicacion import HiloProbandoAplicacion
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

class Ui_prueba(QtGui.QWidget):
    #senal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(Ui_prueba, self).__init__(parent)
        
        self.login=None
        self.datos=None
        self.root=None
        self.evento=None
        self.string=""
    @QtCore.pyqtSlot(str)
    def recibirSenal(self, message):
        self.string=self.string+message
        self.textEdit.setText(self.string)
        self.raise_()

    def setupUi(self, Form):
        #self.datos.setInterfaz(self)

        self.root=Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(625, 501)
        screen = QtGui.QDesktopWidget().screenGeometry()
        mysize = Form.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        Form.move(hpos, vpos)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 181, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 581, 361))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 40, 181, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))


        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 40, 181, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton.clicked.connect(self.escribir)
        self.pushButton_2.clicked.connect(self.detener)
        self.pushButton_3.clicked.connect(self.limpiar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Escribir", None))
        self.pushButton_2.setText(_translate("Form", "Detener", None))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_3.setText(_translate("Form", "Limpiar", None))
    
    def setLogin(self,login):
        self.login=login
    def setDatos(self,datos):
        self.datos=datos
    def setEvento(self,evento):
        self.evento=evento

    def escribir(self):
        print "Escribir..."
        self.datos.setEstado(True)
        self.datos.setProbando(True)
        
    def detener(self):
        #self.textEdit.setText("")
        self.datos.setEstado(False)
        self.datos.setProbando(False)
    def limpiar(self):
        self.string=""
        self.textEdit.setText(self.string)


'''
if __name__ == "__main__":
    import sys
    d=RecolectarDatos()
    d.setIdLetra(1)
    d.setString("Hola mundo")

    log=Login()
    log.setId(1)

    evento=threading.Event()

    ap=Aplicacion()


    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_prueba()

    evento.set()

    ui.setLogin(log)
    ui.setDatos(d)
    ui.setEvento(evento)
    ui.setupUi(Form)
    ap.senal.connect(ui.recibirSenal)
    ap.start()
    #ui.auxiliar()
    Form.show()
    #ui.auxiliar()
    sys.exit(app.exec_())
    #ui.auxiliar()
'''


