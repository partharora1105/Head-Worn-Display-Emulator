import textwrap
from flask import Flask, jsonify, redirect, url_for, request, render_template, send_from_directory
import serial
import time
from serial.serialutil import SerialException

# ARDUINO PORT
arduino = '/dev/cu.usbmodem1301'

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
    pageNums = [0]
    for chapter in chapters:
        arr += textwrap.wrap(chapter, width=462)
        pageNums.append(int(len(textwrap.wrap(chapter, width=462))))
    for i in range(1,len(pageNums)):
        pageNums[i] = pageNums[i-1] + pageNums[i]

    print(pageNums)
    return render_template("index.html", domain=DOMAIN, data=str(0), txt=arr, len=len(arr), sen=sentences,
                           senCount=sentencesCount)


dataCached = 0
issueDetected = False



@app.route("/data")
def openSource():
    threshold = 700
    global dataCached
    global ser
    global issueDetected
    if not issueDetected:
        try:
            data = ser.readline().decode().strip()
            if (not data.isdigit()) or int(data) > 999 or int(data) < 100:
                issueDetected = True
                print("ERROR : Invalid Data Type")
                reinitialize()
                return jsonify(0)
            if int(data) > threshold:
                return jsonify(1) # Hide it
            return jsonify(0)
        except (SerialException, UnicodeDecodeError) as e:
            issueDetected = True
            print("ERROR : Serial Exception")
            reinitialize()
            return jsonify(0)
    else:
        print("Resolving Error")
        return jsonify(0)


def reinitialize():
    global issueDetected
    time.sleep(1)
    global ser
    reinitialized = False
    while not reinitialized:
        try:
            newser = serial.Serial(arduino, 9600)
            ser = newser
            time.sleep(1)
            data = ser.readline().decode().strip()
            if (not data.isdigit()) or int(data) > 999 or int(data) < 100:
                print(data)
                continue
            reinitialized = True
            issueDetected = False
        except serial.serialutil.SerialException:
            print("SerialException occurred while resetting, resetting connection...")
            time.sleep(2)


if __name__ == "__main__":
    app.debug = True
    app.run()
