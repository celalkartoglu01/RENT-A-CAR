from PyQt5.QtWidgets import *
from kullanici_profil import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class KullaniciProfil(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.kullaniciprofil = Ui_MainWindow()
        self.kullaniciprofil.setupUi(self)
        self.kullaniciprofil.kullanicigetir.clicked.connect(self.KullaniciGetir)


    

    def KullaniciGetir(self):
        imlec = db.cursor()
        kulladi = self.kullaniciprofil.kullanicikulladi.text()
        imlec.execute("Select kullaniciad,kullanicisoyad FROM Kullanici where kullanicikulladi = ?", (kulladi,))
        result = imlec.fetchone()
        if result:
            self.kullaniciprofil.kullaniciad_2.setText(result[0])
            self.kullaniciprofil.kullanicisoyad.setText(result[1])
        else:
            self.yoneticiprofil.statusbar.showMessage("Kullanıcı Bulunamadı !")
        imlec.close()

