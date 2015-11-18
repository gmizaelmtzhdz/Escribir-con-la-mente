# -*- coding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
# Form implementation generated from reading ui file 'entrenamiento.ui'
#
# Created: Tue Sep 29 16:48:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys, os,threading,time
sys.path.append("../object")
from entrenarFann import CtrlEntrenarRNA

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

class Ui_Entrenamiento(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui_Entrenamiento, self).__init__(parent)
        self.login=None
        self.datos=None
        self.root=None
        self.evento=None
    def setupUi(self, Entrenamiento):
        self.root=Entrenamiento

        Entrenamiento.setObjectName(_fromUtf8("Entrenamiento"))
        Entrenamiento.resize(800, 483)

        screen = QtGui.QDesktopWidget().screenGeometry()
        mysize = Entrenamiento.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        Entrenamiento.move(hpos, vpos)

        Entrenamiento.setMaximumSize(QtCore.QSize(16777215, 1577215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/1440681999_head-atom_64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Entrenamiento.setWindowIcon(icon)
        #Entrenamiento.setStyleSheet(_fromUtf8("background-image: url(images/666.png);"))
        self.centralwidget = QtGui.QWidget(Entrenamiento)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 60, 171, 21))
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n" #esta
"font: 75 italic 12pt \"Tahoma\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 50, 161, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 171, 31))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n" #esta
"font: 75 italic 12pt \"Tahoma\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 90, 161, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 130, 101, 31))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n" #esta
"font: 75 italic 12pt \"Tahoma\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 130, 161, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 260, 161, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 270, 81, 16))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n"#esta
"font: 75 italic 12pt \"Tahoma\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 370, 181, 41))
        self.pushButton.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Tahoma\";\n" #boton

"color: rgb(0, 85, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))


	self.pushButton1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(190, 370, 181, 41))
        self.pushButton1.setStyleSheet(_fromUtf8("font: 75 italic 12pt \"Tahoma\";\n" #boton2

"color: rgb(0, 85, 255);"))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))



        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 170, 171, 31))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n" #esta
"font: 75 italic 12pt \"Tahoma\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 170, 161, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(500, 210, 161, 31))
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 220, 171, 20))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n" #Esta
"font: 75 italic 12pt \"Tahoma\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        Entrenamiento.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Entrenamiento)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Entrenamiento.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Entrenamiento)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Entrenamiento.setStatusBar(self.statusbar)
        self.retranslateUi(Entrenamiento)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.copy)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.copy)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.copy)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_5.copy)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_6.copy)
        QtCore.QMetaObject.connectSlotsByName(Entrenamiento)
	
	self.pushButton1.clicked.connect(self.lanzarAplicacion)
        self.pushButton.clicked.connect(self.entrenar)
    def retranslateUi(self, Entrenamiento):
        Entrenamiento.setWindowTitle(_translate("Entrenamiento", "Entrenamiento", None))
        self.label.setText(_translate("Entrenamiento", "Numero de Neuronas: ", None))
        self.label_2.setText(_translate("Entrenamiento", "Épocas", None))
        self.label_3.setText(_translate("Entrenamiento", "Error ideal:", None))
        self.label_5.setText(_translate("Entrenamiento", "Error:", None))
        self.pushButton.setText(_translate("Entrenamiento", "Entrenar", None))
	self.pushButton1.setText(_translate("Entrenamiento", "Regresar", None))
        self.label_6.setText(_translate("Entrenamiento", "Tasa de Aprendizaje", None))
        self.label_7.setText(_translate("Entrenamiento", "Reporte Iter.", None))
    def entrenar(self):


        numNeuronas=self.lineEdit.text()
        epocas=self.lineEdit_2.text()
        error_ideal=self.lineEdit_3.text()
        error=self.lineEdit_4.text()
        tasa_aprendizaje=self.lineEdit_5.text()
        max_iteraciones_reporte=self.lineEdit_6.text()

        #self.lineEdit_5.setText("Hola mundo")
        
        print numNeuronas
        print epocas
        print error_ideal
        print tasa_aprendizaje
        print max_iteraciones_reporte
        print error

        o=CtrlEntrenarRNA()
        o.setConeccion(1)
        o.setTasaAprendizaje(float(tasa_aprendizaje))
        o.setNumeroEntradas(8)
        o.setNumeroSalidas(1)
        o.setNeuronasCapaOculta(float(numNeuronas))
        o.setErrorDeseado(float(error_ideal))
        o.setEpocas(int(epocas))
        o.setIteracionesEntreReporte(int(max_iteraciones_reporte))
        o.setUrlPrueba("rna.data")
        o.setInterfaz(self)
        o.entrenar()
	
    def lanzarAplicacion(self):
        print "Abriendo [Recolectar Datos]..."
        inicio = QtGui.QMainWindow()
        self.root.setVisible(False)
        a=Ui_aplication()
        
        print self.login.getId()

        a.setLogin(self.login)
        a.setDatos(self.datos)
        a.setEvento(self.evento)

        a.setupUi(inicio)
        inicio.show()
        self.centralWidget = QtGui.QStackedWidget()
        self.centralWidget.addWidget(a)	

        #print self.lineEdit.text()
        #print self.lineEdit_2.text()
        #print self.lineEdit_3.text()
        #print self.lineEdit_4.text()
        #print self.lineEdit_5.text()
        #print self.lineEdit_6.text()
    def setLogin(self,login):
        self.login=login
    def setDatos(self,datos):
        self.datos=datos
    def setEvento(self,evento):
        self.evento=evento


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Entrenamiento = QtGui.QMainWindow()
    ui = Ui_Entrenamiento()
    ui.setupUi(Entrenamiento)
    Entrenamiento.show()
    sys.exit(app.exec_())
