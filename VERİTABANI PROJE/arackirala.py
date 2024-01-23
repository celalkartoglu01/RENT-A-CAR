from PyQt5.QtWidgets import *
from arac_kirala import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class AracKirala(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.arackirala = Ui_MainWindow()
        self.arackirala.setupUi(self)
        self.arackirala.aracikirala.clicked.connect(self.AraciKirala)
        self.arackirala.araclarigoster.clicked.connect(self.AraclariGoster)
        self.arackirala.araclar.setColumnCount(5)
        self.arackirala.araclar.setHorizontalHeaderLabels(("Araç Marka", "Araç Model", "Araç Plaka", "Araç Km"))
    

    def AraciKirala(self):
        plaka = self.arackirala.aracplaka.text()
        ad = self.arackirala.kiralayanad.text()
        soyad = self.arackirala.kiralayansoyad.text()
        gun = self.arackirala.gun.text()
        imlec = db.cursor()
        satir = imlec.execute(f"SELECT * FROM Araclar WHERE aracplaka = '{plaka}'").fetchone()
        imlec.execute(f"INSERT INTO KiralananAraclar (aracmarka, aracmodel, aracplaka, arackm,kiralayanad,kiralayansoyad,gun,fiyat) VALUES ('{satir[0]}', '{satir[1]}', '{satir[2]}', '{satir[3]}', '{ad}', '{soyad}', '{gun}', '{satir[4]}')")
        imlec.execute(f"DELETE FROM Araclar WHERE aracplaka = '{plaka}'")
        imlec.commit()
        self.arackirala.statusbar.showMessage("Aracı Kiraladınız, Hayırlı Olsun !")
        self.arackirala.kiralayanad.clear()
        self.arackirala.kiralayansoyad.clear()
        self.arackirala.gun.clear()
        self.arackirala.aracplaka.clear()
        self.arackirala.araclar.clear()
        self.arackirala.araclar.setHorizontalHeaderLabels(("Araç Marka", "Araç Model", "Araç Plaka", "Araç Km","Fiyat"))
        imlec.close()

    def AraclariGoster(self):
        imlec = db.cursor()
        imlec.execute("Select aracmarka,aracmodel,aracplaka,arackm,aracfiyat from Araclar")
        result = imlec.fetchall()
        self.arackirala.araclar.setRowCount(len(result))
        
        for i in range(len(result)):
            self.arackirala.araclar.setItem(i,0,QTableWidgetItem(result[i][0]))
            self.arackirala.araclar.setItem(i,1,QTableWidgetItem(str(result[i][1])))
            self.arackirala.araclar.setItem(i,2,QTableWidgetItem(result[i][2]))
            self.arackirala.araclar.setItem(i,3,QTableWidgetItem(str(result[i][3])))
            self.arackirala.araclar.setItem(i,4,QTableWidgetItem(str(result[i][4])))
        
        imlec.close()
