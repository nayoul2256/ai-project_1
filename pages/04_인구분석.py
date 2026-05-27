import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ==================================================
# 페이지 설정
# ==================================================
st.set_page_config(
    page_title="서울시 행정구별 인구수",
    layout="wide"
)

st.title("🏙️ 서울시 행정구별 인구수 분석")

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
                "population.csv",
                encoding=enc
            )
        except:
            pass

    raise Exception("population.csv 파일을 읽을 수 없습니다.")

df = load_data()

# ==================================================
# 첫 번째 컬럼 = 행정구
# ==================================================
region_col = df.columns[0]

# ==================================================
# 숫자형 변환
# ==================================================
for col in df.columns[1:]:

    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# ==================================================
# 연령대 컬럼
# ==================================================
age_cols = [
    "0~9세",
    "10~19세",
    "20~29세",
    "30~39세",
    "40~49세",
    "50~59세",
    "60~69세",
    "70~79세",
    "80~89세",
    "90~99세",
    "100세 이상"
]

# 실제 존재하는 컬럼만 사용
age_cols = [
    col for col in age_cols
    if col in df.columns
]

# ==================================================
# 서울특별시 행 제거
# ==================================================
district_df = df[
    df[region_col] != "서울특별시"
].copy()

# ==================================================
# 1. 행정구 선택 그래프
# ==================================================
st.subheader("📈 행정구 연령대별 인구")

district = st.selectbox(
    "행정구 선택",
    district_df[region_col].tolist()
)

selected = district_df[
    district_df[region_col] == district
].iloc[0]

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=age_cols,
        y=[selected[col] for col in age_cols],
        mode="lines+markers",
        line=dict(
            color="#2F6F4F",
            width=4
        ),
        marker=dict(size=8)
    )
)

fig1.update_layout(
    title=f"{district} 연령대별 인구",
    paper_bgcolor="#E8F5E9",
    plot_bgcolor="#E8F5E9",
    font=dict(
        family="Malgun Gothic"
    ),
    xaxis_title="연령대",
    yaxis_title="인구수",
    height=600
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()

# ==================================================
# 2. 연령대별 TOP10 행정구
# ==================================================
st.subheader("🏆 연령대별 인구 TOP10 행정구")

selected_age = st.selectbox(
    "연령대 선택",
    age_cols,
    key="age_select"
)

top10 = (
    district_df[
        [region_col, selected_age]
    ]
    .sort_values(
        by=selected_age,
        ascending=False
    )
    .head(10)
)

# 그래프용 정렬
top10_graph = top10.sort_values(
    by=selected_age,
    ascending=True
)

fig2 = px.bar(
    top10_graph,
    x=selected_age,
    y=region_col,
    orientation="h",
    color=selected_age,
    text=selected_age,
    color_continuous_scale="Tealgrn"
)

fig2.update_traces(
    texttemplate="%{text:,}",
    textposition="outside"
)

fig2.update_layout(
    title=f"{selected_age} 인구 상위 10개 행정구",
    paper_bgcolor="#E8F5E9",
    plot_bgcolor="#E8F5E9",
    font=dict(
        family="Malgun Gothic"
    ),
    xaxis_title="인구수",
    yaxis_title="행정구",
    height=700,
    coloraxis_showscale=False
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==================================================
# TOP10 표
# ==================================================
st.subheader("📋 TOP10 행정구 데이터")

st.dataframe(
    top10,
    use_container_width=True
)

# ==================================================
# 전체 데이터 보기
# ==================================================
with st.expander("전체 데이터 보기"):
    st.dataframe(
        district_df,
        use_container_width=True
    )
