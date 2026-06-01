import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==================================================
# TOP10 보관소
# ==================================================
df = load_data()

st.subheader("🏆 서울시 보관대수 TOP10")

top10 = (
    df[
        ["자전거보관소명", "보관대수", "관리기관명"]
    ]
    .sort_values(
        by="보관대수",
        ascending=False
    )
    .head(10)
)

fig2 = px.bar(
    top10.sort_values(
        by="보관대수",
        ascending=True
    ),
    x="보관대수",
    y="자전거보관소명",
    orientation="h",
    color="보관대수",
    text="보관대수",
    color_continuous_scale="Tealgrn"
)

fig2.update_layout(
    height=700,
    xaxis_title="보관대수",
    yaxis_title="자전거보관소"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.dataframe(
    top10,
    use_container_width=True
)

st.divider()

# ==================================================
# 지도 시각화
# ==================================================
st.subheader("🗺️ 서울시 자전거보관소 지도")

map_df = df.dropna(
    subset=["WGS84위도", "WGS84경도"]
)

fig3 = px.scatter_mapbox(
    map_df,
    lat="WGS84위도",
    lon="WGS84경도",
    hover_name="자전거보관소명",
    hover_data={
        "보관대수": True,
        "관리기관명": True
    },
    zoom=10,
    height=700
)

fig3.update_layout(
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==================================================
# 보관소 상세정보
# ==================================================
st.subheader("🔍 자전거보관소 상세정보")

bike_name = st.selectbox(
    "보관소 선택",
    sorted(df["자전거보관소명"].dropna().unique())
)

selected = df[
    df["자전거보관소명"] == bike_name
].iloc[0]

st.info(
    f"""
    📍 주소 : {selected['소재지도로명주소']}

    🚲 보관대수 : {selected['보관대수']}대

    🏗 설치형태 : {selected['설치형태']}

    ☂ 차양막 : {selected['차양막설치여부']}

    🔧 수리대 : {selected['수리대설치여부']}

    💨 공기주입기 : {selected['공기주입기비치여부']}
    """
)

# ==================================================
# 전체 데이터
# ==================================================
with st.expander("전체 데이터 보기"):
    st.dataframe(
        df,
        use_container_width=True
    )
