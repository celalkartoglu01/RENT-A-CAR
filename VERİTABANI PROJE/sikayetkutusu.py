from PyQt5.QtWidgets import *
from sikayet_kutusu import Ui_MainWindow
import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class SikayetKutusu(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.sikayetkutusu = Ui_MainWindow()
        self.sikayetkutusu.setupUi(self)
        self.sikayetkutusu.sikayetgonder.clicked.connect(self.SikayetEt)



    def SikayetEt(self):
        sikayet = self.sikayetkutusu.sikayet.text()
        ad = self.sikayetkutusu.ad.text()
        soyad = self.sikayetkutusu.soyad.text()
        imlec = db.cursor()
        imlec.execute("insert into Sikayet values(?,?,?)",(sikayet,ad,soyad))
        imlec.commit()
        self.sikayetkutusu.statusbar.showMessage("Şikayetiniz Başarıyla Gönderildi !")
        imlec.close()


