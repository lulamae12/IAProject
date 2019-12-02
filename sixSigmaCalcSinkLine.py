import pandas,numpy,sys
from statistics import stdev
import lineGraphFloat
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
    df = pandas.read_csv(fileName)
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
        floatPercent = round((floatL[i] / totalL[i]) * 100,1)
        floatPercents.append(floatPercent)
        
def sinkPercent(totalL,sinkL):
    del sinkPercents[:]
    for i in range(len(sinkL)):
        sinkPercent = round((sinkL[i] / totalL[i]) * 100,1)
        sinkPercents.append(sinkPercent)


###########################################################################

def findAverage(sinkPercents):# return average of list
    itemCount =  len(sinkPercents)
    total = 0
    for percentage in sinkPercents:
        total = total + percentage
        
    average = total/itemCount
    print(average)
    return average

def standardDeviation(sinkPercents):#return std of floats
    std = stdev(sinkPercents)
    print(std)
    return std

def findControlLimits(average,std,uclTarget,roundTo100):#return sigma count and control limits based on how many stds to get to 100%
    currentSigma =  average
    lclAvg = average
    sigmaCount = 0

    
    while currentSigma <= round(uclTarget,0):
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
    averageN = findAverage(sinkPercents)
    std = standardDeviation(sinkPercents)
    
    with open("sinkSettings.txt","r") as settingsFile:
        lines = settingsFile.readlines()
        uclTarget = int(lines[0])

    
    
    
    
    ucl,lcl,sigmas = findControlLimits(averageN,std,uclTarget,roundTo100)

    print("Sigmas: ",sigmas)
    print("Upper control limit: ",ucl)
    print("lower control limit: ",lcl)


    return sigmas,ucl,lcl



def callLineGraphs(sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates):
    graphSink.plotGraphs(sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates)




#average = findAverage(floatPercents)
#standardDeviation(floatPercents)


print("\n")

#ssigmas,ucl,lcl = updateControls(100,True)
#floatGraphs = lineGraphFloat.FloatGraphs(3,ucl,lcl,average,floatPercents,sinkPercents,dates)

def call():
    dataSet = getDataFrame("sinking_data.csv")
    getDates()
    getSinkWeight()
    getFloatWeight()
    totalWeight(sinkingWeights,floatingWeights)
    floatPercent(totalWeights,floatingWeights)
    sinkPercent(totalWeights,sinkingWeights)
    
    average = findAverage(sinkPercents)
    
    sigmas,ucl,lcl = updateControls(100,True)
    
    sinkGraphs = lineGraphSink.SinkGraphs(3,ucl,lcl,average,floatPercents,sinkPercents,dates)
    #floatGraphs.lineGraph()
#dataSet = getDataFrame("floating_data.csv")