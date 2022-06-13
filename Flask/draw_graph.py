import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import platform

def draw_graph(score):


    if platform.system() == "Darwin":  # 맥
        plt.rc('font', family='AppleGothic')
    elif platform.system() == "Windows":  # 윈도우
        plt.rc('font', family='Malgun Gothic')
    elif platform.system() == "Linux":  # 리눅스 = 코랩
        plt.rc('font', family='Malgun Gothic')
    if len(score) == 11:
        columns = ['여성/가족', '남성', '성소수자', '인종/국적', '연령', '지역', '종교', '기타 혐오', '악플/욕설', 'clean', '분쟁유발']
    else: 
        columns = ['여성/가족', '남성', '성소수자', '인종/국적', '연령', '지역', '종교', '기타 혐오', '악플/욕설', 'clean']

    matplotlib.rcParams['axes.unicode_minus'] = False
    lst = []
    for element in score:
        lst.append(element*100)

    x = np.arange(len(lst))
    plt.figure(figsize=(16, 8))
    plt.bar(x, lst)
    plt.xticks(x, columns)
    plt.rc('font', size = 15)
    plt.xlabel('유형')
    plt.ylabel('확률')
    plt.legend()
    plt.savefig('static/img/comment_graph.png', bbox_inches='tight')
    plt.close()
    