

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.veiwGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwGraphButton.setGeometry(QtCore.QRect(80, 340, 260, 31))
        self.veiwGraphButton.setObjectName("veiwGraphButton")
        self.addDataPointButton = QtWidgets.QPushButton(self.centralwidget)
        self.addDataPointButton.setGeometry(QtCore.QRect(80, 300, 260, 31))
        self.addDataPointButton.setObjectName("addDataPointButton")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(80, 420, 131, 31))
        self.settingsButton.setObjectName("settingsButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(230, 420, 111, 31))
        self.quitButton.setObjectName("quitButton")
        self.editDataPointButton = QtWidgets.QPushButton(self.centralwidget)
        self.editDataPointButton.setGeometry(QtCore.QRect(80, 380, 260, 31))
        self.editDataPointButton.setObjectName("editDataPointButton")
        self.addNewDPandGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNewDPandGraphButton.setGeometry(QtCore.QRect(80, 260, 260, 31))
        self.addNewDPandGraphButton.setObjectName("addNewDPandGraphButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 417, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #button fucntions

        self.quitButton.clicked.connect(self.quitProgram)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.veiwGraphButton.setText(_translate("MainWindow", "Veiw Graphs"))
        self.addDataPointButton.setText(_translate("MainWindow", "Add New Data Point"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.editDataPointButton.setText(_translate("MainWindow", "Veiw And Edit Data Points"))
        self.addNewDPandGraphButton.setText(_translate("MainWindow", "Add New Data Point and Graph"))

    def quitProgram(self, MainWindow):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
