import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime
from matplotlib.widgets import Button,Slider
import matplotlib.patches as patches

class PercentFloatGraph(object):
    def __init__(self,sigmas,ucl,lcl,average,floatPercents,sinkPercents,dates,std):
        self.sigmas = sigmas
        self.ucl = ucl
        self.std = std  
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
        self.percentDevGraph()
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
    

    
    def percentDevGraph(self):
        print("self float percents: ",self.floatPercents)
        print("self float percents len : ",len(self.floatPercents))
        y = np.array(self.floatPercents,float)
        x = np.array(len(self.dates))
        print(len(self.dates))
        ##24th
        

        oneSig = self.average + self.std
        twoSig = self.average + self.std + self.std
        oneSigUnd = self.average - self.std
        twoSigUnd = self.average - self.std - self.std

        print(self.lcl,twoSigUnd,oneSigUnd,self.average,oneSig,twoSig, self.ucl)


        plt.yticks([self.lcl,twoSigUnd,oneSigUnd,self.average,oneSig,twoSig, self.ucl],["-3 σ","-2 σ","-1 σ","Average","+1 σ","+2 σ","+3 σ"])
        #plt.yticklabels({'y = 0','y = 50','y = 100'})
        #plt.yticks(y, step=0.2)
        #x = np.linspace(0.1,2*np.pi,10)
        #markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')
        
        
        # Create a color if the group is "B"
        my_color=np.where(y>=0, 'orange', 'skyblue')
        
        #plt.setp(baseline,"color","r","linewidth",2)
        plt.stem([0,1,2,3,4,5,6,7,8,9,10],y, use_line_collection=True,markerfmt=' ', bottom=self.average,color=my_color)
        
        plt.ylim(self.lcl - 1,self.ucl+1)
 

        



        plt.axhline(self.average, color='r', linestyle='-')#plot avg line
        
        # Don't mess with the limits!
        plt.autoscale(enable=False)
        
        plt.grid(axis="y")
        plt.show()