from PyQt5.QtWidgets import *
from arac_kaldir import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)


class AracKaldir(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.arackaldir = Ui_MainWindow()
        self.arackaldir.setupUi(self)
        self.arackaldir.aracgoster.clicked.connect(self.AracGoster)
        self.arackaldir.aracikaldir.clicked.connect(self.AraciKaldir)
        self.arackaldir.arackaldir.setColumnCount(4)
        self.arackaldir.arackaldir.setHorizontalHeaderLabels(("Araç Marka", "Araç Model", "Araç Plaka", "Araç Km"))


    def AraciKaldir(self):
        plaka = self.arackaldir.aracplaka.text()
        imlec = db.cursor()
        imlec.execute("delete from Araclar where aracplaka = ?" , (plaka,))
        imlec.commit()
        self.arackaldir.statusbar.showMessage("Araç Başarıyla Kaldırıldı !")
        self.arackaldir.arackaldir.clear()
        self.arackaldir.arackaldir.setHorizontalHeaderLabels(("Araç Marka", "Araç Model", "Araç Plaka", "Araç Km"))
        imlec.close()
    

    def AracGoster(self):
        imlec = db.cursor()
        imlec.execute("Select aracmarka,aracmodel,aracplaka,arackm from Araclar")
        result = imlec.fetchall()
        self.arackaldir.arackaldir.setRowCount(len(result))
        
        for i in range(len(result)):
            self.arackaldir.arackaldir.setItem(i,0,QTableWidgetItem(result[i][0]))
            self.arackaldir.arackaldir.setItem(i,1,QTableWidgetItem(str(result[i][1])))
            self.arackaldir.arackaldir.setItem(i,2,QTableWidgetItem(result[i][2]))
            self.arackaldir.arackaldir.setItem(i,3,QTableWidgetItem(str(result[i][3])))
        
        imlec.close()
