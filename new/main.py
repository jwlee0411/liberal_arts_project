import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import p0_home, p1_nutshell, p2_soongsil, p3_kaist, p4_kyeonghi, p5_korea, p6_sogang, p7_seoul
import p8_seoul_city, p9_seongkyunkwan, p10_yonsei, p11_ewha, p12_joongang, p13_pohang, p14_hanyang, p15_hufs
import p16_fin

st.sidebar.title("서울시 주요대학 교양교육 데이터 분석")


menu = ["개요", "종합 분석", "숭실대학교", "KAIST","경희대학교", "고려대학교", "서강대학교", "서울대학교", "서울시립대학교", "성균관대학교", "연세대학교", "이화여자대학교"
        , "중앙대학교", "포항공과대학교", "한양대학교", "한국외국어대학교", "결론"]

choice = st.sidebar.selectbox("메뉴", menu)

reg_semester = ['2003-1', '2003-2', '2004-1', '2004-2', '2005-1', '2005-2',
                    '2006-1', '2006-2', '2007-1', '2007-2', '2008-1', '2008-2',
                    '2009-1', '2009-2', '2010-1', '2010-2', '2011-1', '2011-2',
                    '2012-1', '2012-2', '2013-1', '2013-2', '2014-1', '2014-2',
                    '2015-1', '2015-2', '2016-1', '2016-2', '2017-1', '2017-2',
                    '2018-1', '2018-2', '2019-1', '2019-2', '2020-1', '2020-2',
                    '2021-1', '2021-2', '2022-1', '2022-2', '2023-1', '2023-2', *[str(y) for y in range(2008, 2024)]]


font_path = './res/gyeonggi_medium.ttf'

if choice == "개요":
    p0_home.show()
elif choice == "종합 분석":
    p1_nutshell.show(reg_semester, font_path)
elif choice == "숭실대학교":
    p2_soongsil.show(reg_semester, font_path)
elif choice == "KAIST":
    p3_kaist.show(reg_semester, font_path)
elif choice == "경희대학교":
    p4_kyeonghi.show(reg_semester, font_path)
elif choice == "고려대학교":
    p5_korea.show(reg_semester, font_path)
elif choice == "서강대학교":
    p6_sogang.show(reg_semester, font_path)
elif choice == "서울대학교":
    p7_seoul.show(reg_semester, font_path)
elif choice == "서울시립대학교":
    p8_seoul_city.show(reg_semester, font_path)
elif choice == "성균관대학교":
    p9_seongkyunkwan.show(reg_semester, font_path)
elif choice == "연세대학교":
    p10_yonsei.show(reg_semester, font_path)
elif choice == "이화여자대학교":
    p11_ewha.show(reg_semester, font_path)
elif choice == "중앙대학교":
    p12_joongang.show(reg_semester, font_path)
elif choice == "포항공과대학교":
    p13_pohang.show(reg_semester, font_path)
elif choice == "한양대학교":
    p14_hanyang.show(reg_semester, font_path)
elif choice == "한국외국어대학교":
    p15_hufs.show(reg_semester, font_path)
elif choice == "결론":
    p16_fin.show()
else:
    p0_home.show()

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

