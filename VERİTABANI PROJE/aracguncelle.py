from PyQt5.QtWidgets import *
from arac_guncelle import Ui_MainWindow
import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-NQ9S85UA\SQLEXPRESS01;'
    'Database=rentacar;'
    'Trusted_Connection=True'
)

class AracGuncelle(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.aracguncelle = Ui_MainWindow()
        self.aracguncelle.setupUi(self)
        self.aracguncelle.aracgoster.clicked.connect(self.AracGoster)
        self.aracguncelle.aracgoster.clicked.connect(self.AracGuncelle)
        self.aracguncelle.araclar.setColumnCount(5)
        self.aracguncelle.araclar.setHorizontalHeaderLabels(("Araç Marka", "Araç Model", "Araç Plaka", "Araç Km","Araç Fiyat"))
    


    def AracGuncelle(self):
        imlec = db.cursor()
        marka = self.aracguncelle.aracmarka.text()
        model = self.aracguncelle.aracmodel.text()
        plaka = self.aracguncelle.aracplaka.text()
        km = self.aracguncelle.arackm.text()
        fiyat = self.aracguncelle.aracfiyat.text()


        if marka == "" and model == "" and fiyat == "":
            imlec.execute("update Araclar set arackm = ? where aracplaka = ?",(km,plaka))
            self.aracguncelle.statusbar.showMessage("KM Başarıyla Güncellendi !")
            imlec.commit()

        elif marka == "" and km == "" and fiyat == "":
            imlec.execute("update Araclar set aracmodel = ? where aracplaka = ?",(model,plaka))
            self.aracguncelle.statusbar.showMessage("Model Başarıyla Güncellendi !")
            imlec.commit()

        elif model == "" and km == "" and fiyat == "":
            imlec.execute("update Araclar set aracmarka = ? where aracplaka = ?",(marka,plaka))
            self.aracguncelle.statusbar.showMessage("Marka Başarıyla Güncellendi !")
            imlec.commit()
        elif model == "" and km == "" and marka == "":
            imlec.execute("update Araclar set aracfiyat = ? where aracplaka = ?",(fiyat,plaka))

        else:
            imlec.execute("update Araclar set aracmarka = ?,aracmodel= ?,arackm = ?,aracfiyat = ? where aracplaka = ? ",(marka,model,km,fiyat,plaka))
            self.aracguncelle.statusbar.showMessage("Bilgiler Başarıyla Güncellendi !")
            imlec.commit()
            self.aracguncelle.aracmarka.clear()
            self.aracguncelle.aracmodel.clear()
            self.aracguncelle.arackm.clear()
            self.aracguncelle.aracfiyat.clear()      

    




    def AracGoster(self):
        imlec = db.cursor()
        imlec.execute("Select aracmarka,aracmodel,aracplaka,arackm,aracfiyat from Araclar")
        result = imlec.fetchall()
        self.aracguncelle.araclar.setRowCount(len(result))
        
        for i in range(len(result)):
            self.aracguncelle.araclar.setItem(i,0,QTableWidgetItem(result[i][0]))
            self.aracguncelle.araclar.setItem(i,1,QTableWidgetItem(str(result[i][1])))
            self.aracguncelle.araclar.setItem(i,2,QTableWidgetItem(result[i][2]))
            self.aracguncelle.araclar.setItem(i,3,QTableWidgetItem(str(result[i][3])))
            self.aracguncelle.araclar.setItem(i,4,QTableWidgetItem(str(result[i][4])))
        
        imlec.close()

