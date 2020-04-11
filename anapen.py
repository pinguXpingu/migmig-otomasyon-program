'''
Created on 30 Mar 2020

@author: ata
'''
from PyQt5.Qt import QMainWindow, QWidget, QGridLayout, QLabel, QPixmap,\
    QPushButton
from faaliyet_pen import pen_faaliyet
from tespit_pen import pen_tespit
from kayit_pen import pen_kayit
from mimo_modules import buton_stili

class anapen(QMainWindow):
    '''
    Ana pencere
    '''


    def __init__(self,ana=None):
        super(anapen,self).__init__(ana)
        self.setWindowTitle("MigMig TMGD Tic. Ltd. Şti.")
        
        alan=QWidget()
        kutu=QGridLayout()
        
        alan.setLayout(kutu)
        
        resim=QPixmap("./doc/logo.png")
        resim=resim.scaled(128,128)
        logo=QLabel()
        logo.setPixmap(resim)
        logo.show()
        
        kutu.addWidget(logo,1,1,3,1)
        
        buton_kayit=QPushButton("Yeni Kayıt")
        buton_kayit.clicked.connect(self.kayit)
        buton_kayit.setStyleSheet(buton_stili)
        
        buton_rapor=QPushButton("Faaliyet Raporu")
        buton_rapor.clicked.connect(self.faaliyet)
        buton_rapor.setStyleSheet(buton_stili)
        
        buton_tespit=QPushButton("Tespit Formu")
        buton_tespit.clicked.connect(self.tespit)
        buton_tespit.setStyleSheet(buton_stili)
        
        kutu.addWidget(buton_kayit,1,2)
        kutu.addWidget(buton_rapor,2,2)
        kutu.addWidget(buton_tespit,3,2)
        
        
        self.p1=pen_kayit()
        self.p2=pen_tespit()
        self.p3=pen_faaliyet()
        self.setCentralWidget(alan)
        self.show()

    def kayit(self):
        self.p1.show()

    def tespit(self):
        self.p2.show()

    def faaliyet(self):
        self.p3.show()








