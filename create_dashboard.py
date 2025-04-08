import plotly.express as px
import plotly.io as pio
import os

# Make a folder for the dashboard
os.makedirs("dashboard1", exist_ok=True)

# Create a simple plot
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Iris Scatter Plot")

# Save the plot as an HTML file
pio.write_html(fig, file="dashboard1/index.html", auto_open=False)
