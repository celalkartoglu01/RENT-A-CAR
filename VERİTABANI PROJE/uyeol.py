from PyQt5.QtWidgets import *
from uye_ol import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)


class UyeOl(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.uyeol = Ui_MainWindow()
        self.uyeol.setupUi(self)
        self.uyeol.uyeol.clicked.connect(self.UyeOll)
    

    def UyeOll(self):
        ad = self.uyeol.uyead.text()
        soyad = self.uyeol.uyesoyad.text()
        kulladi = self.uyeol.uyekulladi.text()
        sifre = self.uyeol.uyesifre.text()
        imlec = db.cursor()
        imlec.execute("insert into Kullanici values(?,?,?,?)",(ad,soyad,kulladi,sifre))
        imlec.commit()  
        imlec.close()
        self.uyeol.statusbar.showMessage("Üye Oldunuz !")
        self.uyeol.uyead.clear()
        self.uyeol.uyesoyad.clear()
        self.uyeol.uyekulladi.clear()
        self.uyeol.uyesifre.clear()
