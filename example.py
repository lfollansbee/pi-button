import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

score_1 = 0
score_2 = 0

while True:
    input_state_4 = GPIO.input(4)
    input_state_5 = GPIO.input(5)
    if input_state_4 == False:
        print('Score +1')
        score_1 += 1
        time.sleep(0.2)

    if input_state_5 == False:
        print('Score -1')
        score_1 -= 1
        time.sleep(0.2)
