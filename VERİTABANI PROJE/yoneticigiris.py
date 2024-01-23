from PyQt5.QtWidgets import *
from yonetici_giris import Ui_MainWindow
from yonetici import Yonetici
import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class YoneticiGirisPaneli(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.yoneticigirisform = Ui_MainWindow()
        self.yoneticigirisform.setupUi(self)
        self.yonetici = Yonetici()
        self.yoneticigirisform.yoneticigirisyap.clicked.connect(self.YoneticiPaneli)


    def YoneticiPaneli(self):
        kulladi = self.yoneticigirisform.yoneticikulladi.text()
        sifre = self.yoneticigirisform.yoneticisifre.text()
        imlec = db.cursor()
        query = ("Select * From Yonetici where yoneticikulladi = '"+kulladi+"'and yoneticisifre ='" + sifre + "'")
        imlec.execute(query)
        result = imlec.fetchone()
        if result:
            self.hide()
            self.yonetici.show()
            self.yoneticigirisform.yoneticikulladi.clear()
            self.yoneticigirisform.yoneticisifre.clear()
        else:
            self.yoneticigirisform.statusbar.showMessage("Kullanıcı Adı veya Şifre Hatalı !")
        