from PyQt5 import QtCore, QtGui, QtWidgets
import sys,datetime,json,pickle,os,time
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import sixSigmaCalcFloatLine as SSCFL
import sixSigmaCalcFloatBar as SSCFB
import sixSigmaCalcFloatPercentChangeChart as SSCFPCC
import csvMaker as csvMaker
from tkinter import *
from tkinter.filedialog import askopenfilename



#choose what graph to run
class sinkChooseGraphType(object):
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
        self.veiwBarGraphFloatButton.clicked.connect(self.veiwBarGraphPressed)
        self.veiwLPercentageChangeFloatButton.clicked.connect(self.veiwSTDGraphPressed)

    #go back to add data point menu
    @staticmethod
    def backButtonPressed(self):
        runClass("floatMainMenu")
    
    #veiw Linegraph
    @staticmethod
    def veiwLineGraphPressed(self):
        csvMaker.create("floatData.txt")
        SSCFL.call()#six sigma calc float line graph    

    #veiw BarGraph
    @staticmethod
    def veiwBarGraphPressed(self):
        print("hi")
        csvMaker.create("floatData.txt")
        SSCFB.call()#six sigma calc float bar graph    

    #veiw std graph
    @staticmethod
    def veiwSTDGraphPressed(self):
        csvMaker.create("floatData.txt")
        SSCFPCC.call()#six sigma calc float bar graph    





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.veiwLineGraphFloatButton.setText(_translate("MainWindow", "Veiw Floating Percentage Data Line Graph"))
        self.label.setText(_translate("MainWindow", "Default graph. Contains UCL and LCL data for floating data percentages in a detailed line graph"))
        self.veiwBarGraphFloatButton.setText(_translate("MainWindow", "Veiw Floating Distribution Bar Graph"))
        self.label_2.setText(_translate("MainWindow", "Bar graph that shows the distribution of the percent of floating plastic versus the sinking plastic percentage."))
        self.veiwLPercentageChangeFloatButton.setText(_translate("MainWindow", "Veiw Floating Percentage Deviation Graph"))
        self.label_3.setText(_translate("MainWindow", "Graph that shows distrubitons from the mean of the dataset. Can be used as another way to analyze data from the line graph."))
        self.returnToFloatMenuButton.setText(_translate("MainWindow", "Return to Float menu"))
        self.label_4.setText(_translate("MainWindow", "Return to previous menu."))
        self.label_5.setText(_translate("MainWindow", "How would you like to veiw your data?"))


