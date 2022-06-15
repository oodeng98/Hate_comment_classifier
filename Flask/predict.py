import re
from tensorflow.keras.models import load_model
from konlpy.tag import Mecab
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib

def sentiment_predict(review, m_name = 'BiLSTM_LSTM', max_len = 70):
    best_model = load_model(f'static/model/{m_name}.h5')
    review = re.sub('[^ㄱ-ㅎㅏ-ㅑ가-힣]', ' ',review).strip()
    mecab = Mecab()
    t = joblib.load(f'static/model/tokenizer_{m_name}.pkl')

    stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','을','ㅋㅋ','ㅠㅠ','ㅎㅎ']
    morphs = mecab.morphs(review)
    morphs = [word for word in morphs if word not in stopwords]
    encoded = t.texts_to_sequences([morphs])
    padded = pad_sequences(encoded, maxlen = max_len)
    score = best_model.predict(padded)

    return score