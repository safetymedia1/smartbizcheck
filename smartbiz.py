import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("🧠 스마트상권 헬스체크")
st.write("AI가 분석한 경주의 주요 상권 건강지수를 확인해보세요.")

df = pd.DataFrame({
    '상권': ['황리단길', '성건동', '충효동', '외동읍', '동천동', '불국동', '감포읍', '서악동', '보문동'],
    '위도': [35.8352, 35.8573, 35.8700, 35.7316, 35.8428, 35.7882, 35.7126, 35.8417, 35.8323],
    '경도': [129.2113, 129.2167, 129.2201, 129.3514, 129.2102, 129.3377, 129.4615, 129.1932, 129.2904],
    '건강지수': [85.3, 70.1, 62.7, 55.0, 65.5, 78.0, 60.3, 66.7, 72.5],
    '추천업종': ['패션소품', '카페', '디저트', '식당', '편의점', '기념품점', '횟집', '문화체험관', '레저용품']
})

m = folium.Map(location=[35.84, 129.21], zoom_start=12)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=10,
        popup=f"{row['상권']} (건강지수 {row['건강지수']}) - 추천: {row['추천업종']}",
        color='blue',
        fill=True,
        fill_color='green' if row['건강지수'] > 75 else 'orange'
    ).add_to(m)

st_data = st_folium(m, width=800, height=600)
