import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="서울 따릉이 인기 대여소 TOP10",
layout="wide"
)

st.title("🚲 서울 따릉이 인기 대여소 TOP10")

@st.cache_data
def load_data():

```
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

st.error("CSV 파일을 읽을 수 없습니다.")
st.stop()
```

df = load_data()

df["보관대수"] = pd.to_numeric(
df["보관대수"],
errors="coerce"
)

st.subheader("🏆 서울 따릉이 인기 대여소 TOP10")

top10 = (
df[
["자전거보관소명", "보관대수", "관리기관명"]
]
.dropna(subset=["보관대수"])
.sort_values(
by="보관대수",
ascending=False
)
.head(10)
)

fig = px.bar(
top10.sort_values(
by="보관대수",
ascending=True
),
x="보관대수",
y="자전거보관소명",
orientation="h",
text="보관대수",
color="보관대수",
color_continuous_scale="Tealgrn"
)

fig.update_layout(
height=650,
xaxis_title="보관대수",
yaxis_title="자전거보관소명",
coloraxis_showscale=False
)

st.plotly_chart(
fig,
use_container_width=True
)

st.markdown("### 📋 TOP10 데이터")

st.dataframe(
top10,
use_container_width=True
)

st.divider()

st.subheader("🗺️ 서울시 자전거보관소 지도")

map_df = df.dropna(
subset=["WGS84위도", "WGS84경도"]
)

fig_map = px.scatter_mapbox(
map_df,
lat="WGS84위도",
lon="WGS84경도",
hover_name="자전거보관소명",
hover_data=[
"보관대수",
"관리기관명"
],
zoom=10,
height=700
)

fig_map.update_layout(
mapbox_style="open-street-map"
)

st.plotly_chart(
fig_map,
use_container_width=True
)

st.divider()

st.subheader("🔍 자전거보관소 상세정보")

bike_name = st.selectbox(
"보관소 선택",
sorted(
df["자전거보관소명"]
.dropna()
.unique()
)
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

🏢 관리기관 : {selected['관리기관명']}
"""
)

st.divider()

st.subheader("📋 전체 데이터 보기")

st.dataframe(
df,
use_container_width=True
)
