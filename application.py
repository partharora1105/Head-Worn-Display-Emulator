import textwrap
from flask import Flask, jsonify, redirect, url_for, request, render_template, send_from_directory
import serial
import time

from serial.serialutil import SerialException

app = Flask(__name__, static_folder="static")
localDomain = "http://localhost:5000"
publicDomain = ""
DOMAIN = localDomain
localPath = ""
publicPath = ""
PATH = localPath
# arduino = '/dev/cu.usbmodem1201' # if you use a different adapter
arduino = '/dev/cu.usbmodem1401'

# try:
#     ser = serial.Serial('/dev/cu.usbmodem1301', 9600)  # Change this to the port your device is connected to
#     ser.timeout = 5  # Set the timeout to 100ms
# except SerialException:
#     ser = None
#     print("screwing up")

initialized = False
while not initialized:
    try:
        ser = serial.Serial(arduino, 9600)
        initialized = True
        # process the data

    except serial.serialutil.SerialException:
        print("SerialException occurred, resetting connection...")
        ser = serial.Serial(arduino, 9600)



# try:
#     ser = serial.Serial('/dev/cu.usbmodem1301', 9600)  # Change this to the port your device is connected to
#     ser.timeout = 0.1  # Set the timeout to 100ms
# except:
#     print("No Port Found")
#     ser = None

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
    for i in range(2, len(output)-1):
        if output[i-1:i+1] == "<<":
            j = i+1
            while (output[j:j+2] != ">>"):
                j+=1
            output = output[:i-1] + output[i+1:j] + output[j+2:]
            sentences += 1
            sentencesCount[i // 462] += 1

    chapters= output.split("*********")
    arr = []
    for chapter in chapters:
        arr += textwrap.wrap(chapter, width=462)
        print(str(len(textwrap.wrap(chapter, width=462))))

    return render_template("index.html", domain=DOMAIN, data=str(0), txt=arr, len=len(arr), sen=sentences,
                           senCount=sentencesCount)
    chapters = []

    # arr = []
    #
    # remainingText = output
    # for i in range(5):
    #     ind = remainingText[500:].find("=========III")
    #     print(ind)
    #     print(output[ind])
    #     item = textwrap.wrap(output[:ind], width=462)
    #     print(item)
    #     arr += item
    #     remainingText = output[ind:]


    # newArr = []
    # arr = textwrap.wrap(output, width=462)
    # for i in range(len(arr)):
    #     page = arr[i]
    #     ind = page.find("=========")
    #     if ind == -1:
    #         newArr.append(page)
    #     else:
    #         newArr.append(page[:ind])
    #         newArr.append(page[ind:])
    # arr = newArr



    # for i in range(0, len(output)):
    #     if i % 462 == 0:
    #         arr.append(output[i:i + 462])

    # if ser != None:
    #     val = int(ser.readline().decode().strip())
    #     resitor = 680
    #     voltage = 5
    #     prVal = ((resitor * val) / voltage - val)
    #     prVal = val
    #     return render_template("index.html", domain=DOMAIN, data=str(prVal), txt=arr, len = len(arr), sen = sentences, senCount = sentencesCount)
    # else:
    #     return render_template("index.html", domain=DOMAIN, data=str(0), txt=arr, len = len(arr), sen = sentences, senCount = sentencesCount)
#

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
    # if ser.in_waiting > 0:
    #     data = ser.readline().decode('utf-8').strip()
    #     print(data)


if __name__ == "__main__":
    app.debug = True
    app.run()
