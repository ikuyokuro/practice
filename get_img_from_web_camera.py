import os
from time import sleep

import cv2


cap = cv2.VideoCapture(1)
print("cap.grab()",cap.grab())
if cap.isOpened() is False:
   raise("IO Error")
print(cap.isOpened())
dirt = "20200615//4-1"
dirt = os.path.join(os.path.dirname(os.path.abspath(__file__)), dirt)
# dirt = f"c://Users//0465071//Python Scripts//make_dataset_for_OB_python//20200615//1-1"
print("save at: ", dirt)

if not os.path.exists(dirt):
   print("no dirctory to save images")
   raise Exception

for i in range(1,201):
   print(i,"-"*10)
   ret, frame = cap.read()
   cv2.imshow('camera capture', frame)
   cv2.waitKey(0)
   a = i
   while(True):
      if os.path.exists(dirt+f"//{a}.jpg"):
         a = a + 1
      else:
         break
   cv2.imwrite(dirt+f"//{a}.jpg", frame)
   # cv2.imwrite(path+f"\{i}.jpg", frame)
cv2.destroyAllWindows()


"""
ret, frame = cap.read()
cv2.imshow('camera capture', frame)
sleep(2)
ret, frame = cap.read()
cv2.imshow('camera capture', frame)
cap.release()
sleep(10)
"""