import cv2
import pickle
try:
    with open("pos",'rb')as f:
            places=pickle.load(f)
except:
    places=[]
    
cap=cv2.VideoCapture(0) #capturer la video de la camera
e = 0
drawing = False
ix,iy = -1,-1
# fonction qui permet de definir les positions des parking et de definir le nombre des pixels qu il contient
#et ajouter les coordonnees et description des places au fichier 'pos'
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, e , c
    if event == cv2.EVENT_LBUTTONDOWN:
      drawing = True
      ix = x
      iy = y
    elif event == cv2.EVENT_LBUTTONUP:
      drawing = False
      count(frame,ix, iy, x, y)
      places.append((ix, iy, x, y, e, c)) 
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pts in enumerate(places):
            x0, y0, x1 ,y1 ,e ,c = pts
            if x0 < x < x1 and y0 < y < y1 :
                places.pop(i)
    with open('pos', 'wb') as f:
        pickle.dump(places, f) 
        
#fonction qui fait un "thresholding" pour compter les nombres des pixels "nonzero" 
def count(f,x0,y0,x1,y1):
    global c
    gray=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)#conversion frame to gray
    frameBlur=cv2.GaussianBlur(gray,(5,5),1)#application d un "flou" ou "blur" avec un filtre gaussian
    frameThreshold=cv2.adaptiveThreshold(frameBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,105,9)  
    #segmenter le frame en sorte que le blanc et noir seront inversé
    crop=frameThreshold[y0:y1,x0:x1] #definir la zone de calcule de pixels
    c=cv2.countNonZero(crop) #calcule de nombres de pixels
        
while True:
    success,frame=cap.read()
    if success==False:
        break
    frame=cv2.resize(frame,(640,480)) 
    for key,pts in enumerate(places):
        cv2.rectangle(frame,(pts[0],pts[1]),(pts[2],pts[3]),(0,0,255),2) 
        #dessiner un rectange autours des position des parkings
        cv2.putText(frame,str(key)+"|"+str(pts[5]),(pts[0],pts[1]),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2) 
        #ecrire le numero du parking et le nombre de pixels correspondant
    cv2.imshow("Frame", frame) #afficher l image
    cv2.setMouseCallback("Frame",draw_rectangle) #dessiner les rectangle qui definissent les positions
    cv2.waitKey(5)
    if cv2.waitKey(1) & 0xFF == ord('q'): #exit si on click sur 'q'
        break
cap.release()
cv2.destroyAllWindows()
