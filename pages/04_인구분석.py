fig2 = go.Figure()

colors = px.colors.sequential.Tealgrn

for i, (_, row) in enumerate(top10.iterrows()):

    fig2.add_trace(
        go.Scatter(
            x=[selected_age],
            y=[row[selected_age]],
            mode="markers+text",
            name=row[region_col],
            text=[row[region_col]],
            textposition="top center",
            marker=dict(
                size=14,
                color=colors[i % len(colors)]
            )
        )
    )
