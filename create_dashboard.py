import plotly.express as px
import plotly.io as pio
import os

# ---------- Dashboard 1: Iris Scatter with Filter ----------
os.makedirs("dashboard1", exist_ok=True)
df_iris = px.data.iris()

fig1 = px.scatter(
    df_iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    title="Iris Scatter Plot",
    hover_data=["petal_width", "petal_length"],
)

fig1.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(label="All", method="update", args=[{"visible": [True, True, True]}]),
                dict(label="Setosa", method="update", args=[{"visible": [True, False, False]}]),
                dict(label="Versicolor", method="update", args=[{"visible": [False, True, False]}]),
                dict(label="Virginica", method="update", args=[{"visible": [False, False, True]}]),
            ],
            direction="down",
            showactive=True,
        )
    ]
)

pio.write_html(fig1, file="dashboard1/index.html", auto_open=False)

# ---------- Dashboard 2: Gapminder Line Plot with Slider ----------
os.makedirs("dashboard2", exist_ok=True)
df_gap = px.data.gapminder().query("country=='Colombia' or country=='Argentina'")

fig2 = px.line(
    df_gap,
    x="year",
    y="lifeExp",
    color="country",
    markers=True,
    title="Life Expectancy Over Time (Colombia vs Argentina)",
)

fig2.update_layout(
    xaxis=dict(
        rangeslider=dict(visible=True),
        tickmode="linear",
        tick0=1952,
        dtick=5
    )
)

pio.write_html(fig2, file="dashboard2/index.html", auto_open=False)

print("✅ Dashboards created in dashboard1/ and dashboard2/")
