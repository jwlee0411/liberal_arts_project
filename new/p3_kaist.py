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
    st.write("""
        ㅇㅇㅇㅇ

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

