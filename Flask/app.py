from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





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
        return render_template('menu1_res.html', menu=menu)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
