from PyQt5.QtWidgets import *
from yonetici_profil import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class YoneticiProfil(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.yoneticiprofil = Ui_MainWindow()
        self.yoneticiprofil.setupUi(self)
        self.yoneticiprofil.goster.clicked.connect(self.BilgileriGoster)
    

    def BilgileriGoster(self):
            imlec = db.cursor()
            kulladi = self.yoneticiprofil.yoneticikulladi.text()
            imlec.execute("Select yoneticiadi,yoneticisoyadi,yoneticiunvan FROM Yonetici where yoneticikulladi = ?", (kulladi,))
            result = imlec.fetchone()
            if result:
                self.yoneticiprofil.yoneticiad.setText(result[0])
                self.yoneticiprofil.yoneticisoyad.setText(result[1])
                self.yoneticiprofil.yoneticiunvan.setText(result[2])
            else:
                 self.yoneticiprofil.statusbar.showMessage("Kullanıcı Bulunamadı !")
            imlec.close()
            


