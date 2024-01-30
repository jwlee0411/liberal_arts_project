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
    st.title('이화여자대학교')
    st.write("""
      
이화여자대학교의 호크마교양대학은 전공을 결정하지 않고 들어오는 제도로 자유전공학부에서 더 발전한 형태인 미래지향적 교양교육을 위해서 2015년 설립된 교양교육 전담 교육기관이다. 이화여자대학교 교양 과목은 2009년, 2016년 교양교육과정 전면 개편을 거쳤으며, 기초교양은 '기독교와 세계', '나눔과 공존의 리더십' 등의 교과목을 통한 기초인성 교육과 이론적, 실천적 인성 교육의 통합형 교과목을 개설한 '이화진선미', '사고와 표현', '글로벌 의사소통', '컴퓨팅과 수리적 사고' 영역으로 구성되고, '문학과 언어', '역사와 철학', '예술과 표현', '과학과 기술', '인간과 사회' 5개의 융복합교양 영역, '인문학큐브', '콘텐츠큐브', '디자인큐브' 3개 큐브 영역이 있다. 이화여대 교양과목 개설학과는 이화인문과학원, 사학과가 많은 것을 알 수 있다.
         """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '이화여대']

    # Word Cloud
    subjects_data = data[data['대학교'].isin(['이화여대'])]['과목명']
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


    st.write("""
     ### 출처
      
    • 이화여대 교양교과안내 https://hokma.ewha.ac.kr/hokma/curriculum/info02.do
    
    • 이화여대 교양교과이수안내 https://hokma.ewha.ac.kr/hokma/
    
    • 강의시간표 강의계획안 https://eureka.ewha.ac.kr/eureka/my/public.do
    
    ### 수집 방법
    
    1. 이화여대 호크마교양대학 사이트 - 교양교과안내 탭
    2. 교양교과과정과 교양교과안내를 통하여 전체적인 교양 교과를 파악
    3. 교양교과이수안내 - 교과과정 및 교과목 소개 링크 접근
    4. 입학생 대상 교양필수 교과목 이수 안내 파일을 다운로드
         """)

