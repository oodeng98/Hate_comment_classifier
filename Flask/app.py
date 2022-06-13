from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, re, joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from my_util.global_vars import okt


app = Flask(__name__)


@app.route('/')
def index():
    menu = {'home': 1, 'menu1': 0, 'menu2': 0, 'menu3': 0, 'menu4': 0}

    return render_template('index.html', menu=menu)


@app.route('/menu1', methods=['GET', 'POST'])
def menu1():    
    menu = {'home': 0, 'menu1': 1, 'menu2': 0, 'menu3': 0, 'menu4': 0, 'menu5': 0}
    if request.method == 'GET':
        return render_template('menu1.html', menu=menu)
    else:
        sentence = request.form['sentence']

        stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','을','ㅋㅋ','ㅠㅠ','ㅎㅎ']
        t = joblib.load('static/model/unsmile_tokenizer.pkl')
        max_len = 60
        model = load_model('static/model/unsmile_bilstm.h5')

        sentence = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', sentence)
        morphs = okt.morphs(sentence, stem=True)
        morphs = [word for word in morphs if word not in stopwords]
        encoded = t.texts_to_sequences([morphs])
        padded = pad_sequences(encoded, maxlen=max_len)
        score = float(model.predict(padded))
        return render_template('menu1_res.html', menu=menu, sentence=sentence)


@app.route('/menu2', methods=['GET', 'POST'])
def menu2():    
    menu = {'home': 0, 'menu1': 0, 'menu2': 1, 'menu3': 0, 'menu4': 0, 'menu5': 0}
    if request.method == 'GET':
        return render_template('menu2.html', menu=menu)
    else:
        return render_template('menu2_res.html', menu=menu)


@app.route('/menu3', methods=['GET', 'POST'])
def menu3():
    menu = {'home': 0, 'menu1': 0, 'menu2': 0, 'menu3': 1, 'menu4': 0, 'menu5': 0}
    if request.method == 'GET':
        return render_template('menu3.html', menu=menu)
    else:
        
        return render_template('menu3_res.html', menu=menu)

@app.route('/menu4', methods=['GET', 'POST'])
def menu4():
    menu = {'home': 0, 'menu1': 0, 'menu2': 0, 'menu3': 0, 'menu4': 1, 'menu5': 0}
    if request.method == 'GET':
        return render_template('menu4.html', menu=menu)
    else:
        
        return render_template('menu4_res.html', menu=menu)

@app.route('/menu5', methods=['GET', 'POST'])
def menu5():
    menu = {'home': 0, 'menu1': 0, 'menu2': 0, 'menu3': 0, 'menu4': 0, 'menu5': 1}
    if request.method == 'GET':
        return render_template('menu5.html', menu=menu)
    else:
        
        return render_template('menu5_res.html', menu=menu)
# background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    # 여기 악플 판별 모듈 불러오기
    return 1

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
