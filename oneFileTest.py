from PyQt5 import QtCore, QtGui, QtWidgets
import sys,datetime,json
from PyQt5.QtWidgets import QMessageBox
import sixSigmaCalcFloatLine as SSCFL
import csvMaker as csvMaker


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
    
    
    
    @staticmethod#static binds the function just to object, in this case window, instead of float pressed
    def floatPressed(self):
        #call run class and run flmm section
        runClass("floatMainMenu")


    def sinkingPressed(self):
        #sinkPressed()
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindsow"))
        self.floatingButton.setText(_translate("MainWindow", "Floating"))
        self.sinkingButton.setText(_translate("MainWindow", "Shrinking"))
        self.label.setText(_translate("MainWindow", "Would you like to run the program for floating or shrinking?"))


#choose what graph to run
class floatChooseGraphType(object):
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

        self.returnToFloatMenuButton.clicked.connect(self.backButtonPressed)
        
        self.veiwLineGraphFloatButton.clicked.connect(self.veiwLineGraphPressed)

    #go back to add data point menu
    @staticmethod
    def backButtonPressed(self):
        runClass("floatMainMenu")
    
    #veiw Linegraph
    @staticmethod
    def veiwLineGraphPressed(self):
        csvMaker.create("floatData.txt")
        SSCFL.call()#six sigma calc flaot line graph    





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


