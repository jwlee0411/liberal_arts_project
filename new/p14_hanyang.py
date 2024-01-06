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
    st.title('한양대학교')
    st.write("""
        한양대학교의 교양교육은 매년 약 750개 전후의 다양한 교양과목을 개설하고 있습니다. 2023년 1학기를 기준으로 대다수의 교양과목은 1개의 분반만 개설되었습니다.

        가장 많은 분반이 개설된 과목은 "인공지능과기계학습" 과목은 9개의 분반이 개설되어 있어 인공지능 분야에 대한 높은 관심을 확인할 수 있습니다.

        교양영역은 가상대학영역, 일반영역, 소프트웨어영역, 인문과예술영역, 고전읽기영역, 과학과기술영역, 글로벌언어와문화영역, 미래산업과창업영역, 사회와세계영역으로 나뉘어져 있습니다. 

        2020-2023 교육과정의 세부 목표는 다음과 같다

        - 세부목표 1: 4차 산업혁명 관련 과목 필수이수 강화
        - 세부목표 2: 교양필수 교과목 교육과정 개편
        - 세부목표 3: 역량 기반, IC-PBL 및 융복합 교양교육 강화

        세부목표 1에 따라 2023년 1학기에 개설된 교양과목 중 "인공지능과기계학습" 과목이 9개의 분반으로 개설되어 있습니다. 이는 4차 산업혁명과 관련된 핵심 분야에 대한 수요가 크다는 것을 확인할 수 있습니다. 또한, 해당 교과목은 가상대학영역과 소프트웨어영역에 속하므로 다양한 분야에서의 필수 이수를 강화하고 있음을 시사합니다.

        다양한 교양과목에서 세부목표 3에 기반한 학생 참여형 인터캠퍼스 프로젝트 기반 학습(IC-PBL)이 강화되고 있는 것으로 나타났습니다. 이는 역량 기반 교육과 융복합 교육에 대한 관심이 높아지고 있다는 것을 의미합니다. 미래산업과창업영역, 사회와세계영역 등에서도 이러한 추세를 확인할 수 있었습니다. 따라서 현재 교양교육과 관련해 학교에서 추진한 세부 목표가 잘 추진되고 있는 것을 확인할 수 있었습니다.
        """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '한양대학교']

    # Word Cloud
    subjects_data = data[data['대학교'].isin(['한양대학교'])]['과목명']
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



    st.subheader('교양영역 별 2023년 개설과목 수')
    st.bar_chart(
        uni_subset[uni_subset['개설연도'].isin(['2023', '2023-2', '2023-1', '2023-겨울', '2023-여름'])].groupby('교양영역')[
            ['개설연도', '과목명']].count()['과목명'])

    st.write("""
                출처: 한양대학교 수강신청 포털 수강편람
    https://portal.hanyang.ac.kr/sugang/sulg.do#!UDMxMDI3OCRAXnN1Z2FuZy8kQF4wJEBeTTAwNjYzMSRAXuyImOqwle2OuOuejCRAXk0wMDY2MzEkQF5lOTA2ODU5ODUyNGUwMDRhNGFmNmQ5NmQzNDQxMGZhNTY3MDVlNzZiYjJmN2ZjMmRmMzU3Mjk0NzFiMGYzYjQ1IA==!
                """)

    st.subheader('수집 방법')

    st.write("""
            1. 한양대학교 수강신청 포털 - 상단 메뉴 수강편람 - 조건 검색
    2. 조건검색 후 엑셀 다운로드
            """)


