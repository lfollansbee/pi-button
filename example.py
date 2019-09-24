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
    player_1_increment = GPIO.input(4)
    player_1_decrement = GPIO.input(5)

    player_2_increment = GPIO.input(20)
    player_2_decrement = GPIO.input(21)

    reset_button = GPIO.input(26)

    # Player 1
    if player_1_increment == False:
        score.score_1 += 1
        time.sleep(.4)

    if player_1_decrement == False:
        score.score_1 -= 1
        if score.score_1 <= 0:
            score.score_1 = 0
        time.sleep(0.4)

    # Player 2
    if player_2_increment == False:
        score.score_2 += 1
        time.sleep(.4)

    if player_2_decrement == False:
        score.score_2 -= 1
        if score.score_2 <= 0:
            score.score_2 = 0
        time.sleep(0.4)
    
    # RESET
    if reset_button == False:
        score.score_1 = 0
        score.score_2 = 0
        time.sleep(.4)

    if player_1_increment == False or player_1_decrement == False or player_2_increment == False or player_2_decrement == False or reset_button == False:
        print(score.score_1, score.score_2)
        publish.single(MQTT_PATH, json.dumps(score.__dict__), hostname=MQTT_SERVER)

