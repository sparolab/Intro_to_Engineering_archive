import cv2
import numpy as np
import os 


# 학습한 정보 분류기에 넣어주기
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# ID 별 이름 0, 1, 2, 3 순서
#         ['None', '<1번이름>', '<2번이름>']
# 첫번째는 'None'으로 놔둔다 (우리 iD는 1번에서 시작함)
names = ['None', 'Younggun'] 

# 카메라 시작하기
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# 얼굴은 최소한 원래 이미지 크기의 10%는 되어야 함
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, difference = recognizer.predict(gray[y:y+h,x:x+w])

        # difference로 검출 되었는지 확인
        if (difference < 100):
            id_name = names[id]
            confidence = "  {0}%".format(round(100 - difference))
        else:
            id_name = "unknown"
            confidence = "  {0}%".format(round(100 - difference))
        
        cv2.putText(img, str(id_name), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
