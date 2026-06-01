import streamlit as st
import pandas as pd

from streamlit_folium import st_folium
st.title("서울 자전거 대여소 TOP10")

df = pd.read_csv("bike_top10.csv")

st.map(
    df.rename(
        columns={
            "위도": "lat",
            "경도": "lon"
        }
    )
)

selected = st.selectbox(
    "대여소 선택",
    df["대여소명"]
)

row = df[df["대여소명"] == selected].iloc[0]

st.subheader(row["대여소명"])
st.write("주소:", row["주소"])
st.write("대여건수:", f"{row['대여건수']:,}건")
