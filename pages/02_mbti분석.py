import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="World MBTI Dashboard",
    page_icon="🌍",
    layout="wide"
)

# --------------------------------------------------
# 데이터 불러오기
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df


df = load_data()

mbti_columns = [
    "INFJ", "INFP", "INTJ", "INTP",
    "ISFJ", "ISFP", "ISTJ", "ISTP",
    "ENFJ", "ENFP", "ENTJ", "ENTP",
    "ESFJ", "ESFP", "ESTJ", "ESTP"
]

# --------------------------------------------------
# 사이드바
# --------------------------------------------------
st.sidebar.title("🌍 국가 선택")

selected_country = st.sidebar.selectbox(
    "국가를 선택하세요",
    sorted(df["Country"].unique())
)

# --------------------------------------------------
# 선택된 국가 데이터
# --------------------------------------------------
country_data = df[df["Country"] == selected_country].iloc[0]

mbti_values = pd.DataFrame({
    "MBTI": mbti_columns,
    "Ratio": [country_data[col] for col in mbti_columns]
})

# 내림차순 정렬
mbti_values = mbti_values.sort_values("Ratio", ascending=False).reset_index(drop=True)

# --------------------------------------------------
# 색상 설정
# 1등 = 빨간색
# 나머지 = 파란색 그라데이션 느낌
# --------------------------------------------------
colors = []
for i in range(len(mbti_values)):
    if i == 0:
        colors.append("#E53935")  # 빨강
    else:
        blue_scale = [
            "#1565C0", "#1976D2", "#1E88E5", "#2196F3",
            "#42A5F5", "#64B5F6", "#90CAF9", "#BBDEFB"
        ]
        colors.append(blue_scale[(i - 1) % len(blue_scale)])

# --------------------------------------------------
# 메인 화면
# --------------------------------------------------
st.title("🌎 World MBTI Dashboard")
st.subheader(f"📍 {selected_country}의 MBTI 분포")

col1, col2 = st.columns([2, 1])

with col1:
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=mbti_values["MBTI"],
        y=mbti_values["Ratio"],
        marker_color=colors,
        text=[f"{v:.2%}" for v in mbti_values["Ratio"]],
        textposition="outside",
        hovertemplate="MBTI: %{x}<br>비율: %{y:.2%}<extra></extra>"
    ))

    fig.update_layout(
        height=650,
        template="plotly_white",
        title=f"{selected_country} MBTI 비율",
        xaxis_title="MBTI 유형",
        yaxis_title="비율",
        font=dict(size=14),
        showlegend=False,
        margin=dict(t=80, l=40, r=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("## 🏆 가장 높은 MBTI")
    top_mbti = mbti_values.iloc[0]

    st.metric(
        label=top_mbti["MBTI"],
        value=f"{top_mbti['Ratio']:.2%}"
    )

    st.markdown("---")
    st.markdown("## 📊 상위 5개")
    st.dataframe(
        mbti_values.head(5),
        use_container_width=True,
        hide_index=True
    )

st.markdown("---")
st.caption("Made with Streamlit + Plotly")
