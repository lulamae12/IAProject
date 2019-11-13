import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np




sigmas = ""
ucl = ""
lcl = ""
average = ""
floatPercentsAr = []
sinkPercents = []
datesL = []





def plotLineGraph():
    
    y = np.array(floatPercentsAr,float)

    
    
    print(datesL)
    print(len(datesL))
    
    #for percentage in floatPercents:
    plt.plot(datesL,y, linestyle='-', marker='o', color='b')
   
    plt.show()




def main():
    print("asasas")
    plotLineGraph()

def getValues(sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates):
    
    sigmas = sigmas
    ucl = ucl
    lcl = lcl
    average = average
    for item in floatPercents:
        floatPercentsAr.append(item)
    
    for item in dates:
        datesL.append(item)
    

    
    print(floatPercents)
    main()


