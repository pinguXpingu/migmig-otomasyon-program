'''
Created on 30 Mar 2020

@author: ata
'''

import sqlite3,os
from PyQt5.Qt import QPrinter,QPrintDialog, QDialog, QByteArray, QBuffer,\
QTextDocument, QPushButton, QRadioButton, QGridLayout, QIntValidator,\
    QMessageBox
from PyQt5.QtCore import Qt
from time import time

def olustur():
    baglan=sqlite3.connect(db_dosyam)
    imlec=baglan.cursor()
    imlec.execute("create table firmalar(\
    isletme_no integer primary key, \
    isletme_adi varchar(50), \
    isletme_adresi varchar(50), \
    isletme_unetno varchar(8), \
    isletme_vergino varchar(11), \
    isletme_belgeno varchar(25),\
    eklenme_tarihi integer, \
    ziyaret_tarihi integer, \
    son_ziyaretci varchar(8), \
    rapor varchar(10), \
    fatura varchar(12), \
    tahsilat varchar(10)\
    notlar varchar(50)\
)")
    imlec.execute("create table danisman(\
    d_no integer primary key, \
    d_belgeno varchar(10), \
    d_adi_soyadi varchar(50), \
    d_kimlikno varchar(11), \
    d_telefon varchar(11), \
    d_eposta varchar(20),\
    eklenme_tarihi integer, \
    son_faaliyet integer\
)")
    imlec.execute("create table sirket(\
    tmgd_no integer primary key, \
    tmgd_adi varchar(50), \
    tmgd_belgeno varchar(25), \
    tmgd_unetno varchar(8), \
    tmgd_vergino varchar(11)\
)")
    imlec.execute("create table faaliyet(\
    f_no integer primary key, \
    f_tarih integer, \
    f_toplam integer, \
    f_net integer, \
    f_yemek integer, \
    f_yakit integer, \
    f_benzin integer, \
    f_motorin integer, \
    f_lpg integer, \
    f_diger integer, \
    f_katilimci varchar(20)\
)")


db_dosyam="./doc/migmigdb"
if not os.path.isfile(db_dosyam):
    olustur()

###############################################################################

def ekle(tablo,*args):
    zaman=time()
    baglan=sqlite3.connect(db_dosyam)
    imlec=baglan.cursor()
    if args:
        if tablo=="firmalar":
            imlec.execute(f"insert into firmalar(\
            isletme_adi,isletme_adresi,isletme_vergino,isletme_unetno,isletme_belgeno,rapor,fatura,tahsilat,notlar,eklenme_tarihi,ziyaret_tarihi)\
            values('{args[0]}','{args[1]}','{args[2]}','{args[3]}','{args[4]}','{args[5]}','{args[6]}','{args[7]}',null,{zaman},null\
            )")
        if tablo=="sirket":
            imlec.execute(f"insert into sirket(\
            tmgd_adi,tmgd_unetno,tmgd_vergino,tmgd_belgeno)\
            values('{args[0]}','{args[1]}','{args[2]}','{args[3]}')\
            ")
        if tablo=="danisman":
            imlec.execute(f"insert into danisman(\
            d_adi_soyadi,d_belgeno,d_kimlikno,d_telefon,d_eposta,eklenme_tarihi,son_faaliyet)\
            values('{args[0]}','{args[1]}','{args[2]}','{args[3]}','{args[4]}',{zaman},null)\
            ")
        if tablo=="danisman_ek":
            imlec.execute(f"update danisman\
            set son_faaliyet={zaman} where d_adi_soyadi='{args[0]}'")
    baglan.commit()
    baglan.close()


def getir(g,*args):
    baglan=sqlite3.connect(db_dosyam)
    imlec=baglan.cursor()
    if g=="firmalar":
        if args:
            imlec.execute(f"select * from firmalar where isletme_adi='{args[0]}'")
            x=imlec.fetchall()
        else:
            imlec.execute("select * from firmalar")
            x=imlec.fetchall()
    if g=="danışman":
        if args:
            imlec.execute(f"select * from danisman where d_adi_soyadi='{args[0]}'")
            x=imlec.fetchone()
        else:
            imlec.execute("select * from danisman")
            x=imlec.fetchall()
    if g=="şirket":
        if args:
            imlec.execute(f"select * from sirket where tmgd_adi='{args[0]}'")
            x=imlec.fetchall()
        else:
            imlec.execute("select * from sirket")
            x=imlec.fetchall()
    return x

def guncelle(*args):
    pass



def uyar(t):
    msg=QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(t)
    msg.exec_()



###############################################################################

class yazdırUlan:
    
    def __init__(self,buton,hedef):
        self.yazdir_butonu=buton
        self.hedef=hedef

    def yazdir(self):
        if self.soruSor()=="P":
            print("PDF'ye yazılacak")
        else:
            print("Yazıcıya gönderilecek")
        self.yazdir_butonu.hide()
        printer = QPrinter()
        yazdirPen=QPrintDialog(printer,self.hedef)
        if yazdirPen.exec_()==QPrintDialog.Accepted:
            printer.setPageSize(QPrinter.A4)
            printer.setOrientation(QPrinter.Portrait)
            printer.setResolution(600)
            printer.setColorMode(QPrinter.Color)
            size = printer.pageRect(QPrinter.DevicePixel).size()
            pixmap = self.hedef.grab().scaled(size.toSize(), Qt.KeepAspectRatio,Qt.SmoothTransformation)
            data = QByteArray()
            buffer = QBuffer(data)
            pixmap.save(buffer, 'PNG')
            document = QTextDocument()
            document.setPageSize(size)
            document.setHtml('<img src="data:image/png;base64,%s"/>' %
                             bytes(data.toBase64()).decode('ascii'))
            document.print_(printer)
            self.yazdir_butonu.show()
        else:
            self.yazdir_butonu.show()

    def soruSor(self):
        self.mesgBox=QDialog()
        self.s1=QRadioButton("PDF")
        self.s2=QRadioButton("Yazıcı")
        b1=QPushButton("Tamam")
        b1.clicked.connect(self.yaziciSec)
        a=QGridLayout()
        a.addWidget(self.s1,1,1)
        a.addWidget(self.s2,1,2)
        a.addWidget(b1,2,2)
        self.mesgBox.setLayout(a)
        self.mesgBox.exec()
        return self.yaziciSec()
        
    def yaziciSec(self):
        if self.s1.isChecked():
            self.mesgBox.close()
            return "P"
        if self.s2.isChecked():
            self.mesgBox.close()
            return "Y"

###############################################################################

buton_stili=("QPushButton:hover{background-color:#222; color:white}"\
             "QPushButton:pressed{color:#C4DF20}")
etiket_rengi1=("QLabel{color:red; qproperty-alignment: AlignRight;}")
etiket_rengi2=("QLabel{color:blue; qproperty-alignment: AlignRight;}")
etiket_hiza1=("QLabel{qproperty-alignment: AlignRight;}")

penceroye=("QLineEdit{qproperty-frame: true}"\
           "QWidget{background-color:white}"\
           "QLineEdit{qproperty-alignment: AlignCenter}")

rakam=QIntValidator
sag=Qt.AlignRight
sol=Qt.AlignLeft
orta=Qt.AlignCenter






















