# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IaFloatMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.veiwGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwGraphButton.setGeometry(QtCore.QRect(20, 110, 260, 31))
        self.veiwGraphButton.setObjectName("veiwGraphButton")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(20, 190, 82, 31))
        self.settingsButton.setObjectName("settingsButton")
        self.quitToSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToSelectButton.setGeometry(QtCore.QRect(200, 190, 80, 31))
        self.quitToSelectButton.setObjectName("quitToSelectButton")
        self.editDataPointButton = QtWidgets.QPushButton(self.centralwidget)
        self.editDataPointButton.setGeometry(QtCore.QRect(20, 150, 260, 31))
        self.editDataPointButton.setObjectName("editDataPointButton")
        self.addNewDPandGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNewDPandGraphButton.setGeometry(QtCore.QRect(20, 70, 260, 31))
        self.addNewDPandGraphButton.setObjectName("addNewDPandGraphButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 40, 260, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.helpMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpMenuButton.setGeometry(QtCore.QRect(110, 190, 82, 31))
        self.helpMenuButton.setObjectName("helpMenuButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.veiwGraphButton.setText(_translate("MainWindow", "Veiw Graphs"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.quitToSelectButton.setText(_translate("MainWindow", "Quit to Select"))
        self.editDataPointButton.setText(_translate("MainWindow", "Veiw And Edit Data Points"))
        self.addNewDPandGraphButton.setText(_translate("MainWindow", "Add New Data Point and Graph"))
        self.label.setText(_translate("MainWindow", "Floating Data"))
        self.helpMenuButton.setText(_translate("MainWindow", "Help Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
