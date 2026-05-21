import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울시 행정구별 인구수",
    layout="wide"
)

st.title("서울시 행정구별 인구수")

# 데이터 불러오기
df = pd.read_csv("population.csv", encoding="utf-8")

# 첫 번째 열(행정구명)
region_col = df.columns[0]

# 숫자형 변환
for col in df.columns[1:]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 나이 컬럼 추출
age_cols = []

for col in df.columns:
    col_name = str(col)

    if col_name.endswith("세"):
        try:
            int(col_name.replace("세", ""))
            age_cols.append(col)
        except:
            pass

    elif "100세 이상" in col_name:
        age_cols.append(col)

# 나이순 정렬
def age_sort(x):
    x = str(x)
    if "100세 이상" in x:
        return 100
    return int(x.replace("세", ""))

age_cols = sorted(age_cols, key=age_sort)

# 행정구 목록
districts = df[region_col].unique()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택된 행정구 데이터
selected_row = df[df[region_col] == selected_district].iloc[0]

ages = [str(col) for col in age_cols]
population = [selected_row[col] for col in age_cols]

# 그래프
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=ages,
        y=population,
        mode="lines+markers",
        line=dict(
            color="#2F6F4F",
            width=4
        ),
        marker=dict(
            size=7,
            color="#2F6F4F"
        ),
        name="인구수"
    )
)

fig.update_layout(
    title={
        "text": "서울시 행정구별 인구수",
        "x": 0.5
    },
    paper_bgcolor="#E8F5E9",
    plot_bgcolor="#E8F5E9",
    height=700,
    hovermode="x unified",
    font=dict(
        family="Malgun Gothic",
        size=14
    ),
    xaxis_title="나이",
    yaxis_title="인구수"
)

fig.update_xaxes(
    tickangle=45,
    showgrid=False
)

fig.update_yaxes(
    gridcolor="#C8E6C9"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
