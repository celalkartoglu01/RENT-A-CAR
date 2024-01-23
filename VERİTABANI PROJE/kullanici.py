from PyQt5.QtWidgets import *
from kullanici_ import Ui_MainWindow
from kullaniciprofil import KullaniciProfil
from arackirala import AracKirala
from aracteslim import AracTeslim
from sikayetkutusu import SikayetKutusu

class Kullanici(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.kullaniciform = Ui_MainWindow()
        self.kullaniciform.setupUi(self)
        self.kullaniciprofill = KullaniciProfil()
        self.arackiralaa = AracKirala()
        self.aracteslimm = AracTeslim()
        self.sikayetkutusuu = SikayetKutusu()
        self.kullaniciform.kullaniciprofil.clicked.connect(self.KullaniciProfill)
        self.kullaniciform.arackirala.clicked.connect(self.AracKiralaa)
        self.kullaniciform.aracteslim.clicked.connect(self.AracTeslimm)
        self.kullaniciform.sikayet.clicked.connect(self.SikayetKutusuu)

    def KullaniciProfill(self):
        self.kullaniciprofill.show()

    def AracKiralaa(self):
        self.arackiralaa.show()

    def AracTeslimm(self):
        self.aracteslimm.show()

    def SikayetKutusuu(self):
        self.sikayetkutusuu.show()