#main menu for float data
class sinkMainMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewGraphButton.setGeometry(QtCore.QRect(20, 110, 260, 31))
        self.viewGraphButton.setObjectName("viewGraphButton")
        
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(20, 190, 260, 31))
        self.settingsButton.setObjectName("settingsButton")
        self.quitToSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitToSelectButton.setGeometry(QtCore.QRect(150, 230, 131, 31))
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
        self.helpMenuButton.setGeometry(QtCore.QRect(20, 230, 128, 31))
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

        #Back to float main menu
        self.quitToSelectButton.clicked.connect(self.backButtonPressed)

        self.addNewDPandGraphButton.clicked.connect(self.addPointsPressed)
        
        
        self.viewGraphButton.clicked.connect(self.graphSelection)
        
        
        self.editDataPointButton.clicked.connect(self.veiwAndEditDatapoints)

        self.settingsButton.clicked.connect(self.floatSettingsPressed)


    #run graph selection class
    @staticmethod
    def graphSelection(self):
        runClass("floatChooseGraphType")

    @staticmethod
    def backButtonPressed(self):
        runClass("floatOrSinkMenu")

    @staticmethod
    def addPointsPressed(self):
        runClass("smmAddDP")

    @staticmethod
    def veiwAndEditDatapoints(self):
        runClass("editFloatDataPoint")

    #run settings
    @staticmethod
    def floatSettingsPressed(self):
        runClass("floatSettings")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sinking Data - Main Menu"))
        self.viewGraphButton.setText(_translate("MainWindow", "view Graphs"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.quitToSelectButton.setText(_translate("MainWindow", "Quit to Select"))
        self.editDataPointButton.setText(_translate("MainWindow", "view And Edit Data Points"))
        self.addNewDPandGraphButton.setText(_translate("MainWindow", "Add New Data Point"))
        self.label.setText(_translate("MainWindow", "Floating Data"))
        self.helpMenuButton.setText(_translate("MainWindow", "Help Menu"))


class smmAddDP(object):
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

#edit fmm data points
class editFloatDataPoint(object):
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

        #get current item
        self.currentItem = ""
        self.listWidget.itemSelectionChanged.connect(self.returnSelectedItem)

    




        #return to menu
        self.returnToMenuButton.clicked.connect(self.returnToMenuPressed)
        
        #remove entry pressed
        
        #lamba im using kinda like static
        #maybe better than static for non class things?
        self.removeEntryButton.clicked.connect(lambda: self.removeEntryPressed(self.currentItem))
    


    #return active item
    def returnSelectedItem(self):
        selectedItem = self.listWidget.currentItem().text()
        print(selectedItem)
        self.currentItem = selectedItem
        print("current item")
        print(self.currentItem)


    def removeEntryPressed(self,currentItem):
        entryStr = currentItem
        self.confirmDeleteMessage(entryStr)


    def removeItemFromList(self,item,file):
        #HOW WORKS
        #FIND DATA IN FILE AND THEN WRITE BACK TO FILE EXCLUDING ORIGNINAL DATA POINT
        dataLines = []
        
        itemData = item.strip("\n")
        itemData = itemData.replace("Entry Date: ","")
        itemData = itemData.replace("Sinking Plastic Weight: ",":")
        itemData = itemData.replace("Floating Plastic Weight: ",":")
        itemData = itemData.replace("\n","")
        
        itemDataList = itemData.split(":")

        date = itemDataList[0]
        sinking = itemDataList[1]
        floating = itemDataList[2]
        
        
        print("====================================")
        print("itemData: ",itemDataList)
        print("====================================")

        

        with open(str(file),"r") as entryFile:
            for entry in entryFile.readlines():
                dataLines.append(entry)
        entryFile.close

        for line in dataLines:
            lineJson = json.loads(line)
            
            

            if str(lineJson["date"]) == str(date) and str(lineJson["sink"]) == str(sinking) and str(lineJson["float"]) == str(floating):
                print("MATCH FOUND")
                print(lineJson)
                print(itemDataList)
                lineToExclude = line#exclude this line during writeback thus deleting it

                print("Lines: ",dataLines)

                with open(str(file),"r") as entryFile:
                    lines = entryFile.readlines()
                with open(str(file),"w") as entryFile:
                    for line in lines:
                        
                        if line != lineToExclude:
                            entryFile.write(line)
                        else:
                            print("LINE REMOVED")
                self.createAlertPopup("Removed!","Entry was removed succesfully!","Entry Removed!")
                
                runClass("editFloatDataPoint") #it updates

    def createAlertPopup(self,title,message,winTitle):
        alertMsg = QMessageBox()
        alertMsg.setIcon(QMessageBox.Information)
        alertMsg.setText(title)
        alertMsg.setInformativeText(message)
        alertMsg.setWindowTitle(winTitle)
        alertMsg.exec()

    @staticmethod
    def returnToMenuPressed(self):
        runClass("floatMainMenu")

    def confirmDeleteMessage(self,item):
        item = item.replace("----------------------------------------------------","")

        confirmDeleteMessagebox= QMessageBox()
        confirmDeleteMessagebox.setIcon(QMessageBox.Warning)
        confirmDeleteMessagebox.setText("Are you sure you would like to delete the following entry? This action cannot be undone.")
        
        
        confirmDeleteMessagebox.setInformativeText(item)
        confirmDeleteMessagebox.setWindowTitle("Confirm Deletion?")
        confirmDeleteMessagebox.addButton(QMessageBox.Yes)
        confirmDeleteMessagebox.addButton(QMessageBox.No)
        confirmDeleteMessagebox.exec()
        buttonResult = confirmDeleteMessagebox.clickedButton().text() #could cause probs
        buttonResult= buttonResult.replace("&","").lower()
        
        print(buttonResult)

        if buttonResult == "yes":#yes button is pressed
            print("yes")
            self.removeItemFromList(item,"floatData.txt")
        
        if buttonResult == "no":#no button is pressed
            print("nomegalul")
            pass
        
        

       

    def fillList(self,list):
        entries = []
        with open(str(list),"r") as entryFile:
            for entry in entryFile.readlines():
                entries.append(entry)
                print(entry,"\n")
                
        #print(entries)
        entryFile.close()
        return entries



    def formatEntry(self,item):
        
        item = json.loads(item)
        date = item["date"]
        sinkingWeight = item["sink"]
        floatingWeight = item["float"]

        #==================================
        #----------------------------------------------------
        formattedString = "----------------------------------------------------\nEntry Date: " + str(date) + "\nSinking Plastic Weight: " + str(sinkingWeight) + "\nFloating Plastic Weight: " + str(floatingWeight) +"\n----------------------------------------------------" 

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





class floatSettings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 411, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.uclTargetInput = QtWidgets.QTextEdit(self.centralwidget)
        self.uclTargetInput.setGeometry(QtCore.QRect(220, 80, 41, 21))
        self.uclTargetInput.setAcceptDrops(True)
        self.uclTargetInput.setAutoFillBackground(False)
        self.uclTargetInput.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uclTargetInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.uclTargetInput.setObjectName("uclTargetInput")
        self.setUclTargetButton = QtWidgets.QPushButton(self.centralwidget)
        self.setUclTargetButton.setGeometry(QtCore.QRect(270, 80, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setUclTargetButton.setFont(font)
        self.setUclTargetButton.setObjectName("setUclTargetButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.uclTargetLabel = QtWidgets.QLabel(self.centralwidget)
        self.uclTargetLabel.setGeometry(QtCore.QRect(170, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uclTargetLabel.setFont(font)
        self.uclTargetLabel.setObjectName("uclTargetLabel")
        self.exportDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportDataButton.setGeometry(QtCore.QRect(20, 180, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exportDataButton.setFont(font)
        self.exportDataButton.setObjectName("exportDataButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.importDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.importDataButton.setGeometry(QtCore.QRect(20, 250, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.importDataButton.setFont(font)
        self.importDataButton.setObjectName("importDataButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.resetDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetDataButton.setGeometry(QtCore.QRect(20, 390, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resetDataButton.setFont(font)
        self.resetDataButton.setObjectName("resetDataButton")
        self.returnToMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnToMenuButton.setGeometry(QtCore.QRect(20, 460, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returnToMenuButton.setFont(font)
        self.returnToMenuButton.setObjectName("returnToMenuButton")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 150, 201, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.createBackupButton = QtWidgets.QPushButton(self.centralwidget)
        self.createBackupButton.setGeometry(QtCore.QRect(20, 320, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createBackupButton.setFont(font)
        self.createBackupButton.setObjectName("createBackupButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 340, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.updateUclLabel()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.returnToMenuButton.clicked.connect(self.returnToMenuPressed)

        self.setUclTargetButton.clicked.connect(lambda: self.settingsSetUcl())

        self.exportDataButton.clicked.connect(lambda: self.exportFloatData("floatDataExported.ssg"))

        self.importDataButton.clicked.connect(lambda: self.importFloatData())

        self.resetDataButton.clicked.connect(lambda: self.clearAllData())
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Float Settings"))
        self.label_2.setText(_translate("MainWindow", "Upper Control Limit Target: "))
        self.setUclTargetButton.setText(_translate("MainWindow", "Set"))
        self.label_3.setText(_translate("MainWindow", "Current UCL Target:"))
        self.label_4.setText(_translate("MainWindow", "Sets the upper control limit target. Default = 100"))
        self.uclTargetLabel.setText(_translate("MainWindow", "100"))
        self.exportDataButton.setText(_translate("MainWindow", "Export Data"))
        self.label_5.setText(_translate("MainWindow", "Export floating data in .SSG format so that it can be reimported to the program elsewhere "))
        self.label_6.setText(_translate("MainWindow", "Import floating data in .SSG format so that it can be used."))
        self.importDataButton.setText(_translate("MainWindow", "Import Data"))
        self.label_7.setText(_translate("MainWindow", "Resets all floating data"))
        self.resetDataButton.setText(_translate("MainWindow", "Reset all Floating Data"))
        self.returnToMenuButton.setText(_translate("MainWindow", "Return To Menu"))
        self.createBackupButton.setText(_translate("MainWindow", "Create a Data Backup"))
        self.label_8.setText(_translate("MainWindow", "Import floating data in .SSG format so that it can be used."))

        self.updateUclLabel()
        
    


    @staticmethod
    def returnToMenuPressed(self):
        runClass("floatMainMenu")
    
    def settingsSetUcl(self):
        
        
        uclString = self.uclTargetInput.toPlainText()
        
        
        try:
            uclInt = round(int(uclString),0)
        except ValueError:
            self.createErrorMessage("Value Error","Error! Value must be a whole number (ex. '100') not a decimal or non numeric value.)")
            return

        print("ucl int: ",uclInt)

        
        
        with open("floatSettings.txt","w") as settingsFile:
            
            
            settingsFile.write(str(uclInt))
        settingsFile.close()
        self.updateUclLabel()

    def updateUclLabel(self):

        try:
            with open("floatSettings.txt","r") as settingsFile:
                
                
                lines = settingsFile.readlines()
                print(lines)
            settingsFile.close()
        except FileNotFoundError:
            with open("floatSettings.txt","w") as settingsFile:
                
                
                settingsFile.write("100")
            settingsFile.close()
            with open("floatSettings.txt","r") as settingsFile:
                
                
                lines = settingsFile.readlines()
                print(lines)
            settingsFile.close()
        
        ucl = lines[0]
        self.uclTargetLabel.setText(str(ucl))
    

    #create error message based on input
    def createErrorMessage(self,title,message):
        errorMsg = QMessageBox()
        errorMsg.setIcon(QMessageBox.Critical)
        errorMsg.setText(title)
        errorMsg.setInformativeText(message)
        errorMsg.setWindowTitle(title)
        errorMsg.exec()
    
    def createInfoMessage(self,title,message):
        infoMsg = QMessageBox()
        infoMsg.setIcon(QMessageBox.Information)
        infoMsg.setText(title)
        infoMsg.setInformativeText(message)
        infoMsg.setWindowTitle(title)
        infoMsg.exec()

    def exportFloatData(self,fileExportName):
        lines =[]
        cwd = os.getcwd()
        print("cwd: ",cwd)
        with open("floatData.txt","r") as floatData:
            lines = floatData.readlines() 
        floatData.close()

        #"floatDataExported.ssg"

        with open(fileExportName,"wb") as outfile:
            pickle.dump(lines,outfile)
        outfile.close()
        self.createInfoMessage("Data Exported Succesfully!","File: '"+ str(fileExportName) +"' has been exported to directory: " +str(cwd) +"")

    def importFloatData(self):
        root = Tk()
        
        root.withdraw() #don't want a full GUi keep the root window from appearing
        ftypes = [
        ('Six Sigma Grapher files', '*.ssg'),  
        ('All files', '*'), 
        ]
        
        filePath = askopenfilename(filetypes=ftypes) # show "Open" dialog box and return path
        
        if ".ssg" in filePath:
            print("acceptable file")

            
        

            confirmImportMessagebox= QMessageBox()
            confirmImportMessagebox.setIcon(QMessageBox.Warning)
            confirmImportMessagebox.setText("Are you sure you would like to import this data? This action cannot be undone and all current data will be overwritten.")
        

            
            confirmImportMessagebox.setWindowTitle("Import and Overwrite?")
            confirmImportMessagebox.addButton(QMessageBox.Yes)
            confirmImportMessagebox.addButton(QMessageBox.No)
            confirmImportMessagebox.exec()
            buttonResult = confirmImportMessagebox.clickedButton().text() #could cause probs
            buttonResult= buttonResult.replace("&","").lower()

            

            if buttonResult == "yes":#yes button is pressed
                print("yes")
                importedFile = open(filePath,"rb")
                importedFileData = pickle.load(importedFile)
                importedFile.close()
                print(importedFileData)
                print(type(importedFileData))
                
                with open("floatData.txt","w") as floatData:
                    for line in importedFileData:
                        floatData.write(line)
                floatData.close()
                self.createInfoMessage("File imported succesfully!","File: 'floatData.txt' has been imported succesfully!")

                
        
            if buttonResult == "no":#no button is pressed
                print("nomegalul")
                pass


        else:
            self.createErrorMessage("Invalid Filetype!","This is an invalid filetype! Only '.ssg' files are accepeted!")
            return
        

    def clearAllData(self):
        confirmDeleteMessagebox= QMessageBox()
        confirmDeleteMessagebox.setIcon(QMessageBox.Warning)
        confirmDeleteMessagebox.setText("Are you sure you would like to delete all data? This action is irreversible and all current data will be lost!")
    

        
        confirmDeleteMessagebox.setWindowTitle("Delete data?")
        confirmDeleteMessagebox.addButton(QMessageBox.Yes)
        confirmDeleteMessagebox.addButton(QMessageBox.No)
        confirmDeleteMessagebox.exec()
        buttonResult = confirmDeleteMessagebox.clickedButton().text() #could cause probs
        buttonResult= buttonResult.replace("&","").lower()

        if buttonResult == "yes":#yes button is pressed
            
            time.sleep(1)
            
            proceedMessagebox= QMessageBox()
            proceedMessagebox.setIcon(QMessageBox.Warning)
            proceedMessagebox.setText("Are you sure you would like proceed?")
        

            
            proceedMessagebox.setWindowTitle("Proceed?")
            proceedMessagebox.addButton(QMessageBox.Yes)
            proceedMessagebox.addButton(QMessageBox.No)
            proceedMessagebox.exec()
            proceedButtonResult =proceedMessagebox.clickedButton().text() #could cause probs
            proceedButtonResult= buttonResult.replace("&","").lower()

            if proceedButtonResult == "yes":#yes button is pressed
                print("proceeding to delete.")
                time.sleep(.3)
                print("proceeding to delete..")
                time.sleep(.3)
                print("proceeding to delete...")
                time.sleep(.3)
                print("Deleted!")

                currentDate = datetime.date.today()
                day = currentDate.day
                month = currentDate.month
                year = currentDate.year

                formattedDate = "%s-%s-%s" % (month,day,year)
        

                backupFileName = str("floatDataExported-Backup-"+formattedDate+".ssg")


                self.exportFloatData(str(backupFileName))
                
                
                
                with open("floatData.txt","w") as floatData:
                    floatData.write("")
                floatData.close()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                self.createInfoMessage("Data Deleted and Backup Created!","All exsiting data has been deleted. A backup of the data was saved to file '"+str(backupFileName)+"' before it was deleted.")


                

#callable class called to call another class. hows that for an alitteration?
def runClass(name):
    #must calll as a static method
    MainWindow.close
    className = eval(name)()
    className.setupUi(MainWindow)
    MainWindow.show

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
 
def run():

    while Running:
        continue