#main menu for float data
class floatMainMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewGraphButton.setGeometry(QtCore.QRect(80, 200, 260, 31))
        self.viewGraphButton.setObjectName("viewGraphButton")
        
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(80, 280, 131, 31))
        self.settingsButton.setObjectName("settingsButton")
        self.quitToSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToSelectButton.setGeometry(QtCore.QRect(210, 280, 131, 31))
        self.quitToSelectButton.setObjectName("quitToSelectButton")
        self.editDataPointButton = QtWidgets.QPushButton(self.centralwidget)
        self.editDataPointButton.setGeometry(QtCore.QRect(80, 240, 260, 31))
        self.editDataPointButton.setObjectName("editDataPointButton")
        self.addNewDPandGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNewDPandGraphButton.setGeometry(QtCore.QRect(80, 160, 260, 31))
        self.addNewDPandGraphButton.setObjectName("addNewDPandGraphButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 120, 260, 31))
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
        self.label.setGeometry(QtCore.QRect(150, 100, 121, 31))
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

        #Back to float main menu
        self.quitToSelectButton.clicked.connect(self.backButtonPressed)

        self.addNewDPandGraphButton.clicked.connect(self.addPointsPressed)
        self.viewGraphButton.clicked.connect(self.graphSelection)

    #run graph selection class
    @staticmethod
    def graphSelection(self):
        runClass("floatChooseGraphType")

    @staticmethod
    def backButtonPressed(self):
        runClass("floatOrSinkMenu")

    @staticmethod
    def addPointsPressed(self):
        runClass("fmmAddDP")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Float Data - Main Menu"))
        self.viewGraphButton.setText(_translate("MainWindow", "view Graphs"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.quitToSelectButton.setText(_translate("MainWindow", "Quit to Select"))
        self.editDataPointButton.setText(_translate("MainWindow", "view And Edit Data Points"))
        self.addNewDPandGraphButton.setText(_translate("MainWindow", "Add New Data Point"))
        self.label.setText(_translate("MainWindow", "Floating Data"))



class fmmAddDP(object):
    def setupUi(self, MainWindow):
        self.currentDateCBChecked = True
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 377)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sinkingWeightTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.sinkingWeightTextBox.setEnabled(True)
        self.sinkingWeightTextBox.setGeometry(QtCore.QRect(220, 70, 111, 21))
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
        self.floatingWeightTextBox.setGeometry(QtCore.QRect(220, 100, 111, 21))
        self.floatingWeightTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.floatingWeightTextBox.setObjectName("floatingWeightTextBox")
        self.useCurrentDatecheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.useCurrentDatecheckBox.setGeometry(QtCore.QRect(30, 160, 171, 20))
        self.useCurrentDatecheckBox.setObjectName("useCurrentDatecheckBox")
        self.useCurrentDatecheckBox.toggle()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 181, 41))
        self.label_3.setObjectName("label_3")
        self.dateTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.dateTextBox.setEnabled(True)
        self.dateTextBox.setGeometry(QtCore.QRect(220, 130, 111, 21))
        self.dateTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dateTextBox.setObjectName("dateTextBox")
        #get date and disable date box
        self.dateTextBox.setDisabled(True)
        self.currentDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentDateLabel.setGeometry(QtCore.QRect(190, 160, 121, 20))
        self.currentDateLabel.setObjectName("currentDateLabel")
        self.currentDateLabel.setText(_translate("MainWindow", self.currentDateFormatted()))
        
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 271, 31))
        self.pushButton.setObjectName("pushButton")#veiw graphs
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
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(110, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
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
        
        self.useCurrentDatecheckBox.stateChanged.connect(lambda:self.dateCBEval(self.useCurrentDatecheckBox))#lambda fycbiton call checkbox eval

        self.pushButton.clicked.connect(self.addPoint)

        self.quitToMenuButton.clicked.connect(self.backButtonPressed)
        self.pushButton_2.clicked.connect(self.graphSelection)

    #run graph selection class
    @staticmethod
    def graphSelection(self):
        runClass("floatChooseGraphType")
    #go back to flaot main menu
    @staticmethod
    def backButtonPressed(self):
        runClass("floatMainMenu")
    
    #create error message based on input
    def createErrorMessage(self,title,message):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Critical)
        errorMsg.setText(title)
        errorMsg.setInformativeText(message)
        errorMsg.setWindowTitle(title)
        errorMsg.exec()

    def dateCBEval(self,checkbox):#toggle text box
        if checkbox.isChecked() == True:
            self.dateTextBox.setDisabled(True)
        else:
            self.dateTextBox.setDisabled(False)
        

    def addPoint(self):
        sinkWeightFloat = ""
        floatWeightFloat = ""
        
        if self.useCurrentDatecheckBox.isChecked():
            dateString = str(self.currentDateFormatted())
        else:
            dateString = self.dateTextBox.toPlainText()
        sinkWeightString = self.sinkingWeightTextBox.toPlainText()
        floatWeightString = self.floatingWeightTextBox.toPlainText()

        sinkErrorIn = False
        floatErrorIn = False
        try:
            sinkWeightFloat = float(sinkWeightString)
        except ValueError:
            self.createErrorMessage("Error!","Input for Sink Weight is Invalid!")
            sinkErrorIn = True
        try:
            floatWeightFloat = float(floatWeightString)
        except ValueError:
            self.createErrorMessage("Error!","Input for Float Weight is Invalid!")
            floatErrorIn = True

        if floatErrorIn != False or sinkErrorIn != False:
            print(floatErrorIn)
            print(sinkErrorIn)
            return None

        print(dateString)
        print(sinkWeightFloat)
        print(floatWeightFloat)
        
        
        data = self.makeJsonData(dateString,sinkWeightFloat,floatWeightFloat)
        self.saveToJson(data)
    
    #format data to json dict
    def makeJsonData(self,date,sinkWeight,floatWeight):
        
        data = {"date":date,"sink":sinkWeight,"float":floatWeight}
            
        print(data)
        return data
    #save data
    def saveToJson(self,data):
        with open('floatData.txt', 'a') as file:
            json.dump(data, file)
            file.write("\n")

         

        





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sinking weight (g) :"))
        self.label_2.setText(_translate("MainWindow", "Floating weight (g) :"))
        self.useCurrentDatecheckBox.setText(_translate("MainWindow", "use Current Date : "))
        self.label_3.setText(_translate("MainWindow", "Date ( MM/DD/YYYY) :"))
        
        self.pushButton.setText(_translate("MainWindow", "Add data point"))
        self.pushButton_2.setText(_translate("MainWindow", "Veiw Graphs"))
        self.label_4.setText(_translate("MainWindow", "Add Float Data point"))
        self.quitToMenuButton.setText(_translate("MainWindow", "Return to menu"))
    
    def currentDateFormatted(self):
        currentDate = datetime.date.today()
        day = currentDate.day
        month = currentDate.month
        year = currentDate.year

        formattedDate = "%s/%s/%s" % (month,day,year)

        return formattedDate









#class called to call another class. hows that for an alitteration?
def runClass(name):
    #must calll as a static method
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
