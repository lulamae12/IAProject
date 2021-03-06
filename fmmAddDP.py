# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fmmAddDataPoint.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 377)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sinkingWeightTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.sinkingWeightTextBox.setEnabled(True)
        self.sinkingWeightTextBox.setGeometry(QtCore.QRect(220, 70, 81, 21))
        self.sinkingWeightTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sinkingWeightTextBox.setObjectName("sinkingWeightTextBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 151, 41))
        self.label_2.setObjectName("label_2")
        self.floatingWeightTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.floatingWeightTextBox.setEnabled(True)
        self.floatingWeightTextBox.setGeometry(QtCore.QRect(220, 100, 81, 21))
        self.floatingWeightTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.floatingWeightTextBox.setObjectName("floatingWeightTextBox")
        self.useCurrentDatecheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.useCurrentDatecheckBox.setGeometry(QtCore.QRect(30, 160, 171, 20))
        self.useCurrentDatecheckBox.setObjectName("useCurrentDatecheckBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 181, 41))
        self.label_3.setObjectName("label_3")
        self.dateTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.dateTextBox.setEnabled(True)
        self.dateTextBox.setGeometry(QtCore.QRect(220, 130, 81, 21))
        self.dateTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dateTextBox.setObjectName("dateTextBox")
        self.currentDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentDateLabel.setGeometry(QtCore.QRect(190, 160, 121, 20))
        self.currentDateLabel.setObjectName("currentDateLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 271, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 240, 271, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 271, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 271, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.quitToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToMenuButton.setGeometry(QtCore.QRect(30, 280, 271, 31))
        self.quitToMenuButton.setObjectName("quitToMenuButton")
        self.isPointAddedLabel = QtWidgets.QLabel(self.centralwidget)
        self.isPointAddedLabel.setGeometry(QtCore.QRect(110, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.isPointAddedLabel.setFont(font)
        self.isPointAddedLabel.setText("")
        self.isPointAddedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.isPointAddedLabel.setObjectName("isPointAddedLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
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
        self.label.setText(_translate("MainWindow", "Sinking weight (g) :"))
        self.label_2.setText(_translate("MainWindow", "Floating weight (g) :"))
        self.useCurrentDatecheckBox.setText(_translate("MainWindow", "use Current Date : "))
        self.label_3.setText(_translate("MainWindow", "Date ( MM/DD/YYYY) :"))
        self.currentDateLabel.setText(_translate("MainWindow", "MM/DD/YYYY"))
        self.pushButton.setText(_translate("MainWindow", "Add another data point"))
        self.pushButton_2.setText(_translate("MainWindow", "Add data point and Veiw Graph"))
        self.label_4.setText(_translate("MainWindow", "Add Float Data point"))
        self.quitToMenuButton.setText(_translate("MainWindow", "Save and quit to menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
