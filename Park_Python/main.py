import cv2
import pickle
import numpy as np
import glob
import json
import requests
import lcdservo

cap=cv2.VideoCapture(0)  #capturer la video de la camera
with open("pos",'rb')as f:
     points=pickle.load(f)

vide = []

#fonction qui permet la detection des places si ils sont vides ou plennes a traver de la compararaison du pixel
#count de la place vide et du nouveau pixel count calculé de la meme facon
#si le numero pixels et > a numero initial , alors la place et "full=>e=1" sinon elle est "empty=>e=0"
def detect(f):
    for key,pts in enumerate(points) :
        x0,y0,x1,y1,e,c=pts
        crop=f[y0:y1,x0:x1]
        count=cv2.countNonZero(crop)
        if c==0:
            if count > 100:
                e=1
                cv2.putText(frame,str(count)+"/"+str(c),(x0,y0 -1),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
                cv2.rectangle(frame,(pts[0],pts[1]),(pts[2],pts[3]),(0,0,255),2)
            else:
                e=0
                cv2.putText(frame,str(count)+"/"+str(c),(x0,y0 -1),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
                cv2.rectangle(frame,(pts[0],pts[1]),(pts[2],pts[3]),(0,255,0),2)
        else:
            if c - c*80/100 < count < 2.5*c :
                e=0
                cv2.putText(frame,str(count)+"/"+str(c),(x0,y0 -1),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
                cv2.rectangle(frame,(pts[0],pts[1]),(pts[2],pts[3]),(0,255,0),2)
            if count > 2.5*c or c - c*80/100 > count :
                e=1
                cv2.putText(frame,str(count)+"/"+str(c),(x0,y0 -1),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
                cv2.rectangle(frame,(pts[0],pts[1]),(pts[2],pts[3]),(0,0,255),2)
        i=0    
        if e == 0:
            for vi in vide:
                if vi == key :
                    i=1
            if i == 0:
                vide.append(key)
                
        if e == 1:
            for v in vide:
                if v == key :
                    i=1
            if i ==1:
                vide.remove(key)

#fonction qui envoi les données "variables" au serveur pour qu ils seront afficher dans un site web
def addJson():
    with open("obj.json",mode="r") as jsonFile:
        model = json.load(jsonFile)
        model[0]["amount"]=len(points)
        model[1]["amount"]=len(vide)
        model[2]["amount"]=vide
        dumpJson=json.dumps(model)
        print(dumpJson)
    try:
        r = requests.post("http://192.168.43.5:65432", json=dumpJson)
    except Exception as inst:
        print(inst)      
def main():
    global frame,cap
    lcdservo.setup()
    while True:
        lcdservo.job(len(vide))
        success, frame = cap.read()
        if success==False:
            break
        frame=cv2.resize(frame,(640,480))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#conversion frame to gray
        frameBlur=cv2.GaussianBlur(gray,(5,5),1)#application d un "flou" ou "blur" avec un filtre gaussian
        frameThreshold=cv2.adaptiveThreshold(frameBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV,105,9)
        #segmenter le frame en sorte que le blanc et noir seront inversé
        detect(frameThreshold)
        cv2.putText(frame,f'FreeSpace:{len(vide)}/{len(points)} | {vide}',(50,50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
        addJson()
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


