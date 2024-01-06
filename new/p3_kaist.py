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
        숭실대학교는 최근 10년 내 4회 이상 개편이 이루어질 정도로 적극적으로 교양교육체계 개편을 모색해왔다. 건학이념을 기반으로 교양교육 체계가 특징이며, 타 학교와 가장 큰 차이점은 기독교와 통일 관련 과목이다.

        2024년 현재 교양필수 교과목은 9개로 구성되어 있으며 다음과 같다.

        1. 인문적 상상력과 소통
        2. 비판적 사고와 표현
        3. 창의적 사고와 혁신
        4. 인간과 성서
        5. 글로벌 시민의식
        6. 글로벌 소통과 언어
        7. 한반도 평화와 통일
        8. 컴퓨팅적 사고
        9. SW와 AI

        #### 인문적 상상력과 소통

        1. 인문적 상상력과 데이터 기반 토론
        2. 융합 독서 디베이트
        3. 디지털 미래 세계와 소통
        4. 고전 읽기와 상상력

        #### 비판적 사고와 표현

        1. 비판적 사고와 학술적 글쓰기
        2. 미디어 사회와 비평적 글쓰기
        3. 기술혁신사회와 과학기술 글쓰기

        #### 창의적 사고와 혁신

        1. 혁신과 기업가 정신
        2. 디자인씽킹
        3. 노코드 스타트업
        4. 미래 기술 스타트업

        #### 인간과 성서

        1. 인문학과 성서
        2. 인류문명과 기독교
        3. 현대사회 이슈와 기독교

        #### 글로벌 시민의식

        1. 글로벌 시민과 국제기구
        2. 세계화와 글로벌 이슈
        3. 글로벌 도시 이해

        #### 글로벌 소통과 언어

        1. CTE for Liberal Arts & Humanities
        2. CTE for Social Science & Business
        3. CTE for IT, Engineering &Natural Science

        #### 한반도 평화와 통일

        1. 한반도 평화와 통일

        #### 컴퓨팅적 사고

        1. 컴퓨팅적 사고와 코딩기초
        2. 컴퓨팅적 사고와 알고리즘
        3. 컴퓨팅적 사고와 활용

        #### SW와 AI

        1. AI와 데이터 기초
        2. AI와 머신러닝
        3. AI 개발과 실전

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

