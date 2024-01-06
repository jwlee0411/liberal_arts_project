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

def show():

    data = main.load_data()

    # 나눔글꼴 경로 설정
    font_path = './res/gyeonggi_medium.ttf'

    # 폰트 이름 가져오기
    font_name = fm.FontProperties(fname=font_path).get_name()

    # 폰트 설정
    plt.rc('font', family=font_name)


    reg_semester = ['2003-1', '2003-2', '2004-1', '2004-2', '2005-1', '2005-2',
       '2006-1', '2006-2', '2007-1', '2007-2', '2008-1', '2008-2',
       '2009-1', '2009-2', '2010-1', '2010-2', '2011-1', '2011-2',
       '2012-1', '2012-2', '2013-1', '2013-2', '2014-1', '2014-2',
       '2015-1', '2015-2', '2016-1', '2016-2', '2017-1', '2017-2',
       '2018-1', '2018-2', '2019-1', '2019-2', '2020-1', '2020-2',
       '2021-1', '2021-2', '2022-1', '2022-2', '2023-1', '2023-2', *[str(y) for y in range(2008, 2024)]]

    st.header('종합 분석', divider='rainbow')


    # 2023년 개설 교양과목 수
    st.subheader('2023년 개설 교양과목 수')
    st.write("일부 대학은 교양필수 과목 데이터만 수집되어, 데이터 해석에 주의바람")

    st.bar_chart(data[data['개설연도'].isin(['2023-2', '2023-1', '2023', '2023-여름', '2023-겨울'])].groupby('대학교').count()['과목명'])







    # 2023 Word Cloud
    subjects_data = data[data['개설연도'].isin(['2023-2', '2023-1', '2023', '2023-여름', '2023-겨울'])]['과목명']
    all_subjects_text = ' '.join(subjects_data.astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(
        all_subjects_text)
    st.subheader('2023년 개설 교양과목 키워드 Word Cloud')
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
    st.write("실행할 때마다 조금씩 다르게 출력됨")



    st.subheader('대학별 인공지능(AI) 관련 과목 수')
    st.write("AI, 인공지능, 머신러닝, 기계학습, 딥러닝, 빅데이터")
    st.bar_chart(
        data[data['과목명'].str.contains('AI|인공지능|머신러닝|기계학습|딥러닝|빅데이터', case=False, na=False)].groupby('대학교').count()['과목명']
    )



    # 키워드별로 그룹화하여 카운트
    keywords = ['AI', '인공지능', '빅데이터', '머신러닝', '기계학습', '딥러닝', ]
    keyword_counts = {}
    for keyword in keywords:
        keyword_counts[keyword] = data[data['과목명'].str.contains(keyword, case=False, na=False)].groupby('대학교').count()[
            '과목명']

    # 스트림릿 앱에 출력
    st.subheader('키워드별 인공지능(AI) 관련 과목 수')
    for keyword, counts in keyword_counts.items():
        st.write(f"{keyword}:")
        st.bar_chart(counts)



    # AI 관련 과목 Word Cloud

    subjects_data = data[data['과목명'].str.contains('AI|인공지능|머신러닝|기계학습|딥러닝|빅데이터', case=False, na=False)]['과목명']
    all_subjects_text = ' '.join(subjects_data.astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(
        all_subjects_text)
    st.subheader('AI 관련 과목 Word Cloud')
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
    st.write("실행할 때마다 조금씩 다르게 출력됨")







