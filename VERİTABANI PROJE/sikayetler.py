from PyQt5.QtWidgets import *
from sikayetler_ import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)


class Sikayet(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.sikayetler = Ui_MainWindow()
        self.sikayetler.setupUi(self)
        self.sikayetler.goster.clicked.connect(self.Sikayetler)
        self.sikayetler.sikayetler.setColumnCount(3)
        self.sikayetler.sikayetler.setHorizontalHeaderLabels(("Şikayet", "Ad", "Soyad"))
    


    def Sikayetler(self):
        imlec = db.cursor()
        imlec.execute("Select sikayet,ad,soyad from Sikayet")
        result = imlec.fetchall()
        self.sikayetler.sikayetler.setRowCount(len(result))


        for i in range(len(result)):
            self.sikayetler.sikayetler.setItem(i,0,QTableWidgetItem(result[i][0]))
            self.sikayetler.sikayetler.setItem(i,1,QTableWidgetItem(result[i][1]))
            self.sikayetler.sikayetler.setItem(i,2,QTableWidgetItem(result[i][2]))
           
