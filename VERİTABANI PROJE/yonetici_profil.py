# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yoneticiprofil.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, -60, 861, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("75515051-dark-background-with-spotlights-light-studio.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 391, 91))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 150, 141, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 230, 171, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 310, 231, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 380, 181, 41))
        self.label_6.setObjectName("label_6")
        self.goster = QtWidgets.QPushButton(self.centralwidget)
        self.goster.setGeometry(QtCore.QRect(370, 480, 111, 31))
        self.goster.setObjectName("goster")
        self.yoneticiad = QtWidgets.QLineEdit(self.centralwidget)
        self.yoneticiad.setGeometry(QtCore.QRect(460, 160, 141, 31))
        self.yoneticiad.setObjectName("yoneticiad")
        self.yoneticisoyad = QtWidgets.QLineEdit(self.centralwidget)
        self.yoneticisoyad.setGeometry(QtCore.QRect(460, 240, 141, 31))
        self.yoneticisoyad.setObjectName("yoneticisoyad")
        self.yoneticikulladi = QtWidgets.QLineEdit(self.centralwidget)
        self.yoneticikulladi.setGeometry(QtCore.QRect(460, 320, 141, 31))
        self.yoneticikulladi.setObjectName("yoneticikulladi")
        self.yoneticiunvan = QtWidgets.QLineEdit(self.centralwidget)
        self.yoneticiunvan.setGeometry(QtCore.QRect(460, 390, 141, 31))
        self.yoneticiunvan.setObjectName("yoneticiunvan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-style:italic; color:#ffffff;\">YÖNETİCİ PROFİL</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Yönetici Adı :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Yönetici Soyadı :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Yönetici Kullanıcı Adı :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Yönetici Unvan :</span></p></body></html>"))
        self.goster.setText(_translate("MainWindow", "Bilgileri Goster"))
