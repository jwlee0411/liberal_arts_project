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

    data = main.load_data()






    st.title('종합 분석')

    st.write('본 보고서는 각 대학 별 교양교육 목적 및 이수체계와 교양과목 데이터 수집 방법을 정리하는 목적아래 작성되었다. 각 대학별로 공개적으로 수집가능한 개설 교양과목 데이터가 상이했다. (수집 기간, 수집 가능 데이터의 종류 등) 따라서 본 보고서에서 제한적인 범위에서 분석이 이루어졌다. 또한 본 보고서 작성을 위해 수집된 데이터들은 2차 사용 가능여부를 확인하지 않고, 웹에서 자체적으로 수집하여 진행하였으므로 추후 연구 등 2차 사용목적으로 데이터를 수집 및 이용하기 전 데이터 사용 범위를 확인 할 필요가 있다.')

    st.write("\n")

    # 2023년 개설 교양과목 수
    st.bar_chart(data[data['개설연도'].isin(['2023-2', '2023-1', '2023', '2023-여름', '2023-겨울'])].groupby('대학교').count()['과목명'])

    st.markdown("""
        <style>
        .centered {
            text-align: center;
            color: gray;
        }
        </style>
        <div class="centered">2023년 개설 교양과목 수</div>
        """, unsafe_allow_html=True)


    st.write("")



    # 2023 Word Cloud
    subjects_data = data[data['개설연도'].isin(['2023-2', '2023-1', '2023', '2023-여름', '2023-겨울'])]['과목명']
    all_subjects_text = ' '.join(subjects_data.astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(
        all_subjects_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    st.markdown("""
        <style>
        .centered {
            text-align: center;
            color: gray;
        }
        </style>
        <div class="centered">2023년 개설 교양과목 키워드 Word Cloud</div>
        """, unsafe_allow_html=True)


    st.write("")

    st.write('코로나19 이후 교양과목 데이터에서는 ’대면’이라는 키워드를 가장 크게 확인할 수 있었다. 수업 관련 키워드로는 ’고전읽기’가 가장 눈에 띄는 것으로 확인할 수 있었고, 데이터를 가장 많이 확보하고 있는 숭실대학교 교양데이터 키워드가 많이 확인되는 것을 볼 수 있다.')




    st.bar_chart(
        data[data['과목명'].str.contains('AI|인공지능|머신러닝|기계학습|딥러닝|빅데이터', case=False, na=False)].groupby('대학교').count()['과목명']
    )



    st.markdown("""
        <style>
        .centered {
            text-align: center;
            color: gray;
        }
        </style>
        <div class="centered">대학별 인공지능(AI) 관련 과목 수 (키워드: AI, 인공지능, 머신러닝, 기계학습, 딥러닝, 빅데이터)</div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("각 대학별 데이터를 일일이 살펴본 결과 소프트웨어 및 인공지능 관련 교과목이 최근 많이 개설된 것을 확인할 수 있었다. 따라서 각 키워드 별로 대학별 데이터를 정리하였다.")


    # 키워드별로 그룹화하여 카운트
    keywords = ['AI', '인공지능', '빅데이터', '머신러닝', '기계학습', '딥러닝', ]
    keyword_counts = {}
    for keyword in keywords:
        keyword_counts[keyword] = data[data['과목명'].str.contains(keyword, case=False, na=False)].groupby('대학교').count()[
            '과목명']



    for keyword, counts in keyword_counts.items():

        st.bar_chart(counts)

        st.markdown(f"""
               <style>
               .centered {{
                   text-align: center;
                   color: gray;
               }}
               </style>
               <div class="centered">대학별 인공지능(AI) 관련 과목 수 (키워드 : {keyword})</div>
               """, unsafe_allow_html=True)
        st.write("")
        st.write("")




    # AI 관련 과목 Word Cloud

    subjects_data = data[data['과목명'].str.contains('AI|인공지능|머신러닝|기계학습|딥러닝|빅데이터', case=False, na=False)]['과목명']
    all_subjects_text = ' '.join(subjects_data.astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(
        all_subjects_text)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    st.markdown(f"""
                   <style>
                   .centered {{
                       text-align: center;
                       color: gray;
                   }}
                   </style>
                   <div class="centered">AI 관련 개설 교양과목 키워드 Word Cloud</div>
                   """, unsafe_allow_html=True)







