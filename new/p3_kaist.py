import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from collections import Counter
import plotly.express as px
import main
from PIL import Image

def show(reg_semester, font_path):
    st.title('KAIST')
    st.write(f"""
        
카이스트 교양과목 수는 2023년 서울 주요대학 개설교양과목 수를 비교한 그래프를 보면 평이한 편이다. 교양과목 개설 분야는 문학과예술, 사회, 인문에 치우쳐져 있으며, 카이스트는 강의 내용에 따라 인선 과목의 계열을 인문, 사회, 문학과 예술로 구분할 뿐만 아니라 성격에 따라 핵심, 융합, 일반으로도 구분하고 있다. 특히 핵심 과목으로 지정되면 수강 정원이 20명으로 제한되고 글쓰기 및 체험을 포함하는 등 차별화된 교육 방침을 채택한다. 또한, 융합과목의 경우 ‘음악과 뇌’와 같이 과학과 인문사회학의 교집합에서 독특한 콘텐츠를 제공하고 있다. 이 같은 핵심 및 융합 과목의 경우 타 대학에서 찾을 수 없는 차별화된 강의를 가지고 있다. 그러나 2023년 2월 28일부터 3월 3일까지 지난 4일간 카이스트신문에서 실시한 설문조사에 따르면 학생들의 의견은 사뭇 달랐다. 57명의 카이스트 학생들을 대상으로 설문 조사 결과 개설 강의의 다양성을 묻는 질문에는 매우 부족(32%), 부족한 편(43%)이라는 응답의 합이 75%에 달해 다양성 측면에서 아쉽다는 의견이 압도적으로 높게 나타났다. 이를 통해 교양과목의 다양성에 상당히 기여하는 것은 교양과목의 목적인 인문학적 소양 함양을 달성하기 위해 반드시 필요한 부분인 것을 알 수 있다. 학생들을 위해, 학생들에 의한 교양 과목으로 변화해야 교양 과목의 이수요건 채우기로 전락하지 않고, 교양과목의 본 취지와 부합할 수 있는 것이다. 이를 위해 학생들의 의견을 적극적으로 듣고, 반영하기 위한 적극적인 노력이 필요하다. 총학생회 등 공식적인 창구뿐만 아니라 학생들의 수요를 파악하고 충족시키기 위해 고민하며, 공론화 과정을 통해 학교와 학생의 양측의 의견 차를 좁히기 위한 소통의 장을 마련하고, 구성원 모두 만족할 수 있는 강의가 제공되어야 함을 시사한다.

        """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == 'KAIST']

    # Word Cloud
    subjects_data = data[data['대학교'].isin(['KAIST'])]['과목명']
    all_subjects_text = ' '.join(subjects_data.astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(
        all_subjects_text)
    st.subheader('개설 교양과목 키워드 Word Cloud')
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)



    st.subheader('교양과목 개설학과')
    st.bar_chart(uni_subset.groupby('개설학과').count()['과목명'])
    ex_vac_session = uni_subset[uni_subset['개설연도'].isin(reg_semester)]





    st.write(f"""
                출처:
KAIST Academic System: https://cais.kaist.ac.kr/totalOpeningCourse

KAIST 학사요람 SYSTEM: https://bulletin.kaist.ac.kr/html/kr/?year=2023&id=kr20230301&gbn=C2
1. KAIST Academic System 접속
2. 과목구분 교양선택/교양필수/교양필수(봉사)/교양필수(체육) 선택
3. 조회된 테이블을 Excel에 복사 붙여넣기하여 수집
                """)

