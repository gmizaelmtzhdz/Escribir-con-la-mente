# -*- coding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
# Form implementation generated from reading ui file 'principal.ui'
#
# Created: Tue Sep 29 12:36:43 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_principal(object):
    def setupUi(self, principal):
        principal.setObjectName(_fromUtf8("principal"))
        principal.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons RNAS/1440681999_head-atom_64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        principal.setWindowIcon(icon)
        principal.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(principal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 411, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 150, 91, 201))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons RNAS/cerebro1 - copia.JPG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(200, 200))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 150, 91, 201))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.pushButton_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons RNAS/ymcl.JPG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 360, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 360, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        principal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        principal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(principal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        principal.setStatusBar(self.statusbar)

        self.retranslateUi(principal)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), principal.AbrirEntrenamiento)
        QtCore.QMetaObject.connectSlotsByName(principal)

    def retranslateUi(self, principal):
        principal.setWindowTitle(_translate("principal", "Redes Neuronales-Principal", None))
        self.label.setText(_translate("principal", "SELEECIONE UNA OPCION", None))
        self.label_2.setText(_translate("principal", "ENTRENAR RNA", None))
        self.label_3.setText(_translate("principal", "INICIAR RNA", None))

#import imagenes_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    principal = QtGui.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec_())

