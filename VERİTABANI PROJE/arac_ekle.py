# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aracekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -40, 1141, 741))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("75515051-dark-background-with-spotlights-light-studio.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 561, 131))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 170, 151, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 270, 151, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 350, 151, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 430, 151, 31))
        self.label_6.setObjectName("label_6")
        self.aracekleme = QtWidgets.QPushButton(self.centralwidget)
        self.aracekleme.setGeometry(QtCore.QRect(460, 580, 161, 51))
        self.aracekleme.setObjectName("aracekleme")
        self.aracmarka = QtWidgets.QLineEdit(self.centralwidget)
        self.aracmarka.setGeometry(QtCore.QRect(550, 170, 161, 31))
        self.aracmarka.setObjectName("aracmarka")
        self.aracmodel = QtWidgets.QLineEdit(self.centralwidget)
        self.aracmodel.setGeometry(QtCore.QRect(550, 270, 161, 31))
        self.aracmodel.setObjectName("aracmodel")
        self.aracplaka = QtWidgets.QLineEdit(self.centralwidget)
        self.aracplaka.setGeometry(QtCore.QRect(550, 350, 161, 31))
        self.aracplaka.setObjectName("aracplaka")
        self.arackm = QtWidgets.QLineEdit(self.centralwidget)
        self.arackm.setGeometry(QtCore.QRect(550, 430, 161, 31))
        self.arackm.setObjectName("arackm")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 510, 151, 31))
        self.label_7.setObjectName("label_7")
        self.aracfiyat = QtWidgets.QLineEdit(self.centralwidget)
        self.aracfiyat.setGeometry(QtCore.QRect(550, 510, 161, 31))
        self.aracfiyat.setObjectName("aracfiyat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic; color:#ffffff;\">ARAÇ EKLEME PANELİ</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Araç Markası :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Araç Modeli :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Araç Plakası :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Araç Km\'si :</span></p></body></html>"))
        self.aracekleme.setText(_translate("MainWindow", "Aracı Ekle"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Araç Fiyatı :</span></p></body></html>"))
