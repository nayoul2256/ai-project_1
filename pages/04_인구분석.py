import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울시 행정구별 인구수",
    layout="wide"
)

st.title("서울시 행정구별 인구수")

# CSV 읽기
df = pd.read_csv("population.csv", encoding="utf-8")

# 첫 번째 열 이름(행정구명)
region_col = df.columns[0]

# 숫자형 변환
for col in df.columns[1:]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 연령 컬럼 추출
age_columns = []

for col in df.columns:
    col_str = str(col)

    if (
        "세" in col_str
        or "~" in col_str
        or "이상" in col_str
    ):
        age_columns.append(col)

# 행정구 선택
district = st.selectbox(
    "행정구를 선택하세요",
    df[region_col].unique()
)

selected_row = df[df[region_col] == district].iloc[0]

ages = [str(col) for col in age_columns]
population = [selected_row[col] for col in age_columns]

# 그래프
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=ages,
        y=population,
        mode="lines+markers",
        line=dict(
            color="#2E8B57",
            width=4
        ),
        marker=dict(
            size=8,
            color="#2E8B57"
        ),
        name="인구수"
    )
)

fig.update_layout(
    title={
        "text": "서울시 행정구별 인구수",
        "x": 0.5
    },
    xaxis_title="나이",
    yaxis_title="인구수",
    height=650,

    paper_bgcolor="#E8F5E9",
    plot_bgcolor="#E8F5E9",

    font=dict(
        family="Malgun Gothic",
        size=14
    ),

    hovermode="x unified"
)

fig.update_xaxes(
    showgrid=False
)

fig.update_yaxes(
    gridcolor="#C8E6C9"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
