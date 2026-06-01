import streamlit as st
import folium

# 페이지 설정
st.set_page_config(
    page_title="서울 따릉이 인기 대여소 TOP10",
    layout="wide"
)

st.title("🚲 서울 따릉이 인기 대여소 TOP10")
st.write("아래 버튼을 눌러 대여소 정보를 확인하세요.")

stations = [
    ["여의도역 1번출구", 37.5217, 126.9243, "영등포구", 158000],
    ["강남역 11번출구", 37.4979, 127.0276, "강남구", 151000],
    ["홍대입구역 2번출구", 37.5571, 126.9244, "마포구", 146000],
    ["잠실역 8번출구", 37.5133, 127.1001, "송파구", 142000],
    ["서울역 15번출구", 37.5559, 126.9723, "중구", 139000],
    ["건대입구역 6번출구", 37.5403, 127.0704, "광진구", 135000],
    ["신림역 3번출구", 37.4840, 126.9295, "관악구", 132000],
    ["고속터미널역 8번출구", 37.5048, 127.0048, "서초구", 128000],
    ["왕십리역 6번출구", 37.5612, 127.0372, "성동구", 125000],
    ["종로3가역 15번출구", 37.5701, 126.9910, "종로구", 121000]
]

if "selected_station" not in st.session_state:
    st.session_state.selected_station = None

m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

for station in stations:
    folium.Marker(
        location=[station[1], station[2]],
        popup=station[0],
        tooltip=station[0]
    ).add_to(m)

st.components.v1.html(
    m._repr_html_(),
    height=600
)

st.markdown("---")
st.subheader("📌 대여소 정보")

cols = st.columns(2)

for i, station in enumerate(stations):
    with cols[i % 2]:
        if st.button(station[0]):
            st.session_state.selected_station = station

if st.session_state.selected_station:

    station = st.session_state.selected_station

    st.success(
        f"""
📍 대여소명 : {station[0]}

🏙️ 지역 : {station[3]}

🚲 대여 건수 : {station[4]:,}건
"""
    )

else:
    st.info("대여소 버튼을 선택하세요.")
