import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.widgets import Button
class FloatGraphs(object):


    def __init__(self,sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates):
        self.sigmas = sigmas
        self.ucl = ucl  
        self.lcl = lcl
        avg = average
        self.average = avg
        self.floatPercents = floatPercents
        self.sinkPercents = sinkPercents
        self.dates = dates
        self.floatPercentsMin = self.listMin(floatPercents)
        self.floatPercentsMax = self.listMax(floatPercents)
    def listMin(self,list):
        print(min(list))
        return min(list)
    def listMax(self,list):
        print(max(list))
        return max(list)
    def returnYLims(self,ucl,lcl,floatPercentsMin,floatPercentsMax):
        lowerYLim = 0
        upperYLim = 0
        

        if lcl < floatPercentsMin:
            lowerYLim = lcl
        else:
            lowerYLim = floatPercentsMin    
        if ucl > floatPercentsMax:
            upperYLim = ucl
        else:
            upperYLim = floatPercentsMax

        return lowerYLim,upperYLim
    
    
    @staticmethod
    def test(self):
        
        print("test")
    def lineGraph(self):
        y = np.array(self.floatPercents,float)
        x = np.array(self.dates)
        print(x)
        plt.xlabel("Dates")
        
        #setup graph limits
        yLimLow,yLimHigh = self.returnYLims(self.ucl,self.lcl,self.floatPercentsMin,self.floatPercentsMax)
        plt.ylim(yLimLow - 1,yLimHigh + 1)
        
        #create lcl and ucl lines
        print("lcl: ",self.lcl)
        plt.axhline(self.lcl, color='r', linestyle='-')#plot lcl line
        
        print("ucl: ",self.ucl)
        plt.axhline(self.ucl, color='g', linestyle='-')#plot lcl line
        
        
        #plot average line
        print("average: ",self.average)
        plt.axhline(self.average, color='y', linestyle='--')#plot lcl line





        li = plt.plot(self.dates,y, linestyle='-', marker='o', color='b')
        
        xVals = li[0].get_xdata()
        yVals = li[0].get_ydata()
        
        for i in range(len(self.floatPercents)):
            plt.annotate(str(yVals[i]),(xVals[i],yVals[i]),textcoords="offset points",xytext=(0,10))
        print(type(self.average))








        nextGraph = plt.axes([0.81, 0.01, 0.15, 0.05])#ButtonPosition
        bnext = Button(nextGraph, 'Next Graph')#Button
        bnext.on_clicked(self.test)#ButtonCallbackset
        
        plt.show()
        
    #def next(self,event):

  
    #subPlots()
