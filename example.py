import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish
import json

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

MQTT_SERVER = "ec2-34-216-22-106.us-west-2.compute.amazonaws.com"
MQTT_PATH = "mychanel"

class Score:
  score_1 = 0
  score_2 = 0

score = Score()
score.score_1 = 0
score.score_2 = 0

while True:
    input_state_4 = GPIO.input(4)
    input_state_5 = GPIO.input(5)

    input_state_20 = GPIO.input(20)
    input_state_21 = GPIO.input(21)

    input_state_26 = GPIO.input(26)

    # Player 1
    if input_state_4 == False:
        score.score_1 += 1
        time.sleep(.4)

    if input_state_5 == False:
        score.score_1 -= 1
        if score.score_1 <= 0:
            score.score_1 = 0
        time.sleep(0.4)

    # Player 2
    if input_state_20 == False:
        score.score_2 += 1
        time.sleep(.4)

    if input_state_21 == False:
        score.score_2 -= 1
        if score.score_2 <= 0:
            score.score_2 = 0
        time.sleep(0.4)
    
    # RESET
    if input_state_26 == False:
        score.score_1 = 0
        score.score_2 = 0
        time.sleep(.4)

    if input_state_4 == False or input_state_5 == False or input_state_20 == False or input_state_21 == False or input_state_26 == False:
        print(score.score_1, score.score_2)
        publish.single(MQTT_PATH, json.dumps(score.__dict__), hostname=MQTT_SERVER)

