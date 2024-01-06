from src import app
from flask import render_template
from flask import request
import os
import random
import re

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        written_text = request.form.get('written-text')
        showed_text = request.form.get('showed-text')  
        timer = request.form.get('counter')
        print(timer)
        
        info_to_show = get_info_to_show(showed_text, written_text)
        
        return render_template('info_to_show.html', info=info_to_show)
    else:
        text_to_show = get_start_info()
        
        return render_template('index.html', text=text_to_show)


def get_start_info():
    file_path = os.getcwd() + "/src/static/texts.txt"

    with open(file_path) as file_data:
        data = file_data.read().split("\n,.,.,.,.,\n")

    text_to_show = random.choice(data)
    
    return text_to_show



def get_info_to_show(showed_text, written_text):
    quantity_of_accurate_words = get_quantity_of_accurate_words(showed_text, written_text)
    
    words = get_words(showed_text)
    
    
    typing_speed = quantity_of_accurate_words 
    
    
    
    

    return {}
    
def get_quantity_of_accurate_words(showed_text, written_text):
    words_in_showed_text = get_words(showed_text)
    words_in_written_text = get_words(written_text)
    
    accurate_words = 0
    
    for i, word_in_showed_text in enumerate(words_in_showed_text):
        if i < len(words_in_written_text) and words_in_written_text[i] == word_in_showed_text:
            accurate_words += 1
    
    return accurate_words    
        
    
def get_words(text):
    if text:
        return re.split(', | |: ', text)
    else:
        return []
    
    

    







