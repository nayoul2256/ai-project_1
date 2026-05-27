import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==================================================
# 페이지 설정
# ==================================================
st.set_page_config(
    page_title="서울 기온 연도별 비교",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 기온 연도별 비교")
st.markdown(
    "월과 일을 선택하면 해당 날짜의 연도별 최고기온과 최저기온을 비교합니다."
)

# ==================================================
# 데이터 불러오기
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
            df = pd.read_csv(
                "seoul.csv",
                encoding=enc
            )
            return df
        except:
            pass

    raise Exception("seoul.csv 파일을 읽을 수 없습니다.")

df = load_data()

# ==================================================
# 날짜 처리
# ==================================================
df["날짜"] = pd.to_datetime(df["날짜"])

df["연도"] = df["날짜"].dt.year
df["월"] = df["날짜"].dt.month
df["일"] = df["날짜"].dt.day

# ==================================================
# 월/일 선택
# ==================================================
col1, col2 = st.columns(2)

with col1:
    selected_month = st.selectbox(
        "월 선택",
        range(1, 13),
        index=7
    )

with col2:
    selected_day = st.selectbox(
        "일 선택",
        range(1, 32),
        index=0
    )

# ==================================================
# 선택 날짜 데이터 추출
# ==================================================
filtered = df[
    (df["월"] == selected_month)
    &
    (df["일"] == selected_day)
].copy()

filtered = filtered.sort_values("연도")

filtered = filtered.dropna(
    subset=[
        "최고기온(℃)",
        "최저기온(℃)"
    ]
)

# ==================================================
# 데이터 없을 경우
# ==================================================
if len(filtered) == 0:

    st.warning(
        "해당 날짜의 데이터가 없습니다."
    )

else:

    # ==================================================
    # 그래프
    # ==================================================

    fig = go.Figure()

    # 최고기온
    fig.add_trace(
        go.Scatter(
            x=filtered["연도"],
            y=filtered["최고기온(℃)"],
            mode="lines+markers",
            name="최고기온",
            line=dict(
                color="#E53935",
                width=3
            ),
            marker=dict(
                size=7
            )
        )
    )

    # 최저기온
    fig.add_trace(
        go.Scatter(
            x=filtered["연도"],
            y=filtered["최저기온(℃)"],
            mode="lines+markers",
            name="최저기온",
            line=dict(
                color="#1E88E5",
                width=3
            ),
            marker=dict(
                size=7
            )
        )
    )

    fig.update_layout(
        title=f"{selected_month}월 {selected_day}일의 연도별 기온 변화",
        template="plotly_white",
        hovermode="x unified",
        height=700,
        xaxis_title="연도",
        yaxis_title="기온 (℃)",
        legend_title="구분",
        font=dict(
            family="Malgun Gothic"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==================================================
    # 통계
    # ==================================================

    col1, col2 = st.columns(2)

    with col1:
        hottest = filtered.loc[
            filtered["최고기온(℃)"].idxmax()
        ]

        st.metric(
            "🔥 가장 더운 해",
            f"{int(hottest['연도'])}년",
            f"{hottest['최고기온(℃)']:.1f}℃"
        )

    with col2:
        coldest = filtered.loc[
            filtered["최저기온(℃)"].idxmin()
        ]

        st.metric(
            "❄️ 가장 추운 해",
            f"{int(coldest['연도'])}년",
            f"{coldest['최저기온(℃)']:.1f}℃"
        )

    st.divider()

    st.subheader("📋 선택 날짜 데이터")

    st.dataframe(
        filtered[
            [
                "연도",
                "최고기온(℃)",
                "최저기온(℃)"
            ]
        ],
        use_container_width=True
    )
