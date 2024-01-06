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
    st.title('고려대학교')
    st.write("""
            고려대학교는 자유/정의/진리의 교육이념을 바탕으로 학문적 통찰력과 공감적 협업능력을 갖춰 세계 변화를 추동하는 실천적 인간의 형성을 목표로 교양교육을 디자인하였다.

            교양교육은 3가지 영역으로 구분된다.

            1. 공감적 인격교육
            2. 합리적 소통교육
            3. 성찰적 융합교육

            고려대학교 데이터는 교양필수 데이터만 수집되었으며, 홈페이지에서도 제한적으로 정보를 제공하고 있어 분석에 어려움이 있었다. 현재 고려대학교 교양필수 과목은 다음과 같다.

            1. 자유 정의 진리
            2. 글쓰기, 심화 글쓰기
            3. 핵심교양

            핵심교양은 다음 7개 세부영역으로 구분된다.
            1. 세계의 문화
            2. 역사의 탐구
            3. 윤리와 사상
            4. 문학과 예술
            5. 사회의 이해
            6. 과학과 기술
            7. 디지털 혁신과 인간
            """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '고려대학교']

    # Word Cloud
    subjects_data = data[data['대학교'].isin(['고려대학교'])]['과목명']
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

    st.subheader('교양영역 별 2023년 개설과목 수')
    st.bar_chart(
        uni_subset[uni_subset['개설연도'].isin(['2023', '2023-2', '2023-1', '2023-겨울', '2023-여름'])].groupby('교양영역')[
            ['개설연도', '과목명']].count()['과목명'])

    st.subheader("수집 방법")

    st.write("""
            1. 고려대학교 교양교육원 홈페이지 - 상단 메뉴 교과목 안내
2. 각 과목별 페이지 접근하여 수기 또는 자동화 웹 스크래핑 프로그램으로 수집

            """)
