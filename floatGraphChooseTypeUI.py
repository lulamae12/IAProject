# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'floatGraphTupe.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.veiwLineGraphFloatButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwLineGraphFloatButton.setGeometry(QtCore.QRect(10, 80, 411, 31))
        self.veiwLineGraphFloatButton.setObjectName("veiwLineGraphFloatButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.veiwBarGraphFloatButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwBarGraphFloatButton.setGeometry(QtCore.QRect(10, 150, 411, 31))
        self.veiwBarGraphFloatButton.setObjectName("veiwBarGraphFloatButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.veiwLPercentageChangeFloatButton = QtWidgets.QPushButton(self.centralwidget)
        self.veiwLPercentageChangeFloatButton.setGeometry(QtCore.QRect(10, 230, 411, 31))
        self.veiwLPercentageChangeFloatButton.setObjectName("veiwLPercentageChangeFloatButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.returnToFloatMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToFloatMenuButton.setGeometry(QtCore.QRect(10, 310, 411, 31))
        self.returnToFloatMenuButton.setObjectName("returnToFloatMenuButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 330, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 411, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
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
        self.veiwLineGraphFloatButton.setText(_translate("MainWindow", "Veiw Floating Percentage Data Line Graph"))
        self.label.setText(_translate("MainWindow", "Default graph. Contains UCL and LCL data for floating data percentages in a detailed line graph"))
        self.veiwBarGraphFloatButton.setText(_translate("MainWindow", "Veiw Floating Distribution Bar Graph"))
        self.label_2.setText(_translate("MainWindow", "Bar graph that shows the distribution of the percent of floating plastic versus the sinking plastic percentage."))
        self.veiwLPercentageChangeFloatButton.setText(_translate("MainWindow", "Veiw Floating Percentage Change Graph"))
        self.label_3.setText(_translate("MainWindow", "Graph that shows the percentage distrubiton from the mean of the dataset. can be used as another way to analyze data from the line graph."))
        self.returnToFloatMenuButton.setText(_translate("MainWindow", "Return to Float menu"))
        self.label_4.setText(_translate("MainWindow", "Return to previous menu."))
        self.label_5.setText(_translate("MainWindow", "How would you like to veiw your data?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
