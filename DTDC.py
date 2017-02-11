import requests as r
rdict={'activityType':'','dateWithNoSuffix':'','deliveryStatus':'','origin':'','time':'','orgCode':'','mode':''}
track=[]
path=input("Enter path of Your file")
file=open(path,"r")
print("Name of File"+file.name)
for i in file:
    track.append(i.splitlines())
print(track[0])
for j in range(len(track)):
    url="http://track.dtdc.com/ctbs-tracking/customerInterface.tr?submitName=getLoadMovementDetails&cnNo="+str(str(str(track[j]).replace("[",'')).replace("]",'')).strip("'")
    print("Your Tracking Details of Tracking Id"+str(track[j]))
    fetched=r.get(url)
    json_data=fetched.json()
    for ind in json_data:
        for i in ind:
            rdict[i]=ind[i]
        #print("Date "+rdict['dateWithNoSuffix']+" Time "+rdict['time']+" "+rdict['activityType']+" "+rdict['origin'])
    print("Lates Updates are "+"Date "+json_data[0]['dateWithNoSuffix']+" Time "+json_data[0]['time']+" "+json_data[0]['activityType']+" "+json_data[0]['origin'])