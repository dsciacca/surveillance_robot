from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

m11 = 18
m12 = 23
m21 = 24
m22 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.output(m11, 0)
GPIO.output(m12, 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)

print("Done")

a = 1


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/left_side")
def left_side():
    print("LEFT")
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    return 'true'


@app.route('/right_side')
def right_side():
    print("RIGHT")
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
    return 'true'


@app.route('/up_side')
def up_side():
    print("FORWARD")
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    return 'true'


@app.route('/down_side')
def down_side():
    print("BACK")
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    return 'true'


@app.route('/stop')
def stop():
    print("STOP")
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
    return 'true'


if __name__ == "__main__":
    print("Start")
    app.run(host='0.0.0.0', port=5010)
