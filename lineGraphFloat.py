import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.widgets import Button
import matplotlib.patches as patches
class FloatGraphs(object):


    def __init__(self,sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates):
        self.sigmas = sigmas
        self.ucl = ucl  
        self.lcl = lcl
        self.lineRunning = True
        self.barRunning = False
        avg = average
        self.average = avg
        self.floatPercents = floatPercents
        self.sinkPercents = sinkPercents
        self.dates = dates
        self.floatPercentsMin = self.listMin(floatPercents)
        self.floatPercentsMax = self.listMax(floatPercents)
        self.lineGraph()
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
    
    def lineGraph(self):
        print("self float percents: ",self.floatPercents)
        print("self float percents len : ",len(self.floatPercents))
        y = np.array(self.floatPercents,float)
        x = np.array(self.dates)
        xRange = len(x)
        print(xRange)
        
        
        print(x)
        plt.xlabel("Date")
        plt.ylabel("Percentage")
        


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


        


        # rotate and align the tick labels so they look better
        plt.gcf().autofmt_xdate()
        print(self.dates,len(self.dates))
        print(y,len(y))
        li = plt.plot(self.dates,y, linestyle='-', marker='o', color='b')
        
        xVals = li[0].get_xdata()
        yVals = li[0].get_ydata()

        uclPatch = patches.Patch(color="green",label="Upper Control Limit : " + str(self.ucl) )
        lclPatch = patches.Patch(color="red",label="Lower Control Limit : " + str(round(self.lcl,2)) )
        avgPatch = patches.Patch(color = "yellow",label="Average: "+str(round(self.average,2)))
        floatPatch = patches.Patch(color = "blue",label="Floating Percentage")

        plt.legend(bbox_to_anchor=(0., 1, 1., .102), loc='lower left',ncol=2,handles=[uclPatch,avgPatch,lclPatch,floatPatch],framealpha=1, mode="expand",title="Floating Graph", borderaxespad=0.9)
        #plt.legend(bbox_to_anchor=(1,0.5), loc='center right',handles=[uclPatch,avgPatch,lclPatch])
        
       
       


        #label points 
        for i in range(len(self.floatPercents)):
            plt.annotate(str(yVals[i]),(xVals[i],yVals[i]),textcoords="offset points",xytext=(0,10))
       


        
        plt.grid(True,which="both",axis="both")


 
       
        
       
        
        plt.show()
        
        
    #def next(self,event):

  
    #subPlots()
