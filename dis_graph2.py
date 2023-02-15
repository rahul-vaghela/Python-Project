
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os
from os.path import isfile, join
import datetime
import random


def vid2dens(dr):
    if dr == "E":
        #pathIn= './images/E/'
        i=1
    elif dr == "N":
        #pathIn= './images/N/'
        i=2
    elif dr == "W":
        #pathIn= './images/W/'
        i=3
    elif dr == "S":
        #pathIn= './images/S/'
        i=4
    
    

    vidcap = cv2.VideoCapture(i,cv2.CAP_DSHOW)
    
    def getFrame(sec,dr):    
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
           cv2.imwrite("./images/NW/image"+dat.strftime('%Y%m%d%H%M%S')+""+str(count)+".jpg", image)     # save frame as JPG file
    
        return hasFrames
    
    sec = random.randint(1,5)
    frameRate = 3 #//it will capture image in each x second
    count=1
    dat= datetime.datetime.now()
    success = getFrame(sec,dr)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec,dr)
        if count == 2:
           break
  
    vidcap.release()
    cv2.destroyAllWindows()

    pathIn = "./images/NW/"

    

    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    files.sort(reverse=True)

    car = []
    motorcycle= []
    truck=[]
    bicycle = []
    bus = []

    for i in range(2):
        #print(files[i])
        filename=pathIn + files[i]
        im = cv2.imread(filename)
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)
        #print(len(files))    
        #for j in range(2):
        c1=label.count('car')
        car.append(c1)
        #print(car[i])
        t1 = label.count('truck')
        truck.append(t1)
        b1 = label.count('bus')
        bus.append(b1)
        b2 =label.count('bicycle')
        bicycle.append(b2)
        m1 = label.count('motorcycle')
        motorcycle.append(m1)


        print( "car::",car[i]," ","Motorcycle::",motorcycle[i],"  ","Truck::",truck[i]," ","Bicycle::",bicycle[i]," ","Bus::",bus[i])
    #print(car)
    s1=(car[0]+(motorcycle[0]/2)+truck[0]+(bicycle[0]/3)+bus[0])
    q1=(car[1]+(motorcycle[1]/2)+truck[1]+(bicycle[1]/3)+bus[1])
    
    ds = {
        "s1": s1,
        "q1": q1,
    }
    
    return ds

