from PyQt5.QtWidgets import *
from kiradaki_araclar import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class KiradakiAraclar(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.kiradakiaraclar = Ui_MainWindow()
        self.kiradakiaraclar.setupUi(self)
        self.kiradakiaraclar.goster.clicked.connect(self.Goster)
        self.kiradakiaraclar.kiradakiaraclar.setColumnCount(8)
        self.kiradakiaraclar.kiradakiaraclar.setHorizontalHeaderLabels(("Araç Marka", "Araç Model", "Araç Plaka", "Araç Km","Kiralayan Ad","Kiralayan Soyad","Gün","Fiyat"))

    

    def Goster(self):
        imlec = db.cursor()
        imlec.execute("Select * from KiralananAraclar")
        result = imlec.fetchall()
        self.kiradakiaraclar.kiradakiaraclar.setRowCount(len(result))
        for i in range(len(result)):
            self.kiradakiaraclar.kiradakiaraclar.setItem(i,0,QTableWidgetItem(result[i][0]))
            self.kiradakiaraclar.kiradakiaraclar.setItem(i,1,QTableWidgetItem(str(result[i][1])))
            self.kiradakiaraclar.kiradakiaraclar.setItem(i,2,QTableWidgetItem(result[i][2]))
            self.kiradakiaraclar.kiradakiaraclar.setItem(i,3,QTableWidgetItem(str(result[i][3])))
            self.kiradakiaraclar.kiradakiaraclar.setItem(i,4,QTableWidgetItem(result[i][4]))
            self.kiradakiaraclar.kiradakiaraclar.setItem(i,5,QTableWidgetItem(result[i][5]))
            self.kiradakiaraclar.kiradakiaraclar.setItem(i,6,QTableWidgetItem(str(result[i][6])))
            self.kiradakiaraclar.kiradakiaraclar.setItem(i,7,QTableWidgetItem(str(result[i][7])))
        

        imlec.close()
        

        


