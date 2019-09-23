
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

score_1 = 0
score_2 = 0

while True:
    input_state_4 = GPIO.input(4)
    input_state_5 = GPIO.input(5)

    input_state_20 = GPIO.input(20)
    input_state_21 = GPIO.input(21)

    #Player 1
    if input_state_4 == False:
    #    print('Score1 +1')
        score_1 += 1
#         print(score_1)
        time.sleep(.4)

    if input_state_5 == False:
    #    print('Score1 -1')
        score_1 -= 1
        if score_1 <= 0:
            score_1 = 0
#         print(score_1)
        time.sleep(0.4)

    #Player 2
    if input_state_20 == False:
#         print('Score2 +1')
        score_2 += 1
#         print(score_2)
        time.sleep(.4)

    if input_state_21 == False:
#         print('Score2 -1')
        score_2 -= 1
        if score_2 <= 0:
            score_2 = 0
#         print(score_2)
        time.sleep(0.4)
    
    if input_state_4 == False or input_state_5 == False or input_state_20 == False or input_state_21 == False:
        print('PLAYER1 SCORE')
        print(score_1)
        print('PLAYER2 SCORE')
        print(score_2)
        
# RESET

