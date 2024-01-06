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
      데이터가 왜 안뜨지 이거
         """)

    data = main.load_data()
    uni_subset = data[data['대학교'] == '이화여자대학교']

    st.subheader('교양과목 개설학과')
    st.bar_chart(uni_subset.groupby('개설학과').count()['과목명'])
    ex_vac_session = uni_subset[uni_subset['개설연도'].isin(reg_semester)]


    st.write("""
      출처: 이화여자대학교 호크마교양대학 https://hokma.ewha.ac.kr/hokma/index.do
         """)
