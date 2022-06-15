import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import platform

def draw_graph(score, class_text):


    if platform.system() == "Darwin":  # 맥
        plt.rc('font', family='AppleGothic')
    elif platform.system() == "Windows":  # 윈도우
        plt.rc('font', family='Malgun Gothic')
    elif platform.system() == "Linux":  # 리눅스 = 코랩
        plt.rc('font', family='Malgun Gothic')


    matplotlib.rcParams['axes.unicode_minus'] = False
    lst = []
    for element in score:
        lst.append(element*100)

    x = np.arange(len(lst))
    plt.figure(figsize=(16, 8))
    plt.bar(x, lst)
    plt.xticks(x, class_text)
    plt.rc('font', size = 15)
    plt.xlabel('유형')
    plt.ylabel('확률')
    plt.legend()
    plt.savefig('static/img/comment_graph.png', bbox_inches='tight')
    plt.close()
    