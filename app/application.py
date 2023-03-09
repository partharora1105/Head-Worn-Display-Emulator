import os
import csv
from datetime import datetime
from werkzeug.utils import secure_filename

from flask import Flask, redirect, url_for, request, render_template, send_from_directory
import serial
import sqlite3
from flask import g
import time

ser = serial.Serial('/dev/cu.usbmodem1301', 9600) # replace with your serial port and baud rate

app = Flask(__name__, static_folder="static")
localDomain = "http://localhost:5000"
publicDomain = "http://www.gtxr.club"
DOMAIN = localDomain

localPath = ""
publicPath = "/home/GTXR/mysite/"
PATH = localPath

# DATABASE = PATH + "static/database/database.db"
#
# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db
#
# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

@app.route("/")
def openHome():
    val = int(ser.readline().decode().strip())
    resitor = 680
    voltage = 5
    prVal = ((resitor * val)/voltage-val)
    #prVal = str(round(prVal/10000, 2))
    print(prVal)
    #return str(prVal)
    return render_template("index.html", domain=DOMAIN, data = str(prVal))

@app.route("/source")
def openSource():
    val = int(ser.readline().decode().strip())
    resitor = 680
    voltage = 5
    prVal = ((resitor * val) / voltage - val)
    # prVal = str(round(prVal/10000, 2))
    print(prVal)
    # return str(prVal)
    return render_template("index.html", domain=DOMAIN, data=str(prVal))

# @app.route("/values", methods=["POST", "GET"])
# def addAndShow():
#     #Writing
#     Name = request.form["name"]
#     Age = request.form["age"]
#     val = (Name, Age)
#     sql = ''' INSERT INTO People(name,age) VALUES(?,?) '''
#     get_db().execute(sql,val)
#     get_db().commit()
#     #Reading
#     query = "SELECT * FROM People"
#     cur = get_db().execute(query, ())
#     rv = cur.fetchall()
#     cur.close()
#     return str(rv)

if __name__ == "__main__":
    app.debug = True
    app.run()
