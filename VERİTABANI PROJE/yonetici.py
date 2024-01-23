from PyQt5.QtWidgets import *
from yonetici_ import Ui_MainWindow
from aracekle import AracEkle
from yoneticiprofil import YoneticiProfil
from kiradakiaraclar import KiradakiAraclar
from arackaldir import AracKaldir
from aracguncelle import AracGuncelle
from sikayetler import Sikayet

class Yonetici(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.yoneticiform = Ui_MainWindow()
        self.yoneticiform.setupUi(self)
        self.aracekle = AracEkle()
        self.yoneticiprofill = YoneticiProfil()
        self.kiradakiaraclarr = KiradakiAraclar()
        self.arackaldirr = AracKaldir()
        self.aracguncellee = AracGuncelle()
        self.sikayetler = Sikayet()
        self.yoneticiform.aracekle.clicked.connect(self.AracEklemePaneli)
        self.yoneticiform.yoneticiprofil.clicked.connect(self.YoneticiProfilPaneli)
        self.yoneticiform.kiradakiaraclar.clicked.connect(self.AracKirala)
        self.yoneticiform.arackaldir.clicked.connect(self.AracKaldirr)
        self.yoneticiform.aracguncelle.clicked.connect(self.AracGuncellee)
        self.yoneticiform.sikayetler.clicked.connect(self.Sikayetlerr)



    def AracEklemePaneli(self):
        self.aracekle.show()

    def YoneticiProfilPaneli(self):
        self.yoneticiprofill.show()


    def AracKirala(self):
        self.kiradakiaraclarr.show()

    def AracKaldirr(self):
        self.arackaldirr.show()

    def AracGuncellee(self):
        self.aracguncellee.show()
    

    def Sikayetlerr(self):
        self.sikayetler.show()