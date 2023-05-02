import textwrap
from flask import Flask, jsonify, redirect, url_for, request, render_template, send_from_directory
import serial
import time

from serial.serialutil import SerialException

# ARDUINO PORT
arduino = '/dev/cu.usbmodem1201'

app = Flask(__name__, static_folder="static")
localDomain = "http://localhost:5000"
publicDomain = ""
DOMAIN = localDomain
localPath = ""
publicPath = ""
PATH = localPath

initialized = False
while not initialized:
    try:
        ser = serial.Serial(arduino, 9600)
        initialized = True
        # process the data

    except serial.serialutil.SerialException:
        print("SerialException occurred, resetting connection...")
        ser = serial.Serial(arduino, 9600)


@app.route("/")
def openHome():
    txt = ""
    with open('book.txt') as f:
        txt = f.read()

    lines = textwrap.wrap(txt, width=23)
    output = ""
    for i in range(0, len(lines), 23):
        output += "\n".join(lines[i:i + 23]) + "\n"

    arr = []
    sentencesCount = [0 for i in range(0, len(output), 462)]
    sentences = 0
    for i in range(2, len(output) - 1):
        if output[i - 1:i + 1] == "<<":
            j = i + 1
            while (output[j:j + 2] != ">>"):
                j += 1
            output = output[:i - 1] + output[i + 1:j] + output[j + 2:]
            sentences += 1
            sentencesCount[i // 462] += 1

    chapters = output.split("*********")
    arr = []
    for chapter in chapters:
        arr += textwrap.wrap(chapter, width=462)
        print(str(len(textwrap.wrap(chapter, width=462))))

    return render_template("index.html", domain=DOMAIN, data=str(0), txt=arr, len=len(arr), sen=sentences,
                           senCount=sentencesCount)


dataCached = 0


@app.route("/data")
def openSource():
    global dataCached
    global ser
    try:
        data = ser.readline().decode().strip()
        if (not data.isdigit()) or int(data) > 999 or int(data) < 100:
            reinitialize()
            return jsonify(dataCached)
        dataCached = data
        return jsonify(data)
    except (SerialException, UnicodeDecodeError) as e:
        reinitialize()
        return jsonify(dataCached)


def reinitialize():
    print("Some Error!")
    global ser
    reinitialized = False
    while not reinitialized:
        try:
            newser = serial.Serial(arduino, 9600)
            ser = newser
            reinitialized = True
            # process the data
        except serial.serialutil.SerialException:
            print("SerialException occurred, resetting connection...")


if __name__ == "__main__":
    app.debug = True
    app.run()
