import streamlit as st
import pandas as pd

# ==========================
# 페이지 설정
# ==========================
st.set_page_config(
    page_title="서울 자전거 대여소 TOP10",
    page_icon="🚲",
    layout="wide"
)

st.title("🚲 서울 자전거 대여소 TOP10")
st.markdown("서울에서 가장 많이 이용되는 자전거 대여소 TOP10")

# ==========================
# 데이터 불러오기
# ==========================
@st.cache_data
def load_data():
    return pd.read_csv("bike_top10.csv")

df = load_data()

# ==========================
# 지도 표시
# ==========================
st.subheader("📍 대여소 위치")

map_df = df.rename(
    columns={
        "위도": "lat",
        "경도": "lon"
    }
)

st.map(map_df)

# ==========================
# 대여소 선택
# ==========================
st.subheader("🚲 대여소 정보")

selected_station = st.selectbox(
    "대여소를 선택하세요",
    df["대여소명"]
)

row = df[df["대여소명"] == selected_station].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "순위",
        f"{row['순위']}위"
    )

with col2:
    st.metric(
        "대여건수",
        f"{row['대여건수']:,}건"
    )

st.write("📍 주소 :", row["주소"])

# ==========================
# 전체 TOP10 표
# ==========================
st.subheader("🏆 TOP10 목록")

st.dataframe(
    df.sort_values(
        "순위"
    ),
    use_container_width=True
)
