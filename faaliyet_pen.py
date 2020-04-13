'''
Created on 30 Mar 2020

@author: ata
'''

from PyQt5.Qt import QWidget, QGridLayout, QLineEdit, QTextEdit, QComboBox,\
    QLabel, QHBoxLayout, QPushButton
from mimo_modules import getir, etiket_rengi1, etiket_rengi2, ekle

class pen_faaliyet(QWidget):
    '''
    Faaliyet Raporu Penceresi
    '''


    def __init__(self,ana=None):
        super(pen_faaliyet,self).__init__(ana)
        self.setWindowTitle("MigMig Danışmanlık")
        self.setWindowModality(2)
        
        self.kutu=QGridLayout()
        
        
########etiketler
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
        etiket7=QLabel("KATILAN")
        etiket7.setStyleSheet(etiket_rengi1)
        etiket8=QLabel("MASRAFLAR")
        etiket8.setStyleSheet("QLabel{color:red; qproperty-alignment: AlignLeft;}")
        etiket9=QLabel("Yemek")
        etiket9.setStyleSheet(etiket_rengi2)
        etiket10=QLabel("Yakıt")
        etiket10.setStyleSheet(etiket_rengi2)
        etiket11=QLabel("Diğer")
        etiket11.setStyleSheet(etiket_rengi2)
        etiket12=QLabel("TOPLAM")
        etiket13=QLabel("GELİR")
        etiket13.setStyleSheet("QLabel{qproperty-alignment: AlignCenter;}")
        etiket14=QLabel("GİDER")
        etiket14.setStyleSheet("QLabel{qproperty-alignment: AlignCenter;}")

        toplu=QHBoxLayout()
        toplu.addWidget(etiket13)
        toplu.addWidget(etiket14)

        self.kutu.addWidget(etiket1,1,1)
        self.kutu.addWidget(etiket2,2,1)
        self.kutu.addWidget(etiket3,3,1)
        self.kutu.addWidget(etiket4,4,1)
        self.kutu.addWidget(etiket5,5,1)
        self.kutu.addWidget(etiket6,6,1)
        self.kutu.addWidget(etiket7,7,1)
        self.kutu.addWidget(etiket8,9,2)
        self.kutu.addWidget(etiket9,10,1)
        self.kutu.addWidget(etiket10,11,1)
        self.kutu.addWidget(etiket11,12,1)
        self.kutu.addWidget(etiket12,13,1)
        self.kutu.addLayout(toplu,13,2,1,3)


########kutular
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
        
        self.tahsil=QHBoxLayout()
        self.tahsilat=QComboBox()
        self.tahsilat.addItem("")
        self.tahsilat.addItem("Yapıldı")
        self.tahsilat.addItem("Yapılmadı")
        self.tahsilat.currentIndexChanged.connect(self.kutuEkle)
        self.tahsil.addWidget(self.tahsilat)
        
        
        self.notlar=QTextEdit()
        self.notlar.setMaximumHeight(48)

########kimler katıldı
        katilim=QHBoxLayout()
        self.katilim_list=[]
        self.katilan=QComboBox()
        self.katilan.addItem("Mehmet Atasoy")
        self.katilan.addItem("Fernando Muslera")
        ekle_b=QPushButton("Ekle")
        ekle_b.clicked.connect(self.katilim_ekle)
        katilim.addWidget(self.katilan)
        katilim.addWidget(ekle_b)
        self.katilanlar=QTextEdit()
        self.katilanlar.setMaximumHeight(48)

########masraf bölümü
        self.yemek=QLineEdit("0")
        self.yemek.textChanged.connect(self.netTahsilat)
        
        yak=QHBoxLayout()
        self.yakit=QLineEdit("0")
        self.yakit.textChanged.connect(self.netTahsilat)
        yakitsec=QComboBox()
        yakitsec.addItem("")
        yakitsec.addItem("Benzin")
        yakitsec.addItem("Motorin")
        yakitsec.addItem("LPG")
        yak.addWidget(self.yakit)
        yak.addWidget(yakitsec)

        self.diger=QLineEdit("0")
        self.diger.textChanged.connect(self.netTahsilat)

        self.kutu.addWidget(self.isletme,1,2,1,2)
        self.kutu.addWidget(self.adres,2,2,1,2)
        self.kutu.addWidget(self.rapor,3,2,1,2)
        self.kutu.addWidget(self.fatura,4,2,1,2)
        self.kutu.addLayout(self.tahsil,5,2,1,2)
        self.kutu.addWidget(self.notlar,6,2,1,2)
        self.kutu.addLayout(katilim,7,2,1,2)
        self.kutu.addWidget(self.katilanlar,8,2,1,2)
        self.kutu.addWidget(self.yemek,10,2,1,2)
        self.kutu.addLayout(yak,11,2,1,2)
        self.kutu.addWidget(self.diger,12,2,1,2)

#######toplamlar
        self.gider=QLineEdit("0")
        self.gelir=QLineEdit("0")
        toplu_k=QHBoxLayout()
        toplu_k.addWidget(self.gelir)
        toplu_k.addWidget(self.gider)

        self.kutu.addLayout(toplu_k,14,2,1,2)
        self.kontrol=0

        b1=QPushButton("Tamam")
        b1.clicked.connect(self.tamam)
        b2=QPushButton("İptal")
        b2.clicked.connect(self.iptal)
        
        iptal_tamam=QHBoxLayout()
        iptal_tamam.addWidget(b2)
        iptal_tamam.addWidget(b1)

        self.kutu.addLayout(iptal_tamam,15,2,1,2)
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
        if self.kontrol==1:
            b=int(self.tahsilatMktar.text())
        else:
            b=0
        self.gelir.setText(str(b-a))
        self.gider.setText(str(a))
        return 0

    def kutuEkle(self):
        if self.tahsilat.currentText()=="Yapıldı":
            self.tahsilatMktar=QLineEdit("0")
            self.tahsil.addWidget(self.tahsilatMktar)
            self.kontrol=1
        else:
            try:
                self.tahsilatMktar.close()
                self.kontrol=0
            except:
                print()

    def katilim_ekle(self):
        k=self.katilan.currentText()
        self.katilim_list.append(k)
        self.katilanlar.append(k) 

    def tamam(self):
        firma=self.isletme.currentText()
        rapor=self.rapor.text()
        fatura=self.fatura.currentText()
        if self.kontrol==1:
            tahsilat=self.tahsilatMktar.text()
            toplam=int(tahsilat)
        else:
            tahsilat=self.tahsilat.currentText()
            toplam=0
        notlar=self.notlar.toPlainText()
        katilan=self.katilanlar.toPlainText()
        yemek=int(self.yemek.text())
        yakit=int(self.yakit.text())
        diger=int(self.diger.text())
        net=toplam-(yemek+yakit+diger)


        if "" not in [firma,rapor,fatura,tahsilat,toplam,katilan]:
            for i in self.katilim_list:
                ekle("danisman_ek",i)
            self.close()










































    def iptal(self):
        self.close()



