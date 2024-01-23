from PyQt5.QtWidgets import *
from arac_ekle import Ui_MainWindow
import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class AracEkle(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.aracekle = Ui_MainWindow()
        self.aracekle.setupUi(self)
        self.aracekle.aracekleme.clicked.connect(self.AracEkle)
    

    def AracEkle(self):
        marka = self.aracekle.aracmarka.text()
        model = self.aracekle.aracmodel.text()
        plaka = self.aracekle.aracplaka.text()
        km = self.aracekle.arackm.text()
        fiyat = self.aracekle.aracfiyat.text()
        imlec = db.cursor()
        imlec.execute("insert into Araclar values(?,?,?,?,?)",(marka,model,plaka,km,fiyat))
        imlec.commit()  
        imlec.close()
        self.aracekle.statusbar.showMessage("Araç Eklendi !")


        
