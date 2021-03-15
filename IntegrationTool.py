#Import   
import numpy as np
import scipy.integrate as integrate
import statistics as stats

import os
import re
import sys
filename = sys.argv[1]



###Parameter###
threshold = 60000 #Tradeoff between noise and signal. #Intensity counts of XIC #input("Please enter the threshold you want for integration of XIC") 

### time in amount of spectras needed to move the stage.

#84 = 58 spectra each 1s shot +26 spectra per stage move of 500ms, having a CT of 17ms. num is the last spectra number of a valid signal.
signalgap = 27 
signallength = 87

deviation = 3

###end of parameter###

# Integration and lists
#yerr = []
area = []
integrationpeak = []
peakintegration = []
omittedpeaks = []
belowthresholdpeaks = []

error = []
emptyobject = ''

abovethreshlist = []
blacklist = []
whitelist = []

formernum = 1


# File reading
with open(filename) as data:
    y = np.genfromtxt(
         data,
    #    (line.replace(',', '.') for line in data), # might be useful for data that is manually exported from the raw-files
        #skip_header=1,
        delimiter='\n') #,' )
    #    unpack=True)


with open('errfile.log', 'a') as f2:
    for num, row in enumerate(y, 1):
        if(row >= threshold/1.0 and num-1 not in whitelist): #make threshold float.
            abovethreshlist = [n for n in y[num:num+(signallength+deviation)]>=threshold/1.0] # For signals falling below the threshold. Nice list comprehension may suit the other loops as well, but are hard to get.
            # returns ooi error is the measurement is finished too fast.. should include error handling, but works almost every time
            if ( str(abovethreshlist).count("False") > 0 and str(abovethreshlist).count("True") > 0 ): #If the signal falls below threshold..
                if(num not in blacklist):
                    peakintegration.append( max(y[num:num+(signallength+deviation)]) ) # take the maximum of the signal and blacklist the rest of it to avoid splitting of signals.
                    whitelist.append(num) # Put it to a whitelist for integration
                    #print("listedAmbigous"+str(num)) # Debugging
                    for n in range(num+1,num+(signallength+deviation),1):
                        blacklist.append(n)
                    #print("blacklisted"+str(n)) # Debugging
            else:
                peakintegration.append(row)    # Proper signal, add to integration list
                #print("listed"+str(num)) #Debugging
        # check if not empty. Some peaks are in, integrate.  All values above threshold of the same shot are now added to peakintegration. Multiple lists are created. Each list represents a peak.                
        elif peakintegration and num-1 not in blacklist: 
            #print("integrated"+str(num)) #Debugging
            abovethreshlist = []
            spectradiff = (num-formernum)
            shot = int(spectradiff/signallength) # may not be ideal for >x.5, but round cannot round as one would expect it.  See https://stackoverflow.com/questions/56820/round-doesnt-seem-to-be-rounding-properly/15398691#15398691
            if ( spectradiff >= signalgap-deviation ) or shot > 1: #final plausability check. May filter some noise if the threshold and the minimum signal or maximum plasma noise are close
                if shot > 1:
                    for i in range(0,shot,1):
                        #print(str(num)+":"+str(i)+":"+str(shot)) #Debugging
                        #yerr.append(emptyobject) #this should tell how many zeros are in between two valid signals. The relative beginning is cut off. 
                        area.append(emptyobject) 
                    #print(str(num)+":"+str(shot)) #Debugging
                if(len(peakintegration)>1):
                    integrationpeak = integrate.cumtrapz(peakintegration) #integrates for each list record and adds to the initial value. Therefore, the last value (per list) is the one needed.
                    #print("integrated:"+str(num))#+":"+str(row)+":"+str(integrationpeak[-1])) #Debugging
                    #print("integrated:"+str(num)+":"+str(formernum)+":"+str(spectradiff)+":"+str(shot)) #Debugging
                    #yerr.append(stats.stdev(peakintegration)) #integrates for each list record and adds to the initial value. Therefore, the last value (per list) is the one needed.
                    area.append(integrationpeak[-1]) #only last element, see above.
                else:
                    #print("integrated:"+str(num))#+":"+str(formernum)+":"+str(spectradiff)+":"+str(shot)) #Debugging
                    area.append(peakintegration)
                formernum = num #only the last number is taken for next check
                #Some more debugging. Very useful stuff I imo
                #print(area)
                    #print(num)
                    #print(formernum)
                    #print(spectradiff)
                    #print((num-formernum)/signallength)
                    #print(len(peakintegration))
                    #print(max(peakintegration))
            else:
                omittedpeaks.append(num)
                #print("Omitted:"+str(num)+":"+str(spectradiff)+":"+str(signalgap-deviation)+":"+str(signalgap+deviation)) #Very useful debugging
            integrationpeak = [] #important, as things go nasty if we dont empty the list after integration
            peakintegration = []
        elif(row < threshold/1.0 and num not in blacklist): #handle the other peaks and store them somewhere..
            belowthresholdpeaks.append(row)
            #print("belowthreshold:"+str(num))
        elif num in blacklist:
            abovethreshlist = []
            belowthresholdpeaks.append(row)
            peakintegration = []
            #print("blacklist"+str(num)) #Debugging
        else:
            error.append(row)
            print("FATAL ERROR:"+str(num)) # I think this should be left on, cause this should not happen
                
    print("The threshold excluded peaks (usually noise) in "+str(filename)+":"+"\n"+"#####"+str(belowthresholdpeaks)+"######"+"\n", file=f2)
    print("Peaks of "+str(filename)+"above threshold failed plausbility tests:"+"\n"+"#####"+str(omittedpeaks)+"######"+"\n" , file=f2) 
    if(error):
        print(" !!!!! Unknown error in "+str(filename)+" !!!!!! Check list threshold, list row and peakintegration", file=f2)


    pattern =  re.compile(r'[^\d.,]+') #clear off anything other than ,. and floats
    area = pattern.sub('', str(area))
    #yerr = pattern.sub('', str(yerr))
  
#write to file  
with open('results_s.txt', 'a') as file:
    file.write(str(filename)+","+str(area)+"\n")#",YERR:,"+str(yerr)+
    file.close()
