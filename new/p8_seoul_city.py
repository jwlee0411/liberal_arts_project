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
    st.title('서울시립대학교')
    st.write("""
         서울시립대학교의 교양교육 목표는 전문적인 학문을 수행하는 데 필요한 기초 역량을 함양하고, 다양한 학
문을 통해 폭넓은 지식을 갖춘 지성인을 양성하는 것과, 사회적 통섭 역량과 공익적 인성 역량을 갖춘 시민을
양성하는 것이다. 서울시립대학교의 교양교육과정은 기초교양, 자유교양, 미래교양과 같이 3 가지 범주에 따
라 구성되어있는데, 기초교양은 교양필수와 교양선택을 포함하고 있다
         """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '서울시립대학교']




    # 2023 Word Cloud
    subjects_data = data[data['대학교'].isin(['서울시립대학교'])]['과목명']
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

    st.subheader('교양영역 별 2023년 개설과목 수')
    st.bar_chart(
        uni_subset[uni_subset['개설연도'].isin(['2023', '2023-2', '2023-1', '2023-겨울', '2023-여름'])].groupby('교양영역')[
            ['개설연도', '과목명']].count()['과목명'])






    st.write(f"""
                출처: 서울시립대학교 [https://www.uos.ac.kr/kor/](https://www.uos.ac.kr/)
                
                ### 수집 방법
                
                1. 상단 메뉴 대학 및 대학원 - 학사 - 전공/교과/교직
                2. 교과과정 선택
                3. 교양교과목 다운로드
                4. HWP 파일에서 교양과목 데이터 수기로 데이터 수집


                """)

