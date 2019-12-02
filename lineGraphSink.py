import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime
from matplotlib.widgets import Button,Slider
import matplotlib.patches as patches

class SinkGraphs(object):


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
        self.sinkPercentsMin = self.listMin(sinkPercents)
        self.sinkPercentsMax = self.listMax(sinkPercents)
        self.lineGraph()
    def listMin(self,list):
        print(min(list))
        return min(list)
    def listMax(self,list):
        print(max(list))
        return max(list)
    def returnYLims(self,ucl,lcl,sinkPercentsMin,sinkPercentsMax):
        lowerYLim = 0
        upperYLim = 0
        

        if lcl < sinkPercentsMin:
            lowerYLim = lcl
        else:
            lowerYLim = sinkPercentsMin    
        if ucl > sinkPercentsMax:
            upperYLim = ucl
        else:
            upperYLim = sinkPercentsMax

        return lowerYLim,upperYLim
    
    def lineGraph(self):
        print("self sink percents: ",self.sinkPercents)
        print("self sink percents len : ",len(self.sinkPercents))
        y = np.array(self.sinkPercents,float)
        x = np.array(self.dates)
        xRange = len(x)
        print(xRange)
        

        fig, ax = plt.subplots(figsize=(7,6.6))
        plt.subplots_adjust(bottom=0.25)#create as subplot for better integration of sldier
        
        

        print(x)
        plt.xlabel("Date")
        plt.ylabel("Percentage")
        


        #setup graph limits
        yLimLow,yLimHigh = self.returnYLims(self.ucl,self.lcl,self.sinkPercentsMin,self.sinkPercentsMax)
        plt.ylim(yLimLow - 1,yLimHigh + 1)
        
        #create lcl and ucl lines
        print("lcl: ",self.lcl)
        plt.axhline(self.lcl, color='r', linestyle='-')#plot lcl line
        print("ucl: ",self.ucl)
        plt.axhline(self.ucl, color='g', linestyle='-')#plot ucl line
        
        
        #plot average line
        print("average: ",self.average)
        plt.axhline(self.average, color='y', linestyle='--')#plot lcl line


        plt.xlim(-1,7)


        # rotate and align the tick labels so they look better
        plt.gcf().autofmt_xdate()
        print(self.dates,len(self.dates))
        print(y,len(y))
        
        self.dates.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
       

        li = plt.plot(self.dates,y, linestyle='-', marker='o', color='b')
        
        xVals = li[0].get_xdata()
        yVals = li[0].get_ydata()

        uclPatch = patches.Patch(color="green",label="Upper Control Limit : " + str(self.ucl) )
        lclPatch = patches.Patch(color="red",label="Lower Control Limit : " + str(round(self.lcl,2)) )
        avgPatch = patches.Patch(color = "yellow",label="Average: "+str(round(self.average,2)))
        sinkPatch = patches.Patch(color = "blue",label="Sinking Percentage")

        plt.legend(bbox_to_anchor=(0., 1, 1., .10), loc='lower left',ncol=2,handles=[uclPatch,avgPatch,lclPatch,sinkPatch],framealpha=1, mode="expand",title="Sinking Percentage Graph", borderaxespad=0.9)
        #plt.legend(bbox_to_anchor=(1,0.5), loc='center right',handles=[uclPatch,avgPatch,lclPatch])
        
       
       


        #label points 
        for i in range(len(self.sinkPercents)):
            plt.annotate(str(yVals[i]),(xVals[i],yVals[i]),textcoords="offset points",xytext=(0,10))
       


        
        plt.grid(True,which="both",axis="both")

        #under is for slider subplot
        #create slider widget
        axpos = plt.axes([0.2, 0.01, 0.65, 0.03])
        positionSlider = Slider(axpos, 'Position: ', -1, len(self.dates),valfmt="%1.0f",dragging=True,valstep=None)

        def updatePosition(val):#update slider position and change axis veiw
            pos = positionSlider.val
            ax.axis([pos,pos+10,yLimLow - 1,yLimHigh + 1])
            fig.canvas.draw_idle()
        

        

        positionSlider.on_changed(updatePosition)#call on changed


 
       
        
       
        
        plt.show()
        
        
    #def next(self,event):

  
    #subPlots()
