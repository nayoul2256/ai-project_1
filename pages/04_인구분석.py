fig2 = px.bar(
    top10,
    x=selected_age,
    y=region_col,
    orientation="h",
    color=selected_age,
    color_continuous_scale="Tealgrn",
    text=selected_age
)

fig2.update_layout(
    title=f"{selected_age} 인구 상위 10개 행정구",
    paper_bgcolor="#E8F5E9",
    plot_bgcolor="#E8F5E9",
    font=dict(family="Malgun Gothic"),
    height=700,
    yaxis=dict(categoryorder="total ascending")
)

fig2.update_traces(
    texttemplate="%{text:,}",
    textposition="outside"
)
