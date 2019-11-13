import json,csv,pandas
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
    data = []
    date = ""
    sink = ""
    floatV = ""
    with open(fileName,"r") as dataSetFile:
        for entry in dataSetFile.readlines():
            entry = entry.replace("\n","")
            dataSetJsonFormat = json.loads(entry)
            
            date = dataSetJsonFormat["date"]
            sink = dataSetJsonFormat["sink"]
            floatV = dataSetJsonFormat["float"]
            
            listItem = [date,sink,floatV]
            data.append(listItem)


            print(data)
    
    print("\n")
    
    for item in data:
        print(item[0])


    dataSetFile.close()
    
    return data


def createCSVFile(mode,dataList):

    #0 = create float
    if mode == 0:
        dates = []
        sinkingValues = []
        floatingValues = []
        for chunk in dataList:
            dates.append(chunk[0])
            sinkingValues.append(chunk[1])
            floatingValues.append(chunk[2])
        
        with open("floating_data.csv","w+", newline='') as csvFile:
            csvWriter = csv.writer(csvFile,delimiter=",")
            #swriter.writeheader()
            csvWriter.writerow(["Date","Float Weight","Sink Weight"])
            for item in dataList:
                csvWriter.writerow((item[0],item[1],item[2]))
        csvFile.close()





def readCsv(fileName):
    dataframe = pandas.read_csv(fileName)
    print(dataframe)




dataSet = getDataSet("floatData.txt")
createCSVFile(0,dataSet)

readCsv("floating_data.csv")

#def calculateAverage():
