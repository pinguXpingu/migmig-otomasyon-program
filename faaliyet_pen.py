'''
Created on 30 Mar 2020

@author: ata
'''

from PyQt5.Qt import QWidget, QGridLayout, QLineEdit, QTextEdit, QComboBox,\
    QLabel
from mimo_modules import getir, etiket_rengi1, etiket_rengi2

class pen_faaliyet(QWidget):
    '''
    Faaliyet Raporu Penceresi
    '''


    def __init__(self,ana=None):
        super(pen_faaliyet,self).__init__(ana)
        self.setWindowTitle("MigMig Danışmanlık")
        self.setWindowModality(2)
        
        self.kutu=QGridLayout()
        
        
        etiket1=QLabel("İŞLETME")
        etiket1.setStyleSheet(etiket_rengi1)
        etiket2=QLabel("ADRES")
        etiket2.setStyleSheet(etiket_rengi1)
        etiket3=QLabel("RAPOR")
        etiket3.setStyleSheet(etiket_rengi1)
        etiket4=QLabel("FATURA")
        etiket4.setStyleSheet(etiket_rengi1)
        etiket5=QLabel("TAHSİLAT")
        etiket5.setStyleSheet(etiket_rengi1)
        etiket6=QLabel("NOTLAR")
        etiket6.setStyleSheet(etiket_rengi1)
        
        self.kutu.addWidget(etiket1,1,1)
        self.kutu.addWidget(etiket2,2,1)
        self.kutu.addWidget(etiket3,3,1)
        self.kutu.addWidget(etiket4,4,1)
        self.kutu.addWidget(etiket5,5,1)
        self.kutu.addWidget(etiket6,6,1)
        
        
        self.isletme=QComboBox()
        self.isletme.addItem("")
        for i in getir():
            self.isletme.addItem(i[1])
        self.isletme.currentIndexChanged.connect(self.doldur)
        
        self.adres=QLineEdit()
        self.rapor=QLineEdit()
        
        self.fatura=QComboBox()
        self.fatura.addItem("")
        self.fatura.addItem("Bırakıldı")
        self.fatura.addItem("Bırakılmadı")
        
        self.tahsilat=QComboBox()
        self.tahsilat.addItem("")
        self.tahsilat.addItem("Yapıldı")
        self.tahsilat.addItem("Yapılmadı")
        self.tahsilat.currentIndexChanged.connect(self.kutuEkle)
        
        
        notlar=QTextEdit()
        notlar.setMaximumHeight(48)
        
        self.kutu.addWidget(self.isletme,1,2,1,2)
        self.kutu.addWidget(self.adres,2,2,1,2)
        self.kutu.addWidget(self.rapor,3,2,1,2)
        self.kutu.addWidget(self.fatura,4,2,1,2)
        self.kutu.addWidget(self.tahsilat,5,2,1,1)
        self.kutu.addWidget(notlar,6,2,1,2)
        
        
        etiket7=QLabel("TOPLAM TAHSİLAT")
        etiket7.setStyleSheet(etiket_rengi1)
        etiket8=QLabel("MASRAFLAR")
        etiket8.setStyleSheet("QLabel{color:red; qproperty-alignment: AlignLeft;}")
        etiket9=QLabel("Yemek")
        etiket9.setStyleSheet(etiket_rengi2)
        etiket10=QLabel("Yakıt")
        etiket10.setStyleSheet(etiket_rengi2)
        etiket11=QLabel("Diğer")
        etiket11.setStyleSheet(etiket_rengi2)
        etiket12=QLabel("NET TAHSİLAT")
        etiket12.setStyleSheet(etiket_rengi1)
        
        '''
        self.kutu.addWidget(etiket7,7,1)
        self.kutu.addWidget(etiket8,8,2)
        self.kutu.addWidget(etiket9,9,1)
        self.kutu.addWidget(etiket10,10,1)
        self.kutu.addWidget(etiket11,11,1)
        self.kutu.addWidget(etiket12,12,1)
        
        
        self.toplam=QLineEdit("0")
        self.toplam.textChanged.connect(self.netTahsilat)
        
        self.yemek=QLineEdit("0")
        self.yemek.textChanged.connect(self.netTahsilat)
        
        self.yakit=QLineEdit("0")
        self.yakit.textChanged.connect(self.netTahsilat)
        
        self.diger=QLineEdit("0")
        self.diger.textChanged.connect(self.netTahsilat)
        
        self.netgelir=QLineEdit("0")
        
        self.kutu.addWidget(self.toplam,7,2)
        self.kutu.addWidget(self.yemek,9,2)
        self.kutu.addWidget(self.yakit,10,2)
        self.kutu.addWidget(self.diger,11,2)
        self.kutu.addWidget(self.netgelir,12,2)
        '''

        self.setLayout(self.kutu)

    def doldur(self):
        if self.isletme.currentText() != "Firma seç...":
            try:
                x=getir(self.isletme.currentText())
                self.adres.setText(x[2])
                self.rapor.setText(x[5])
            except:
                self.adres.setText("bulunamadı")
                self.rapor.setText("bulunamadı")
        else:
            self.adres.setText("")
            self.rapor.setText("")

    def masraf(self):
        x=int(self.yemek.text())
        y=int(self.yakit.text())
        z=int(self.diger.text())
        return x+y+z
    
    def netTahsilat(self):
        a=int(self.masraf())
        b=int(self.toplam.text())
        self.netgelir.setText(str(b-a))
        return 0

    def kutuEkle(self):
        if self.tahsilat.currentText()=="Yapıldı":
            self.tahsilatMktar=QLineEdit()
            self.kutu.addWidget(self.tahsilatMktar,5,3,1,1)
        else:
            try:
                self.tahsilatMktar.close()
            except:
                print()








