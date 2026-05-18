```python
import streamlit as st
import folium

st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.write("서울의 인기 관광지를 확인해보세요!")

# 관광지 데이터 (TOP10)
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
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "subway": "홍대입구역",
        "fun": "버스킹, 카페 투어"
    },
    {
        "name": "강남",
        "lat": 37.4979,
        "lon": 127.0276,
        "subway": "강남역",
        "fun": "쇼핑, 맛집 탐방"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "subway": "잠실역",
        "fun": "전망대, 쇼핑몰"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.5665,
        "lon": 127.0092,
        "subway": "동대문역사문화공원역",
        "fun": "전시 관람, 야경"
    },
    {
        "name": "인사동",
        "lat": 37.5740,
        "lon": 126.9850,
        "subway": "안국역",
        "fun": "전통 기념품, 찻집"
    },
    {
        "name": "한강공원",
        "lat": 37.5289,
        "lon": 126.9326,
        "subway": "여의나루역",
        "fun": "자전거, 라면 먹기"
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

# HTML로 지도 표시
map_html = m._repr_html_()

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
