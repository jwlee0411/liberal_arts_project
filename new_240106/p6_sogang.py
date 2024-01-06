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
    st.title('서강대학교')
    st.write("""
        ㅇㅇㅇ

        """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '서강대학교']

    # Word Cloud
    subjects_data = data[data['대학교'].isin(['서강대학교'])]['과목명']
    all_subjects_text = ' '.join(subjects_data.astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(
        all_subjects_text)
    st.subheader('개설 교양과목 키워드 Word Cloud')
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)





    st.subheader('교양과목 수')
    st.bar_chart(uni_subset.groupby('개설연도').count()['과목명'])
    ex_vac_session = uni_subset[uni_subset['개설연도'].isin(reg_semester)]
    st.line_chart(ex_vac_session.groupby('개설연도').count()['과목명'])

    st.subheader('교양과목 개설학과')
    st.bar_chart(uni_subset.groupby('개설학과').count()['과목명'])
    ex_vac_session = uni_subset[uni_subset['개설연도'].isin(reg_semester)]

    st.subheader('SW 교육팀 개설 교양과목 추이')
    st.line_chart(ex_vac_session[ex_vac_session['개설연도'].isin(
        ['2020-2', '2021-1', '2021-2', '2022-1', '2022-2', '2023-1', '2023-2'])].groupby(['개설연도', '개설학과'])[
                      '과목명'].count().unstack('개설학과'), y=['SW교육팀'])




    st.write(f"""
                출처: 숭실대학교 유세인트 [https://saint.ssu.ac.kr/](https://saint.ssu.ac.kr/)

                ### 수집 방법

                1. 숭실대학교 유세인트 접속
                2. 학사관리 - 수강신청/교과과정 - 강의시간표 - 교양필수/교양선택 - 학년도 및 학기 선택
                3. 엑스포트
                """)

