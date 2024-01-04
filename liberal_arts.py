import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import soongsil
import snu
import kyeonghi
import yonsei
import hanyang
import seongkyunkwan
import seoulcity
import chungang
import hufs
import korea

st.title('서울시 주요대학 교양교육 데이터')

@st.cache_data
def load_data():
    data = pd.read_csv('./total.csv', encoding='utf-8')
    return data

data = load_data()

reg_semester = ['2003-1', '2003-2', '2004-1', '2004-2', '2005-1', '2005-2',
       '2006-1', '2006-2', '2007-1', '2007-2', '2008-1', '2008-2',
       '2009-1', '2009-2', '2010-1', '2010-2', '2011-1', '2011-2',
       '2012-1', '2012-2', '2013-1', '2013-2', '2014-1', '2014-2',
       '2015-1', '2015-2', '2016-1', '2016-2', '2017-1', '2017-2',
       '2018-1', '2018-2', '2019-1', '2019-2', '2020-1', '2020-2',
       '2021-1', '2021-2', '2022-1', '2022-2', '2023-1', '2023-2', *[str(y) for y in range(2008, 2024)]]

st.header('대학별 종합', divider='rainbow')

st.subheader('2023년 개설 교양과목 수')
st.write("일부 대학은 교양필수 과목 데이터만 수집되어, 데이터 해석에 주의바람")

st.bar_chart(data[data['개설연도'].isin(['2023-2', '2023-1', '2023'])].groupby('대학교').count()['과목명'])

if st.checkbox('원본 데이터 확인'):
    st.write(data)

for uni in ['숭실대학교', 'KAIST', '경희대학교', '고려대학교', '서강대학교', '서울대학교', '서울시립대학교', '성균관대학교',
       '연세대학교', '이화여대', '중앙대학교', '포항공과대학교', '한양대학교']:
    st.header(uni, divider='rainbow')
    uni_subset = data[data['대학교'] == uni]

