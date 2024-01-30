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
         포항공대는 인문사회학부에서 교양과목을 담당한다. 학부 교육의 목표는 폭넓은 소양과 비판적 사고력을 함양하는 인문사회 교육을 기반으로, 학생들이 ‘일반적 소양을 갖춘 전문가(general specialist)’로서 미래 과학기술계의 리더로 성장하는 것을 지원하는 것이다. 인문사회학부가 일류가 되어야 포스텍도 일류가 된다는 사명감으로 다양한 교육, 연구 프로그램을 진행하는 인문사회학부는 상담센터, 포항공대신문사, 어학센터, 스포츠지원센터, 영어도서관, 교육혁신센터 등 교내 기관과의 밀접한 상호협력 속에 21세기에 걸맞은 교양 교육 프로그램을 선도적으로 구현하고 있다.

학생들은 졸업 요건으로 12-14학점의 교양 필수 과목과 15-18학점의 교양 선택 과목을 이수해야 한다. 22년 기준 포스텍 인문사회학부 교과목개요를 보면, 기초필수 과목 27개, 통합 과목이 2개, 인문학 교양 선택은 문학 분야, 철학 분야, 역사 분야가 있으며, 사회과학 교양 선택은 정치약 분야, 경제학 분야, 사회학 분야, 심리학 분야, 커뮤니케이션 분야, 법학 분야, 언어학 분야가 있다. 예술 교양 선택은 예술학 분야가 있으며, 융합부전공 교양선택은 융합문명 융합부전공, 경제·금융 융합부전공, 과학기술학 융합부전공이 있다. 포항공대 교양과목의 특징은 제2외국어의 경우 교양 선택과목으로는 인정되지 않는다는 것이다. 제2외국어 관련 교과는 2017년까지 교양 과목에 해당했으나 2018년부터 제외되어 타 대학에서 관련 과목을 수강하더라도 자유 선택으로만 인정된다.

그러나 2021년 포항공대신문 ‘전공과목과 같은 3학점, 우리대학 교양 과목 실태’라는 신문에 따르면 설문조사에서 인문사회학부의 운영이 현재 설정된 목표에 부합하지 못한다고 생각한 학생들에게 이유를 질문한 결과, 과목의 다양성 부족(18명)을 꼽은 학생들이 가장 많았다. 교양 과목의 개수와 종류가 적절한 수준인지에 대한 질문에서는 70%(72명)의 학생들이 부정적인 의견을 내놓았다. 학교 측의 이유는 현재 대학 정책상 전임 교원 확보가 힘들어 교양 과목의 안정적인 개설에 문제가 있다는 것이다. 그러나 연구중심대학인 포항공대에서 이공계 글로벌 리더를 양성하는 것은 틀을 깨고 비판적으로 사고하며 새로운 지식을 창조할 수 있는 고차원적인 인재를 길러내는 포항공대 인문사회학부의 비전을 달성하기 위해서는 단순히 이공계 지식의 답습을 넘어 인문학적 소양이 필요하다. 따라서 교양과목의 다양성을 증진시키기 위하여 대학 정책 개선 등으로 전임 교원 확보를 늘리고, 안정적으로 교양 과목을 개설하여 학생들의 수요를 충족시킬 필요성이 있다.
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
