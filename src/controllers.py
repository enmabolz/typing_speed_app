from src import app
from flask import render_template
import os
import random


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    file_path = os.getcwd() + "/src/static/texts.txt"

    with open(file_path) as file_data:
        data = file_data.read().split("\n,.,.,.,.,\n")

    text_to_show = random.choice(data)

    return render_template('index.html', text=text_to_show)


@app.route("/calculate")
def finish_and_calulate():
    return "<h1>It works</h1>"
    







