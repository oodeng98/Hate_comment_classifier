### 중간 프로젝트

(실전 빅데이터 분석 프로젝트, 2022-06-02 ~ 2022-06-19)

#### 주제

: 입력되는 댓글의 악플 유무 및 종류를 판별하는 모델을 개발하여 악플 입력을 선제적으로 차단하는 서비스 개발



#### 프로젝트 수행

- 수행방법
    Smilegate AI에서 제공하는 한국어 혐오표현 ‘Unsmile’ 데이터셋
    + 악플 유/무만 구분되어 있는 데이터셋을 새롭게 라벨링

    기존 Smilegate 데이터셋은 여성/가족, 남성, 성소수자, 인종/국적, 연령, 지역, 종교, 기타혐오, 악플/욕설, clean 라벨링

    추가 데이터셋에는 예시로 ‘10년차 방탄팬인데 방탄처럼 성공은 못 하겠다’ 처럼 분쟁을 유발하는 새로운 유형의 악플이 존재

    분쟁유발 라벨을 추가하여 총 11개로 라벨링

- 도구
    - Okt, Mecab 형태소 분석기
    - Colab Pro
    - Github
    - hanspell(Python 한국어 맞춤법 검사기)
- 사용 모델
    - Conv1D 
    - LSTM
     etc...



#### 역할
팀장  
    원동찬 – 데이터 라벨링 및 모델 개발, Flask  
팀원  
    정태완 – 데이터 라벨링 및 모델 개발, Github 관리  
    윤민영 – 데이터 라벨링 및 모델 개발, 최종 발표  
    고은혜 – 데이터 라벨링 및 모델 개발, 기획안 발표
