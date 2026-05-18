# Streamlit Cloud용 서울 관광지 TOP10 지도 앱

## app.py

```python
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🌏 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.markdown("지도를 클릭하면 가까운 지하철역과 놀거리를 아래에서 확인할 수 있습니다.")

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

# 서울 중심 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

for place in places:
    popup_text = f"📍 {place['name']}"

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_text,
        tooltip=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 출력
map_data = st_folium(m, width=1000, height=600)

st.markdown("---")
st.subheader("📌 관광지 정보")

clicked_place = None

if map_data and map_data.get("last_object_clicked"):
    clicked_lat = map_data["last_object_clicked"]["lat"]
    clicked_lon = map_data["last_object_clicked"]["lng"]

    for place in places:
        if abs(place["lat"] - clicked_lat) < 0.001 and abs(place["lon"] - clicked_lon) < 0.001:
            clicked_place = place
            break

if clicked_place:
    st.success(
        f"{clicked_place['name']} → 가까운 지하철역: {clicked_place['subway']} | 놀거리: {clicked_place['fun']}"
    )
else:
    st.info("지도에서 관광지를 클릭해보세요!")
```

---
