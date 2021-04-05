import RPi.GPIO as GPIO
import time

SERVO_PIN = 18 # 서보 핀

SERVO_MAX_DUTY = 12.5 # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY = 1.5 # 서보의 최소(0도) 위치의 주기

GPIO.setwarnings(False)
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50) # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo.start(0)

try:
    while True:
        print('Enter target servo duty')
        servo_duty = float(input())
        print('You Entered Servo duty: ', servo_duty)

        ## servo_duty가 SERVO_MAX_DUTY와 SERVO_MIN_DUTY를 벗어나지 못하도록
        ## 코드 작성하기

        servo.ChangeDutyCycle(servo_duty)
        time.sleep(1)


except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()	# GPIO 모드 초기화
