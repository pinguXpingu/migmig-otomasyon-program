'''
Created on 30 Mar 2020

@author: ata
'''
from PyQt5.Qt import QWidget, QLabel, QGridLayout, QLineEdit, QPushButton,\
    QHBoxLayout, QTextEdit, QComboBox
import time
from mimo_modules import yazdırUlan, penceroye, orta


class pen_tespit(QWidget):
    '''
    Ziyaret ve Tespit Formu için
    '''

    def __init__(self):
        super(pen_tespit,self).__init__()
        self.setWindowTitle("Ziyaret Formu Doldur")
        self.setWindowModality(2)

        izgara=QGridLayout()
        e_1=QLabel("Firma:")
        e_2=QLabel("Danışman:")
        e_3=QLabel("Değerlendirme:")

        self.b_1=QComboBox()
        self.b_1.addItem("")
        self.b_1.addItem("Galatasaray AŞ")
        self.b_1.addItem("AC Milan")
        self.b_1.addItem("Liverpool FC")
        self.b_1.addItem("Valencia CF")
        self.b_2=QComboBox()
        self.b_2.addItem("")
        self.b_2.addItem("Mehmet Atasoy")
        self.b_2.addItem("Manuel Rui Costa")
        self.b_2.addItem("Cesare Maldini")
        self.b_3=QTextEdit()

        izgara.addWidget(e_1,1,1)
        izgara.addWidget(e_2,2,1)
        izgara.addWidget(e_3,3,1)
        izgara.addWidget(self.b_1,1,2)
        izgara.addWidget(self.b_2,2,2)
        izgara.addWidget(self.b_3,3,2)


        buton_1=QPushButton("Tamam")
        buton_1.clicked.connect(self.yazdirmaca)
        izgara.addWidget(buton_1,4,2)

        self.setLayout(izgara)
        
    def yazdirmaca(self):
        x=self.b_1.currentText()
        y=self.b_2.currentText()
        z=self.b_3.toPlainText()
        
        sayfa=form_tespit(x,y,z)
        sayfa.show()



class form_tespit(QWidget):
    '''
    Ziyaret ve Tespit Formu yazdırma için
    '''


    def __init__(self,x,y,z):
        super(form_tespit,self).__init__()
        self.setWindowTitle("Ziyaret ve Tespit Formu")
        self.setWindowModality(2)
        self.setFixedWidth(794)
        
        self.x=x
        self.y=y
        self.z=z

        kutu=QGridLayout()

        baslik=QLabel("ZİYARET VE TESPİT FORMU")
        baslik.setStyleSheet("QLabel{font:bold 16pt;\
        qproperty-alignment:AlignCenter;}")#border:1px solid red;}")
        baslik.setFixedHeight(32)
        
        tarih=QLabel()
        tarih.setStyleSheet("QLabel{qproperty-alignment:AlignLeft;}")
        t=(f"Rapor Tarihi: {time.strftime('%d/%m/%Y %A')}")
        tarih.setText(t)
        
        kutu.addWidget(baslik,1,1,1,5)
        kutu.addWidget(tarih,2,1)
        
        bosluk=QLabel()
        bosluk.setMinimumHeight(16)
        kutu.addWidget(bosluk,3,1)
        
        isletme_E=QLabel("TEHLİKELİ MADDE FAALİYET BELGESİ SAHİBİ İŞLETMENİN")
        isletme_E.setStyleSheet("QLabel{font:bold italic}")
        unvan_E=QLineEdit("TİCARİ ÜNVANI")
        unvan_E.setReadOnly(True)
        unetNo_E=QLineEdit("U-NET NO")
        unetNo_E.setReadOnly(True)
        vergiNo_E=QLineEdit("VERGİ NO")
        vergiNo_E.setReadOnly(True)
        belgeNo_E=QLineEdit("BELGE NO")
        belgeNo_E.setReadOnly(True)
        
        unvan=QTextEdit()
        unvan.setMaximumHeight(64)
        unvan.setText(self.x)
        unvan.setAlignment(orta)
        unetNo=QTextEdit()
        unetNo.setMaximumHeight(64)
        vergiNo=QTextEdit()
        vergiNo.setMaximumHeight(64)
        belgeNo=QTextEdit()
        belgeNo.setMaximumHeight(64)
        
        
        kutu.addWidget(isletme_E,4,1,1,5)
        kutu.addWidget(unvan_E,5,1)
        kutu.addWidget(unvan,6,1)
        kutu.addWidget(unetNo_E,5,2)
        kutu.addWidget(unetNo,6,2)
        kutu.addWidget(vergiNo_E,5,3)
        kutu.addWidget(vergiNo,6,3)
        kutu.addWidget(belgeNo_E,5,4,1,2)
        kutu.addWidget(belgeNo,6,4,1,2)

###############################################################################
        kutu.addWidget(bosluk,7,1)

        tmgd_E=QLabel("TEHLİKELİ MADDE GÜVENLİK DANIŞMANLIK KURULUŞU BELGESİ SAHİBİ İŞLETMENİN")
        tmgd_E.setStyleSheet("QLabel{font:bold italic}")
        tmgd_unvan_E=QLineEdit("TİCARİ ÜNVANI")
        tmgd_unvan_E.setReadOnly(True)
        tmgd_unetNo_E=QLineEdit("U-NET NO")
        tmgd_unetNo_E.setReadOnly(True)
        tmgd_vergiNo_E=QLineEdit("VERGİ NO")
        tmgd_vergiNo_E.setReadOnly(True)
        tmgd_belgeNo_E=QLineEdit("BELGE NO")
        tmgd_belgeNo_E.setReadOnly(True)

        tmgd_unvan=QTextEdit()
        tmgd_unvan.setMaximumHeight(64)
        tmgd_unetNo=QTextEdit()
        tmgd_unetNo.setMaximumHeight(64)
        tmgd_vergiNo=QTextEdit()
        tmgd_vergiNo.setMaximumHeight(64)
        tmgd_belgeNo=QTextEdit()
        tmgd_belgeNo.setMaximumHeight(64)

        kutu.addWidget(tmgd_E,8,1,1,5)
        kutu.addWidget(tmgd_unvan_E,9,1)
        kutu.addWidget(tmgd_unvan,10,1)
        kutu.addWidget(tmgd_unetNo_E,9,2)
        kutu.addWidget(tmgd_unetNo,10,2)
        kutu.addWidget(tmgd_vergiNo_E,9,3)
        kutu.addWidget(tmgd_vergiNo,10,3)
        kutu.addWidget(tmgd_belgeNo_E,9,4,1,2)
        kutu.addWidget(tmgd_belgeNo,10,4,1,2)
        
