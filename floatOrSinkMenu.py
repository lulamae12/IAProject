# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IaFloatORSink.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.floatingButton = QtWidgets.QPushButton(self.centralwidget)
        self.floatingButton.setGeometry(QtCore.QRect(10, 80, 331, 31))
        self.floatingButton.setObjectName("floatingButton")
        self.sinkingButton = QtWidgets.QPushButton(self.centralwidget)
        self.sinkingButton.setGeometry(QtCore.QRect(10, 120, 331, 31))
        self.sinkingButton.setObjectName("sinkingButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #floating pressed
        
        self.floatingButton.clicked.connect(self.floatingPressed)


    def floatingPressed(self):
        print('press')
        return True




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.floatingButton.setText(_translate("MainWindow", "Floating"))
        self.sinkingButton.setText(_translate("MainWindow", "Shrinking"))
        self.label.setText(_translate("MainWindow", "Would you like to run the program for floating or shrinking?"))

    



def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
