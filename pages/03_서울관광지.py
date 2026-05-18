# streamlit_folium 없이 작동하는 버전 (오류 해결)

import streamlit as st
import folium

st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.write("서울의 인기 관광지를 확인해보세요!")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.5796,
        "lon": 126.9770,
        "subway": "경복궁역",
        "fun": "한복 체험, 궁궐 산책"
    },
    {
        "name": "명동",
        "lat": 37.5636,
        "lon": 126.9827,
        "subway": "명동역",
        "fun": "쇼핑, 길거리 음식"
    },
    {
        "name": "N서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "subway": "명동역",
        "fun": "야경 감상, 사랑의 자물쇠"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "subway": "안국역",
        "fun": "전통 골목 산책, 사진 촬영"
    }
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 마커 추가
for place in places:
    popup_text = (
        f"{place['name']}<br>"
        f"가까운 지하철역: {place['subway']}<br>"
        f"놀거리: {place['fun']}"
    )

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_text,
        tooltip=place["name"]
    ).add_to(m)

# HTML로 저장
map_html = m._repr_html_()

# Streamlit에 지도 표시
st.components.v1.html(
    map_html,
    height=600
)

st.markdown("---")
st.subheader("📌 관광지 정보")

for place in places:
    st.write(
        f"{place['name']} → 가까운 지하철역: {place['subway']} | 놀거리: {place['fun']}"
    )
