import os, re, random, json, urllib.parse, urllib.request,datetime,math
from flask import Flask, render_template, request, jsonify, session,abort,redirect,url_for,Response

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=80, debug=True)