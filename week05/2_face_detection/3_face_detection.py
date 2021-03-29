import numpy as np # 이번엔 numpy라는 새로운 라이브러리를 불러왔음
import cv2 # 역시나 카메라 관련 라이브러리

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
# CascadeClassifier <- 얼굴 찾는 (이미지에서 얼굴 위치 찾기) 함수, 이미 만들어져 있음
# 이게 뭔지는 이해할 필요 없음 (어려움), 대신 이런 함수를 쓸 수 있다만 알고 넘어갑시다

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read() # 카메라에서 이미지 불러오기 (1장씩)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # RGB (색영상) -> Gray (흑백)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5
        ,     
        minSize=(20, 20)
    ) # 이 함수로 얼굴을 검출! 얼굴이 검출되면 faces 변수에 얼굴 위치들이 저장된다.

    for (x,y,w,h) in faces: # 저장된 얼굴 정보를 이미지에 표시하기 (파란색 네모)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

    cv2.imshow('video',img) # 화면에 보여주기

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
