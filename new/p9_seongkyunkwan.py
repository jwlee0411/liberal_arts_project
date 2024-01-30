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
    st.title('성균관대학교')
    st.write("""
        성균관대학교의 학부대학 교육과정은 교양교육과정과 기반과정으로 구성되어 있습니다. 교양교육과정은 합리성, 책임성, 도덕성을 겸비한 인성을 키우고, 비판적 사고와 의사소통능력을 강화하며, 공동체 정신을 함양하고 창의적인 판단 능력을 기르는 데 목표를 두고 있습니다. 또한, 글로벌 환경에 능동적으로 대처할 수 있는 능력과 학문적인 다양성을 갖추기 위한 교육을 제공합니다.

        이를 위해 성균교양(중점·균형)영역에서 성균인성·리더십, 고전·명저, 창의, 의사소통, 글로벌 등의 다양한 주제로 최소 학점(총 18학점이상 )을 이수하도록 하고 있습니다. 또한, 균형교양 영역에서는 인간/문화와 사회/역사, 자연/과학/기술의 세 가지 분야로 최소 2개 영역 이수(총 6학점 이상)가 요구됩니다.

        뿐만 아니라, 학문적 전공을 위한 기반영역에서는 인문사회과학/자연과학기반영역 및 DS교육과정을 구분하고, 각 계열 및 학과에 따라 최소 이수학점을 정하고 있습니다. 이를 통해 학생들은 종합적이고 균형 잡힌 교육을 받아 전문 분야에서 활동할 수 있는 능력과 지식을 함양하게 됩니다.

        성균관대학교의 교양과목 데이터를 분석한 결과, 2008년과 2009년의 데이터만을 확보하여 유의미한 결과 도출이 어려웠습니다. 따라서 해당 연도에 대한 정보만으로는 교양 교육의 변화나 추이 등을 파악하는 데에 제한이 있어, 보다 폭넓은 시간대의 데이터 수집이 필요함을 시사하고 있습니다.
        """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '성균관대학교']




    # 2023 Word Cloud
    subjects_data = data[data['대학교'].isin(['성균관대학교'])]['과목명']
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


    st.subheader('교양영역별 교양과목 수')
    st.bar_chart(uni_subset.groupby('교양영역').count()['과목명'])


    



    st.write(f"""
                출처: 성균관대학교 학부대학 홈페이지 https://hakbu.skku.edu/hakbu/index.do
                
                성균관대학교 정보광장 https://kingoinfo.skku.edu/gaia/nxui/outdex.html

                ### 수집 방법
                1. 성균관대학교 정보광장 접속 (성균관대학교 계정이 있어야 접근이 가능하나, 위 링크로 접근하면 강좌목록 페이지에 로그인하지 않고 접근 가능)
                2. 각 과목별 강좌목록 페이지를 수기 또는 웹 스크래핑 프로그램으로 수집
             
                """)

