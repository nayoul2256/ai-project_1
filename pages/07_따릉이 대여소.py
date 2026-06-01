```python
import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# 페이지 설정
# ==================================================
st.set_page_config(
    page_title="서울시 자전거보관소 분석",
    layout="wide"
)

st.title("🚲 서울시 자전거보관소 분석")

# ==================================================
# 데이터 로드
# ==================================================
@st.cache_data
def load_data():

    encodings = [
        "cp949",
        "euc-kr",
        "utf-8-sig",
        "utf-8"
    ]

    for enc in encodings:
        try:
            return pd.read_csv(
                "자전거보관소정보_서울특별시.csv",
                encoding=enc
            )
        except:
            pass

    raise Exception("파일을 읽을 수 없습니다.")

df = load_data()

# ==================================================
# 숫자형 변환
# ==================================================
df["보관대수"] = pd.to_numeric(
    df["보관대수"],
    errors="coerce"
)

# ==================================================
# 서울시 보관대수 TOP20
# ==================================================
st.subheader("🏆 서울시 보관대수 TOP20")

top20 = (
    df[
        ["자전거보관소명", "보관대수", "관리기관명"]
    ]
    .sort_values(
        by="보관대수",
        ascending=False
    )
    .head(20)
)

fig1 = px.bar(
    top20,
    x="자전거보관소명",
    y="보관대수",
    color="보관대수",
    text="보관대수",
    color_continuous_scale="Tealgrn"
)

fig1.update_traces(
    textposition="outside"
)

fig1.update_layout(
    title="서울시 자전거보관소 보관대수 TOP20",
    height=650,
    xaxis_title="자전거보관소명",
    yaxis_title="보관대수"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.dataframe(
    top20,
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

fig2 = px.scatter_mapbox(
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

fig2.update_layout(
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

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
```
