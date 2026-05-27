import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==================================================
# 페이지 설정
# ==================================================
st.set_page_config(
    page_title="서울 기온 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석")
st.markdown("월과 일을 선택하면 해당 날짜의 연도별 최고기온과 최저기온을 비교합니다.")

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
                "seoul.csv",
                encoding=enc
            )
        except:
            continue

    raise Exception("seoul.csv 파일을 읽을 수 없습니다.")

df = load_data()

# 날짜 컬럼 자동 찾기
date_col = None

for col in df.columns:
    if "날짜" in str(col):
        date_col = col
        break

if date_col is None:
    st.error("날짜 컬럼을 찾을 수 없습니다.")
    st.stop()

# ==================================================
# 날짜 처리
# ==================================================
df[date_col] = (
    df[date_col]
    .astype(str)
    .str.strip()
    .str.replace(".", "-", regex=False)
    .str.replace("/", "-", regex=False)
)

df[date_col] = pd.to_datetime(
    df[date_col],
    errors="coerce"
)

df = df.dropna(subset=[date_col])

# ==================================================
# 연/월/일 추출
# ==================================================
df["연도"] = df[date_col].dt.year
df["월"] = df[date_col].dt.month
df["일"] = df[date_col].dt.day

# ==================================================
# 기온 컬럼 찾기
# ==================================================
max_col = None
min_col = None

for col in df.columns:

    col_name = str(col)

    if "최고기온" in col_name:
        max_col = col

    if "최저기온" in col_name:
        min_col = col

if max_col is None or min_col is None:
    st.error("최고기온 또는 최저기온 컬럼을 찾을 수 없습니다.")
    st.stop()

# 숫자 변환
df[max_col] = pd.to_numeric(
    df[max_col],
    errors="coerce"
)

df[min_col] = pd.to_numeric(
    df[min_col],
    errors="coerce"
)

# ==================================================
# 월/일 선택
# ==================================================
col1, col2 = st.columns(2)

with col1:
    selected_month = st.selectbox(
        "월 선택",
        list(range(1, 13)),
        index=0
    )

with col2:
    selected_day = st.selectbox(
        "일 선택",
        list(range(1, 32)),
        index=0
    )

# ==================================================
# 선택 날짜 데이터
# ==================================================
filtered = df[
    (df["월"] == selected_month)
    &
    (df["일"] == selected_day)
].copy()

filtered = filtered.dropna(
    subset=[
        max_col,
        min_col
    ]
)

filtered = filtered.sort_values(
    "연도"
)

# ==================================================
# 데이터 없는 경우
# ==================================================
if len(filtered) == 0:

    st.warning(
        f"{selected_month}월 {selected_day}일 데이터가 없습니다."
    )

    st.stop()

# ==================================================
# 그래프
# ==================================================
fig = go.Figure()

# 최고기온
fig.add_trace(
    go.Scatter(
        x=filtered["연도"],
        y=filtered[max_col],
        mode="lines+markers",
        name="최고기온",
        line=dict(
            color="#E53935",
            width=3
        ),
        marker=dict(
            size=6
        )
    )
)

# 최저기온
fig.add_trace(
    go.Scatter(
        x=filtered["연도"],
        y=filtered[min_col],
        mode="lines+markers",
        name="최저기온",
        line=dict(
            color="#1E88E5",
            width=3
        ),
        marker=dict(
            size=6
        )
    )
)

fig.update_layout(
    title=f"{selected_month}월 {selected_day}일 연도별 최고·최저기온",
    template="plotly_white",
    hovermode="x unified",
    height=700,
    xaxis_title="연도",
    yaxis_title="기온 (℃)",
    legend_title="구분"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==================================================
# 최고/최저 기록
# ==================================================
col1, col2 = st.columns(2)

with col1:

    hottest = filtered.loc[
        filtered[max_col].idxmax()
    ]

    st.metric(
        "🔥 가장 더웠던 해",
        f"{int(hottest['연도'])}년",
        f"{hottest[max_col]:.1f}℃"
    )

with col2:

    coldest = filtered.loc[
        filtered[min_col].idxmin()
    ]

    st.metric(
        "❄️ 가장 추웠던 해",
        f"{int(coldest['연도'])}년",
        f"{coldest[min_col]:.1f}℃"
    )

# ==================================================
# 데이터 테이블
# ==================================================
st.subheader("📋 선택 날짜 데이터")

st.dataframe(
    filtered[
        [
            "연도",
            max_col,
            min_col
        ]
    ],
    use_container_width=True
)
