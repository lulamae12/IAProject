import json
dataSet = []


#Things i need to calculate:
# percent floating
# percent sinking
# average of float% or sink % data
# standard deviation
# UCL & LCL
# 
def getDataSet(fileName):
    dataSetJsonFormat = {}
    with open(fileName,"r") as dataSetFile:
        for entry in dataSetFile.readlines():
            entry = entry.replace("\n","")
            dataSetJsonFormat = json.loads(entry)
            
            for value in dataSetJsonFormat.values():
                
                data = []
                data.append(value)
                print(data)



    dataSetFile.close()
    #print(dataSet)
    #print(dataSetJsonFormat)
getDataSet("floatData.txt")


#def calculateAverage():
