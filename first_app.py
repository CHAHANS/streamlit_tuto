#streamlit run <streamlitapp>.py 로 실행한다.
import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs

def predict__(picture):
    """
    모델 호출
    예측 결과 출력
    """
    result = picture
    return result

def recommend_menu(A):
    data = pd.read_csv("TB_RECIPE_SEARCH-220701.csv", encoding='cp949')
    result = data.query('CKG_NM == @A')
    return result.head()

def recipe_infor(A):
    data= pd.read_csv("recipe_info_20230201", encoding='cp949')

# def recommend_video_url(A):
#     """_summary_
#     구상중..
#     1. 크롤링해서 유튜브 숏츠에서 검색
#     2. 블로그검색.?
#     Args:
#         A (str): 먹고싶은 메뉴를 입력한 문자

#     Returns:
#         _type_: URL크롤링 해서 따옴
#     """
#     main_url = 'https://www.youtube.com/results?search_query='+A
#     short_html = requests.get(main_url)
#     short = bs(short_html.text, "html.parser")
#     short_raw = naver.find(class_="type_5")
#     naver_raw2 = naver_raw.find_all("td", {"class":"number"})
#     a=0
#     b=1
#     for j in naver_raw.find_all(class_="tltle")[:10]:
#         a+=1
#         print(f"{a}위 {j.text} : {naver_raw2[b].text}원") 
#         b+=10
#     return 
    

## main
if __name__ == "__main__":
    tab1, tab2, tab3 = st.tabs(["냉장고서칭", "추천레시피", "content"])
    tab1.title('Recommend Servise')
    picture = tab1.file_uploader("Take a picture")
    result = predict__(picture)
    tab1.text(f"당신의 냉장고에는 {result}가 있습니다.")
    # 추천을 위한 추가 input은 정한 후 삽입
    
    #메뉴 입력시 레시피에서 검색해서 출력
    tab2.title('HELLO')
    menu = tab2.text_input('메뉴를 입력하세요')
    menus = recommend_menu(menu)
    tab2.dataframe(data=menus, width=None, height=None)
    
    #레시피 정보
    
    #결과 기반으로 유튜브 쇼츠 출력창

