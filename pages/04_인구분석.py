import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="서울시 행정구별 인구수",
    layout="wide"
)

st.title("서울시 행정구별 인구수")

# ------------------------
# 데이터 로드
# ------------------------
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
            return pd.read_csv("population.csv", encoding=enc)
        except:
            pass

    raise Exception("CSV 파일을 읽을 수 없습니다.")

df = load_data()

region_col = df.columns[0]

# 숫자 변환
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

# 연령대 컬럼
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

# 서울특별시 제외
district_df = df[
    df[region_col] != "서울특별시"
].copy()

# ===================================
# 1. 행정구 선택 그래프
# ===================================

st.subheader("행정구 연령대별 인구")

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
        marker=dict(
            size=8
        )
    )
)

fig1.update_layout(
    title="서울시 행정구별 인구수",
    paper_bgcolor="#E8F5E9",
    plot_bgcolor="#E8F5E9",
    font=dict(
        family="Malgun Gothic"
    ),
    xaxis_title="나이",
    yaxis_title="인구수",
    height=600
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()

# ===================================
# 2. 연령대 TOP10 비교
# ===================================

st.subheader("연령대별 인구 TOP10 행정구 비교")

selected_age = st.selectbox(
    "연령대 선택",
    age_cols
)

top10 = (
    district_df
    [[region_col, selected_age]]
    .sort_values(
        by=selected_age,
        ascending=False
    )
    .head(10)
)

fig2 = go.Figure()

colors = px.colors.sequential.Tealgrn

for i, row in enumerate(top10.itertuples()):

    fig2.add_trace(
        go.Scatter(
            x=[selected_age],
            y=[getattr(row, selected_age)],
            mode="lines+markers+text",
            name=getattr(row, region_col),
            text=[getattr(row, region_col)],
            textposition="top center",
            line=dict(
                width=3,
                color=colors[i]
            )
        )
    )

fig2.update_layout(
    title=f"{selected_age} 인구 상위 10개 행정구",
    paper_bgcolor="#E8F5E9",
    plot_bgcolor="#E8F5E9",
    font=dict(
        family="Malgun Gothic"
    ),
    xaxis_title="연령대",
    yaxis_title="인구수",
    height=700
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ===================================
# TOP10 표
# ===================================

st.subheader("TOP10 행정구")

st.dataframe(
    top10,
    use_container_width=True
)
여기에서
AttributeError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/ai-project_1/pages/04_인구분석.py", line 152, in <module>
    y=[getattr(row, selected_age)],
       ~~~~~~~^^^^^^^^^^^^^^^^^^^
요게 오류났어 수정해줘.따로따로 알려주지 말고 한거번에 복사할 수 있게 알려줘.
