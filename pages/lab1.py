import streamlit as st

st.title('lab1')

file = st.file_uploader("upload_file")
if file is None:
    file = st.camera_input("take a picture")

st.download_button("사진을 다운로드 받으세요", file)

