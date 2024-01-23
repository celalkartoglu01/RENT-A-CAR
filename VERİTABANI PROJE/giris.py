from PyQt5.QtWidgets import *
from giris_ import Ui_MainWindow
from yoneticigiris import YoneticiGirisPaneli
from kullanicigiris import KullaniciGirisPaneli
from uyeol import UyeOl

class Giris(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.girisform = Ui_MainWindow()
        self.girisform.setupUi(self)
        self.yoneticigiriss = YoneticiGirisPaneli()
        self.kullanicigiriss = KullaniciGirisPaneli()
        self.uyeol = UyeOl()
        self.girisform.yoneticigiris.clicked.connect(self.YoneticiGiris)
        self.girisform.kullanicigiris.clicked.connect(self.KullaniciGiris)
        self.girisform.uyeol.clicked.connect(self.UyeOll)


    def YoneticiGiris(self):
       self.yoneticigiriss.show()

    def KullaniciGiris(self):
        self.kullanicigiriss.show()
    
    def UyeOll(self):
        self.uyeol.show()