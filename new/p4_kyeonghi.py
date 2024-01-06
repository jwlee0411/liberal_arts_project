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
    st.title('경희대학교')
    st.write("""
        경희대학교 교양교육과정은 필수교과, 배분이수교과와  자유이수교과로 나누어져있다.

        필수교과 과목은 인간을 이해하고 세계를 이해하는 것은 전공 지망이 무엇이냐에 관계없이 학부생들이 반드시 공부해야 하고 대학은 반드시 가르쳐야 하는 기본적인 탐구 영역이며, 교양교육이 다루어야 할 핵심주제임을 인지하고 이에 따른 과목으로 수성되어 있다.  배분이수교과는 인간, 사회, 자연, 문화, 예술, 세계, 윤리 등의 다양한 주제들을 다룬다. 이 주제들에 대한 접근방식은 어느 한 가지 학문분과의 접근법에 한정되지 않는 학제적 교육에 강조점을 두고 있으며 각 주제영역의 기본과 원리에 관한 근본적이고 원리적인 것들을 학습할 수 있는 교육과정 영역이다. 자유이수교과는 외국어, 체육, 예술 그리고 기타 주요 영역에서 수강자들이 자유롭게 선택하여 자신들의 다양한 관심과 욕구를 충족시킴과 동시에 자기계발 및 실용성에 도움이 될 수 있는 교과과정이다.
        
        출처: 경희대학교 후마니타스 칼리지 https://hc.khu.ac.kr/hc_kor/user/main/view.do

        """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '경희대학교']

    # Word Cloud
    subjects_data = data[data['대학교'].isin(['경희대학교'])]['과목명']
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


    st.subheader('교양영역 별 2023년 개설과목 수')
    st.bar_chart(
        uni_subset[uni_subset['개설연도'].isin(['2023', '2023-2', '2023-1', '2023-겨울', '2023-여름'])].groupby('교양영역')[
            ['개설연도', '과목명']].count()['과목명'])

    st.subheader('수집 방법')
    st.write("""
           1. 경희대학교 후마니타스 칼리지 홈페이지 - 상단메뉴 학사안내 - 교육과정 - 개설 교과목
            2. PDF 다운로드 이후 수기로 데이터 입력

           """)