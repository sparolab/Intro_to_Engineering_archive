import RPi.GPIO as GPIO
import cv2
import threading
import time
import numpy as np
import pygame
import os


# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 1 #TODO
ECHO = 1 #TODO

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)

distance = 1000

def sonar_thread():
    global distance
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            start = time.time()	 # Echo 핀 상승 시간
        while GPIO.input(ECHO)==1:
            stop= time.time()	 # Echo 핀 하강 시간

        check_time = stop - start
        distance = 1 #TODO: 거리 계산하는는 코드 넣기
        print("Distance : %.1f cm" % distance)

        time.sleep(0.2)


##### Main Function ####
thread1= threading.Thread(target=sonar_thread)
thread1.daemon=True  	# 데몬 쓰레드란 백그라운드에서 실행되는
                    # 쓰레드로 메인 쓰레드가 종료되면 즉시 종료되는 쓰레드이다.
thread1.start()

while True:
    time.sleep(0.2)


thread1.join()