# 대학별 교양 소개

    if uni == '숭실대학교':
        soongsil.intro()

    if uni == 'KAIST':
        st.write("""
        KAIST는 
        """)

    if uni == '경희대학교':
        kyeonghi.intro()

    if uni == '고려대학교':
        korea.intro()

    if uni == '서강대학교':
        st.write("""
        서강대학교는
        """)

    if uni == '서울대학교':
        snu.intro()

    if uni == '중앙대학교':
        chungang.intro()

    if uni == '서울시립대학교':
        seoulcity.intro()

    if uni == '성균관대학교':
        seongkyunkwan.intro()

    if uni == '연세대학교':
        yonsei.intro()

    if uni == '한양대학교':
        hanyang.intro()

    if uni in ['숭실대학교', '서강대학교', '서울시립대학교', '성균관대학교', '한양대학교']:
        st.subheader('교양과목 수')
        st.bar_chart(uni_subset.groupby('개설연도').count()['과목명'])
        ex_vac_session = uni_subset[uni_subset['개설연도'].isin(reg_semester)]
        st.line_chart(ex_vac_session.groupby('개설연도').count()['과목명'])
        if uni == '숭실대학교':
            pass
    if uni in ['숭실대학교', '서울대학교', '고려대학교', 'KAIST', '서강대학교', '성균관대학교', '한양대학교', '이화여대', '서울시립대학교']:
        st.subheader('교양과목 개설학과')
        st.bar_chart(uni_subset.groupby('개설학과').count()['과목명'])
        ex_vac_session = uni_subset[uni_subset['개설연도'].isin(reg_semester)]

    if uni in ['경희대학교', '고려대학교', '서울시립대학교', '연세대학교', '한양대학교']:
        st.subheader('교양영역 별 2023년 개설과목 수')
        st.bar_chart(uni_subset[uni_subset['개설연도'].isin(['2023', '2023-2', '2023-1', '2023-겨울', '2023-여름'])].groupby('교양영역')[['개설연도', '과목명']].count()['과목명'])

    if uni == '포항공과대학교':
        st.subheader('교양영역 별 2022년 개설과목 수')
        st.bar_chart(uni_subset[uni_subset['개설연도'] == '2022'].groupby('교양영역')[['개설연도', '과목명']].count()['과목명'])

    if uni == '숭실대학교':
        st.subheader('SW 교육팀 개설 교양과목 추이')
        st.line_chart(ex_vac_session[ex_vac_session['개설연도'].isin(['2020-2', '2021-1', '2021-2', '2022-1', '2022-2', '2023-1', '2023-2'])].groupby(['개설연도', '개설학과'])['과목명'].count().unstack('개설학과'), y=['SW교육팀'])

        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '숭실대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '숭실대학교'])
        
        st.write(f"""
            출처: 숭실대학교 유세인트 [https://saint.ssu.ac.kr/](https://saint.ssu.ac.kr/)

            ### 수집 방법

            1. 숭실대학교 유세인트 접속
            2. 학사관리 - 수강신청/교과과정 - 강의시간표 - 교양필수/교양선택 - 학년도 및 학기 선택
            3. 엑스포트
            """)

    if uni == 'KAIST':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == 'KAIST'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == 'KAIST'])

        st.write(f"""
            출처:
            - KAIST Academic System: [https://cais.kaist.ac.kr/totalOpeningCourse](https://cais.kaist.ac.kr/totalOpeningCourse)
            - KAIST 학사요람 SYSTEM: [https://bulletin.kaist.ac.kr/html/kr/?year=2023&id=kr20230301&gbn=C2](https://bulletin.kaist.ac.kr/html/kr/?year=2023&id=kr20230301&gbn=C2)

            #### 데이터 수집 방법

            1. KAIST Academic System 접속
            2. 과목구분 교양선택/교양필수/교양필수(봉사)/교양필수(체육) 선택
            3. 조회된 테이블을 Excel에 복사 붙여넣기하여 수집
            """)

    if uni == '경희대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '경희대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '경희대학교'])

        st.write(f"""
            출처: 경희대학교 후마니타스 칼리지 [https://hc.khu.ac.kr/hc_kor/user/main/view.do](https://hc.khu.ac.kr/hc_kor/user/main/view.do)

            ### 수집 방법

            1. 경희대학교 후마니타스 칼리지 홈페이지 - 상단메뉴 학사안내 - 교육과정 - 개설 교과목
            2. PDF 다운로드 이후 수기로 데이터 입력
            """)

    if uni == '고려대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '고려대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '고려대학교'])
        
        st.write(f"""
            출처: 고려대학교 교양교육원 홈페이지 [https://ge.korea.ac.kr/ge/index.do](https://ge.korea.ac.kr/ge/index.do)

            ### 수집 방법

            1. 고려대학교 교양교육원 홈페이지 - 상단 메뉴 교과목 안내
            2. 각 과목별 페이지 접근하여 수기 또는 자동화 웹 스크래핑 프로그램으로 수집
            """)

    if uni == '서강대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '서강대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '서강대학교'])

        st.write("""
            출처:
            - 서강대학교 홈페이지: [https://sogang.ac.kr/index.do](https://sogang.ac.kr/index.do)
            - 서강대학교 전인교육원: [https://scc.sogang.ac.kr/wholeperson/index_new.html](https://scc.sogang.ac.kr/wholeperson/index_new.html)

            ### 수집 방법

            1. 서강대학교 홈페이지 - 상단 메뉴 학사·학생지원 - 개설과목정보 - 조건 검색
            2. 다운로드 버튼 클릭 - excel 다운로드
            """)

    if uni == '서울대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '서울대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '서울대학교'])

        st.write(f"""
            출처: 서울대학교 기초교육원 [https://liberaledu.snu.ac.kr/](https://liberaledu.snu.ac.kr/)

            ### 수집 방법

            1. 서울대학교 기초교육원 홈페이지 접속
            2. 상단 메뉴 교양교육과정 - 영역 및 교과목 - 영역별 교과목 선택
            3. 각 분류별 테이블을 엑셀로 복사/붙여넣기 하거나, 자동화 웹 스크래핑 프로그램으로 수집
            """)

    if uni == '서울시립대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '서울시립대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '서울시립대학교'])

        st.write(f"""
        출처: 서울시립대학교 [https://www.uos.ac.kr/kor/html/uaInfo/major/curriculum/curriculum2020.do](https://www.uos.ac.kr/kor/html/uaInfo/major/curriculum/curriculum2020.do)

        ### 수집 방법

        1. 상단 메뉴 대학 및 대학원 - 학사 - 전공/교과/교직
        2. 교과과정 선택
        3. 교양교과목 다운로드
        4. HWP 파일에서 교양과목 데이터 수기로 데이터 수집
        """)

    if uni == '성균관대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '성균관대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '성균관대학교'])

        st.write("""
        출처: 성균관대학교 학부대학 홈페이지 [https://hakbu.skku.edu/hakbu/index.do](https://hakbu.skku.edu/hakbu/index.do)

        ### 수집 방법

        1. 
        """)

    if uni == '연세대학교':
        yonsei_count = uni_subset.groupby('개설학과').count()['과목명']

        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '연세대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '연세대학교'])
        
        st.write(f"""
        출처: 연세대학교 학부대학 [https://universitycollege.yonsei.ac.kr/fresh/index.do](https://universitycollege.yonsei.ac.kr/fresh/index.do)

        ### 수집 방법

        1. 연세대학교 학부대학 홈페이지 - 상단 메뉴 교양교육 - 교과과정 - 교양기초/대학교양/기초교육
        2. 각 페이지에 접근하여 자동화 웹 스크래핑 프로그램으로 수집
        """)

    if uni == '이화여대':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '이화여대'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '이화여대'])

        st.write(f"""
            출처: 이화여자대학교 호크마교양대학 [https://hokma.ewha.ac.kr/hokma/index.do](https://hokma.ewha.ac.kr/hokma/index.do)

            ### 수집 방법

            1. 
            """)

    if uni == '중앙대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '중앙대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '중앙대학교'])
        
        st.write(f"""
            출처: 

            ### 수집 방법

            1. 
            """)

    if uni == '포항공과대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '포항공과대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '포항공과대학교'])

        st.write(f"""
            출처: POSTECH 인문사회학부 - [https://hss.postech.ac.kr/](https://hss.postech.ac.kr/)

            ### 수집 방법

            1. 상단 교과과정 메뉴 - 교과목 개요
            2. 자동화 웹 스크래핑 프로그램으로 수집
            """)

    if uni == '한양대학교':
        if st.checkbox(f'{uni} 원본 데이터'):
            if st.checkbox('계절학기 데이터 제외하기'):
                st.write(data[data['대학교'] == '한양대학교'][data['개설연도'].isin(reg_semester)])
            else:
                st.write(data[data['대학교'] == '한양대학교'])
        
        st.write("""
            출처: 한양대학교 수강신청 포털 수강편람 [https://portal.hanyang.ac.kr/sugang/sulg.do#!UDMxMDI3OCRAXnN1Z2FuZy8kQF4wJEBeTTAwNjYzMSRAXuyImOqwle2OuOuejCRAXk0wMDY2MzEkQF5lOTA2ODU5ODUyNGUwMDRhNGFmNmQ5NmQzNDQxMGZhNTY3MDVlNzZiYjJmN2ZjMmRmMzU3Mjk0NzFiMGYzYjQ1IA==!](https://portal.hanyang.ac.kr/sugang/sulg.do#!UDMxMDI3OCRAXnN1Z2FuZy8kQF4wJEBeTTAwNjYzMSRAXuyImOqwle2OuOuejCRAXk0wMDY2MzEkQF5lOTA2ODU5ODUyNGUwMDRhNGFmNmQ5NmQzNDQxMGZhNTY3MDVlNzZiYjJmN2ZjMmRmMzU3Mjk0NzFiMGYzYjQ1IA==!)

            ### 수집 방법

            1. 한양대학교 수강신청 포털 - 상단 메뉴 수강편람 - 조건 검색
            2. 조건검색 후 엑셀 다운로드
            """)
            
st.header('한국외국어대학교', divider='rainbow')
hufs.intro()