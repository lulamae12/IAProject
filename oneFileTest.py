from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class floatOrSinkMenu(object):
    
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
        self.floatingButton.clicked.connect(self.floatPressed)
        

        #sinking pressed
        self.sinkingButton.clicked.connect(self.sinkingPressed)
    
    def floatPressed(self):
        #call run class and run flmm section
        runClass("floatMainMenu")

    def sinkingPressed(self):
        #sinkPressed()
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.floatingButton.setText(_translate("MainWindow", "Floating"))
        self.sinkingButton.setText(_translate("MainWindow", "Shrinking"))
        self.label.setText(_translate("MainWindow", "Would you like to run the program for floating or shrinking?"))



class floatMainMenu(object):
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
        self.quitToSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToSelectButton.setGeometry(QtCore.QRect(210, 420, 131, 31))
        self.quitToSelectButton.setObjectName("quitToSelectButton")
        self.editDataPointButton = QtWidgets.QPushButton(self.centralwidget)
        self.editDataPointButton.setGeometry(QtCore.QRect(80, 380, 260, 31))
        self.editDataPointButton.setObjectName("editDataPointButton")
        self.addNewDPandGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNewDPandGraphButton.setGeometry(QtCore.QRect(80, 260, 260, 31))
        self.addNewDPandGraphButton.setObjectName("addNewDPandGraphButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 220, 260, 31))
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
        self.label.setGeometry(QtCore.QRect(150, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.veiwGraphButton.setText(_translate("MainWindow", "Veiw Graphs"))
        self.addDataPointButton.setText(_translate("MainWindow", "Add New Data Point"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.quitToSelectButton.setText(_translate("MainWindow", "Quit to Select"))
        self.editDataPointButton.setText(_translate("MainWindow", "Veiw And Edit Data Points"))
        self.addNewDPandGraphButton.setText(_translate("MainWindow", "Add New Data Point and Graph"))
        self.label.setText(_translate("MainWindow", "Floating Data"))


def runClass(name):
    MainWindow.close
    className = eval(name)()
    className.setupUi(MainWindow)
    MainWindow.show




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
fsm = floatOrSinkMenu()
fsm.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
