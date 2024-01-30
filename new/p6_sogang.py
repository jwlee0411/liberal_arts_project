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
        
서강대학교의 교양교육 과정은 학생들의 전인적인 발달을 목적으로 하며, 창의적 지성, 봉사적 인성, 통합적 영성의 세 가지 주요 요소에 초점을 맞추고 있습니다. 이러한 교양교육의 목표는 학생들이 미래 지향적 학문의 바탕을 형성하고, 창의성과 리더십을 개발하며, 이웃에 대한 관심과 공감 능력을 배양하는 것을 포함합니다. 서강대학교는 학문적 성취, 융합적 창의, 글로벌 역량, 대인관계, 공동체 봉사, 리더십, 자아 성찰, 보편적 세계관, 지행 일치 등 다양한 핵심 역량을 통해 학생들의 융복합 창의 인재 양성을 목표로 합니다.

이러한 교육 과정의 일환으로, 공통필수교과와 공통선택교과 과목이 제공됩니다. 공통필수교과는 모든 학생이 이수해야 하는 교양 기초 과목으로, 총 8학점(국제 학생은 7학점)으로 구성되어 있습니다. 반면, 공통선택교과는 창의적 사고력, 비판적 사고력, 통합적 사고력, 문제 해결 능력, 융합적 역량을 함양하기 위해 설계된 과목들로, 총 12학점 이상을 이수해야 합니다.

교양교육 수는 2019년까지 꾸준히 증가하다가 2020년부터 소폭 감소하는 형태를 보이고 있습니다. 이는 2019년도 교양과목 개편으로 인해 발생한 것으로 보입니다. 2019학년도에 ”중핵필수”, ”중핵선택” 명칭이 ”공통필수”, ”공통선택”으로 바뀌면서 개설 과목은 줄었지만 학생들의 교양과목 선택 폭이 더욱 넓어졌습니다. 이는 대학의 교육과정이 유연성을 높이고 학생들의 다양한 학문적 관심과 필요를 반영하기 위함으로 분석됩니다. 학문 간 경계를 허물고 보다 통합적이고 실용적인 교육에 중점을 둔 변화를 향해 나아가는 과정입니다. 또한 위 자료에서 볼 수 있듯이 대부분의 교양과목은 전인교육원에서 담당하며, 각 학과에서 개설한 교양교육도 존재합니다.

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