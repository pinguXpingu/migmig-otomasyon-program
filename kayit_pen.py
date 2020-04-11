'''
Created on 30 Mar 2020

@author: ata
'''
from PyQt5.Qt import QWidget, QRadioButton, QVBoxLayout, QPushButton,\
    QGridLayout, QLabel, QTextEdit, QLineEdit, QComboBox, QHBoxLayout
from mimo_modules import etiket_hiza1, ekle

class pen_kayit(QWidget):
    '''
    Müşteri kayıt penceresi
    '''
    def __init__(self, parent=None):
        super(pen_kayit,self).__init__(parent)
        self.setWindowTitle("Yeni Kayıt")
        self.setWindowModality(2)
        self.s1=QRadioButton("Yeni Müşteri Kaydı")
        self.s2=QRadioButton("Yeni TMGD Şirket Kaydı")
        self.s3=QRadioButton("Yeni Danışman Kaydı")
        b1=QPushButton("Tamam")
        b1.clicked.connect(self.secilmis)

        diz=QVBoxLayout()
        diz.addWidget(self.s1)
        diz.addWidget(self.s2)
        diz.addWidget(self.s3)
        diz.addWidget(b1)
        self.setLayout(diz)

        self.p0=yeniMusteri()
        self.p1=yeniTMGD()
        self.p2=yeniDanisman()


    def secilmis(self):
        if self.s1.isChecked():
            self.close()
            self.p0.show()
        if self.s2.isChecked():
            self.close()
            self.p1.show()
        if self.s3.isChecked():
            self.close()
            self.p2.show()


class yeniMusteri(QWidget):

    def __init__(self, parent=None):
        super(yeniMusteri,self).__init__(parent)
        self.setWindowTitle("Yeni Müşteri Kaydı")
        self.setWindowModality(2)

        dizgi=QGridLayout()
        e1=QLabel("Ticari Ünvanı:")
        e2=QLabel("Adresi:")
        e3=QLabel("Vergi No:")
        e4=QLabel("U-Net No:")
        e5=QLabel("Belge No:")
        e6 =QLabel("Rapor:")
        e7=QLabel("Fatura:")
        e8=QLabel("Tahsilat:")
        
        self.k1=QTextEdit()
        self.k2=QTextEdit()
        self.k3=QLineEdit()
        self.k4=QLineEdit()
        self.k5=QLineEdit()
        self.k6=QComboBox()
        self.k6.addItem("Yok")
        self.k6.addItem("Var")
        self.k7=QComboBox()
        self.k7.addItem("Kesilmedi")
        self.k7.addItem("Kesildi")
        
        self.tahsil=QHBoxLayout()
        self.k8=QComboBox()
        self.k8.addItem("Yapılmadı")
        self.k8.addItem("Yapıldı")
        self.k8.currentIndexChanged.connect(self.kutuEkle)
        self.tahsil.addWidget(self.k8)
        
        dizgi.addWidget(e1,1,1)
        dizgi.addWidget(e2,2,1)
        dizgi.addWidget(e3,3,1)
        dizgi.addWidget(e4,4,1)
        dizgi.addWidget(e5,5,1)
        dizgi.addWidget(e6,6,1)
        dizgi.addWidget(e7,7,1)
        dizgi.addWidget(e8,8,1)
        dizgi.addWidget(self.k1,1,2)
        dizgi.addWidget(self.k2,2,2)
        dizgi.addWidget(self.k3,3,2)
        dizgi.addWidget(self.k4,4,2)
        dizgi.addWidget(self.k5,5,2)
        dizgi.addWidget(self.k6,6,2)
        dizgi.addWidget(self.k7,7,2)
        dizgi.addLayout(self.tahsil,8,2)
        
        b1=QPushButton("Tamam")
        b1.clicked.connect(self.tamam)
        b2=QPushButton("İptal")
        b2.clicked.connect(self.iptal)
        
        iptal_tamam=QHBoxLayout()
        iptal_tamam.addWidget(b2)
        iptal_tamam.addWidget(b1)

        dizgi.addLayout(iptal_tamam,9,2)

        self.setLayout(dizgi)
        self.setStyleSheet(etiket_hiza1)

    def tamam(self):
        ad=self.k1.toPlainText()
        adres=self.k2.toPlainText()
        vergi=self.k3.text()
        unet=self.k4.text()
        belge=self.k5.text()
        rapor=self.k6.currentText()
        fatura=self.k7.currentText()
        if self.k8.currentText()=="Yapıldı":
            tahsilat=self.para.text()
        else:
            tahsilat=self.k8.currentText()
        ekle("firmalar",ad,adres,vergi,unet,belge,rapor,fatura,tahsilat)
        self.close()

    def iptal(self):
        self.close()

    def kutuEkle(self):
        if self.k8.currentText()=="Yapıldı":
            self.para=QLineEdit()
            self.tahsil.addWidget(self.para)
        else:
            try:
                self.para.close()
            except:
                print()



