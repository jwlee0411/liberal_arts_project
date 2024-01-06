import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import p0_home, p1_nutshell

st.sidebar.title("서울시 주요대학 교양교육 데이터 분석")


menu = ["개요", "종합 분석",]
choice = st.sidebar.selectbox("메뉴", menu)


if choice == "개요":
    p0_home.show()
elif choice == "종합 분석":
    p1_nutshell.show()

# 개요
# 종합 분석
# 숭실대학교
# KAIST
# 경희대학교
# 고려대학교
# 서강대학교
# 서울대학교
# 서울시립대학교
# 성균관대학교
# 연세대학교
# 이화여자대학교
# 중앙대학교
# 포항공과대학교
# 한양대학교
# 한국외국어대학교
# 결론
# 부록 및 참고자료





@st.cache_data
def load_data():
    data = pd.read_csv('./res/total.csv', encoding='utf-8')
    return data
