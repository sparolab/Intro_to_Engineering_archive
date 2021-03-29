import cv2 # OpenCV 라이브러리 불러오기 (각종 카메라 관련)

cap = cv2.VideoCapture(0)  # 카메라 불러오기
cap.set(3,640) # 카메라에서 나오는 이미지 가로 크기 설정!
cap.set(4,480) # 카메라에서 나오는 이미지 세로 크기 설정!

while cap.isOpened(): # 카메라가 잘 연결이 되었다면 while 문 동작
    ret, img = cap.read() # 카메라에서 이미지 불러오기
                          # 이미지가 잘 들어왔다면! ret = True 아니면 False
    if ret: # 이미지가 잘 들어왔다면! 
        cv2.imshow('camera-0', img) # cv2.imshow() 이미지 화면에 띄우기!
        if cv2.waitKey(1) & 0xFF == 27:  # cv2.waitKey(1) 1ms 기다리기 (이거 있어야 화면 나옴)
            break
    else: # 이미지가 잘 안들어왔다면! 
        print('no camera!') # 이미지가 잘 안들어왔다면! 
        break
cap.release() # 카메라 연결해제
cv2.destroyAllWindows() # 화면에 띄운 이미지 (새로운 창) 다 끄기

