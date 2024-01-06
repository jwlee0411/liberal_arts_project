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
    st.title('한국외국어대학교')
    st.write("""
        한국외국어대학교의 교양과정은 다방면에 걸쳐 넓고 깊고 건전한 교양인을 양성하기 위한 인간교육을 그 이념으로 하고 있다. 즉, 교양과정을 통하여 인간으로서의 건전한 가치관을 확립하며 전문분야에서 놓치기 쉬운 제 학문에 대한 편협성을 제거하여 학문 간의 상호관련성에 대한 이해를 증진시키고, 지적발달과 함께 정서적, 신체적 발달의 균형을 꾀하여 전인적 인간을 양성하는 데 있다. 이와 같은 목적을 달성하기 위하여 한국외국어대학교에서는 다양한 교양 교과목을 개설하여 학생들이 자유로이 선택수강할 수 있도록 하고 있다. 교양 교과목은 보통 2학점(2시간)으로 편성되어 있다. 

        교양교육 영역은 크게 인성교육 영역, 미네르바인문 영역, 대학 외국어 영역, 소프트웨어 기초 영역, 핵심인문기초 영역, 언어와 문학 영역, 문화와 예술 영역, 역사와 철학영역 등으로 구성되어 있음을 확인할 수 있다. 
        """)

    st.write(f"""
        출처: 한국외국어대학교 홈페이지 [https://builder.hufs.ac.kr/index.html](https://builder.hufs.ac.kr/index.html)

        ### 수집 방법

        1. 한국외국어대학교 홈페이지 - 상단 메뉴 학사정보 - 교육과정 - 교과과정일람
        2. 각 년도별 교과과정 PDF 다운로드
        3. Excel로 수기 입력
        """)