###############################################################################
        kutu.addWidget(bosluk,11,1)

        tmgd_kutu=QHBoxLayout()
        tmgd2_kutu=QHBoxLayout()
        
        tmgdci_E=QLabel("TEHLİKELİ MADDE GÜVENLİK DANIŞMANININ")
        tmgdci_E.setStyleSheet("QLabel{font:bold italic}")
        tmgdci_belgeNo_E=QLineEdit("BELGE NO")
        tmgdci_belgeNo_E.setReadOnly(True)
        tmgdci_belgeNo_E.setMaximumWidth(96)
        tmgdci_adisoyadi_E=QLineEdit("ADI SOYADI")
        tmgdci_adisoyadi_E.setReadOnly(True)
        tmgdci_kimlikno_E=QLineEdit("TC KİMLİK NO")
        tmgdci_kimlikno_E.setReadOnly(True)
        tmgdci_kimlikno_E.setMaximumWidth(128)
        tmgdci_cepno_E=QLineEdit("CEP TELEFONU")
        tmgdci_cepno_E.setReadOnly(True)
        tmgdci_cepno_E.setMaximumWidth(128)
        tmgdci_eposta_E=QLineEdit("E-POSTA")
        tmgdci_eposta_E.setReadOnly(True)

        tmgdci_belgeNo=QLineEdit("ADR-7865")
        tmgdci_belgeNo.setMaximumWidth(96)
        tmgdci_adisoyadi=QLineEdit()
        tmgdci_adisoyadi.setText(self.y)
        tmgdci_kimlikno=QLineEdit("49021076694")
        tmgdci_kimlikno.setMaximumWidth(128)
        tmgdci_cepno=QLineEdit("0531 464 4150")
        tmgdci_cepno.setMaximumWidth(128)
        tmgdci_eposta=QLineEdit("cevrem33@gmail.com")

        tmgd_kutu.addWidget(tmgdci_belgeNo_E)
        tmgd_kutu.addWidget(tmgdci_adisoyadi_E)
        tmgd_kutu.addWidget(tmgdci_kimlikno_E)
        tmgd_kutu.addWidget(tmgdci_cepno_E)
        tmgd_kutu.addWidget(tmgdci_eposta_E)
        tmgd2_kutu.addWidget(tmgdci_belgeNo)
        tmgd2_kutu.addWidget(tmgdci_adisoyadi)
        tmgd2_kutu.addWidget(tmgdci_kimlikno)
        tmgd2_kutu.addWidget(tmgdci_cepno)
        tmgd2_kutu.addWidget(tmgdci_eposta)
        
        kutu.addWidget(tmgdci_E,12,1)
        kutu.addLayout(tmgd_kutu,13,1,1,5)
        kutu.addLayout(tmgd2_kutu,14,1,1,5)

###############################################################################
        kutu.addWidget(bosluk,15,1)

        degerlendirme_E=QLabel("İŞLETME İÇİN GEREK GÖRÜLEN DEĞERLENDİRME VE ÖNERİLER")
        degerlendirme_E.setStyleSheet("QLabel{font:bold italic}")
        degerlendirme=QTextEdit()
        degerlendirme.setText(self.z)
        degerlendirme.setMaximumHeight(64)

        kutu.addWidget(bosluk,16,1)
        kutu.addWidget(degerlendirme_E,17,1,1,5)
        kutu.addWidget(degerlendirme,18,1,1,5)

###############################################################################
        kutu.addWidget(bosluk,19,1)

        imza_kutusu=QHBoxLayout()
        imza2_kutusu=QHBoxLayout()

        tmgd_imza_E=QLineEdit("Hazırlayan TMGD")
        isletme_imza_E=QLineEdit("Onaylayan İşletme Yetkilisi")

        imza_kutusu.addWidget(tmgd_imza_E)
        imza_kutusu.addWidget(isletme_imza_E)

        tmgd_imza=QTextEdit("İmza:")
        tmgd_imza.setMaximumHeight(64)
        isletme_imza=QTextEdit("İmza:")
        isletme_imza.setMaximumHeight(64)

        imza2_kutusu.addWidget(tmgd_imza)
        imza2_kutusu.addWidget(isletme_imza)

        kutu.addLayout(imza_kutusu,20,1,1,5)
        kutu.addLayout(imza2_kutusu,21,1,1,5)

###############################################################################
        kutu.addWidget(bosluk,22,1)

        self.yaz_buton=QPushButton("Yazdır")        
        self.yazdirma=yazdırUlan(self.yaz_buton,self)
        self.yaz_buton.clicked.connect(self.yazdirma.yazdir)

        kutu.addWidget(self.yaz_buton,23,5)


        kutu.setVerticalSpacing(0)
        kutu.setHorizontalSpacing(0)
        self.setLayout(kutu)
        self.setStyleSheet(penceroye)





