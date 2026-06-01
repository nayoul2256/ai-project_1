import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 따릉이 TOP10",
    page_icon="🚲",
    layout="wide"
)

st.title("🚲 서울 따릉이 인기 대여소 TOP10")

# ==========================
# 데이터 불러오기
# ==========================
@st.cache_data
def load_data():
    df = pd.read_csv("bike_top10.csv")
    return df

df = load_data()

# ==========================
# TOP10
# ==========================
top10 = df.sort_values(
    "대여건수",
    ascending=False
).head(10)

# ==========================
# 지도
# ==========================
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

for _, row in top10.iterrows():

    popup_html = f"""
    <b>{row['대여소명']}</b><br>
    대여건수: {row['대여건수']:,}
    """

    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=popup_html,
        tooltip=row["대여소명"]
    ).add_to(m)

map_data = st_folium(
    m,
    width=None,
    height=600
)

# ==========================
# 클릭한 마커 정보
# ==========================
st.markdown("---")
st.subheader("📍 대여소 정보")

clicked = map_data.get("last_object_clicked")

if clicked:

    lat = clicked["lat"]
    lng = clicked["lng"]

    nearest = top10[
        (top10["위도"] == lat)
        &
        (top10["경도"] == lng)
    ]

    if not nearest.empty:

        row = nearest.iloc[0]

        st.success(row["대여소명"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "대여건수",
                f"{row['대여건수']:,}건"
            )

        with col2:
            st.metric(
                "순위",
                f"{row['순위']}위"
            )

        st.write("주소 :", row["주소"])

else:
    st.info("지도에서 마커를 클릭하세요.")
