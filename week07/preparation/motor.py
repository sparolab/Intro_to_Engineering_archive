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

'''
DC, 서보 모터 설정
'''
# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWARD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# 실제 핀 정의
#PWM PIN
ENA = 1 #TODO #37 pin

#GPIO PIN
IN1 = 1 #TODO #37 pin
IN2 = 1 #TODO #35 pin

### Servo
SERVO_PIN = 1 #TODO # 서보 핀

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
    HIGH = 1
    LOW = 0
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

def setServoMotor(duty):
    servo.ChangeDutyCycle(duty)


GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50) # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo.start(0)

#모터 핀 설정
pwmA = setMotorPinConfig(ENA, IN1, IN2)


# ##### Main Function 1 ####
# while True:
#     print('Enter target servo duty (2~10)')
#     servo_duty = float(input())
#     print('You Entered Servo duty: ', servo_duty)
#
#     setServoMotor(servo_duty)
#     time.sleep(1)


##### Main Function 2 ####
while True:
    print('Enter DC Motor speed duty (20~50)')
    motorspeed = int(input())
    if motorspeed > 0:
        setMotor(CH1, motorspeed, FORWARD)
    elif motorspeed < 0:
        setMotor(CH1, -motorspeed, BACKWARD)
    else:
        setMotor(CH1, 0, STOP)
    time.sleep(2)
