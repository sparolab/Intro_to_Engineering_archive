import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 사람별로 데이터 저장하기 (1번 사람, 2번 사람, 3번 사람.. )
# 사람별로 데이터 저장하기 (1번 사람 저장 후 종료 -> 2번 사람 저장 후 종료)
face_id = input('\n type user id (1, 2, 3...) end press <enter> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")

count = 0

while(cam.isOpened()):
    ret, img = cam.read() # 이미지 읽어오기
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 색깔 -> 흑백
        faces = face_detector.detectMultiScale(gray, 1.3, 5) # 검출!

        for (x,y,w,h) in faces: # 얼굴이 검출 되었다!
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1 # 우린 30장만 저장할거니까, 몇번 검출되었는지 확인
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w]) # 검출된 얼굴들 저장하기 

            cv2.imshow('image', img) # 검출된 얼굴들 보여주기

        k = cv2.waitKey(100) & 0xff # 0.1초에 한번씩 찍도록! wait에 100ms
        if k == 27:
            break
        elif count >= 30: # 30장 다 찍었으면 이제 그만!
             break
    else:
        print('no camera!')
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


