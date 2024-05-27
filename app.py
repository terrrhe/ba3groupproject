
from flask import Flask, render_template, request, Response, url_for, send_file, jsonify, make_response, session, redirect
import logic as myLogic

app = Flask(__name__)

@app.route("/")
def hello_world():
     return render_template(
         "home.html"
    )

@app.route("/answer",  methods=["POST"])
def answer():

     ask = request.form["ask"]
    
     return myLogic.answer(ask)

