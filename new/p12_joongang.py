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
    st.title('중앙대학교')
    st.write("""
         2023년 중앙대학교 교양교육과정은 공통교양, 핵심교양, 선택교양으로 구분되어 있다. 해당 대학의 인재상
은 「다빈치형 창의인재」로 4차 산업혁명 시대를 선도할 창의역량과 융합적 전공지식을 갖춘 인재를 의미한
다. 핵심역량은 「문화적 상상력(Cultural imagination)」기반의 창의(Creativity), 소통(Communication), 도전
(Challenge), 신뢰(Credibility), 융합(Convergence)역량을 의미하며, 이러한 핵심역량을 바탕으로 교양교육
과정을 편성하였다. 중앙대학교의 핵심역량은 4차 산업혁명의 4C 핵심역량과 연계하여 미래 사회에서도 인
공지능과 로봇이 대체할 수 없는, 여전히 인간의 영역으로 유지될 활동을 수행하기 위한 4C 역량(Critical
Thinking, Creativity, Communication, Collaboration) 강화를 목적으로 한다.

         """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '중앙대학교']




    # Word Cloud
    subjects_data = data[data['대학교'].isin(['중앙대학교'])]['과목명']
    all_subjects_text = ' '.join(subjects_data.astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(
        all_subjects_text)
    st.subheader('개설 교양과목 키워드 Word Cloud')
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)







