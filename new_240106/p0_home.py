import streamlit as st
from PIL import Image
def show():
    st.title("개요")
    st.write("이 웹사이트는 숭실교양공동체 2기 데이터사이언스팀에서 제작했습니다.")
    img = Image.open('res/p0_1.png')
    st.image(img)

    st.subheader('소스코드')
    st.write("[Github](https://github.com/jwlee0411/liberal_arts_project)")