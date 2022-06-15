from flask import Flask, render_template, request, flash, redirect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from draw_graph import draw_graph
from predict import sentiment_predict
app = Flask(__name__)
app.secret_key = '1234'

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
        class_text = ['여성/가족', '남성', '성소수자', '인종/국적', '연령', '지역', '종교', '기타 혐오', '악플/욕설', 'clean', '분쟁유발']
        score = sentiment_predict(sentence, m_name)
        result = f"'{sentence}'\n {score[0][score.argmax()]*100}%의 확률로 {class_text[score.argmax()]}에 대한 악플입니다."
        return render_template('menu1_res.html', menu=menu, sentence=sentence, result=result, m_name=m_name)

 
@app.route('/menu2', methods=['GET', 'POST'])
def menu2():    
    menu = {'home': 0, 'menu1': 0, 'menu2': 1, 'menu3': 0, 'menu4': 0, 'menu5': 0}
    if request.method == 'GET':
        return render_template('menu2.html', menu=menu)
    else:
        sentence = request.form['sentence']
        m_name = request.form['m_name']
        class_text = ['여성/가족', '남성', '성소수자', '인종/국적', '연령', '지역', '종교', '기타 혐오', '악플/욕설', 'clean', '분쟁유발']

        score = sentiment_predict(sentence, m_name)
        draw_graph(score[0],class_text)
        result = f'{m_name}모델의 댓글 "{sentence}" 유형별 확률'
        return render_template('menu2_res.html', menu=menu, sentence=sentence, result=result)


@app.route('/menu3', methods=['GET', 'POST'])
def menu3():
    menu = {'home': 0, 'menu1': 0, 'menu2': 0, 'menu3': 1, 'menu4': 0, 'menu5': 0}
    if request.method == 'GET':
        return render_template('menu3.html', menu=menu)
    else:
        sentence = request.form['sentence']
        score = sentiment_predict(sentence)
        c_type = np.argmax(score[0])
        if np.argmax(score[0]) != 9:
            if c_type == 0:
                flash("여성에 대한 혐오 표현을 자제해주세요.")
            elif c_type == 1:
                flash("남성에 대한 혐오 표현을 자제해주세요.")
            elif c_type == 2:
                flash("성소수자에 대한 혐오 표현을 자제해주세요.")
            elif c_type == 3:
                flash("인종차별 표현을 자제해주세요.")
            elif c_type == 4:
                flash("세대 갈등 표현을 자제해주세요.")
            elif c_type == 5:
                flash("지역 갈등 표현을 자제해주세요.")
            elif c_type == 6:
                flash("종교에 대한 혐오 표현을 자제해주세요.")
            elif c_type == 7:
                flash("악플을 자제해주세요.")
            elif c_type == 8:
                flash("악플을 자제해주세요.")
            elif c_type == 10:
                flash("분쟁 유발 댓글을 자제해주세요.")
            return redirect('menu3')
        else:
            pass
        return render_template('menu3_res.html', menu=menu, sentence=sentence)

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
