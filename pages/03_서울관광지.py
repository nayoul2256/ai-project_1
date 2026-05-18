import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.write("지도에서 관광지를 클릭해보세요!")

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
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "subway": "홍대입구역",
        "fun": "버스킹, 카페 투어"
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
        place["name"] + "<br>"
        + "가까운 지하철역: " + place["subway"] + "<br>"
        + "놀거리: " + place["fun"]
    )

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_text,
        tooltip=place["name"],
        icon=folium.Icon(color="blue")
    ).add_to(m)

# 지도 출력
st_folium(
    m,
    width=1000,
    height=600
)

st.markdown("---")
st.subheader("📌 관광지 정보")

for place in places:
    st.write(
        f"{place['name']} → 가까운 지하철역: {place['subway']} | 놀거리: {place['fun']}"
    )
