import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("🧠 스마트상권 헬스체크")
st.write("AI가 분석한 상권 건강지수를 확인해보세요.")

df = pd.DataFrame({
    '상권': ['황리단길', '성건동', '충효동'],
    '위도': [35.8352, 35.8573, 35.8700],
    '경도': [129.2113, 129.2167, 129.2201],
    '건강지수': [85.3, 70.1, 62.7],
    '추천업종': ['패션소품', '카페', '디저트']
})

m = folium.Map(location=[35.84, 129.21], zoom_start=13)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=10,
        popup=f"{row['상권']} (건강지수 {row['건강지수']})",
        color='blue',
        fill=True,
        fill_color='green' if row['건강지수'] > 75 else 'orange'
    ).add_to(m)

st_data = st_folium(m, width=700, height=500)
