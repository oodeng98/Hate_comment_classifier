from flask import Flask, render_template, request, flash, url_for, redirect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, re, joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from konlpy.tag import Okt
from draw_graph import draw_graph

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
        m_name = request.form['m_name']
        okt = Okt()
        columns = ['여성/가족', '남성', '성소수자', '인종/국적', '연령', '지역', '종교', '기타 혐오', '악플/욕설', 'clean', '분쟁유발']
        stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','을','ㅋㅋ','ㅠㅠ','ㅎㅎ']
        t = joblib.load('static/model/tokenizer.pkl')
        max_len = 100
        model = load_model(f'static/model/{m_name}.h5')

        sentence = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', sentence)
        morphs = okt.morphs(sentence, stem=True)
        morphs = [word for word in morphs if word not in stopwords]
        encoded = t.texts_to_sequences([morphs])
        padded = pad_sequences(encoded, maxlen=max_len)
        score = model.predict(padded)
        max = 0
        for i in range(len(score[0])):
            if score[0][i] >= score[0][max]:
                max = i
            else:
                continue
  
        result = f'{m_name} 모델: {score[0][max]*100}%의 확률로 {columns[max]}에 관한 댓글입니다.'
        return render_template('menu1_res.html', menu=menu, sentence=sentence, result=result, m_name=m_name)


@app.route('/menu2', methods=['GET', 'POST'])
def menu2():    
    menu = {'home': 0, 'menu1': 0, 'menu2': 1, 'menu3': 0, 'menu4': 0, 'menu5': 0}
    if request.method == 'GET':
        return render_template('menu2.html', menu=menu)
    else:
        sentence = request.form['sentence']
        m_name = request.form['m_name']
        okt = Okt()
        stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','을','ㅋㅋ','ㅠㅠ','ㅎㅎ']
        t = joblib.load('static/model/tokenizer.pkl')
        
        model = load_model(f'static/model/{m_name}.h5')
        if m_name == 'BiLSTM':
            max_len = 100
        else:
            max_len = 30
        sentence = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', sentence)
        morphs = okt.morphs(sentence, stem=True)
        morphs = [word for word in morphs if word not in stopwords]
        encoded = t.texts_to_sequences([morphs])
        padded = pad_sequences(encoded, maxlen=max_len)
        score = model.predict(padded)
        draw_graph(score[0])
        result = f'{m_name}모델의 댓글 "{sentence}" 유형별 확률'
        return render_template('menu2_res.html', menu=menu, sentence=sentence, result=result)


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
