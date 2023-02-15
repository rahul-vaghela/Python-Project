
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os
from os.path import isfile, join
import datetime
import random




def dis_sig(ng,nr,nd,sg,sr,sd,eg,er,ed,wg,wr,wd):
    print("                                       ")
    print("                                       ")
    print("     East                    North     ")
    print("  Green :",eg,"            Green:",ng,"")
    print("  Red: ",er,"              Red:",nr,"  ")
    print("  Delta: ",ed,"            Delta:",nd,"")
    print("              |     !     |            ")
    print("              |     !     |            ")
    print("              |     !     |            ")
    print("              |     !     |            ")
    print("              |     !     |            ")
    print("    __________|     N     |__________  ")
    print("                                       ")
    print("                                       ")
    print("     -------- E           W ---------  ")
    print("                                       ")
    print("    ___________     S     ___________  ")
    print("              |     !     |            ")
    print("              |     !     |            ")
    print("              |     !     |            ")
    print("              |     !     |            ")
    print("              |     !     |            ")	
    print("     South                    West     ")
    print("  Green :",sg,"            Green:",wg,"")
    print("  Red: ",sr,"              Red:",wr,"  ")
    print("  Delta: ",sd,"            Delta:",wd,"")
    print("                                       ")
    print("                                       ")
    
    
def ini():
    car = random.randint(0,25)
    motorcycle= random.randint(0,20)
    truck=random.randint(0,4)
    bicycle = random.randint(0,15)
    bus = random.randint(0,8)
    
    #print( "car::",car," ","Motorcycle::",motorcycle,"  ","Truck::",truck," ","Bicycle::",bicycle," ","Bus::",bus)
    
    return [car,motorcycle,truck,bicycle,bus] 


def vid2dens(dr):
    vidcap3 = cv2.VideoCapture(3,cv2.CAP_DSHOW)
    vidcap1 = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    vidcap4 = cv2.VideoCapture(4,cv2.CAP_DSHOW)
    vidcap2 = cv2.VideoCapture(2,cv2.CAP_DSHOW)
    
    def getFrame(sec,dr):
        #ret0,img = vidcap0.read()
        #if (ret0):
        # Display the resulting frame
         #   cv2.imshow('Cam 0', img)

        if dr == "N":
            vidcap1.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap1.read()
            if hasFrames:
                cv2.imwrite("./images/N/image"+dat.strftime('%Y%m%d%H%M%S')+""+str(count)+".jpg", image)     # save frame as JPG file
        elif dr == "E":
            vidcap2.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap2.read()
            if hasFrames:
                cv2.imwrite("./images/E/image"+dat.strftime('%Y%m%d%H%M%S')+""+str(count)+".jpg", image)     # save frame as JPG file
        elif dr == "W":
            vidcap3.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap3.read()
            if hasFrames:
                cv2.imwrite("./images/W/image"+dat.strftime('%Y%m%d%H%M%S')+""+str(count)+".jpg", image)     # save frame as JPG file
        elif dr == "S":
            vidcap4.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap4.read()
            if hasFrames:
                cv2.imwrite("./images/S/image"+dat.strftime('%Y%m%d%H%M%S')+""+str(count)+".jpg", image)     # save frame as JPG file 
        else:
            vidcap1.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap1.read()
            if hasFrames:
                cv2.imwrite("./images/S/image"+dat.strftime('%Y%m%d%H%M%S')+""+str(count)+".jpg", image)     # save frame as JPG file
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
  
    vidcap3.release()
    vidcap1.release()
    vidcap2.release()
    vidcap4.release()
    cv2.destroyAllWindows()

    if dr == "N":
        pathIn= './images/N/'
    elif dr == "E":
        pathIn= './images/E/'
    elif dr == "W":
        pathIn= './images/W/'
    else: 
        pathIn= './images/S/'

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

