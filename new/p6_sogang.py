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

    st.subheader('교양과목 개설학과 (2023)')
    st.bar_chart(
        uni_subset[uni_subset['개설연도'].isin(['2023', '2023-2', '2023-1', '2023-겨울', '2023-여름'])].groupby('개설학과')[
            ['개설연도', '과목명']].count()['과목명'])


    st.write(f"""
                출처:
서강대학교 홈페이지: https://sogang.ac.kr/index.do
서강대학교 전인교육원: https://scc.sogang.ac.kr/wholeperson/index_new.html
                """)

    st.subheader("수집 방법")



    st.write(f"""
               1. 서강대학교 홈페이지 - 상단 메뉴 학사·학생지원 - 개설과목정보 - 조건 검색
2. 다운로드 버튼 클릭 - excel 다운로드
                """)