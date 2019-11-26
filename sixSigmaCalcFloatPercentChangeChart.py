import pandas,numpy,sys
from statistics import stdev
import percentChangeGraphFloat

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
    
    del dates[:]
    for items in dataSet:
        
        
        
        dates.append(items[0])
    
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

def findAverage(floatPercents):# return average of list
    itemCount =  len(floatPercents)
    total = 0
    for percentage in floatPercents:
        total = total + percentage
        
    average = total/itemCount
    print(average)
    return average

def standardDeviation(floatPercents):#return std of floats
    std = stdev(floatPercents)
    print(std)
    return std

def findControlLimits(average,std,uclTarget,roundTo100):#return sigma count and control limits based on how many stds to get to 100%
    currentSigma =  average
    lclAvg = average
    sigmaCount = 0
    while currentSigma <= round(uclTarget,0):
        currentSigma = currentSigma + std
        sigmaCount = sigmaCount + 1
    
    ucl = currentSigma
    
    if roundTo100:
        ucl = round(ucl,0)

    for sigma in range(sigmaCount):
        lclAvg = lclAvg - std
    lcl = lclAvg
    return ucl,lcl,sigmaCount

def UCL(average,std,sigmas,roundTo100):#calc upper control sigmas is test. roundTo100 rounds it down to 100
    ucl = average
    for sigma in range(sigmas):
        ucl = ucl + std
    
    if roundTo100:
        ucl = round(ucl,0)
    print(ucl)
    return ucl


def updateControls(uclTarget,roundTo100):
    averageN = findAverage(floatPercents)
    std = standardDeviation(floatPercents)
    ucl,lcl,sigmas = findControlLimits(averageN,std,uclTarget,roundTo100)

    return sigmas,ucl,lcl




def call():
    dataSet = getDataFrame("floating_data.csv")
    getDates()
    getSinkWeight()
    getFloatWeight()
    totalWeight(sinkingWeights,floatingWeights)
    floatPercent(totalWeights,floatingWeights)
    sinkPercent(totalWeights,sinkingWeights)
    
    average = findAverage(floatPercents)
    
    sigmas,ucl,lcl = updateControls(100,True)
    
    floatGraphs = percentChangeGraphFloat.PercentFloatGraph(3,ucl,lcl,average,floatPercents,sinkPercents,dates)
call()