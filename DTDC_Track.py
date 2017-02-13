import requests as r
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import time
start=time.time()
class GettrackData:
    track = []
    root = Tk()
    root.withdraw()
    jdata = []
    rdict = {'activityType': '', 'dateWithNoSuffix': '', 'deliveryStatus': '', 'origin': '', 'time': '',
                 'orgCode': '',
                 'mode': ''}
    def openfile () :
        path = filedialog.askopenfilename(filetype=(("txt", "*.txt"), ("All Files", "*.*")))
        file = open(path, 'r')
        return file
    def readfile():         #Read Opened File
        for i in GettrackData.openfile():
            GettrackData.track.append(i.strip("\n"))
        return GettrackData.track

    def SaveFile(self):

            file=open("Tracking_Result.txt",'a')
            file.write(("\n"+GettrackData.rdict['dateWithNoSuffix']+" "+GettrackData.rdict['time']
                          +" "+GettrackData.rdict['activityType']+"("+GettrackData.rdict['origin']+") "+GettrackData.rdict['deliveryStatus']))

    def getjsondata(track):
            i=track
            url="http://track.dtdc.com/ctbs-tracking/customerInterface.tr?submitName=getLoadMovementDetails&cnNo="+str(GettrackData.track[i])
            try:
                data=r.get(url)
            finally:
                wfile = open("Tracking_Result.txt", 'a')
                jdata = data.json()
                jdata.reverse()
                for jin in jdata:
                    for i in jin:
                        if i in GettrackData.rdict:
                            GettrackData.rdict[i]=jin[i]
                            # uncomment this for detailed records
                    """print(GettrackData.rdict['dateWithNoSuffix']+" "+GettrackData.rdict['time']
                          +" "+GettrackData.rdict['activityType']+" ("+GettrackData.rdict['origin']+") "+GettrackData.rdict['deliveryStatus'])"""

                wfile.close()

rcords=GettrackData.readfile()

for i in range(len(rcords)):
    print("\n"+"Record for  " + GettrackData.track[i])
    GettrackData.getjsondata(i)
    print("Latest updates are "+GettrackData.rdict['deliveryStatus']+" at "+GettrackData.rdict['origin']+"( "+GettrackData.rdict['activityType']+")")
#print("Your Tracking Details are stored in Tracking_Results.txt\nExiting Windows Please wait")
print("%s Seconds"%(time.time()-start))