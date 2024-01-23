from PyQt5.QtWidgets import *
from arac_teslim import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)


class AracTeslim(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.aracteslim = Ui_MainWindow()
        self.aracteslim.setupUi(self)
        self.aracteslim.teslimet.clicked.connect(self.TeslimEt)
    

    def TeslimEt(self):
        plaka = self.aracteslim.aracplaka.text()
        imlec = db.cursor()
        satir = imlec.execute(f"SELECT * FROM KiralananAraclar WHERE aracplaka = '{plaka}'").fetchone()
        imlec.execute(f"INSERT INTO Araclar (aracmarka, aracmodel, aracplaka, arackm, aracfiyat) VALUES ('{satir[0]}', '{satir[1]}', '{satir[2]}', '{satir[3]}',  '{satir[7]}')")
        imlec.execute(f"DELETE FROM KiralananAraclar WHERE aracplaka = '{plaka}'")
        imlec.commit()
        self.aracteslim.statusbar.showMessage("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz !")
        self.aracteslim.aracplaka.clear()