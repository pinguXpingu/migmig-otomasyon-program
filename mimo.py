'''
Created on 30 Mar 2020

@author: ata
'''
from PyQt5.Qt import QApplication
from anapen import anapen

if __name__ == '__main__':
    uygulama=QApplication([])
    p0=anapen()
    uygulama.exec()