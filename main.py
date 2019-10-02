import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit, QWidget, QVBoxLayout, QMessageBox
import floatOrSinkMenu as floatOrSinkMenu
from floatMainMenu import *

floatOrSinkMenu.main()
running = True
while running:
    
    
    if floatOrSinkMenu.floatingPressed():
        print("pressed")
    


