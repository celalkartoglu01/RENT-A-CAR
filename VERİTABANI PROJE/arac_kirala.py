# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arackirala.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, -30, 1041, 711))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("75515051-dark-background-with-spotlights-light-studio.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 30, 481, 71))
        self.label_2.setObjectName("label_2")
        self.araclar = QtWidgets.QTableWidget(self.centralwidget)
        self.araclar.setGeometry(QtCore.QRect(190, 100, 621, 321))
        self.araclar.setObjectName("araclar")
        self.araclar.setColumnCount(5)
        self.araclar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.araclar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.araclar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.araclar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.araclar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.araclar.setHorizontalHeaderItem(4, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 580, 141, 31))
        self.label_3.setObjectName("label_3")
        self.aracikirala = QtWidgets.QPushButton(self.centralwidget)
        self.aracikirala.setGeometry(QtCore.QRect(590, 580, 93, 28))
        self.aracikirala.setObjectName("aracikirala")
        self.aracplaka = QtWidgets.QLineEdit(self.centralwidget)
        self.aracplaka.setGeometry(QtCore.QRect(450, 580, 121, 31))
        self.aracplaka.setObjectName("aracplaka")
        self.araclarigoster = QtWidgets.QPushButton(self.centralwidget)
        self.araclarigoster.setGeometry(QtCore.QRect(730, 460, 111, 28))
        self.araclarigoster.setObjectName("araclarigoster")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 430, 141, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 480, 141, 31))
        self.label_5.setObjectName("label_5")
        self.kiralayansoyad = QtWidgets.QLineEdit(self.centralwidget)
        self.kiralayansoyad.setGeometry(QtCore.QRect(450, 480, 121, 31))
        self.kiralayansoyad.setObjectName("kiralayansoyad")
        self.kiralayanad = QtWidgets.QLineEdit(self.centralwidget)
        self.kiralayanad.setGeometry(QtCore.QRect(450, 430, 121, 31))
        self.kiralayanad.setObjectName("kiralayanad")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 530, 141, 31))
        self.label_6.setObjectName("label_6")
        self.gun = QtWidgets.QLineEdit(self.centralwidget)
        self.gun.setGeometry(QtCore.QRect(450, 530, 121, 31))
        self.gun.setObjectName("gun")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 26))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-style:italic; color:#ffffff;\">ARAÇ KİRALAMA PANELİ</span></p></body></html>"))
        item = self.araclar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Araç Marka"))
        item = self.araclar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Araç Model"))
        item = self.araclar.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Araç Plaka"))
        item = self.araclar.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Araç Km"))
        item = self.araclar.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fiyat"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Araç Plaka :</span></p></body></html>"))
        self.aracikirala.setText(_translate("MainWindow", "Aracı Kirala"))
        self.araclarigoster.setText(_translate("MainWindow", "Araçları Göster"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Ad :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Soyad :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Gün :</span></p></body></html>"))
