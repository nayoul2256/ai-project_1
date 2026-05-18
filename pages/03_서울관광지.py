import streamlit as st
import folium

# 페이지 설정
st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🌏 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.write("지도에서 관광 명소를 클릭하면 아래에 설명이 표시됩니다!")

# 관광지 데이터
places = [
    ["경복궁", 37.5796, 126.9770, "경복궁역", "한복 체험, 궁궐 산책"],
    ["명동", 37.5636, 126.9827, "명동역", "쇼핑, 길거리 음식"],
    ["N서울타워", 37.5512, 126.9882, "명동역", "야경 감상, 사랑의 자물쇠"],
    ["북촌한옥마을", 37.5826, 126.9830, "안국역", "전통 골목 산책, 사진 촬영"],
    ["홍대거리", 37.5563, 126.9220, "홍대입구역", "버스킹, 카페 투어"],
    ["강남", 37.4979, 127.0276, "강남역", "쇼핑, 맛집 탐방"],
    ["롯데월드타워", 37.5131, 127.1025, "잠실역", "전망대, 쇼핑몰"],
    ["DDP", 37.5665, 127.0092, "동대문역사문화공원역", "전시 관람, 야경"],
    ["인사동", 37.5740, 126.9850, "안국역", "전통 기념품, 찻집"],
    ["한강공원", 37.5289, 126.9326, "여의나루역", "자전거, 라면 먹기"]
]

# 세션 상태로 클릭된 장소 저장
if "selected_place" not in st.session_state:
    st.session_state.selected_place = None

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 마커 추가
for place in places:
    name = place[0]
    lat = place[1]
    lon = place[2]
    subway = place[3]
    fun = place[4]

    popup_text = name

    folium.Marker(
        location=[lat, lon],
        popup=popup_text,
        tooltip=name
    ).add_to(m)

# 지도 출력
map_html = m._repr_html_()
st.components.v1.html(map_html, height=600)

st.markdown("---")
st.subheader("📌 관광지 설명")

# 버튼으로 선택 가능하게 추가 (클릭 대체)
cols = st.columns(2)

for i, place in enumerate(places):
    with cols[i % 2]:
        if st.button(place[0]):
            st.session_state.selected_place = place

# 선택된 관광지 설명 출력
if st.session_state.selected_place:
    place = st.session_state.selected_place

    st.success(
        f"""
        📍 관광지: {place[0]}

        🚇 가까운 지하철역: {place[3]}

        🎉 놀거리: {place[4]}
        """
    )
else:
    st.info("아래 버튼에서 관광지를 선택하면 설명이 표시됩니다.")