class yeniTMGD(QWidget):

    def __init__(self, parent=None):
        super(yeniTMGD,self).__init__(parent)
        self.setWindowTitle("Yeni TMGD Şirket Kaydı")
        self.setWindowModality(2)

        dizgi=QGridLayout()
        e1=QLabel("Ticari Ünvanı:")
        e2=QLabel("U-Net No:")
        e3=QLabel("Vergi No:")
        e4=QLabel("Belge No:")
        
        self.k1=QTextEdit()
        self.k2=QLineEdit()
        self.k3=QLineEdit()
        self.k4=QLineEdit()

        dizgi.addWidget(e1,1,1)
        dizgi.addWidget(e2,2,1)
        dizgi.addWidget(e3,3,1)
        dizgi.addWidget(e4,4,1)
        dizgi.addWidget(self.k1,1,2)
        dizgi.addWidget(self.k2,2,2)
        dizgi.addWidget(self.k3,3,2)
        dizgi.addWidget(self.k4,4,2)
        
        b1=QPushButton("Tamam")
        b1.clicked.connect(self.tamam)
        b2=QPushButton("İptal")
        b2.clicked.connect(self.iptal)
        
        iptal_tamam=QHBoxLayout()
        iptal_tamam.addWidget(b2)
        iptal_tamam.addWidget(b1)

        dizgi.addLayout(iptal_tamam,5,2)

        self.setLayout(dizgi)
        self.setStyleSheet(etiket_hiza1)

    def tamam(self):
        ad=self.k1.toPlainText()
        unet=self.k2.text()
        vergi=self.k3.text()
        belge=self.k4.text()
        
        ekle("sirket",ad,unet,vergi,belge)
        self.close()

    def iptal(self):
        self.close()



class yeniDanisman(QWidget):

    def __init__(self, parent=None):
        super(yeniDanisman,self).__init__(parent)
        self.setWindowTitle("Yeni Danışman Kaydı")
        self.setWindowModality(2)
        
        dizgi=QGridLayout()
        e1=QLabel("Adı Soyadı:")
        e2=QLabel("Belge No:")
        e3=QLabel("Kimlik No:")
        e4=QLabel("Telefon No:")
        e5=QLabel("E Posta:")
        e6=QLabel("@")

        self.k1=QLineEdit()
        self.k2=QLineEdit()
        self.k3=QLineEdit()
        self.k4=QLineEdit()
        self.k5=QLineEdit()
        self.k6=QLineEdit()
        
        epostaci=QHBoxLayout()
        epostaci.addWidget(self.k5)
        epostaci.addWidget(e6)
        epostaci.addWidget(self.k6)
        
        dizgi.addWidget(e1,1,1)
        dizgi.addWidget(e2,2,1)
        dizgi.addWidget(e3,3,1)
        dizgi.addWidget(e4,4,1)
        dizgi.addWidget(e5,5,1)
        dizgi.addWidget(self.k1,1,2)
        dizgi.addWidget(self.k2,2,2)
        dizgi.addWidget(self.k3,3,2)
        dizgi.addWidget(self.k4,4,2)
        dizgi.addLayout(epostaci,5,2)
        
        b1=QPushButton("Tamam")
        b1.clicked.connect(self.tamam)
        b2=QPushButton("İptal")
        b2.clicked.connect(self.iptal)
        
        iptal_tamam=QHBoxLayout()
        iptal_tamam.addWidget(b2)
        iptal_tamam.addWidget(b1)

        dizgi.addLayout(iptal_tamam,6,2)

        self.setLayout(dizgi)
        self.setStyleSheet(etiket_hiza1)

    def tamam(self):
        ad=self.k1.text()
        belge=self.k2.text()
        kimlik=self.k3.text()
        telefon=self.k4.text()
        posta=f"{self.k5.text()}@{self.k6.text()}"
        
        ekle("danisman",ad,belge,kimlik,telefon,posta)
        self.close()

    def iptal(self):
        self.close()

