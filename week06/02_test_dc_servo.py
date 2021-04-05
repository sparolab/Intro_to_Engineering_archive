import RPi.GPIO as GPIO
import cv2
import threading
import queue
from time import sleep #time 라이브러리의 sleep함수 사용
import numpy as np
import termios, sys, tty


# Configurations

# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWARD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 26  #37 pin

#GPIO PIN
IN1 = 19  #37 pin
IN2 = 13  #35 pin

SPEED = 35  # DC 모터 속도



# 핀 설정 함수
def setMotorPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # 100hz 로 PWM 동작 시킴
    pwm = GPIO.PWM(EN, 100)
    # 우선 PWM 멈춤.
    pwm.start(0)
    return pwm

# 모터 제어 함수
def setMotorContorl(pwm, INA, INB, speed, stat):
    #모터 속도 제어 PWM
    pwm.ChangeDutyCycle(speed)
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)

    #뒤로
    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)


# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    if ch == CH1:
        #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        #pwmB는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmB, IN3, IN4, speed, stat)


## -------------------------------------------------------------##
## Main Function -----------------------------------------------##
## -------------------------------------------------------------##

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

#모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴
pwmA = setMotorPinConfig(ENA, IN1, IN2)



try:
    while True:
        motorspeed = int(input())

        if motorspeed > 0:
            setMotor(CH1, motorspeed, FORWARD)
        elif motorspeed < 0:
            setMotor(CH1, -motorspeed, BACKWARD)
        else:
            setMotor(CH1, 0, STOP)

        sleep(5)

except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
