from PyQt5.QtWidgets import *
from kullanici_giris import Ui_MainWindow
from kullanici import Kullanici
import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class KullaniciGirisPaneli(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.kullanicigirisform = Ui_MainWindow()
        self.kullanicigirisform.setupUi(self)
        self.kullanici = Kullanici()
        self.kullanicigirisform.kullanicigirisyap.clicked.connect(self.KullaniciPaneli)


    def KullaniciPaneli(self):
        kulladi = self.kullanicigirisform.kullanicikulladi.text()
        sifre = self.kullanicigirisform.kullanicisifre.text()
        imlec = db.cursor()
        query = ("Select * From Kullanici where kullanicikulladi = '"+kulladi+"'and kullanicisifre ='" + sifre + "'")
        imlec.execute(query)
        result = imlec.fetchone()
        if result:
            self.hide()
            self.kullanici.show()
            self.kullanicigirisform.kullanicikulladi.clear()
            self.kullanicigirisform.kullanicisifre.clear()
        else:
            self.kullanicigirisform.statusbar.showMessage("Kullanıcı Adı veya Şifre Hatalı !")
   