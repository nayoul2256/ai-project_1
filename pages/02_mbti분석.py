import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="World MBTI Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------
# 데이터 불러오기
# ---------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")


df = load_data()

mbti_columns = [
    "INFJ", "INFP", "INTJ", "INTP",
    "ISFJ", "ISFP", "ISTJ", "ISTP",
    "ENFJ", "ENFP", "ENTJ", "ENTP",
    "ESFJ", "ESFP", "ESTJ", "ESTP"
]

# ---------------------------------
# 사이드바
# ---------------------------------
st.sidebar.title("🌍 국가 선택")
selected_country = st.sidebar.selectbox(
    "국가를 선택하세요",
    sorted(df["Country"].unique())
)

# ---------------------------------
# 선택 국가 데이터 정리
# ---------------------------------
country_row = df[df["Country"] == selected_country].iloc[0]

mbti_df = pd.DataFrame({
    "MBTI": mbti_columns,
    "Ratio": [country_row[col] for col in mbti_columns]
})

mbti_df = mbti_df.sort_values("Ratio", ascending=False).reset_index(drop=True)

# ---------------------------------
# 색상 설정
# 1등 = 빨간색
# 나머지 = 파란색 그라데이션
# ---------------------------------
blue_gradient = [
    "#0D47A1", "#1565C0", "#1976D2", "#1E88E5",
    "#2196F3", "#42A5F5", "#64B5F6", "#90CAF9",
    "#BBDEFB", "#E3F2FD"
]

colors = []
for i in range(len(mbti_df)):
    if i == 0:
        colors.append("#E53935")
    else:
        colors.append(blue_gradient[(i - 1) % len(blue_gradient)])

# ---------------------------------
# 메인 화면
# ---------------------------------
st.title("🌎 World MBTI Dashboard")
st.subheader(f"📍 {selected_country}의 MBTI 비율")

col1, col2 = st.columns([3, 1])

with col1:
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=mbti_df["MBTI"],
        y=mbti_df["Ratio"],
        marker_color=colors,
        text=[f"{x:.2%}" for x in mbti_df["Ratio"]],
        textposition="outside",
        hovertemplate="MBTI: %{x}<br>비율: %{y:.2%}<extra></extra>"
    ))

    fig.update_layout(
        template="plotly_white",
        height=650,
        title=f"{selected_country} MBTI Distribution",
        xaxis_title="MBTI Type",
        yaxis_title="Ratio",
        showlegend=False,
        margin=dict(t=80, l=40, r=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    top_mbti = mbti_df.iloc[0]

    st.markdown("## 🏆 가장 높은 MBTI")
    st.metric(
        label=top_mbti["MBTI"],
        value=f"{top_mbti['Ratio']:.2%}"
    )

    st.markdown("---")
    st.markdown("## 📊 TOP 5")
    st.dataframe(
        mbti_df.head(5),
        use_container_width=True,
        hide_index=True
    )

st.markdown("---")
st.caption("Made with Streamlit + Plotly + Pandas")
