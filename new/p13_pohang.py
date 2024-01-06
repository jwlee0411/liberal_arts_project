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
    st.title('포항공과대학교')
    st.write("""
         ㅇㅇㅇㅇ
         """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '포항공과대학교']




    # 2023 Word Cloud
    subjects_data = data[data['대학교'].isin(['포항공과대학교'])]['과목명']
    all_subjects_text = ' '.join(subjects_data.astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(
        all_subjects_text)
    st.subheader('개설 교양과목 키워드 Word Cloud')
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)






    st.subheader('교양영역 별 2022년 개설과목 수')
    st.bar_chart(
        uni_subset[uni_subset['개설연도'].isin(['2022', '2022-2', '2022-1', '2022-겨울', '2022-여름'])].groupby('교양영역')[
            ['개설연도', '과목명']].count()['과목명'])

    st.write(f"""
             출처: POSTECH 인문사회학부 - [https://hss.postech.ac.kr/](https://hss.postech.ac.kr/)

             ### 수집 방법

             1. 상단 교과과정 메뉴 - 교과목 개요
             2. 자동화 웹 스크래핑 프로그램으로 수집
             """)
