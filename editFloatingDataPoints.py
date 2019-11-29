# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editFloatingDatapoints.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 51, 301, 291))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSpacing(5)
        self.removeEntryButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeEntryButton.setGeometry(QtCore.QRect(15, 360, 301, 31))
        self.removeEntryButton.setObjectName("removeEntryButton")
        self.returnToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToMenuButton.setGeometry(QtCore.QRect(15, 400, 301, 31))
        self.returnToMenuButton.setObjectName("returnToMenuButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(15, 40, 301, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 10, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.entries = self.fillList("floatData.txt")
        
        print(self.entries)

        self.fillTable(self.entries)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def fillList(self,list):
        entries = []
        with open(str(list),"r") as entryFile:
            for entry in entryFile.readlines():
                entries.append(entry)
                print(entry,"\n")
                
        #print(entries)
        return entries
    def formatEntry(self,item):
        
        item = json.loads(item)
        date = item["date"]
        sinkingWeight = item["sink"]
        floatingWeight = item["float"]
    
        formattedString = "Entry Date: " + str(date) + "\nSinking Plastic Weight: " + str(sinkingWeight) + "\nFloating Plastic Weight: " + str(floatingWeight) 

        print(formattedString)


        return(formattedString)


    def fillTable(self,entryList):
        for item in entryList:
            item = self.formatEntry(item)
            
            self.listWidget.addItem(item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.removeEntryButton.setText(_translate("MainWindow", "Remove Selected Entry"))
        self.returnToMenuButton.setText(_translate("MainWindow", "Return To Menu"))
        self.label.setText(_translate("MainWindow", "Edit Floating Data"))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
