import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit, QWidget, QVBoxLayout, QMessageBox
import floatOrSinkMenu as floatOrSinkMenu
import floatMainMenu
import asyncio,os,subprocess
subprocess.call(['python.exe', 'floatOrSinkMenu.py'])


running = True
#fsm = float or sink menu
def fsmFloatPressed():#if float key  
    return True
    
def fsmSinkPressed():
    return True

def closeWindow(fileDescriptor):
    os.system("taskkill /f /im " + fileDescriptor)




def runProgram():
    if __name__  == "__main__":
        floatOrSinkMenu.main()
    if fsmFloatPressed:
        #floatOrSinkMenu.ma
        #print(floatOrSinkMenu.fileno())
        closeWindow("float or Sink")
        print("float")
        floatMainMenu.MainWindow.show()


runProgram()