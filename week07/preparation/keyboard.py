import RPi.GPIO as GPIO
import time
import numpy as np
import pygame

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


def keyboard_init():
    pygame.init()
    win = pygame.display.set_mode((100, 100))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()

    return ans

keyboard_init()


##### Main Function 1 ####

dc_speed2 = 40 #TODO: 키보드로 조정시 속도
left_duty = 4 #TODO: 왼쪽 키보드 눌렀을 때 서보 듀티
centor_duty = 5 #TODO: 중앙 서보 듀티
right_duty = 7 #TODO: 오른쪽 키보드 눌렀을 때 서보 듀티

while True: #TODO: 전, 후, 좌, 우 키보드 눌렀을 때 동작하는 코드 넣기
    if getKey('LEFT'):
        print('Key Left was pressed')
        #TODO
    elif getKey('RIGHT'):
        print('Key Right was pressed')
        #TODO
    elif getKey('UP'):
        print('Key Up was pressed')
        setMotor(CH1, dc_speed2, FORWARD)
        #TODO
    elif getKey('DOWN'):
        print('Key Down was pressed')
        #TODO
    elif getKey('ESCAPE'):
        print('Key ESC was pressed')
        print('QUIT Program')
        #TODO: 'ESC'누르면 종료하는 부분
        #TODO: 서보모터 직진방향 정렬, DC모터 정지
        time.sleep(1)
        break
    else:
        #TODO: 서보모터 직진방향 정렬
        setMotor(CH1, 0, STOP)

    time.sleep(0.1)
