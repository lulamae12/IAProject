import pandas,numpy,sys,os
from statistics import stdev
import lineGraphFloat
import tkinter as tk
from tkinter import ttk
#Things i need to calculate:
# percent floating
# percent sinking
# average of float% or sink % data
# standard deviation
# UCL & LCL
#
#################################################################################
#init
#################################################################################
dates = []
floatingWeights = []
sinkingWeights = []
totalWeights = []
floatPercents = []
sinkPercents = []
dataSet = []



def getDataFrame(fileName):
    global dataSet
    del dataSet[:]
    cwd = os.getcwd()
    df = pandas.read_csv(os.path.join(cwd,"Float Data\\",fileName))
    print(df)
    dataset = df.values.tolist()
    for item in dataset:
        dataSet.append(item)
    print(dataset)
    
    return dataset

def getDates():
    global dates
    print("dates: ",dates)
    
    del dates[:]
    print("dataset: ",dataSet)
    print("dates after del: ",dates)
    for items in dataSet:
        #print(items[0])
        
        
        dates.append(items[0])
    print("dates: ", dates)

def getFloatWeight():
    del floatingWeights[:]
    for items in dataSet:
        #print(items[1])
        floatingWeights.append(items[2])

def getSinkWeight():
    del sinkingWeights[:]
    for items in dataSet:
        #print(items[2])
        sinkingWeights.append(items[1])

def totalWeight(sinkL,floatL): #get total weight of sink weight and float weight and add to list
    del totalWeights[:]
    for i in range(len(sinkL)):
        totalWeightItem = sinkL[i] + floatL[i]
        totalWeights.append(totalWeightItem) 
def floatPercent(totalL,floatL):
    
    del floatPercents[:]
    for i in range(len(floatL)):
        #PROBLEM IS HERE SOMEWHERE
        print(floatL[i])
        print(totalL[i])
        floatPercent = round((floatL[i] / totalL[i]) * 100,1)
        floatPercents.append(floatPercent)
        print("floatPercent def ",floatPercent)
    print(floatPercents)
def sinkPercent(totalL,sinkL):
    del sinkPercents[:]
    for i in range(len(sinkL)):
        sinkPercent = round((sinkL[i] / totalL[i]) * 100,1)
        sinkPercents.append(sinkPercent)


###########################################################################

def findAverage(floatPercents):# return average of list
    itemCount =  len(floatPercents)
    total = 0
    for percentage in floatPercents:
        total = total + percentage
        
    average = total/itemCount
    print(average)
    return average

def standardDeviation(floatPercents):#return std of floats

    #check if all items in list are the same value
    if floatPercents.count(floatPercents[0]) == len(floatPercents):
        
        floatPercents[0] = floatPercents[0] + 0.1
        popupmsg("STD is ~ 0. Please verify your data is correct")
    std = stdev(floatPercents)    

    

    print(floatPercents)
    print("std func",std)
    
    return std
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Close", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def findControlLimits(average,std,uclTarget,roundTo100):#return sigma count and control limits based on how many stds to get to 100%
    currentSigma =  average
    lclAvg = average
    sigmaCount = 0
    
    
    #gets stuck here
    while currentSigma <= round(uclTarget,0):
        print("ucl targee",round(uclTarget,0))
        print("Current sigma",currentSigma)
        print("std",std)
        currentSigma = currentSigma + std
        sigmaCount = sigmaCount + 1
        
    
    ucl = uclTarget
    
    if roundTo100:
        ucl = round(ucl,0)

    for sigma in range(sigmaCount):
        lclAvg = lclAvg - std
    lcl = lclAvg
    
    #ucl = 100
    
    return ucl,lcl,sigmaCount

def UCL(average,std,sigmas,roundTo100):#calc upper control sigmas is test. roundTo100 rounds it down to 100
    ucl = average
    for sigma in range(sigmas):
        ucl = ucl + std
    
    if roundTo100:
        ucl = round(ucl,0)
    print(ucl)
    print("hellllllo")
    return ucl

#def LCL(average,std):#calc lower control sigmas is test
def updateControls(uclTarget,roundTo100):
    print("float percent",floatPercents)
    averageN = findAverage(floatPercents)
    std = standardDeviation(floatPercents)
    
    with open("floatSettings.txt","r") as settingsFile:
        lines = settingsFile.readlines()
        uclTarget = int(lines[0])

    
    
    
    
    ucl,lcl,sigmas = findControlLimits(averageN,std,uclTarget,roundTo100)

    print("Sigmas: ",sigmas)
    print("Upper control limit: ",ucl)
    print("lower control limit: ",lcl)


    return sigmas,ucl,lcl



def callLineGraphs(sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates):
    graphFloat.plotGraphs(sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates)




#average = findAverage(floatPercents)
#standardDeviation(floatPercents)


print("\n")

#ssigmas,ucl,lcl = updateControls(100,True)
#floatGraphs = lineGraphFloat.FloatGraphs(3,ucl,lcl,average,floatPercents,sinkPercents,dates)

def call():
    dataSet = getDataFrame("floating_data.csv")
    getDates()
    getSinkWeight()
    getFloatWeight()
    totalWeight(sinkingWeights,floatingWeights)
    floatPercent(totalWeights,floatingWeights)
    sinkPercent(totalWeights,sinkingWeights)
    
    try:
        average = findAverage(floatPercents)
    except ZeroDivisionError:
        popupmsg("Error! 2 or more values must be given to view this graph!")
        return None
    
    try:
       
        sigmas,ucl,lcl = updateControls(100,True)
        
    except:
        
        popupmsg("Error! 2 or more values must be given to view this graph!")
        return None
    
    floatGraphs = lineGraphFloat.FloatGraphs(3,ucl,lcl,average,floatPercents,sinkPercents,dates)
    #floatGraphs.lineGraph()
#dataSet = getDataFrame("floating_data.csv")