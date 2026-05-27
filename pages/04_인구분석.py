# ===================================
# 2. 연령대 TOP10 비교
# ===================================

st.subheader("연령대별 인구 TOP10 행정구 비교")

selected_age = st.selectbox(
    "연령대 선택",
    age_cols
)

top10 = (
    district_df[[region_col, selected_age]]
    .sort_values(
        by=selected_age,
        ascending=False
    )
    .head(10)
)

# 가독성을 위해 내림차순 막대그래프
top10 = top10.sort_values(
    by=selected_age,
    ascending=True
)

fig2 = px.bar(
    top10,
    x=selected_age,
    y=region_col,
    orientation="h",
    text=selected_age,
    color=selected_age,
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

# ===================================
# TOP10 표
# ===================================

st.subheader("TOP10 행정구")

st.dataframe(
    top10.sort_values(
        by=selected_age,
        ascending=False
    ),
    use_container_width=True
)
